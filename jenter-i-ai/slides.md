---
marp: true
theme: theme.css
paginate: true
math: katex
---

<!-- _class: title title-photo -->
<!-- _header: '24.09.2026' -->
<!-- paginate: false -->

<!-- FORSIDEN. Bakgrunnen er vindanalysen fra «Analyser i Autodesk Forma».
     Temaet er bygget for byttet: photo-variabelen på section.title-photo
     finnes nettopp for å kunne overstyres her, og standardverdien
     (gløshaugen-streamlines.png) er den forsiden dekket hadde før.

     TITTELEN STÅR IKKE SKREVET HER, med vilje: arrangementets logo SIER
     «Jenter i AI», og en h1 med de samme ordene under den var det samme to
     ganger. Skal teksten tilbake, legg inn «# Jenter i AI» — temaet styler den
     fortsatt (section.title h1 / section.title-photo h1), så den lander nede
     til venstre, i svart.

     paginate: false står her, uten understrek, og gjelder derfor videre
     nedover til «# Jenter i Autodesk» slår den på igjen. Fjerner du linja, får
     forsiden sidetall.

     JiA-logoen står nede til HØYRE. Den ble prøvd nede til
     venstre, der bildet er roligst og utfadingen kunne vært svakere, men
     høyre hjørne ser bedre ut og er valgt. Det koster et tettere hvitt sjikt,
     siden det er der strømlinjene krøller seg sammen i mørkeblå virvler; se
     stilen under.

     To ting å være klar over:

     1. Bildet er 2126x1190 og vises på full flate, altså 1,66x oppskalering.
        Det er under de 2x README-en setter som norm for fullflatebilder
        (gløshaugen-streamlines.png lå på 2,5x). På projektor er det trolig
        greit, men det er det svakeste bildet i dekket på den målestokken.
     2. Motivet er det samme som «Simulering i Forma» viser et nærbilde av
        lenger bak. Det binder åpningen til foredragets kjerne, men det er
        også en gjentakelse: salen har sett strømlinjene før du forklarer
        dem. -->

<style scoped>
/* Bildet, og et tettere hvitt sjikt i hjørnet der JiA-logoen ligger. Alt
   annet, inkludert plasseringen av logoen, arves fra section.title /
   section.title-photo.

   Gradientstabelen er den samme som i theme.css og i samme rekkefølge: hjørnet
   nede til høyre, hjørnet nede til venstre, og bildet nederst. Bare den første
   er endret, på to måter: den er STØRRE (76% x 74% mot temaets 64% x 56%,
   altså 973 x 533 px mot 819 x 403 px) og TETTERE lenger ut (0.97 ved 50% og
   0.62 ved 78%, mot 0.86 og 0.40).

   Tallene er satt mot LOGOEN, ikke mot hjørnet: logoen dekker x 972 til 1216
   og y 438 til 668 på en 1280 x 720-slide. Med ellipsen sentrert i 99%/103%
   ligger logoens øvre kant på 0,57 av den loddrette radien og venstre kant på
   0,30 av den vannrette, altså godt innenfor det første stoppet på 50%. Da er
   flata logoen står på helt hvit, og utfadingen fortsetter et stykke OPP og
   til VENSTRE for den før bildet kommer tilbake.

   Venstre gradient er kopiert uendret fra temaet. Den må være med:
   background-image erstatter hele stabelen, så utelater du den, forsvinner
   sjiktet i venstre hjørne også.

   Radiene er i prosent av slidens bredde og høyde, og stoppene i prosent av
   radien, så de skalerer sammen: skal utfadingen dekke mer, er det 76%/74%
   som skal opp. Skal den bli tettere der den alt dekker, er det stoppet på
   0.62 ved 78%. Setter du 1.0 helt ut, blir hjørnet en hvit flate med en
   synlig kant der bildet begynner igjen. En hvit plate med hårstrek ble prøvd
   først, og forkastet nettopp der: den leste som en klistrelapp oppå bildet i
   stedet for som en del av det. */
section {
  --photo: url('figures/analyser/wind.png');
  background-image:
    radial-gradient(ellipse 76% 74% at 99% 103%,
      rgba(255, 255, 255, 0.99) 0%,
      rgba(255, 255, 255, 0.97) 50%,
      rgba(255, 255, 255, 0.62) 78%,
      rgba(255, 255, 255, 0) 100%),
    radial-gradient(ellipse 78% 62% at 2% 104%,
      rgba(255, 255, 255, 0.95) 0%,
      rgba(255, 255, 255, 0.82) 42%,
      rgba(255, 255, 255, 0.34) 70%,
      rgba(255, 255, 255, 0) 100%),
    var(--photo);
}

/* Absolutt posisjonert, ikke i flyten: section.title er en flex-kolonne som
   pakker fra bunnen og venstrestiller, og den vil ha logoen til venstre. 64 px
   fra høyre er --margin-x, samme marg som Autodesk-logoen oppe til venstre.
   52 px fra bunnen: sidetallet er av på forsiden, så det er bare kanten å
   holde avstand til. */
.event-logo {
  position: absolute;
  right: var(--margin-x);
  bottom: 52px;
  line-height: 0;
}
/* viewBoxen er strammet til motivet i SVG-fila, så denne høyden ER logoens
   høyde — ingen skjult marg å kompensere for. Forholdet er 1,061:1: 230 px høy
   blir 244 px bred, og logoen dekker da x 972-1216 og y 438-668, innenfor der
   sjiktet over er tettest. Blir den mye større, vokser den ut av sjiktet. */
.event-logo img { height: 230px; width: auto; display: block; }
</style>

<div class="event-logo">
  <img src="figures/logos/JiA-logo.svg" alt="Jenter i AI">
</div>

---

<!-- paginate: true -->

# Jenter i Autodesk

<style scoped>

.jenter {
  --k: 1.38;
  display: grid;
  grid-template-columns: max-content max-content;
  justify-content: center;
  align-items: start;
  gap: 190px;
  margin-top: 0.2em;
}

.jente { display: flex; flex-direction: column; align-items: center; }

.jente .photo-cluster {
  width: calc(250px * var(--k));
  height: calc(340px * var(--k));
}
.jente .photo-cluster .family {
  width: calc(250px * var(--k));
  height: calc(250px * var(--k));
  top: 0;
  left: 0;
  right: auto;
}
.jente .photo-cluster .portrait {
  width: calc(125px * var(--k));
  height: calc(125px * var(--k));
  top: calc(212px * var(--k));
  /* (250 - 125) / 2 = 62,5 — sentrert i boksen */
  left: calc(62.5px * var(--k));
  /* Ringen vokser med bildene, ellers blir den en tynn strek på 345 px. */
  box-shadow: 0 0 0 8px var(--paper), 0 0 0 9px rgba(0, 0, 0, 0.08);
}


.jente .kicker { margin: 0.8em 0 0; }

.jente.vilde .photo-cluster .family img { object-position: center 55%; transform: scale(1.4); }
.jente.sunniva .photo-cluster .family img { object-position: center 58%; }
</style>

<div class="jenter">

<div class="jente vilde">
  <div class="photo-cluster">
    <div class="frame family"><img src="figures/people/vilde-2.jpg" alt="Vilde på sandvolleyballbanen"/></div>
    <div class="frame portrait"><img src="figures/people/vilde-3.jpg" alt="Vilde"/></div>
  </div>
  <div class="kicker">Vilde</div>
</div>

<div class="jente sunniva">
  <div class="photo-cluster">
    <div class="frame family"><img src="figures/people/sunniva-2.jpg" alt="Sunniva med familien"/></div>
    <div class="frame portrait"><img src="figures/people/sunniva-color.jpg" alt="Sunniva"/></div>
  </div>
  <div class="kicker">Sunniva</div>
</div>

</div>

<!--
TATT VARE PÅ: kulepunktene og callout-ene som sto på de to gamle slidene.
Ikke slettet, fordi de er ekte innhold — men de står ikke på sliden nå, og
skal fortelles muntlig i stedet. Vil du ha dem tilbake på flata, er de her:

  Vilde
  - Fra indøk til Autodesk
  - Internship som utvikler under studiene
  - Gøy å bygge produkt i stedet for slides
  - Jobbe i en produktorganisasjon
  callout: Jobbe for en mer bærekraftig verden med koding og matte.

  Sunniva
  - fra Fysmat til Autodesk — å gjøre ligninger om til kode
  - Da: skrev et paper som kanskje fem mennesker i verden har lest
  - Nå: også ligninger i et verktøy tusenvis av arkitekter åpner hver dag
  callout: Samme type jobb, men høyere påvirkning i den virkelige verden.
-->

<!-- Say: la hver av dere fortelle selv, kort. Poenget for publikum er at det
     finnes flere veier inn — indøk og Fysmat, ikke datateknikk — og at «jeg
     gikk ikke datateknikk» ikke er en sperre. Punktene står ikke på sliden
     lenger, så de må sies. -->
<!-- TODO ~1:40 -->


---

<!-- _class: demo overlay -->

<!-- Hesthagen-parkeringen, ikke Filipstad. Bildet sto før på et skjermbilde fra
     demofilmen — en tomt i Oslo, med hele Forma-grensesnittet rundt. Det sa
     «programvare» på en slide som skal si «tomt». Nå er det stedet selv: en
     parkeringsplass full av biler, der halve salen har stått.

     Flyfoto fra 2022, siste årgang før anlegget startet. Rød strek er
     tomtegrensa fra OpenStreetMap, ikke tegnet på frihånd.

     Denne sliden bruker -lys-utgaven: hele flata er like lys, så man ser
     nabolaget rundt like godt som parkeringsplassen. Sliden skal vise STEDET.
     Slide 4 og 5 bruker den dempede, der blikket skal ligge på tomta og
     boblene. Bildet skifter altså her — det leser som at lyset dempes og
     rollene trer fram.

     Bildet lages av tools/hesthagen_slide4.py, varianten «flyfoto». Den har
     sin egen ramme (ROLLER i skriptet) der tomta ligger til høyre og litt opp
     — nettopp for at snakkeboblene på de to neste slidene skal få plass til
     venstre uten å dekke den røde streken.

     Slide 4, 5 og 6 deler dette bildet. Det skal IKKE bytte når arkitekten og
     utbyggeren kommer inn; det er oppbyggingen som er poenget. -->

![](figures/tidligfase/hesthagen-flyfoto-lys.jpg)

<style scoped>
/* Tittelen skal stå på ÉN linje. Temaet kapper merkelappen på 72 % av flata og
   h1-en på 64 % av lappen, og «Kunsten å fylle opp en tomt» brakk derfor i to.

   Det er plass: lappen ligger nederst til venstre, og der nede er den røde
   streken trukket tilbake til x≈785, mens lappen trenger ca. 590 px.

   nowrap i tillegg til max-width, så den ikke begynner å brekke igjen hvis
   noen legger til et ord. Blir tittelen mye lengre, stikker den i stedet ut
   mot tomta — da er det tittelen som må kortes, ikke denne regelen som skal
   fjernes. */
.overlay-label { max-width: none; }
.overlay-label h1 { max-width: none; white-space: nowrap; }
</style>

<div class="overlay-label">
  <div class="kicker">Tidligfase</div>
  <h1>Kunsten å fylle opp en tomt</h1>
</div>

<div class="photo-credit">
  Flyfoto 2022 © Geovekst / Trondheim kommune · Kart © Kartverket, CC BY 4.0
</div>

<!-- Say: la bildet stå et øyeblikk før du sier noe. Tomt kvartal, biler der
     halve salen har parkert, ingen streker. Så: «og her begynner spørsmålene.» -->
<!-- TODO ~0:20 -->

---

<!-- _class: demo overlay -->

<!-- Steg 2 av tre på samme bilde: arkitekten kommer inn. Bildet skal IKKE
     bytte — det er oppbyggingen som er poenget, ikke tre forskjellige bilder.

     roles-holder «venstre» klemmer rollene inn i venstre halvdel, så figurene
     ikke legger seg over tomta. Arkitekten står i spalte 1 her og på neste
     slide, så figuren ikke hopper når du klikker.

     SPØRSMÅLENE STO PÅ FLATA FØR, i en snakkeboble over figuren. De er tatt ut
     — boblene tok nesten halve sliden og tvang figuren ned i 140 px. Nå er
     figuren 480 px og spørsmålene dine, ikke slidens. De er tatt vare på her:

       - Hvor skal bygget stå, og hvor høyt kan det bli?
       - Blir det bra her (lys, støy, vind)?

     Skal de tilbake på flata, står oppskriften i theme.css over
     «section.overlay .bubble». -->

![](figures/tidligfase/hesthagen-flyfoto.jpg)

<div class="photo-credit">
  Flyfoto 2022 © Geovekst / Trondheim kommune · Kart © Kartverket, CC BY 4.0
</div>

<div class="roles-holder venstre">
<div class="roles">
<div class="role">
<div class="figure"><img src="figures/tidligfase/rolle-arkitekt-lys.svg" alt=""><span class="name">Arkitekten</span></div>
</div>
</div>
</div>

<!-- Say: «først kommer arkitekten.» Nå står ingenting skrevet, så spørsmålene
     MÅ sies — de to over, i din egen rekkefølge. Vent til figuren har stått et
     øyeblikk; den er stor nok til å bære pausen. -->
<!-- TODO ~0:20 -->

---

<!-- _class: demo overlay -->

<!-- Steg 3: utbyggeren kommer inn ved siden av, i spalte 2 av samme
     venstrestilte bærer. Arkitekten rører seg ikke — samme spalte, samme
     figurhøyde som på forrige slide.

     UTBYGGERENS SPØRSMÅL sto i en snakkeboble her før, som arkitektens. Begge
     er tatt ut av samme grunn; se kommentaren på forrige slide. Tatt vare på:

       - Går regnestykket opp?
       - Hva koster det å ombestemme seg om tre måneder? -->

![](figures/tidligfase/hesthagen-flyfoto.jpg)

<div class="photo-credit">
  Flyfoto 2022 © Geovekst / Trondheim kommune · Kart © Kartverket, CC BY 4.0
</div>

<div class="roles-holder venstre">
<div class="roles">
<div class="role">
<div class="figure"><img src="figures/tidligfase/rolle-arkitekt-lys.svg" alt=""><span class="name">Arkitekten</span></div>
</div>
<div class="role">
<div class="figure"><img src="figures/tidligfase/rolle-utbygger-lys.svg" alt=""><span class="name">Utbyggeren</span></div>
</div>
</div>
</div>

<!-- Say: «og så kommer den som betaler.» Arkitekten spør om form, utbyggeren om
     risiko — begge trenger svar før noe er tegnet ferdig. Spørsmålene deres
     står ikke på sliden lenger, så de to over må sies. Punchlinja «noen få
     uker der nesten alt avgjøres» lander du her. -->
<!-- TODO ~0:25 -->

---

<!-- _class: demo overlay logo-card -->

<!-- Logokortet som rammer inn Forma-delen. Marp-klassen logo-card skjuler vår
     egen Autodesk-logo nederst til venstre, siden kortet alt har et merke midt
     i bildet.

     Kortet var før et stillbilde fra demofilmen — figures/video/stills/logo.jpg,
     som sa «Forma Site Design». To ting var galt: produktet heter Autodesk
     Forma, og fila var 1920x1080 på en fullflate-slide, altså 1,5x av
     slideflata der decket ellers holder 2x.

     Nå er lockupen BYGD av vektor og tekst i stedet for å være et bilde: se
     .forma-lockup i theme.css for målene og for hvorfor det ikke finnes en
     SVG-fil å bruke i stedet. Den er dermed skarp uansett hvor stor skjermen i
     salen er.

     --lw er lockupens bredde og det eneste tallet som skal endres her. 620 px
     er 48 % av slidebredden: stort nok til å lese som et tittelkort, lite nok
     til at det fortsatt er luft rundt. -->

<style scoped>
.forma-lockup { --lw: 620px; }
</style>

<div class="forma-lockup">
  <img class="merke" src="figures/logos/autodesk-logo-white.svg" alt="Autodesk Forma">
  <div class="produkt">Forma</div>
</div>

<!-- Say: ikke stå her. Klikk videre med én gang — kortet er en sceneanvisning,
     ikke en slide. -->
<!-- TODO ~0:05 -->

---

<!-- _class: demo flipbook on-dark eget-merke -->

<!-- Fire slides erstatter de sju flipbook-bildene fra demofilmen. Grunnen er
     oppløsning: de gamle var hentet ut av en 1080p-video, tre på 1920 px og
     fem beskåret til 1344. Disse er skjermbilder rett fra Forma, nedskalert
     til 2560 px — 2x slideflata, altså deckets standard for fullflate-bilder.
     Originalene på 3456 px ligger i site-design/original/.

     on-dark her og ikke på de tre neste: bakgrunnen er verdensrommet, altså
     svart nede til venstre, og da må Autodesk-logoen og sidetallet være hvite.
     De tre andre har Formas lyse sidepanel i det hjørnet. -->

![](figures/site-design/velg-geolokasjon.png)

<div class="demo-label">
<div class="kicker">Stedet</div>
Velg adresse
</div>

---

<!-- _class: demo flipbook eget-merke -->

![](figures/site-design/bestill-data.png)

<div class="demo-label">
<div class="kicker">Kontekst</div>
Velg relevant data
</div>

---

<!-- _class: demo flipbook eget-merke -->

![](figures/site-design/sett-kontekst.png)

<div class="demo-label">
<div class="kicker">Grunnlaget</div>
Sett tomt i kontekst med omgivelser
</div>

---

<!-- _class: demo flipbook eget-merke -->

![](figures/site-design/vis-hesthagen-med-data.png)

<div class="demo-label">
<div class="kicker">Tomten</div>
Planlegg
</div>

---

<!-- _class: demo flipbook eget-merke -->

![](figures/site-design/hesthagen-med-tegning.png)

<div class="demo-label">
<div class="kicker">Forslag</div>
Iterer over utforming
</div>

---

# Analyser i Autodesk Forma

<style scoped>
/* Portrettene oppe til høyre: «det er dette vi jobber med». De ligger i
   overskriftsbåndet, over streken under h1-en, så de ikke stjeler plass fra
   rutenettet under. 58 px er valgt så de får plass mellom margin-top og streken.
   Sirklene overlapper litt — det leses som «vi to», ikke som to løsrevne bilder.
   Den hvite ringen skiller dem fra hverandre der de overlapper. */
.working-on {
  position: absolute;
  right: var(--margin-x);
  top: 46px;
  display: flex;
  align-items: center;
  gap: 0.85em;
}
.working-on span {
  font-size: 0.58em;
  font-weight: 500;
  letter-spacing: 0.05em;
  text-transform: uppercase;
  color: var(--muted);
  text-align: right;
  line-height: 1.35;
  /* Bredt nok til at <br>-en styrer brekket, ikke innpakkingen. */
  max-width: 11em;
}
.working-on .faces { display: flex; flex: none; }
.working-on .faces img {
  width: 58px;
  height: 58px;
  border-radius: 50%;
  object-fit: cover;
  background: #ECEEEF;
  display: block;
  box-shadow: 0 0 0 3px var(--paper), 0 0 0 4px rgba(0, 0, 0, 0.10);
}
.working-on .faces img + img { margin-left: -14px; }
.cols-3 .card {
  padding: 0;
  overflow: hidden;
  align-self: start;
  border-top: 1px solid var(--rule);
}
.cols-3 .card img {
  display: block;
  width: 100%;
  /* 6.6em, ikke 7: bildeteksten under rutenettet trenger luft mot logoen. */
  height: 6.6em;
  object-fit: cover;
}
.cols-3 .card .figcap {
  padding: 0.5em 0.7em;
  margin: 0;
}
</style>

<div class="working-on">
  <div class="faces">
    <img src="figures/people/vilde-3.jpg" alt="Vilde">
    <img src="figures/people/sunniva-color.jpg" alt="Sunniva">
  </div>
</div>

<div class="cols-3">

<div class="card">
<img src="figures/analyser/noise.png" alt="Støy">
<div class="figcap"><span class="figref">Støy</span></div>
</div>

<div class="card">
<img src="figures/analyser/solar-energy.png" alt="Solenergi">
<div class="figcap"><span class="figref">Solenergi</span></div>
</div>

<div class="card">
<img src="figures/analyser/daylight.png" alt="Dagslys">
<div class="figcap"><span class="figref">Dagslys</span></div>
</div>

<div class="card">
<img src="figures/analyser/microclimate.png" alt="Mikroklima">
<div class="figcap"><span class="figref">Mikroklima</span></div>
</div>

<div class="card">
<img src="figures/analyser/sun.png" alt="Sol">
<div class="figcap"><span class="figref">Sol</span></div>
</div>

<div class="card">
<img src="figures/analyser/wind.png" alt="Vind">
<div class="figcap"><span class="figref">Vind</span></div>
</div>

</div>


<!-- Say: seks analyser, samme modell, samme ettermiddag. La dem se bredden
     her — ikke pek på noen enkelt ennå. Neste slide er den samme, med vind
     markert, og da tar du valget for dem. -->
<!-- TODO ~0:40 -->

---

# Analyser i Autodesk Forma

<style scoped>
/* Portrettene oppe til høyre: «det er dette vi jobber med». De ligger i
   overskriftsbåndet, over streken under h1-en, så de ikke stjeler plass fra
   rutenettet under. 58 px er valgt så de får plass mellom margin-top og streken.
   Sirklene overlapper litt — det leses som «vi to», ikke som to løsrevne bilder.
   Den hvite ringen skiller dem fra hverandre der de overlapper. */
.working-on {
  position: absolute;
  right: var(--margin-x);
  top: 46px;
  display: flex;
  align-items: center;
  gap: 0.85em;
}
.working-on span {
  font-size: 0.58em;
  font-weight: 500;
  letter-spacing: 0.05em;
  text-transform: uppercase;
  color: var(--muted);
  text-align: right;
  line-height: 1.35;
  /* Bredt nok til at <br>-en styrer brekket, ikke innpakkingen. */
  max-width: 11em;
}
.working-on .faces { display: flex; flex: none; }
.working-on .faces img {
  width: 58px;
  height: 58px;
  border-radius: 50%;
  object-fit: cover;
  background: #ECEEEF;
  display: block;
  box-shadow: 0 0 0 3px var(--paper), 0 0 0 4px rgba(0, 0, 0, 0.10);
}
.working-on .faces img + img { margin-left: -14px; }
.cols-3 .card {
  padding: 0;
  overflow: hidden;
  align-self: start;
  border-top: 1px solid var(--rule);
}
.cols-3 .card img {
  display: block;
  width: 100%;
  /* 6.6em, ikke 7: bildeteksten under rutenettet trenger luft mot logoen. */
  height: 6.6em;
  object-fit: cover;
}
.cols-3 .card .figcap {
  padding: 0.5em 0.7em;
  margin: 0;
}
/* Vindkortet er markert med en ramme rundt selve kortet, ikke en ellipse rundt
   det. outline og ikke border: outline tar ikke plass i rutenettet, så de seks
   kortene står like store og på samme linje som uten markeringen.

   Fargen er --accent, deckets aksentblå. Den var #0A42D7 før — plukket fra
   kjernen av strømlinjene i vindbildet — men et eget blått som ikke finnes
   noe annet sted i decket leser som en tredje farge, ikke som deckets måte å
   peke på noe. Aksentblå sier «dette er den vi følger videre» med samme
   stemme som kickerne og AI-kortene. */
.cols-3 .card.ring {
  position: relative;
  outline: 3px solid var(--accent);
  outline-offset: 3px;
}
</style>

<div class="working-on">
  <div class="faces">
    <img src="figures/people/vilde-3.jpg" alt="Vilde">
    <img src="figures/people/sunniva-color.jpg" alt="Sunniva">
  </div>
</div>

<div class="cols-3">

<div class="card">
<img src="figures/analyser/noise.png" alt="Støy">
<div class="figcap"><span class="figref">Støy</span></div>
</div>

<div class="card">
<img src="figures/analyser/solar-energy.png" alt="Solenergi">
<div class="figcap"><span class="figref">Solenergi</span></div>
</div>

<div class="card">
<img src="figures/analyser/daylight.png" alt="Dagslys">
<div class="figcap"><span class="figref">Dagslys</span></div>
</div>

<div class="card">
<img src="figures/analyser/microclimate.png" alt="Mikroklima">
<div class="figcap"><span class="figref">Mikroklima</span></div>
</div>

<div class="card">
<img src="figures/analyser/sun.png" alt="Sol">
<div class="figcap"><span class="figref">Sol</span></div>
</div>

<div class="card ring">
<img src="figures/analyser/wind.png" alt="Vind">
<div class="figcap"><span class="figref">Vind</span></div>
</div>

</div>


<!-- Say: «og det er denne ene vi skal bruke resten av tiden på.» Hold på
     rammen et øyeblikk før du går videre — det er her vindfortellingen
     begynner. Ikke forklar hvorfor vind ennå; det kommer på neste slide. -->
<!-- TODO ~0:15 -->

---

<!-- _class: comfort-map -->

<!-- Trinn 1 av 4: kartet alene. Merkelappene kommer én av gangen på de tre
     neste slidene, som er identiske bortsett fra dem — samme grep som
     rollekortene på tomt-sliden og stigen lenger bak. Marp har ingen
     fragmenter, så oppbygging gjøres ved å duplisere sliden.

     Bildet, skalaen og alt annet MÅ være likt på alle fire, ellers hopper det
     når du klikker. Retter du noe her, rett det samme på trinn 2–4. -->

# Vindkomfort

<div class="use">

<div class="map">

<img src="figures/vind/windcomfortgløs2.png" alt="Komfortkart for vind over Gløshaugen, sett på skrå: uterommene mellom byggene er i hovedsak grønne, med gule flater i de åpne partiene og enkelte oransje felt">

</div>

<div class="side">

<div class="legend">
<div class="kicker">Komfortskalaen</div>

<div class="row"><span class="sw" style="background:#B2F8DA"></span><div><b>Sitte</b><span class="t">under 2,5 m/s</span></div></div>
<div class="row"><span class="sw" style="background:#55DCA2"></span><div><b>Stå</b><span class="t">over 2,5 m/s</span></div></div>
<div class="row"><span class="sw" style="background:#FED52A"></span><div><b>Rusle</b><span class="t">over 4 m/s</span></div></div>
<div class="row"><span class="sw" style="background:#FFA900"></span><div><b>Gå</b><span class="t">over 6 m/s</span></div></div>
<div class="row"><span class="sw" style="background:#FF463A"></span><div><b>Ukomfortabelt</b><span class="t">over 8 m/s</span></div></div>
</div>
</div>

</div>

<!-- Say: la kartet stå alene et øyeblikk. «Dette er svaret — ett kart over
     hele tomta.» Gi salen tid til å se fargene og kjenne igjen stedet før du
     begynner å forklare. Så klikker du, og merkelappene kommer på. -->
<!-- TODO ~0:10 -->

---
<!-- _class: comfort-map -->

<!-- Trinn 2 av 4: første merkelapp. Kartet er nå bygget opp over fire slides —
     først kartet alene, så én merkelapp av gangen. Samme grep som rollekortene
     på tomt-sliden: Marp har ingen fragmenter, så oppbygging gjøres ved å
     duplisere sliden.

     Bildet, skalaen og alt annet MÅ være likt på alle fire, ellers hopper det
     når du klikker. Retter du noe her, rett det samme på de andre tre.

     Prosentene i .pin-ene er lest av fargene i windcomfortgløs2.png og
     verifisert mot pikslene: ring 1 ligger på Rusle (gult), ring 2 på Sitte
     (lysegrønt) og ring 3 på Gå (oransje). Byttes bildet, må de sjekkes på nytt. -->

# Vindkomfort

<div class="use">

<div class="map">

<img src="figures/vind/windcomfortgløs2.png" alt="Komfortkart for vind over Gløshaugen, sett på skrå: uterommene mellom byggene er i hovedsak grønne, med gule flater i de åpne partiene og enkelte oransje felt">

<div class="pin" style="left: 21%; top: 15%;">
  <span class="dot"></span>
  <span class="lbl"><b>Åpent område</b><span>Ingenting bremser vinden.</span></span>
</div>

</div>

<div class="side">

<div class="legend">
<div class="kicker">Komfortskalaen</div>

<div class="row"><span class="sw" style="background:#B2F8DA"></span><div><b>Sitte</b><span class="t">under 2,5 m/s</span></div></div>
<div class="row"><span class="sw" style="background:#55DCA2"></span><div><b>Stå</b><span class="t">over 2,5 m/s</span></div></div>
<div class="row"><span class="sw" style="background:#FED52A"></span><div><b>Rusle</b><span class="t">over 4 m/s</span></div></div>
<div class="row"><span class="sw" style="background:#FFA900"></span><div><b>Gå</b><span class="t">over 6 m/s</span></div></div>
<div class="row"><span class="sw" style="background:#FF463A"></span><div><b>Ukomfortabelt</b><span class="t">over 8 m/s</span></div></div>
</div>
</div>

</div>

<!-- Say: her leser du kartet for salen, ett sted av gangen. Tre steder, ikke
     flere — resten ser de selv.

     Det åpne området først: ingenting står i veien, så vinden får fart. Gult
     betyr at det er fint å gå gjennom, ikke å bli sittende. -->
<!-- TODO ~0:12 -->

---
<!-- _class: comfort-map -->

<!-- Trinn 3 av 4: første og andre merkelapp. Alt utenom .pin-ene skal være
     identisk med de andre tre trinnene — se kommentaren på trinn 2. -->

# Vindkomfort

<div class="use">

<div class="map">

<img src="figures/vind/windcomfortgløs2.png" alt="Komfortkart for vind over Gløshaugen, sett på skrå: uterommene mellom byggene er i hovedsak grønne, med gule flater i de åpne partiene og enkelte oransje felt">

<div class="pin" style="left: 21%; top: 15%;">
  <span class="dot"></span>
  <span class="lbl"><b>Åpent område</b><span>Ingenting bremser vinden.</span></span>
</div>

<div class="pin" style="left: 62%; top: 51%;">
  <span class="dot"></span>
  <span class="lbl"><b>I le av byggene</b><span>Vinden blokkeres av byggene rundt.</span></span>
</div>

</div>

<div class="side">

<div class="legend">
<div class="kicker">Komfortskalaen</div>

<div class="row"><span class="sw" style="background:#B2F8DA"></span><div><b>Sitte</b><span class="t">under 2,5 m/s</span></div></div>
<div class="row"><span class="sw" style="background:#55DCA2"></span><div><b>Stå</b><span class="t">over 2,5 m/s</span></div></div>
<div class="row"><span class="sw" style="background:#FED52A"></span><div><b>Rusle</b><span class="t">over 4 m/s</span></div></div>
<div class="row"><span class="sw" style="background:#FFA900"></span><div><b>Gå</b><span class="t">over 6 m/s</span></div></div>
<div class="row"><span class="sw" style="background:#FF463A"></span><div><b>Ukomfortabelt</b><span class="t">over 8 m/s</span></div></div>
</div>
</div>

</div>

<!-- Say: le-sonen mellom byggene: det er her uterommet skal ligge. Lyst grønt er
     «sitte» — kaffen står i ro. Sett den opp mot det åpne feltet du nettopp
     snakket om; kontrasten er hele poenget. -->
<!-- TODO ~0:10 -->

---
<!-- _class: comfort-map -->

<!-- Trinn 4 av 4: alle tre merkelappene på. Alt utenom .pin-ene skal være
     identisk med de andre tre trinnene — se kommentaren på trinn 2. -->

# Vindkomfort

<div class="use">

<div class="map">

<img src="figures/vind/windcomfortgløs2.png" alt="Komfortkart for vind over Gløshaugen, sett på skrå: uterommene mellom byggene er i hovedsak grønne, med gule flater i de åpne partiene og enkelte oransje felt">

<div class="pin" style="left: 21%; top: 15%;">
  <span class="dot"></span>
  <span class="lbl"><b>Åpent område</b><span>Ingenting bremser vinden.</span></span>
</div>

<div class="pin" style="left: 62%; top: 51%;">
  <span class="dot"></span>
  <span class="lbl"><b>I le av byggene</b><span>Vinden blokkeres av byggene rundt.</span></span>
</div>

<div class="pin" style="left: 22%; top: 74%;">
  <span class="dot"></span>
  <span class="lbl"><b>Mellom to bygg</b><span>Vinden presses gjennom og akselererer.</span></span>
</div>

</div>

<div class="side">

<div class="legend">
<div class="kicker">Komfortskalaen</div>

<div class="row"><span class="sw" style="background:#B2F8DA"></span><div><b>Sitte</b><span class="t">under 2,5 m/s</span></div></div>
<div class="row"><span class="sw" style="background:#55DCA2"></span><div><b>Stå</b><span class="t">over 2,5 m/s</span></div></div>
<div class="row"><span class="sw" style="background:#FED52A"></span><div><b>Rusle</b><span class="t">over 4 m/s</span></div></div>
<div class="row"><span class="sw" style="background:#FFA900"></span><div><b>Gå</b><span class="t">over 6 m/s</span></div></div>
<div class="row"><span class="sw" style="background:#FF463A"></span><div><b>Ukomfortabelt</b><span class="t">over 8 m/s</span></div></div>
</div>
</div>

</div>

<!-- Say: passasjen mellom to bygg: vinden presses gjennom et trangere tverrsnitt
     og akselererer. Det er den effekten folk kjenner uten å kunne forklare, og
     den eneste måten å fikse den er å endre byggene — ikke å sette opp en
     skjerm etterpå.

     Poenget å lande, nå som alle tre står på: arkitekten trenger ikke tallene.
     Hun trenger å se hvor det er grønt før volumene er låst. -->
<!-- TODO ~0:15 -->

---

<!-- _class: ladder -->

# Hvordan analyserer arkitekten vinden?

<div class="steps">

<div class="card past">
  <div class="kicker">Før</div>
  <img src="figures/modeller/modell-ekspert.svg" alt="">
  <p class="name">Vindekspert</p>
  <p class="clock">Uker</p>
</div>

<div></div>

<div></div>

</div>

<!-- Say: før måtte du leie inn noen. Vindanalyse var en konsulenttjeneste:
     du bestilte den, og du ventet. Den kom sent i prosjektet, den kom én
     gang, og den fortalte deg om det du alt hadde bestemt var greit. -->
<!-- TODO ~0:10 -->

---

<style scoped>
section { font-size: 22px; }

/* De to ingrediensene i oppskriften, med et plusstegn mellom. Resultatkortet er
   tatt ut: komfortkartet er alt vist på de fire slidene rett foran, og en
   fjerde visning av det samme bildet forteller salen ingenting nytt.
   Plusstegnet er en egen kolonne i rutenettet og ikke en marg, så de to kortene
   blir like brede uansett hvor mye tekst de har. Faste kolonnebredder og
   justify-content: center, ikke 1fr: med bare to kort ville 1fr strukket hvert
   kort over en halv slide, og miniatyrene med. */
.recipe {
  display: grid;
  grid-template-columns: 408px 46px 408px;
  justify-content: center;
  gap: 0.9em;
  align-items: stretch;
  /* Samme margin og korthøyde som section.ladder: dette er samme slags slide
     — trinn på rad — og de tre ladder-slidene kommer rett etter. Holder de
     samme mål, leses de som én figur som bygges videre på. */
  margin: 1.7em 0 0;
}

.recipe .card {
  display: flex;
  flex-direction: column;
  padding: 1.1em 1.1em 1.2em;
}
/* Miniatyrene: fast høyde, så de to boksene er like store uansett hvilket
   format kildefila har. 324 px, opp fra 185: kortene har bare en tittel over
   figuren nå, og all plassen teksten ga fra seg skal figurene ha — de er det
   salen faktisk leser herfra. Overflow: hidden er bare et sikkerhetsnett nå;
   ingen av de to figurene beskjæres lenger.

   Tittelen står OVER figuren, ikke under: med den under fløt den langt nede i
   kortet, løsrevet fra figuren, fordi begge figurfilene har rikelig med luft i
   bunnen selv. Over figuren leses ordet først og bildet etterpå — samme
   rekkefølge som kickeren på ladder-kortene rett etter. Derfor ingen
   margin-bottom her, og ingen min-height på kortet: høyden er tittel + figur. */
.recipe .thumb {
  position: relative;
  /* 360 px = bredden på miniatyren i en 408 px bred kortspalte (408 minus 2 ×
     1,1em padding), altså en kvadratisk boks. Retningsfiguren har kvadratisk
     viewBox nettopp for å passe her uten at preserveAspectRatio skalerer den
     ned — så kortbredden og denne høyden MÅ endres i par.

     Opp fra 324/340: kortene stod på 340 px mens denne stod på 324, og da var
     boksen 292 bred og 324 høy — ikke kvadratisk, så retningsfiguren ble
     klippet 16 px inn på hver side. Nå stemmer de igjen, og siden det var
     ~190 px ubrukt flate på hver side av rutenettet er det samtidig den
     billigste måten å gjøre figurene større: alt i dem vokser 11 %. */
  height: 360px;
  overflow: hidden;
}
.recipe .thumb img { position: absolute; top: 0; left: 0; width: 100%; display: block; }

/* Retningsfiguren er to lag: tomta sett ovenfra i en sirkel, og pilene oppå.
   Begge er sentrert og skalert etter HØYDEN til boksen, så de holder seg på
   hverandre uansett hvor bred kortspalten blir.

   Ringen i SVG-en er borte, så prosenten her er ikke lenger låst til en radius
   i fila. Det eneste kravet er at fotoet holder seg innenfor pilspissene:
   de står på radius 110 av den 312 brede viewBoxen, altså 70,5 % i diameter.
   67 % gir ~5 enheter klaring ned til spissene — går du høyere, legger fotoet
   seg under pilene. */
.recipe .thumb.dirs img {
  width: auto;
  height: 100%;
  left: 50%;
  transform: translateX(-50%);
}
.recipe .thumb.dirs img.site {
  height: 67%;
  top: 50%;
  aspect-ratio: 1;
  border-radius: 50%;
  object-fit: cover;
  transform: translate(-50%, -50%);
}
/* Vindrosefila er stående: rosen øverst og fartsfordelingen under. Begge skal
   med — rosen sier hvilken retning det blåser fra, kurven under hvor hardt, og
   det er to av tre ord i korttittelen. Bildet skaleres derfor etter høyden og
   sentreres, ikke beskjæres. */
.recipe .thumb.rose img {
  width: auto;
  height: 100%;
  left: 50%;
  transform: translateX(-50%);
}

/* Korttitlene er grå og litt større enn før: grå fordi de er merkelapper på
   figurene under, ikke påstander i seg selv — svart ga dem samme vekt som
   tittelen øverst — og større fordi de skal leses fra bakerste rad likevel. */
.recipe h3 {
  font-size: 1.45em;
  margin: 0 0 0.7em;
  color: var(--muted);
}
.recipe p { margin: 0; font-size: 0.86em; line-height: 1.45; color: var(--muted); }
/* Plusstegnet står for «og», som på result-build-slidene. Grått, som
   korttitlene: det er skilletegn mellom de to ingrediensene, ikke et av dem. */
.recipe .plus {
  align-self: center;
  text-align: center;
  font-family: var(--display);
  font-weight: 700;
  font-size: 2.4em;
  line-height: 1;
  color: var(--muted);
}
</style>

# Hvordan beregner vi vindkomfort?

<div class="recipe">

<div class="card">
  <h3>Simulering</h3>
  <div class="thumb dirs">
    <img class="site" src="figures/gløshaugenfromabove.png" alt="">
    <img src="figures/vind/vindretninger-plan.svg" alt="Gløshaugen sett ovenfra, med piler som peker inn mot tomta fra åtte vindretninger">
  </div>
</div>

<div class="plus">+</div>

<div class="card">
  <h3>Historisk data</h3>
  <div class="thumb rose"><img src="figures/vind/vindrose.png" alt="Vindrose for stedet: åtte sektorer med hvor stor andel av tiden det blåser fra hver retning, sørvest størst med 22 prosent"></div>
</div>

</div>

<!-- Say: oppskriften i tre trinn, før figurene på neste slide.

     Trinn 1 og 2 er ingrediensene, trinn 3 er svaret — les plusstegnet og pila
     høyt, så følger salen regnestykket.

     Poenget som er verdt å stoppe på: simuleringen alene sier ingenting om
     komfort. Den sier hva vinden GJØR hvis den kommer fra nordvest. Det er
     først når du vet hvor ofte den faktisk gjør det, at du kan si om et sted
     er lunt. Derfor er de historiske dataene ikke en detalj — uten dem har du
     åtte bilder og ingen konklusjon. -->
<!-- TODO ~0:25 -->
---

<!-- Simuleringen forklart der den hører hjemme: rett etter stigen, mens
     «Simulering — timer» fortsatt henger i salen.

     Tittelen er «Simulering i Forma» med «Fysikkmodell» under — de samme to
     ordene som står på stigekortet, så salen slipper å lære nye ord. Denne sliden og «Estimat i
     Forma» lenger bak er de to forklarings-slidene, én per modell, og de skal
     leses som et par: samme tittelkort, samme ikoner som på stigen og i
     oppsummeringen. Bytter du den ene, bytt den andre.

     Tre ting på sliden: bildet er hva vinden GJØR, likningene er hva maskinen
     regner på, og kostnadslinja er hvorfor det tar timer. Bildet er argumentet
     og står størst. Likningene skal ikke leses fra salen — de skal veie.

     Ligningen er den stasjonære RANS-en simpleFoam løser, med vårt eget
     vegetasjonsledd (c_d a |U| U). Den er flyttet hit fra den gamle «Slik
     regner vi det ut»-sliden, som nå ligger i baklomma nederst i fila. -->

<div class="mhead">
  <h1>Simulering i Forma</h1>
  <div class="mhead-row">
    <img src="figures/modeller/modell-cfd.svg" alt="">
    <p class="sub">Fysikkmodell</p>
  </div>
</div>

<style scoped>
section { font-size: 22px; }

/* Tittelkortet (.mhead) er felles for denne sliden og «Estimat i Forma», og
   reglene står i theme.css. Ikonet her er modell-cfd.svg. */

/* Ingen .lead-regel her lenger: ingressen «Simuleringen løser
   bevegelseslikningene …» er tatt ut, bildet og ligningen sier det samme.
   «Estimat i Forma» har fortsatt sin. */

/* Bildet til venstre, ligningen i en fast spalte til høyre. 440 px og ikke 300:
   ligningen er det ene på sliden som faktisk må kunne leses fra bakerste rad,
   og skriftstørrelsen er låst til spaltebredden — leddene er brutt i markdownen
   under, og blir spalten smalere, bryter KaTeX dem om igjen på egne steder.
   align-items: center, ikke start: «Likningene»-kickeren som holdt kortet oppe
   i flukt med bildets overkant er borte, og uten den er det midten av ligningen
   som skal ligge på midten av bildet. */
.sim {
  display: grid;
  grid-template-columns: minmax(0, 1fr) 440px;
  gap: 1.5em;
  align-items: center;
  margin-top: 1.1em;
}

/* Fila er 1,57:1. Høyden er det som begrenser, ikke bredden: over 400 px legger
   bildeteksten seg ned i Autodesk-logoen. Derfor styrer max-height, og bredden
   følger av formatet — ca. 630 px. margin: 0 og ikke 0 auto: bildet skal ligge
   inntil venstremargen, i flukt med tittelen, ikke sentrert i en
   spalte som er bredere enn det selv. */
.sim img { display: block; width: auto; max-width: 100%; height: auto; max-height: 400px; margin: 0; }

.sim .model { border: 1px solid var(--rule); border-top: 3px solid var(--ink); padding: 0.9em 1em 1em; }
.sim .model .kicker { color: var(--ink); }
/* 0.85em er den største verdien som holder de fire leddene på de fire linjene
   de er brutt på i markdownen, i en 440 px spalte. Går du høyere, bryter KaTeX
   den lengste linja — viskositetsleddet — om igjen midt i en parentes. */
.sim .model .katex-display { margin: 0.2em 0 0; }
.sim .model .katex-display > .katex { font-size: 0.85em; }
/* Kostnaden hører til ligningen, ikke til bildet: den står under likningene, i
   samme kort, skilt med en strek. Den er det ene tallet salen må ha med seg
   videre — «femten forsøk på en ettermiddag» og surrogatmodellen henger begge
   på at dette er dyrt. Den sto bare i talerkommentaren før. */
.sim .model .cost {
  margin: 0.9em 0 0;
  padding-top: 0.75em;
  border-top: 1px solid var(--rule);
  font-size: 0.78em;
  line-height: 1.45;
  color: var(--muted);
}
.sim .model .cost b { color: var(--ink); font-weight: 600; }
</style>

<div class="sim">

<div class="viz">
  <img src="figures/vind/streamlines.png" alt="Strømlinjer fra en vindsimulering med vind fra sørøst: blå baner som deles rundt hovedbygningen, akselererer forbi gavlen og krøller seg sammen i virvler bak byggene">
</div>

<div class="model">

$$
\begin{aligned}
(\mathbf{U}\cdot\nabla)\mathbf{U} \;=\;& -\nabla p \\
&+\; \nabla\cdot\big[(\nu+\nu_t)\big(\nabla\mathbf{U}+\nabla\mathbf{U}^{\top}\big)\big] \\
&-\; c_d\,a\,\lvert\mathbf{U}\rvert\,\mathbf{U} \\[0.3em]
\nabla\cdot\mathbf{U} \;=\;& \;0
\end{aligned}
$$

</div>

</div>

<!-- Say: her er simuleringen, siden du nettopp sa «timer».

     Start med bildet, ikke med ligningen: dette er én retning — vind fra
     sørøst — og hver blå linje er veien en luftpakke tar. Følg én av dem med
     hånda: den deles rundt hovedbygningen, skyter forbi gavlen, og bak byggene
     krøller den seg sammen i virvler. Det er DETTE simuleringen regner ut,
     punkt for punkt i luftrommet over tomta.

     Si «én retning» tydelig — bildet viser sørøst, og det er hele poenget med
     kostnadslinja: gang den opp. Tallet står nå på sliden, så du skal ikke lese
     det opp, du skal regne det ut høyt: åtte retninger, en time eller to hver,
     for det ene komfortkartet de alt har sett.

     Så likningene, og bare som en gest: dette er fysikken den løser. Ikke gå
     gjennom leddene. Det eneste du eventuelt peker på er det siste leddet —
     trær og vegetasjon som bremser vinden — som er vårt eget tillegg.

     Da har salen tallet de trenger til neste steg: åtte retninger x et par
     timer, hver gang du flytter et volum. -->
<!-- TODO ~0:30 -->
---

<!-- _class: ladder -->

# Hvordan analyserer arkitekten vinden?

<div class="steps">

<div class="card past">
  <div class="kicker">Før</div>
  <img src="figures/modeller/modell-ekspert.svg" alt="">
  <p class="name">Vindekspert</p>
  <p class="clock">Uker</p>
</div>

<div></div>

<div></div>

</div>

<!-- Say: før måtte du leie inn noen. Vindanalyse var en konsulenttjeneste:
     du bestilte den, og du ventet. Den kom sent i prosjektet, den kom én
     gang, og den fortalte deg om det du alt hadde bestemt var greit. -->
<!-- TODO ~0:10 -->

---

<!-- _class: ladder -->

# Hvordan analyserer arkitekten vinden?

<div class="steps">

<div class="card past">
  <div class="kicker">Før</div>
  <img src="figures/modeller/modell-ekspert.svg" alt="">
  <p class="name">Vindekspert</p>
  <p class="clock">Uker</p>
</div>

<div class="card">
  <div class="kicker">Med Forma</div>
  <img src="figures/modeller/modell-cfd.svg" alt="">
  <p class="name">Simulering <span class="sub">Fysikkmodell</span></p>
  <p class="clock">Timer</p>
</div>

<div></div>

</div>

<!-- Say: simuleringen i verktøyet var det virkelig store steget, og det er
     verdt å si hvorfor: den er enkel å bruke. Du setter ikke opp et mesh, du
     oppgir ikke randbetingelser — du trykker på en knapp, på geometrien du
     alt har tegnet.

     Det er dét som tar eksperten ut av loopen, ikke bare at det går raskere.
     Vindanalysen i Forma gjorde informasjonen tilgjengelig for arkitekten
     selv. -->
<!-- TODO ~0:12 -->

---
<!-- _class: demo -->

<!-- Femten utsnitt fra samme skjermopptak på Hesthagen-modellen
     (figures/video/hesthagenestimat.mov), samme kamera hver gang: det eneste
     som endrer seg mellom rutene er bebyggelsen og komfortkartet.

     Ingen tittel og full flate: rekka av ruter ER argumentet, og alt som ikke
     er ruter stjeler plass fra dem. Tittelen «Arkitekten kan raskt vurdere
     mange alternativer» sier du i stedet — den sto her før, se talenotatet.
     Rutene er unummererte og uten bildetekst; rekka skal leses som en
     bevegelse, ikke som en liste du kan peke i.

     demo-klassen gir padding 0 og mørk bakgrunn. 5x3 på 1280x720 gir ruter på
     256x240, altså litt høyere enn kilden (3:2), så object-fit: cover skjærer
     noen piksler av sidene. Det tåler bildene — bygget står midt i ruta.

     gap: 4px er streker i --ink mellom rutene. Vil du ha én sammenhengende
     flate i stedet, sett gap: 0 — da flyter naborutene i hverandre der fargene
     er like, og «femten forsøk» blir vanskeligere å telle.

     Logoen må overstyres til den svarte: demo-klassen antar mørkt bilde og
     setter hvit logo, men disse rutene er lyse, så den hvite forsvinner.

     Ta bare bilder der komfortkartet står ferdig tegnet (grønt/gult) — hopp
     over de blå rutene mens den regner, og ruter der en bygning er valgt. -->

<style scoped>
section::before { background-image: url('figures/logos/autodesk-logo-black.svg'); }
section::after { color: var(--muted); }

.iterations {
  display: grid;
  grid-template-columns: repeat(5, 1fr);
  grid-template-rows: repeat(3, 1fr);
  width: 100%;
  height: 100%;
  gap: 4px;
}
.iterations figure { margin: 0; min-height: 0; }
.iterations img {
  display: block;
  width: 100%;
  height: 100%;
  object-fit: cover;
}
</style>

<div class="iterations">


<figure><img src="figures/video/iterations/hesthagen-001.jpg" alt="Lukket kvartal rundt et gårdsrom, komfortkartet grønt inne i gården"></figure>

<figure><img src="figures/video/iterations/hesthagen-002.jpg" alt="To vinkelstilte fløyer, komfortkartet tegnet på nytt"></figure>

<figure><img src="figures/video/iterations/hesthagen-003.jpg" alt="Én lang vinkelstilt lamell langs veien"></figure>

<figure><img src="figures/video/iterations/hesthagen-004.jpg" alt="U-form med et punkthus i nord, gårdsrommet grønt"></figure>

<figure><img src="figures/video/iterations/hesthagen-005.jpg" alt="Buet fløy med punkthus, gårdsrommet nesten helt grønt"></figure>

<figure><img src="figures/video/iterations/hesthagen-006.jpg" alt="Tre frittstående volumer spredt på tomta"></figure>

<figure><img src="figures/video/iterations/hesthagen-007.jpg" alt="Lamell og punkthus vinkelstilt mot hverandre"></figure>

<figure><img src="figures/video/iterations/hesthagen-008.jpg" alt="Vinkelbygg med punkthus, stort grønt uterom"></figure>

<figure><img src="figures/video/iterations/hesthagen-009.jpg" alt="Buet lamell med punkthus, bredt grønt gårdsrom"></figure>

<figure><img src="figures/video/iterations/hesthagen-010.jpg" alt="To parallelle lameller på skrå over tomta"></figure>

<figure><img src="figures/video/iterations/hesthagen-011.jpg" alt="Tre parallelle lameller"></figure>

<figure><img src="figures/video/iterations/hesthagen-012.jpg" alt="Tre forskjøvne lameller"></figure>

<figure><img src="figures/video/iterations/hesthagen-013.jpg" alt="Tre små frittstående volumer, komfortkartet nesten helt grønt"></figure>

<figure><img src="figures/video/iterations/hesthagen-014.jpg" alt="Seks små punkthus i et rutenett"></figure>

<figure><img src="figures/video/iterations/hesthagen-015.jpg" alt="Forskjøvne punkthus i to rekker"></figure>

</div>

<!-- Say: ikke les opp rutene. Tittelen står ikke på sliden lenger, så den må
     sies: «arkitekten kan raskt vurdere mange alternativer — femten forsøk,
     én ettermiddag.» Så peker du på gårdsrommet i den første ruta mot en av de
     siste: gult blir grønt. Poenget er ikke hvilket forslag som vant, det er
     at du rakk å prøve dem alle.

     Stillbilder og ikke video: video spiller ikke i PDF-eksport, se README.
     Bildene er klippet fra skjermopptaket av Hesthagen-modellen. -->
<!-- TODO ~0:40 -->

---

<!-- Broen fra simuleringen til modellen: alle de kjørte simuleringene ER
     treningsdataene. Sliden er med vilje bare to bokser og en pil — den ene
     halvparten er noe vi allerede har, den andre er det vi fikk ut av det.
     Kortene sier bare det aller nødvendigste — «geometri inn, vindfeltet ut»
     og at modellen kjenner igjen i stedet for å regne, sies muntlig.

     Ikonene er de samme to som brukes om modellene ellers i decket (mesh-kuben
     og det nevrale nettet), så de leses som samme par hvis baklomme-slidene om
     surrogatmodellen tas inn igjen. -->

<style scoped>
/* Ingen tittel: «Tusenvis av simuleringer» sa det samme som venstre kort, og
   satte overskrift på ingrediensen i stedet for på overgangen. Den sies
   muntlig, samme grep som på iterasjonsrutene. Uten tittel er det ingenting
   å toppstille mot, så kortene sentreres i flata. */
section { font-size: 22px; justify-content: center; }

/* To bokser og en pil: det vi har, og det vi fikk ut av det. Pila er en egen
   kolonne i rutenettet og ikke en marg, så de to kortene blir like brede — samme
   grep som på «Hvordan beregner vi vindkomfort?». */
.bridge {
  display: grid;
  grid-template-columns: 1fr 46px 1fr;
  gap: 1.2em;
  align-items: stretch;
}

.bridge .card {
  display: flex;
  flex-direction: column;
  padding: 1.2em 1.2em 1.3em;
  min-height: 250px;
}
/* Høyre kort er svaret, ikke enda en ingrediens: aksentblå topplinje og lys
   flate, samme grep som .panel.ai og .card.ai ellers i decket. */
.bridge .card.ai { border-top-color: var(--accent); background: var(--accent-soft); }
.bridge .card.ai h3 { color: var(--accent); }

.bridge .card img { width: 96px; height: 96px; display: block; margin-bottom: 0.9em; }
.bridge h3 { font-size: 1.15em; margin: 0 0 0.35em; }
.bridge p { margin: 0; font-size: 0.88em; line-height: 1.45; color: var(--muted); }
/* Tallet forankret i bunnen, som .clock på stige-slidene: etiketten leses
   først, så faller blikket ned på mengden. */
.bridge .big {
  font-family: var(--display);
  font-weight: 700;
  font-size: 1.5em;
  line-height: 1.15;
  letter-spacing: -0.015em;
  color: var(--ink);
  /* auto-margin dytter ordet ned i bunnen, padding-en holder en luft igjen
     også når teksten over wrapper til to linjer. */
  margin: auto 0 0;
  padding-top: 0.7em;
}
.bridge .card.ai .big { color: var(--accent); }

.bridge .arr { align-self: center; position: relative; height: 3px; background: var(--ink); }
.bridge .arr::after {
  content: '';
  position: absolute;
  top: -6.5px;
  right: -13px;
  width: 0;
  height: 0;
  border-top: 8px solid transparent;
  border-bottom: 8px solid transparent;
  border-left: 13px solid var(--ink);
}
</style>

<div class="bridge">

<div class="card">
  <img src="figures/modeller/modell-cfd.svg" alt="">
  <h3>Det vi har</h3>
  <p>Tusenvis av ferdige simuleringer.</p>
  <p class="big">Treningsdata</p>
</div>

<div class="arr"></div>

<div class="card ai">
  <img src="figures/modeller/modell-surrogat.svg" alt="">
  <h3>Det vi kunne bygge</h3>
  <p>En modell som kjenner igjen hvordan vinden beveger seg.</p>
  <p class="big">Maskinlæringsmodell</p>
</div>

</div>

<!-- Say: her er vendepunktet, og det er verdt å si sakte.

     Simuleringen er dyr, men vi har kjørt den tusenvis av ganger — på ekte
     tomter, i ekte prosjekter. Alle de kjøringene ligger der som ferdige svar:
     denne geometrien gir dette vindfeltet.

     Og det er nettopp det en maskinlæringsmodell trenger. Tusenvis av par av
     spørsmål og svar. Så vi trente en modell på dem, og den kan predikere
     hvordan vinden beveger seg — uten å regne på fysikken i det hele tatt.

     Poenget å understreke hvis du bare får sagt én ting: det er ikke
     nettverket som er arbeidet, det er treningsdataene. Hver gang en kunde
     betaler for den dyre analysen, blir den et eksempel til den raske. -->
<!-- TODO ~0:35 -->
---
<div class="mhead">
  <h1>Estimat i Forma</h1>
  <div class="mhead-row">
    <img src="figures/modeller/modell-surrogat.svg" alt="">
    <p class="sub">Maskinlæringsmodell</p>
  </div>
</div>

<!-- Trinn 1 av 3 i estimat-oppbyggingen. Markupen er den SAMME på alle tre
     slidene — det eneste som skiller dem er klassen på .sg (t1/t2/t3), som
     styrer hvor langt figuren har kommet. Elementene som ikke har kommet ennå
     ligger der og holder plassen, så ingenting flytter seg mellom trinnene.
     Reglene, og hvorfor figuren er bygd i CSS og ikke er et ferdig bilde,
     står under «Estimat-oppbyggingen» i theme.css.

     Retter du på figuren: rett den samme linja på ALLE TRE slidene, ellers
     hopper noe mellom trinnene. Tittelkortet er likt på alle tre, med vilje: salen skal se én slide som vokser, ikke tre nye. -->

<div class="sg t1">
  <div class="inn">
    <p class="lab">Input</p>
    <div class="raster">
      <figure>
        <div class="ring">
          <img src="figures/modeller/predictions/input-hoyde.png" alt="Høyderaster over tomta">
        </div>
        <figcaption>Høyde<div class="ramp"></div></figcaption>
      </figure>
      <figure>
        <div class="ring">
          <img src="figures/modeller/predictions/input-kategori.png" alt="Raster med overflateklasser: terreng, bygg og vegetasjon">
        </div>
        <figcaption>
          <div class="key">
            <span><i style="background:#FFFFFF"></i>Bygg</span>
            <span><i style="background:#CFCFCF"></i>Terreng</span>
            <span><i style="background:#1B7F5A"></i>Vegetasjon</span>
          </div>
        </figcaption>
      </figure>
    </div>
  </div>
  <svg class="pil steg2" width="48" height="12" viewBox="0 0 48 12" aria-hidden="true">
    <path d="M0 6 H40" stroke="currentColor" stroke-width="2.4"/>
    <path d="M38 1 L47 6 L38 11 z" fill="currentColor"/></svg>
  <div class="nett steg2">
    <p class="lab">Nevralt nettverk</p>
    <img src="figures/modeller/modell-surrogat.svg" alt="Nevralt nettverk: tre lag noder bundet sammen av kanter">
  </div>
  <svg class="pil steg3" width="48" height="12" viewBox="0 0 48 12" aria-hidden="true">
    <path d="M0 6 H40" stroke="currentColor" stroke-width="2.4"/>
    <path d="M38 1 L47 6 L38 11 z" fill="currentColor"/></svg>
  <div class="ut steg3">
    <p class="lab">Output</p>
    <div class="panel">
      <div class="disc">
        <img src="figures/modeller/predictions/felt-sv.png" alt="Vindhastighet over tomta, 1,75 meter over bakken">
      </div>
    </div>
  </div>
</div>

<!-- Say: forrige slide sa at alle simuleringene ER treningsdataene. Nå skal
     vi se det samme nettet i bruk — men start med hva som går INN.

     Hele inngangen er dette: høyden på alt som står der, og hva det er —
     bygg, terreng eller vegetasjon. To bilder av tomta.

     Ikke noe mesh. Ingen randbetingelser. Og merk: ingen vindretning i
     inngangen — det kommer vi tilbake til hvis noen spør. -->
<!-- TODO ~0:15 -->

---
<div class="mhead">
  <h1>Estimat i Forma</h1>
  <div class="mhead-row">
    <img src="figures/modeller/modell-surrogat.svg" alt="">
    <p class="sub">Maskinlæringsmodell</p>
  </div>
</div>

<!-- Trinn 2 av 3 i estimat-oppbyggingen. Markupen er den SAMME på alle tre
     slidene — det eneste som skiller dem er klassen på .sg (t1/t2/t3), som
     styrer hvor langt figuren har kommet. Elementene som ikke har kommet ennå
     ligger der og holder plassen, så ingenting flytter seg mellom trinnene.
     Reglene, og hvorfor figuren er bygd i CSS og ikke er et ferdig bilde,
     står under «Estimat-oppbyggingen» i theme.css.

     Retter du på figuren: rett den samme linja på ALLE TRE slidene, ellers
     hopper noe mellom trinnene. Dette er trinnet der pila og nettet slås på. -->

<div class="sg t2">
  <div class="inn">
    <p class="lab">Input</p>
    <div class="raster">
      <figure>
        <div class="ring">
          <img src="figures/modeller/predictions/input-hoyde.png" alt="Høyderaster over tomta">
        </div>
        <figcaption>Høyde<div class="ramp"></div></figcaption>
      </figure>
      <figure>
        <div class="ring">
          <img src="figures/modeller/predictions/input-kategori.png" alt="Raster med overflateklasser: terreng, bygg og vegetasjon">
        </div>
        <figcaption>
          <div class="key">
            <span><i style="background:#FFFFFF"></i>Bygg</span>
            <span><i style="background:#CFCFCF"></i>Terreng</span>
            <span><i style="background:#1B7F5A"></i>Vegetasjon</span>
          </div>
        </figcaption>
      </figure>
    </div>
  </div>
  <svg class="pil steg2" width="48" height="12" viewBox="0 0 48 12" aria-hidden="true">
    <path d="M0 6 H40" stroke="currentColor" stroke-width="2.4"/>
    <path d="M38 1 L47 6 L38 11 z" fill="currentColor"/></svg>
  <div class="nett steg2">
    <p class="lab">Nevralt nettverk</p>
    <img src="figures/modeller/modell-surrogat.svg" alt="Nevralt nettverk: tre lag noder bundet sammen av kanter">
  </div>
  <svg class="pil steg3" width="48" height="12" viewBox="0 0 48 12" aria-hidden="true">
    <path d="M0 6 H40" stroke="currentColor" stroke-width="2.4"/>
    <path d="M38 1 L47 6 L38 11 z" fill="currentColor"/></svg>
  <div class="ut steg3">
    <p class="lab">Output</p>
    <div class="panel">
      <div class="disc">
        <img src="figures/modeller/predictions/felt-sv.png" alt="Vindhastighet over tomta, 1,75 meter over bakken">
      </div>
    </div>
  </div>
</div>

<!-- Say: så går de to bildene inn i nettet. Det er det samme ikonet salen
     har sett på stigen og på bro-sliden — det er den modellen som ble trent
     på de tusenvis av simuleringene.

     Den regner ikke på fysikken. Den kjenner igjen.

     Spør noen hvordan retningen kommer inn når den ikke er en inngang: vi
     roterer geometrien til nettets orientering, kjører, og roterer svaret
     tilbake. Det er med vilje ikke tegnet — det er et implementasjonsdetalj. -->
<!-- TODO ~0:10 -->

---
<div class="mhead">
  <h1>Estimat i Forma</h1>
  <div class="mhead-row">
    <img src="figures/modeller/modell-surrogat.svg" alt="">
    <p class="sub">Maskinlæringsmodell</p>
  </div>
</div>

<!-- Trinn 3 av 3 i estimat-oppbyggingen. Markupen er den SAMME på alle tre
     slidene — det eneste som skiller dem er klassen på .sg (t1/t2/t3), som
     styrer hvor langt figuren har kommet. Elementene som ikke har kommet ennå
     ligger der og holder plassen, så ingenting flytter seg mellom trinnene.
     Reglene, og hvorfor figuren er bygd i CSS og ikke er et ferdig bilde,
     står under «Estimat-oppbyggingen» i theme.css.

     Retter du på figuren: rett den samme linja på ALLE TRE slidene, ellers
     hopper noe mellom trinnene. Dette er trinnet der feltet ut kommer, og figuren er hel. -->

<div class="sg t3">
  <div class="inn">
    <p class="lab">Input</p>
    <div class="raster">
      <figure>
        <div class="ring">
          <img src="figures/modeller/predictions/input-hoyde.png" alt="Høyderaster over tomta">
        </div>
        <figcaption>Høyde<div class="ramp"></div></figcaption>
      </figure>
      <figure>
        <div class="ring">
          <img src="figures/modeller/predictions/input-kategori.png" alt="Raster med overflateklasser: terreng, bygg og vegetasjon">
        </div>
        <figcaption>
          <div class="key">
            <span><i style="background:#FFFFFF"></i>Bygg</span>
            <span><i style="background:#CFCFCF"></i>Terreng</span>
            <span><i style="background:#1B7F5A"></i>Vegetasjon</span>
          </div>
        </figcaption>
      </figure>
    </div>
  </div>
  <svg class="pil steg2" width="48" height="12" viewBox="0 0 48 12" aria-hidden="true">
    <path d="M0 6 H40" stroke="currentColor" stroke-width="2.4"/>
    <path d="M38 1 L47 6 L38 11 z" fill="currentColor"/></svg>
  <div class="nett steg2">
    <p class="lab">Nevralt nettverk</p>
    <img src="figures/modeller/modell-surrogat.svg" alt="Nevralt nettverk: tre lag noder bundet sammen av kanter">
  </div>
  <svg class="pil steg3" width="48" height="12" viewBox="0 0 48 12" aria-hidden="true">
    <path d="M0 6 H40" stroke="currentColor" stroke-width="2.4"/>
    <path d="M38 1 L47 6 L38 11 z" fill="currentColor"/></svg>
  <div class="ut steg3">
    <p class="lab">Output</p>
    <div class="panel">
      <div class="disc">
        <img src="figures/modeller/predictions/felt-sv.png" alt="Vindhastighet over tomta, 1,75 meter over bakken">
      </div>
    </div>
  </div>
</div>

<!-- Say: og ut kommer vindfeltet. Lyst er skjermet, mettet er eksponert.
     Bilde inn, bilde ut — det er hele rammen.

     Feltet her er sørvest-kjøringen, men retningen står ikke på sliden. Si det
     bare hvis noen spør; figuren handler om inn og ut.

     Gjentakelsen sier du, den står ikke på sliden: det samme kjøres for alle
     åtte retningene i én batch — ikke åtte modeller — og vektes med vindrosen
     til komfortkartet de så på Gløshaugen-sliden.

     Har du tid til overs: 8 retninger x noen sekunder mot 8 x flere timer CFD.
     Det er hele poenget med at den kan stå på mens man tegner. -->
<!-- TODO ~0:15 -->

---

<!-- _class: ladder -->

<!-- Kopi av trinn 2 av stigen (den med «Simulering — timer» som siste kort,
     rett før «Simulering i Forma»-sliden) — flata skal være IDENTISK med den,
     ellers hopper stigen når du kommer tilbake til den her. Retter du et kort
     der, rett det samme her.

     Den står her fordi stigen har vært ute av bildet i tre slides (simulering,
     iterasjoner, treningsdata). Publikum trenger å se hvor vi var før trinn 3
     kommer på neste slide. -->

# Hvordan analyserer arkitekten vinden?

<div class="steps">

<div class="card past">
  <div class="kicker">Før</div>
  <img src="figures/modeller/modell-ekspert.svg" alt="">
  <p class="name">Vindekspert</p>
  <p class="clock">Uker</p>
</div>

<div class="card">
  <div class="kicker">Med Forma</div>
  <img src="figures/modeller/modell-cfd.svg" alt="">
  <p class="name">Simulering <span class="sub">Fysikkmodell</span></p>
  <p class="clock">Timer</p>
</div>

<div></div>

</div>

<!-- Say: kort tilbakeblikk, ikke gjenta mesh-forklaringen fra første gang.
     «Her var vi: eksperten tok uker, simuleringen i verktøyet tar timer.» Så
     klikker du, og det tredje trinnet kommer på. -->
<!-- TODO ~0:08 -->

---

<!-- _class: ladder -->

# Hvordan analyserer arkitekten vinden?

<div class="steps">

<div class="card past">
  <div class="kicker">Før</div>
  <img src="figures/modeller/modell-ekspert.svg" alt="">
  <p class="name">Vindekspert</p>
  <p class="clock">Uker</p>
</div>

<div class="card">
  <div class="kicker">Med Forma</div>
  <img src="figures/modeller/modell-cfd.svg" alt="">
  <p class="name">Simulering <span class="sub">Fysikkmodell</span></p>
  <p class="clock">Timer</p>
</div>

<div class="card ai">
  <div class="kicker">Med Forma</div>
  <img src="figures/modeller/modell-surrogat.svg" alt="">
  <p class="name">Estimat <span class="sub">Maskinlæringsmodell</span></p>
  <p class="clock">Sekunder</p>
</div>

</div>

<!-- Say: og så det tredje trinnet. Ikke forklar det her — simuleringen og
     treningsdataene har de alt sett. Pek bare på at estimatet finnes, og si
     «det er dette vi skal se på nå». Neste slide er maskinlæringsmodellen.

     Land det muntlig: når svaret kommer mens du tegner, blir analysen noe du
     tar beslutninger PÅ i designfasen — ikke en rapport som bekrefter et valg
     som alt er tatt.

     Poenget å ta med videre, hvis salen bare husker én ting: når noe blir
     hundre ganger billigere, endrer det ikke bare hvor fort det går. Det
     endrer hvem som får bruke det, og når i prosessen. -->
<!-- TODO ~0:15 -->
---

<!-- Resultatsliden mellom de to modell-forklaringene og byttehandel-plottet.
     «Estimat i Forma»-sliden viser hva modellen GJØR; plottet etterpå
     abstraherer forskjellen til to akser. Denne står imellom og gir salen det
     ene beviset de trenger for at plottet er ærlig: de to kartene ved siden av
     hverandre, samme tomt og samme analyse, det ene simulert og det andre
     estimert. Ser man dem ikke, er «nesten like presis» en påstand.

     Merk at kameraet ikke er helt likt i de to bildene — estimatbildet står
     litt lenger tilbake. Salen leser fargeflatene, ikke utsnittet, så det
     bærer; men skal bildene byttes ut en gang, ta dem fra samme kameravinkel.

     Bildene er 3840x2160 og kommer rett fra Forma, med samme komfortskala som
     Gløshaugen-slidene. De er ikke beskåret. -->

# Ser du forskjellen?

<style scoped>
/* justify-content: start fordi sliden er kortere enn de fleste andre: uten den
   sentrerer Marp innholdet loddrett, og tittelen legger seg et par centimeter
   lavere enn på slidene rundt. Da hopper overskriften når du blar. */
section { font-size: 22px; justify-content: flex-start; }

/* To like brede kort, side ved side. 560 px hver: 2 x 560 + 32 px mellomrom =
   1152 px, som er nøyaktig bredden sliden har mellom margene. Kartene ligger i
   en 560×315 ramme med overflow: hidden og scale() — samme utsnittshøyde som
   før, men zoomet inn på tomten. Estimat-skjermbildet er tatt lenger unna i
   kilden, så det får litt høyere faktor enn simuleringen. */
.compare {
  display: grid;
  grid-template-columns: 560px 560px;
  gap: 32px;
  margin-top: 1.1em;
}

/* Kart først, én etikettstripe under: ikon + navn + undertekst, tida til høyre. */
.compare figure { margin: 0; }
.compare .head {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 1em;
  padding-top: 0.5em;
  margin-top: 0.5em;
  border-top: 2px solid var(--ink);
}
.compare .head .who {
  display: flex;
  align-items: center;
  gap: 0.5em;
  min-width: 0;
}
/* 48 px: lesbart nok for surrogat-ikonet, mindre dominerende enn 60 px over
   et allerede fullt kort. */
.compare .head .who img {
  width: 48px;
  height: 48px;
  display: block;
  flex: none;
}
.compare .labels {
  display: flex;
  flex-direction: column;
  gap: 0.15em;
  min-width: 0;
}
.compare .head .name {
  font-family: var(--display);
  font-weight: 700;
  font-size: 1.1em;
  line-height: 1.15;
  letter-spacing: -0.015em;
}
/* Bruk + presisjon i én setning, som underetiketten på stigekortene. */
.compare .head .sub {
  font-size: 0.8em;
  line-height: 1.3;
  color: var(--muted);
}
.compare .head .time {
  flex: none;
  font-family: var(--display);
  font-weight: 700;
  font-size: 1.05em;
  line-height: 1.15;
  letter-spacing: -0.015em;
  color: var(--muted);
  text-align: right;
}
/* Estimatet er blått her, som på stigen og på byttehandel-plottet: blått er
   modellen vi har laget, svart er fysikken den er trent på. */
.compare .est .head { border-top-color: var(--accent); }
.compare .est .head .name { color: var(--accent); }

.compare .shot {
  width: 560px;
  height: 315px;
  overflow: hidden;
  line-height: 0;
}
.compare .shot img {
  display: block;
  width: 560px;
  height: auto;
  transform-origin: 50% 42%;
}
.compare .sim .shot img { transform: scale(1.32); }
.compare .est .shot img { transform: scale(1.52); }
</style>

<div class="compare">

<figure class="sim">
  <div class="shot">
    <img src="figures/simulation.png" alt="Vindkomfortkart over Gløshaugen fra simuleringen: grønne flater i le mellom byggene, gule felt over de åpne partiene i nord">
  </div>
  <div class="head">
    <div class="who">
      <img src="figures/modeller/modell-cfd.svg" alt="">
      <div class="labels">
        <span class="name">Simulering</span>
        <span class="sub">Dokumentasjon · mer presis</span>
      </div>
    </div>
    <span class="time">1–2 timer</span>
  </div>
</figure>

<figure class="est">
  <div class="shot">
    <img src="figures/estimate.png" alt="Vindkomfortkart over samme område fra maskinlæringsmodellen: de samme grønne og gule feltene, men med mykere overganger og litt mer gult i nord">
  </div>
  <div class="head">
    <div class="who">
      <img src="figures/modeller/modell-surrogat.svg" alt="">
      <div class="labels">
        <span class="name">Estimat</span>
        <span class="sub">Iterasjoner · omtrentlig</span>
      </div>
    </div>
    <span class="time">2–6 sekunder</span>
  </div>
</figure>

</div>

<!-- Say: to kart over samme tomt. Det ene tok et par timer, det andre kom mens
     du tegnet. Ikke si hvilket som er hvilket med en gang — la salen se på dem
     et par sekunder først.

     Poenget er ikke at de er identiske, for det er de ikke: se på de åpne
     feltene i nord, der estimatet legger på litt mer gult, og på kantene
     mellom sonene, som er mykere i estimatet. Det er tilnærmingen som synes.

     Poenget er at konklusjonen er den samme. Uterommet mellom byggene er lunt
     i begge, og de åpne flatene er utsatte i begge. Skal du velge hvor
     inngangen og uteserveringen skal ligge, tar du samme valg av begge to.

     Etikettene sier bruk og presisjon i én linje; tida står til høyre. Si at
     simuleringen er mer presis men tar lengre tid — sekunder mot timer er
     synlig uten at du må lese det opp. -->
<!-- TODO ~0:30 -->

---

# Vi står på stand

<style scoped>
.people-row {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 1.8em;
  margin-top: 1.6em;
}
/* 240 px x 4 + 3 gaper à 47 px = 1012 px av de 1152 px sliden har mellom
   margene. Går portrettene over dette, brekker raden til to linjer. */
.people-row .person-photo .frame { width: 240px; height: 240px; }
.people-row .person-photo span { font-size: 0.7em; }
/* Avslutningslinja: midtstilt under raden, i display-snittet, med luft nok til
   at den leses som en invitasjon og ikke som en bildetekst. */
h2 {
  margin: 1.5em 0 0;
  text-align: center;
  font-family: var(--display);
  font-weight: 700;
  font-size: 1.45em;
  color: var(--ink);
}
</style>

<div class="people-row">

<div class="person-photo">
  <div class="frame"><img src="figures/people/vilde-3.jpg" alt="Vilde"/></div>
  <span>Vilde</span>
</div>

<div class="person-photo">
  <div class="frame"><img src="figures/people/sunniva-color.jpg" alt="Sunniva"/></div>
  <span>Sunniva</span>
</div>

<!-- TODO: legg inn figures/people/elizabeth.jpg -->
<div class="person-photo">
  <div class="frame"></div>
  <span>Elizabeth</span>
</div>

<!-- TODO: legg inn figures/people/guro.jpg -->
<div class="person-photo">
  <div class="frame"></div>
  <span>Guro</span>
</div>

</div>

## Kom og spør oss om alt vi ikke fikk plass til her!

<div class="todo">Portretter av Elizabeth og Guro mangler</div>


<!-- TODO ~0:20 -->

