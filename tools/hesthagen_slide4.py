#!/usr/bin/env python3
"""Lager bakgrunnsbildene til tidligfase-slidene (slide 4-6).

Kjør fra repoets rot:
    python3 tools/hesthagen_slide4.py            # alle variantene
    python3 tools/hesthagen_slide4.py flyfoto    # bare én

Bildene havner i talk/figures/tidligfase/. Slidene 4, 5 og 6 deler
ett og samme bilde — det er oppbyggingen som er poenget, så bildet skal ikke
bytte når arkitekten og utbyggeren kommer inn.

KOMPOSISJON: tomta ligger med vilje litt til høyre og over midten. Nede til
venstre står merkelappen på slide 4, og på slide 5-6 dekker snakkeboblene og
figurene hele nedre to tredjedeler. Flytter du tomta ned, forsvinner den bak
dem.

ÅRGANG: 2022 er siste ortofoto før anlegget startet, og det eneste som viser
plassen full av biler. Nyere årganger viser byggegrop, som sier «noen har alt
bestemt seg» — stikk motsatt av «ingenting er tegnet». Se README.
"""
import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter

sys.path.insert(0, str(Path(__file__).parent))
from hesthagen_geo import SITE, Frame, graatone, orto, site_center

OUT = Path(__file__).parent.parent / 'talk' / 'figures' / 'tidligfase'

W, H = 2560, 1440          # 2x Marp-flaten (1280x720), så PDF-en blir skarp
MPP = 0.113                # ≈ ortofotoets egen oppløsning (ca. 0,10 m/px)
FX, FY = 0.55, 0.40        # der tomtas tyngdepunkt lander i bildet
YEAR = 2022

# Egen ramme for flyfoto-varianten, fordi den brukes på slidene der arkitekten
# og utbyggeren kommer inn. Snakkeboblene skal ikke dekke tomta, så tomta er
# flyttet ut til høyre og litt opp — da blir venstre halvdel ledig til boblene.
#
# 0,135 m/px i stedet for 0,113: et videre utsnitt gjør tomta mindre i flata og
# frigjør plass. Ortofotoet er ca. 0,10 m/px, så vi nedskalerer fortsatt kilden
# og bildet er like skarpt — vi mister utsnitt, ikke oppløsning.
ROLLER = dict(mpp=0.135, fx=0.70, fy=0.44)

RED = (225, 37, 27)        # samme rød som ringen på Hesthagen-kartet
SS = 4                     # supersampling; PIL tegner uten antialias


def frame(mpp=MPP, fx=FX, fy=FY):
    return Frame(W, H, mpp, site_center(), fx, fy)


def site_mask(f, blur=0):
    """1-kanals maske: hvit inne på tomta, svart utenfor."""
    m = Image.new('L', (W * SS, H * SS), 0)
    ImageDraw.Draw(m).polygon([(x * SS, y * SS) for x, y in f.poly_px(SITE)], fill=255)
    m = m.resize((W, H), Image.LANCZOS)
    return m.filter(ImageFilter.GaussianBlur(blur)) if blur else m


def outline(img, f, width=7, colour=RED, glow=True):
    """Tegn tomtegrensa. Gløden under gjør at rødt leses også mot lys asfalt."""
    pts = [(x * SS, y * SS) for x, y in f.poly_px(SITE)]
    if glow:
        g = Image.new('L', (W * SS, H * SS), 0)
        ImageDraw.Draw(g).line(pts + [pts[0]], fill=255, width=(width + 7) * SS, joint='curve')
        g = g.resize((W, H), Image.LANCZOS).filter(ImageFilter.GaussianBlur(6))
        img.paste(Image.new('RGB', (W, H), (0, 0, 0)), (0, 0),
                  g.point(lambda v: int(v * 0.42)))
    ov = Image.new('RGBA', (W * SS, H * SS), (0, 0, 0, 0))
    ImageDraw.Draw(ov).line(pts + [pts[0]], fill=colour + (255,), width=width * SS, joint='curve')
    img.paste(Image.new('RGB', (W, H), colour), (0, 0),
              ov.resize((W, H), Image.LANCZOS).split()[3])
    return img


def darken_outside(img, f, amount=0.34, feather=26):
    """Legg et mørkt sjikt UTENFOR tomta. Tomta blir dermed det lyseste i
    bildet, og blikket havner der uten at noe må peke på den."""
    m = site_mask(f, blur=feather).point(lambda v: int((255 - v) * amount))
    img.paste(Image.new('RGB', (W, H), (6, 14, 22)), (0, 0), m)
    return img


# ── variantene ────────────────────────────────────────────────────────────
def v_flyfoto(_ignored):
    """A: bare flyfotoet, tomta ringet inn og resten dempet.

    Bruker ROLLER-ramma og ikke den felles: dette er bildet slidene 4-6 står
    på, og der må venstre halvdel være ledig til snakkeboblene.
    """
    f = frame(**ROLLER)
    img = orto(f, YEAR)
    darken_outside(img, f)
    return outline(img, f)


def v_blankt(f):
    """D: tomta tømt. Utenfor tomta er verden et foto — inne på den er det
    flatt kartgrått og ingenting. «Ingenting er tegnet», tatt på ordet."""
    img = orto(f, YEAR)
    flat = Image.new('RGB', (W, H), (214, 216, 218))
    img.paste(flat, (0, 0), site_mask(f, blur=3))
    return outline(img, f, width=6, glow=False)


def _crossfade(f, a, b):
    """Kartet til venstre, flyfotoet til høyre, med en myk overgang mellom
    x=a*W og x=b*W. Rampa lages som ett smalt bilde og strekkes — å skrive
    2560x1440 piksler i en Python-løkke tar sekunder, dette tar ingenting."""
    photo = orto(f, YEAR)
    map_ = graatone(f)
    ai, bi = int(W * a), int(W * b)
    row = Image.new('L', (W, 1))
    row.putdata([0 if x <= ai else 255 if x >= bi else int(255 * (x - ai) / (bi - ai))
                 for x in range(W)])
    img = map_.copy()
    img.paste(photo, (0, 0), row.resize((W, H), Image.NEAREST))
    return img


def v_kart_foto(f):
    """B: kartet går over i flyfotoet, og overgangen ligger AKKURAT til venstre
    for tomta. Venstre tredjedel er planen — den abstrakte, umalte versjonen av
    byen, og det er der merkelappen står. Tomta selv er helt foto, så bilene
    leses. Det er hele poenget: planen har ingenting tegnet der, virkeligheten
    er full av parkerte biler."""
    img = _crossfade(f, 0.08, 0.35)
    return outline(img, f)


def v_kart_foto_bred(f):
    """B2: samme idé, men overgangen går tvers over tomta. Da ligger planen og
    fotoet oppå hverandre der det gjelder — tomta er halvt tegnet, halvt
    virkelig. Vakrere, men bilene blir svakere."""
    img = _crossfade(f, 0.30, 0.66)
    return outline(img, f)


def v_innfelling(f):
    """C: flyfoto i full flate, med gråtonekartet som et innfelt kort oppe til
    høyre. Kortet gir den store sammenhengen — hvor i byen dette er — uten å
    ta plassen fotoet trenger."""
    img = orto(f, YEAR)
    darken_outside(img, f, amount=0.26)
    outline(img, f)

    cw, ch = 760, 475
    wide = Frame(cw, ch, 0.62, site_center(), 0.5, 0.5)   # ca. 470x295 m
    card = graatone(wide)
    pts = [(x * SS, y * SS) for x, y in wide.poly_px(SITE)]
    ov = Image.new('RGBA', (cw * SS, ch * SS), (0, 0, 0, 0))
    ImageDraw.Draw(ov).line(pts + [pts[0]], fill=RED + (255,), width=5 * SS, joint='curve')
    card.paste(Image.new('RGB', (cw, ch), RED), (0, 0),
               ov.resize((cw, ch), Image.LANCZOS).split()[3])

    bw = 12                                   # hvit ramme, som .frame i temaet
    plate = Image.new('RGB', (cw + 2 * bw, ch + 2 * bw), (255, 255, 255))
    plate.paste(card, (bw, bw))
    x, y = W - plate.width - 96, 96
    sh = Image.new('L', (W, H), 0)
    ImageDraw.Draw(sh).rectangle([x + 6, y + 10, x + plate.width + 6, y + plate.height + 10], fill=110)
    img.paste(Image.new('RGB', (W, H), (0, 0, 0)), (0, 0), sh.filter(ImageFilter.GaussianBlur(16)))
    img.paste(plate, (x, y))
    return img


def v_flyfoto_lys(_ignored):
    """A2: samme ramme og samme røde strek som «flyfoto», men UTEN dempingen
    utenfor tomta.

    Slide 3 skal vise stedet, ikke peke på tomta — der er hele flata like lys,
    og man ser nabolaget rundt like godt som parkeringsplassen. Dempingen hører
    til slide 4 og 5, der arkitekten og utbyggeren kommer inn og blikket skal
    ligge på tomta og boblene i stedet for på bakgrunnen.

    Bildet skifter altså mellom slide 3 og 4. Det er med vilje: overgangen
    leser som at lyset dempes og rollene trer fram.
    """
    f = frame(**ROLLER)
    return outline(orto(f, YEAR), f)


VARIANTS = {
    'flyfoto': v_flyfoto,
    'flyfoto-lys': v_flyfoto_lys,
    'blankt': v_blankt,
    'kart-foto': v_kart_foto,
    'kart-foto-bred': v_kart_foto_bred,
    'innfelling': v_innfelling,
}

if __name__ == '__main__':
    OUT.mkdir(parents=True, exist_ok=True)
    want = sys.argv[1:] or list(VARIANTS)
    f = frame()
    print(f'utsnitt: {f.describe()}, ortofoto {YEAR}')
    xs = [p[0] for p in f.poly_px(SITE)]
    ys = [p[1] for p in f.poly_px(SITE)]
    print(f'tomta i bildet: x {min(xs):.0f}-{max(xs):.0f}  y {min(ys):.0f}-{max(ys):.0f}')
    fr = frame(**ROLLER)
    xs2 = [q[0] for q in fr.poly_px(SITE)]
    ys2 = [q[1] for q in fr.poly_px(SITE)]
    print(f'ROLLER-ramme: {fr.describe()}')
    print(f'  tomta: x {min(xs2):.0f}-{max(xs2):.0f}  y {min(ys2):.0f}-{max(ys2):.0f}'
          f'  (i slide-px: x {min(xs2)/2:.0f}-{max(xs2)/2:.0f}, y {min(ys2)/2:.0f}-{max(ys2)/2:.0f})')
    for name in want:
        img = VARIANTS[name](frame())
        p = OUT / f'hesthagen-{name}.jpg'
        img.save(p, quality=88, optimize=True, progressive=True)
        print(f'  -> {p.relative_to(OUT.parent.parent.parent.parent)}  {p.stat().st_size/1e6:.2f} MB')
