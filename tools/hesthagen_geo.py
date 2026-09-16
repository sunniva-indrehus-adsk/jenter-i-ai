#!/usr/bin/env python3
"""Geodata-hjelper for Hesthagen-figurene.

Alt regnes i EUREF89 UTM32N (EPSG:25832). Det er ikke tilfeldig: det er det
ENESTE koordinatsystemet både Trondheim kommunes ortofoto-WMS og Kartverkets
gråtone-WMS tilbyr. Da havner flyfotoet og kartet pikselnøyaktig oppå hverandre
uten at noe skal reprojiseres her. UTM er dessuten metrisk på stedet — én piksel
er like mange meter i hele bildet, i motsetning til Web Mercator, som på 63°N
strekker med en faktor 2,2.

Begge tjenestene er WMS og ikke WMTS med vilje. Fliser låser oppløsningen til
zoomtrinnene (Kartverkets fliser stopper på 0,27 m/px her); en WMS tegner det
utsnittet du ber om i den pikselstørrelsen du ber om. Derfor er figurene skarpe.
"""
import io
import math
import urllib.parse
import urllib.request

from PIL import Image

UA = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) jenter-i-ai-slides/1.0'}

# Tomta slik den ligger i OpenStreetMap: way/35838067, «Hesthagen»,
# landuse=construction, 7095 m². Hentet med Overpass, se README.
# Rekkefølge: (lat, lon). Dette er parkeringsplassen som reguleres.
SITE = [
    (63.415866, 10.399239), (63.415824, 10.399264), (63.415377, 10.399534),
    (63.415348, 10.399552), (63.415220, 10.399627), (63.415211, 10.399805),
    (63.415093, 10.401201), (63.415327, 10.401091), (63.415563, 10.400977),
    (63.415667, 10.401014), (63.415804, 10.400962), (63.416060, 10.400799),
    (63.416052, 10.400740), (63.416002, 10.400364),
]

# Nabotomta i samme detaljregulering (way/1427071316, 9623 m²). Brukes ikke i
# figurene nå, men den er halve utbyggingen og ligger her for neste runde.
SITE_NORTH = [
    (63.415327, 10.401091), (63.415378, 10.401580), (63.415490, 10.402596),
    (63.415774, 10.403065), (63.415901, 10.402985), (63.416072, 10.403010),
    (63.416194, 10.402884), (63.416423, 10.401741), (63.416232, 10.401172),
    (63.416060, 10.400799), (63.415804, 10.400962), (63.415667, 10.401014),
]

# Trondheim kommunes åpne GeoServer. Ortofoto ligger som ett lag per årgang, og
# det er derfor vi kan vise parkeringsplassen i stedet for byggegropa: 2022 er
# siste årgang før anlegget startet.
TK_WMS = 'https://kart.trondheim.kommune.no/geoserver/wms'
TK_ORTO = {y: f'Raster:ortofoto{y}' for y in
           (1937, 2006, 2010, 2013, 2014, 2017, 2019, 2020, 2021, 2022, 2023, 2024)}
TK_ORTO['siste'] = 'Raster:ortofoto'

# Kartverkets gråtonekart — samme kartserie som resten av decket bruker.
KV_WMS = 'https://wms.geonorge.no/skwms1/wms.topograatone'


# ── UTM32N (EPSG:25832) ───────────────────────────────────────────────────
# Standard transvers Mercator på GRS80/WGS84. Skrevet ut her i stedet for å
# dra inn pyproj: det er tjue linjer, og repoet skal kunne bygges uten
# kompilerte avhengigheter.
_A, _F = 6378137.0, 1 / 298.257222101      # GRS80
_E2 = 2 * _F - _F * _F
_K0, _LON0, _FE, _FN = 0.9996, 9.0, 500000.0, 0.0


def lonlat_to_utm32(lon, lat):
    lat, dlon = math.radians(lat), math.radians(lon - _LON0)
    e2 = _E2
    ep2 = e2 / (1 - e2)
    N = _A / math.sqrt(1 - e2 * math.sin(lat) ** 2)
    T = math.tan(lat) ** 2
    C = ep2 * math.cos(lat) ** 2
    A = math.cos(lat) * dlon
    M = _A * ((1 - e2/4 - 3*e2**2/64 - 5*e2**3/256) * lat
              - (3*e2/8 + 3*e2**2/32 + 45*e2**3/1024) * math.sin(2*lat)
              + (15*e2**2/256 + 45*e2**3/1024) * math.sin(4*lat)
              - (35*e2**3/3072) * math.sin(6*lat))
    east = _FE + _K0 * N * (A + (1 - T + C) * A**3 / 6
                            + (5 - 18*T + T*T + 72*C - 58*ep2) * A**5 / 120)
    north = _FN + _K0 * (M + N * math.tan(lat) * (A*A/2 + (5 - T + 9*C + 4*C*C) * A**4 / 24
                         + (61 - 58*T + T*T + 600*C - 330*ep2) * A**6 / 720))
    return east, north


class Frame:
    """Et utsnitt: bbox i UTM32-meter + pikselstørrelse.

    Konstrueres fra hvor ankeret (tomtas tyngdepunkt) skal ligge i bildet, som
    brøkdel av bredde og høyde. Komposisjonen styres dermed av motivet, ikke av
    koordinater man må prøve seg fram til. mpp er meter per piksel — sett den,
    og utsnittets størrelse følger av pikselformatet.
    """

    def __init__(self, w, h, mpp, anchor_lonlat, fx=0.5, fy=0.5):
        self.w, self.h, self.mpp = w, h, mpp
        ax, ay = lonlat_to_utm32(*anchor_lonlat)
        self.x0 = ax - fx * w * mpp
        self.y1 = ay + fy * h * mpp          # y vokser oppover i UTM, nedover i piksler
        self.x1 = self.x0 + w * mpp
        self.y0 = self.y1 - h * mpp

    @property
    def bbox(self):
        return (self.x0, self.y0, self.x1, self.y1)

    def px(self, lat, lon):
        x, y = lonlat_to_utm32(lon, lat)
        return (x - self.x0) / self.mpp, (self.y1 - y) / self.mpp

    def poly_px(self, latlons):
        return [self.px(la, lo) for la, lo in latlons]

    def describe(self):
        return (f'{self.w}x{self.h} px, {self.mpp:.3f} m/px, '
                f'dekker {self.w * self.mpp:.0f}x{self.h * self.mpp:.0f} m')


# ── henting ───────────────────────────────────────────────────────────────
def _wms(base, frame, layers, fmt='image/png', extra=None):
    q = {
        'service': 'WMS', 'version': '1.3.0', 'request': 'GetMap',
        'layers': layers, 'styles': '', 'crs': 'EPSG:25832',
        # WMS 1.3.0 med EPSG:25832 vil ha bboxen i akserekkefølgen til CRS-en,
        # og for UTM32 er den east,north — altså x først. (For EPSG:4326 ville
        # det vært lat først; det er den klassiske 1.3.0-fella.)
        'bbox': ','.join(f'{v:.3f}' for v in frame.bbox),
        'width': frame.w, 'height': frame.h, 'format': fmt, 'transparent': 'false',
    }
    q.update(extra or {})
    url = f'{base}?{urllib.parse.urlencode(q)}'
    last = None
    for _ in range(3):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=90) as r:
                b = r.read()
            if b[:4] == b'\x89PNG' or b[:2] == b'\xff\xd8':
                return Image.open(io.BytesIO(b)).convert('RGB')
            last = b[:300]
        except Exception as e:
            last = str(e)
    raise RuntimeError(f'WMS ga ikke bilde: {last!r}\n{url}')


def orto(frame, year=2022):
    """Ortofoto fra Trondheim kommune. year er en nøkkel i TK_ORTO."""
    img = _wms(TK_WMS, frame, TK_ORTO[year], fmt='image/jpeg')
    print(f'  ortofoto {year}      {frame.describe()}')
    return img


def graatone(frame, layers='topograatone'):
    """Kartverkets gråtonekart, samme serie som kartet på Hesthagen-sliden."""
    img = _wms(KV_WMS, frame, layers)
    print(f'  topograatone         {frame.describe()}')
    return img


def site_center():
    return (sum(p[1] for p in SITE) / len(SITE), sum(p[0] for p in SITE) / len(SITE))
