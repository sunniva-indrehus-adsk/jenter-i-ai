---
marp: true
theme: theme.css
paginate: true
math: katex
---

<!-- _class: title title-photo -->
<!-- _header: '24.09.2026' -->
<!-- paginate: false -->

<!-- TITTELEN STÅR IKKE SKREVET HER, med vilje: arrangementets logo SIER
     «Jenter i AI», og en h1 med samme ordene under den var det samme to ganger.
     Skal teksten tilbake, legg inn «# Jenter i AI» — temaet styler den fortsatt
     (section.title h1 / section.title-photo h1), så den lander nede til venstre
     som før, i svart.

     Logoen står nede til HØYRE. Der er renderingen flat og lys (195,206,215),
     så den mørke vinrøde skriften i logoen leses rent, uten plate bak. Nede til
     venstre ligger det hvite sjiktet som tittelteksten trengte — det står
     igjen, og leses nå som en myk vignett.

     «Building geometries by Geodata AS» var brent inn i bildefila nøyaktig der
     logoen nå står. Den er malt ut (flata var ensfarget, så lappen er usynlig)
     — se README, «Tittelslide med bilde», for hvor krediteringen er flyttet. -->

<style scoped>
/* Absolutt posisjonert, ikke i flyten: section.title er en flex-kolonne som
   pakker fra bunnen og venstrestiller, og den vil ha logoen til venstre. Og
   uten h1 er sliden ellers tom, så det er ingenting å forholde seg til.

   64 px fra høyre er --margin-x, samme marg som Autodesk-logoen oppe til
   venstre. 52 px fra bunnen: sidetallet er skrudd av på tittelsliden, så det er
   bare kanten å holde avstand til.

   INGEN PLATE BAK LOGOEN — den ligger rett på renderingen, som en overlay.
   Det er mulig fordi temaet legger et mykt hvitt sjikt i nedre HØYRE hjørne på
   section.title-photo, nettopp for denne logoen. Uten det sjiktet virker dette
   ikke: Hovedbygningens høyre kant er en hard vertikal strek som går tvers
   gjennom logoen, og håret i logofila er tegnet uten fyll, så kanten skinner
   rett gjennom. Begrunnelsen og målene står ved section.title-photo i
   theme.css — endrer du sjiktet der, sjekk denne sliden på nytt.

   En hvit plate med hårstrek ble prøvd først. Den virket, men leste som en
   klistrelapp oppå bildet i stedet for som en del av det. */
.event-logo {
  position: absolute;
  right: var(--margin-x);
  bottom: 52px;
  line-height: 0;
}
/* viewBoxen er strammet til motivet i SVG-fila, så denne høyden ER logoens
   høyde — ingen skjult marg å kompensere for. Forholdet er 1,061:1, altså
   nesten kvadratisk: 230 px høy blir 244 px bred. Logoen dekker da x 972-1216
   og y 438-668, som er innenfor der sjiktet i temaet er tettest. Blir den mye
   større, vokser den ut av sjiktet og bygningskanten kommer til syne igjen. */
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
  grid-template-columns: 372px 46px 372px;
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
  /* 324 px = bredden på miniatyren i en 372 px bred kortspalte, altså en
     kvadratisk boks. Retningsfiguren har kvadratisk viewBox nettopp for å
     passe her uten at preserveAspectRatio skalerer den ned. */
  height: 324px;
  overflow: hidden;
}
.recipe .thumb img { position: absolute; top: 0; left: 0; width: 100%; display: block; }

/* Retningsfiguren er to lag: tomta sett ovenfra i en sirkel, og pilene oppå.
   Begge er sentrert og skalert etter HØYDEN til boksen, så de holder seg på
   hverandre uansett hvor bred kortspalten blir.

   92/304 av den kvadratiske viewBoxen til vindretninger-plan.svg er radien på
   ringen i fila → diameteren er 60,5 % av boksen. Endres r der, må prosenten
   her følge etter, ellers stikker flyfotoet ut under ringen. */
.recipe .thumb.dirs img {
  width: auto;
  height: 100%;
  left: 50%;
  transform: translateX(-50%);
}
.recipe .thumb.dirs img.site {
  height: 60.5%;
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

.recipe h3 { font-size: 1.05em; margin: 0 0 0.7em; }
.recipe p { margin: 0; font-size: 0.86em; line-height: 1.45; color: var(--muted); }
/* Plusstegnet står for «og», som på result-build-slidene. */
.recipe .plus {
  align-self: center;
  text-align: center;
  font-family: var(--display);
  font-weight: 700;
  font-size: 1.5em;
  line-height: 1;
}
</style>

# Hvordan beregner vi vindkomfort?

<div class="recipe">

<div class="card">
  <h3>Simulering</h3>
  <div class="thumb dirs">
    <img class="site" src="figures/gløshaugenfromabove-utsnitt.png" alt="">
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

<!-- _class: ladder -->

# Hvordan analyserer arkitekten vindforholdene?

<div class="steps">

<div class="card past">
  <div class="kicker">Før</div>
  <p class="name">Ekstern vindekspert</p>
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

# Hvordan analyserer arkitekten vindforholdene?

<div class="steps">

<div class="card past">
  <div class="kicker">Før</div>
  <p class="name">Ekstern vindekspert</p>
  <p class="clock">Uker</p>
</div>

<div class="card">
  <div class="kicker">Med Forma</div>
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

<!-- _class: physics -->

# Hvorfor tar det timer?

<style scoped>
.lead { margin: 0.2em 0 0; font-size: 0.82em; color: var(--muted); max-width: 52em; }
</style>

<p class="lead">Fordi vi ikke slår opp et svar — vi løser bevegelseslikningene for luft, i hver celle i et rutenett over hele tomta, om og om igjen til strømningsbildet står stille.</p>

<div class="eqwrap">

$$
\begin{aligned}
\underbrace{(\mathbf{U}\cdot\nabla)\mathbf{U}}_{\textcolor{#6E6E6E}{\text{vinden frakter seg selv}}} \;=\;& -\underbrace{\nabla p}_{\textcolor{#6E6E6E}{\text{trykkforskjeller}}} \\[0.45em]
&+\; \nabla\cdot\big[\underbrace{(\nu+\nu_t)}_{\textcolor{#6E6E6E}{\text{friksjon og turbulens}}}\big(\nabla\mathbf{U}+\nabla\mathbf{U}^{\top}\big)\big] \\[0.45em]
&-\; \underbrace{c_d\,a\,\lvert\mathbf{U}\rvert\,\mathbf{U}}_{\textcolor{#6E6E6E}{\text{trær og vegetasjon som bremser}}} \\[0.45em]
\underbrace{\nabla\cdot\mathbf{U}}_{\textcolor{#6E6E6E}{\text{luft forsvinner ikke}}} \;=\;& \;0
\end{aligned}
$$

<p class="eqcap">Stasjonær RANS — det samme settet likninger vindeksperten løser. Vegetasjonsleddet er vårt eget tillegg.</p>

</div>

<div class="cost">
  <div class="f"><b>millioner av celler</b><span>rutenettet over tomta</span></div>
  <div class="op">×</div>
  <div class="f"><b>tusenvis av runder</b><span>likningen er ikke-lineær — vi må gjette, regne, gjette bedre</span></div>
  <div class="op">×</div>
  <div class="f"><b>8 vindretninger</b><span>én kjøring per retning</span></div>
  <div class="op">=</div>
  <div class="f tot"><b>1–2 timer</b></div>
</div>

<!-- Say: her er svaret på «hvorfor timer?», og det er verdt å ta, fordi det er
     grunnen til at neste slide finnes.

     Ikke les likningen ledd for ledd. Si hva den ER: dette er fysikken for
     luft i bevegelse, og den har vært kjent i 150 år. Pek på to ting og bare
     to: vegetasjonsleddet — «det er vårt eget, trær bremser vinden» — og
     ikke-lineariteten: vinden frakter seg selv, så du kan ikke løse dette i
     ett trekk. Du gjetter et strømningsbilde, regner ut hvor galt det var,
     gjetter bedre, og gjentar til det slutter å endre seg.

     Så regnestykket nederst, sakte: millioner av celler, ganger tusenvis av
     runder, ganger åtte vindretninger. Det er ikke ett ledd som er dyrt — det
     er multiplikasjonen. Og det lander på én til to timer.

     Poenget å sette igjen: timene er ikke dårlig programmering. De er prisen
     på å regne ut fysikken ordentlig. -->
<!-- TODO ~0:35 -->
<!-- TODO: sjekk det faktiske celletallet i mesh-oppsettet før du sier
     «millioner» fra scenen — bytt til det ekte tallet hvis du har det. -->
---

<!-- Simuleringen forklart der den hører hjemme: rett etter stigen, mens
     «Simulering — timer» fortsatt henger i salen.

     To ting på sliden, og bare to: bildet er hva vinden GJØR, ligningen er hva
     maskinen regner på. Bildet er argumentet og står størst. Ligningen skal
     ikke leses fra salen — den skal veie, og forklare hvorfor det tar timer.

     Ligningen er den stasjonære RANS-en simpleFoam løser, med vårt eget
     vegetasjonsledd (c_d a |U| U). Den er flyttet hit fra den gamle «Slik
     regner vi det ut»-sliden, som nå ligger i baklomma nederst i fila. -->

# Slik simulerer vi vinden

<style scoped>
section { font-size: 22px; }

.lead { margin: 0.2em 0 0; font-size: 0.85em; color: var(--muted); max-width: 52em; }

/* Bildet til venstre, ligningen i en fast spalte til høyre. 380 px og ikke 300:
   ligningen er det ene på sliden som faktisk må kunne leses fra bakerste rad,
   og skriftstørrelsen er låst til spaltebredden — leddene er brutt i markdownen
   under, og blir spalten smalere, bryter KaTeX dem om igjen på egne steder. */
.sim {
  display: grid;
  grid-template-columns: minmax(0, 1fr) 380px;
  gap: 1.5em;
  align-items: start;
  margin-top: 1.1em;
}

/* Fila er 1,57:1. Høyden er det som begrenser, ikke bredden: over 400 px legger
   bildeteksten seg ned i Autodesk-logoen. Derfor styrer max-height, og bredden
   følger av formatet — ca. 630 px. margin: 0 og ikke 0 auto: bildet skal ligge
   inntil venstremargen, i flukt med tittelen og lead-linja, ikke sentrert i en
   spalte som er bredere enn det selv. */
.sim img { display: block; width: auto; max-width: 100%; height: auto; max-height: 400px; margin: 0; }

.sim .model { border: 1px solid var(--rule); border-top: 3px solid var(--ink); padding: 0.9em 1em 1em; }
.sim .model .kicker { color: var(--ink); }
/* 0.72em er den største verdien som holder de fire leddene på de fire linjene
   de er brutt på i markdownen, i en 380 px spalte. Går du høyere, bryter KaTeX
   den lengste linja — viskositetsleddet — om igjen midt i en parentes. */
.sim .model .katex-display { margin: 0.2em 0 0; }
.sim .model .katex-display > .katex { font-size: 0.72em; }
</style>

<p class="lead">Simuleringen regner ut fysikken: hvordan luft faktisk beveger seg rundt og mellom byggene.</p>

<div class="sim">

<div class="viz">
  <img src="figures/vind/streamlines.png" alt="Strømlinjer fra en vindsimulering med vind fra sørøst: blå baner som deles rundt hovedbygningen, akselererer forbi gavlen og krøller seg sammen i virvler bak byggene">
  <div class="figcap">Vind fra sørøst.</div>
</div>

<div class="model">
  <div class="kicker">Fysikkmodellen</div>

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

     Si «én retning» tydelig, og si tallet selv — det står ikke på sliden: én
     til to timer per kjøring, åtte kjøringer for å få komfortkartet de alt har
     sett.

     Så ligningen, og bare som en gest: dette er fysikken den løser. Ikke gå
     gjennom leddene — det står ingen tekst under den, så det er du som bærer
     poenget: den er tung nok til å ta én til to timer, og den må kjøres på
     nytt for hver vindretning.

     Da har salen tallet de trenger til neste steg: åtte retninger x et par
     timer, hver gang du flytter et volum. -->
<!-- TODO ~0:30 -->
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

     Ikonene er de samme to som brukes om modellene ellers i decket (mesh-kuben
     og det nevrale nettet), så de leses som samme par hvis baklomme-slidene om
     surrogatmodellen tas inn igjen. -->

# Tusenvis av simuleringer

<style scoped>
section { font-size: 22px; }

.lead { margin: 0.2em 0 0; font-size: 0.85em; color: var(--muted); max-width: 52em; }

/* To bokser og en pil: det vi har, og det vi fikk ut av det. Pila er en egen
   kolonne i rutenettet og ikke en marg, så de to kortene blir like brede — samme
   grep som på «Hvordan beregner vi vindkomfort?». */
.bridge {
  display: grid;
  grid-template-columns: 1fr 46px 1fr;
  gap: 1.2em;
  align-items: stretch;
  margin-top: 1.6em;
}

.bridge .card {
  display: flex;
  flex-direction: column;
  padding: 1.2em 1.2em 1.3em;
  min-height: 300px;
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
  margin: auto 0 0;
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

<p class="lead">Simuleringen har vært kjørt tusenvis av ganger på tomter over hele verden. Hver kjøring er et eksempel på hvordan vinden beveger seg.</p>

<div class="bridge">

<div class="card">
  <img src="figures/modeller/modell-cfd.svg" alt="">
  <h3>Det vi har</h3>
  <p>Tusenvis av ferdige simuleringer: geometri inn, vindfeltet ut. Hver av dem er et løst regnestykke.</p>
  <p class="big">Treningsdata</p>
</div>

<div class="arr"></div>

<div class="card ai">
  <img src="figures/modeller/modell-surrogat.svg" alt="">
  <h3>Det vi kunne bygge</h3>
  <p>En maskinlæringsmodell trent på resultatet av simuleringene. Den regner ikke på fysikken, men kjenner igjen hvordan vinden beveger seg.</p>
  <p class="big">Vindestimat</p>
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

<!-- _class: ladder -->

<!-- Kopi av trinn 2 av stigen (den med «Simulering — timer» som siste kort,
     rett før «Slik simulerer vi vinden») — flata skal være IDENTISK med den,
     ellers hopper stigen når du kommer tilbake til den her. Retter du et kort
     der, rett det samme her.

     Den står her fordi stigen har vært ute av bildet i tre slides (simulering,
     iterasjoner, treningsdata). Publikum trenger å se hvor vi var før trinn 3
     kommer på neste slide. -->

# Hvordan analyserer arkitekten vindforholdene?

<div class="steps">

<div class="card past">
  <div class="kicker">Før</div>
  <p class="name">Ekstern vindekspert</p>
  <p class="clock">Uker</p>
</div>

<div class="card">
  <div class="kicker">Med Forma</div>
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

# Hvordan analyserer arkitekten vindforholdene?

<div class="steps">

<div class="card past">
  <div class="kicker">Før</div>
  <p class="name">Ekstern vindekspert</p>
  <p class="clock">Uker</p>
</div>

<div class="card">
  <div class="kicker">Med Forma</div>
  <p class="name">Simulering <span class="sub">Fysikkmodell</span></p>
  <p class="clock">Timer</p>
</div>

<div class="card ai">
  <div class="kicker">Med Forma</div>
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


# Maskinlæringsmodellen

<style scoped>
/* Figuren er BYGD HER, ikke et ferdig bilde: bare rasterne, nettikonet og
   feltet er filer (figures/illustrations/), resten er tekst og piler i CSS.
   Da arver etikettene Artifakt og theme.css-fargene, og de kan rettes uten å
   rendre noe på nytt. Kildebildene ligger i vis-surrogate/ — input-*.png fra
   render_map.py, felt-*.png er skjermbilder av analysen. Se CONTEXT.md der.

   Nettet er modell-surrogat.svg, det samme ikonet som stigen og oppsummeringen
   bruker for surrogatmodellen. Det sto en tekstpille her før; ikonet sier det
   samme uten å måtte leses, og binder sliden til resten av dekket.

   Bunnstripen med de åtte retningene er TATT UT. Den gjorde sliden til to
   historier; gjentakelsen er nå bare en setning i Say-notatet. Vil du ha den
   tilbake, står 8-oppstillingen i vis-surrogate/slide.html.

   TO FELLER, begge påvist ved rendring:

   1. De innebygde SVG-ene (pilene) krever --html=true. Marp Core
      slipper som standard bare gjennom en allowlist der div/img/p er med, men
      IKKE svg — uten flagget havner SVG-kilden på sliden som synlig tekst.
      Docker-kommandoen prosjektet kjører har --html=true, så det er dekket.

   2. Målene er i px mot en 1280x720-slide, ikke 1600x900. Høyden er det som
      er trangt: h1 tar ca. 80 px, og theme.css legger på 56 px topp- og 72 px
      bunnmarg. Derfor står de to inn-rasterne SIDE OM SIDE.

   Feltet er SIRKULÆRT i appens utlesning, men skjermbildet har grå bakgrunn
   rundt sirkelen. border-radius: 50% klipper den bort — dropper du det, får
   feltet en grå firkant rundt seg. */

.sg { display: flex; align-items: center; justify-content: center; gap: 34px;
      margin: 18px 0 0; }
.sg .lab { font-size: 16px; font-weight: 700; text-align: center; line-height: 1.3;
           margin: 0; }

/* Inn: to rastere side om side. Ingen retning her — det er hele poenget. */
.sg .inn { display: flex; flex-direction: column; align-items: center; gap: 12px; }
.sg .raster { display: flex; gap: 12px; }
.sg .raster figure { margin: 0; width: 176px; border: 1px solid var(--rule);
                     background: #fff; }
.sg .raster img { display: block; width: 100%; }
.sg .raster figcaption { padding: 6px 8px; border-top: 1px solid var(--rule);
                         font-size: 13px; font-weight: 700; line-height: 1.3; }
.sg .key { display: flex; flex-direction: column; gap: 1px; margin-top: 5px;
           font-weight: 400; font-size: 10.5px; color: var(--muted); }
.sg .key i { width: 8px; height: 8px; display: inline-block; margin-right: 5px; }
/* Høyderampen er den samme sekvensielle teal-skalaen render_map.py bruker. */
.sg .ramp { width: 100%; height: 8px; margin-top: 6px;
            background: linear-gradient(90deg,#F2F6F4,#CFE0DC,#96C0BA,#4E9490,#20666B,#0E3A44); }

.sg .pil { flex: 0 0 auto; color: var(--accent); }

/* Nettet: samme ikon som brukes for surrogatmodellen ellers i dekket. */
.sg .nett { display: flex; flex-direction: column; align-items: center; gap: 10px; }
.sg .nett img { display: block; width: 138px; height: 138px; }

/* Ut: feltet, stort.

   INGEN ZOOM HER, og det er med vilje. Feltene er beskåret til 1441x1441 med
   sirkelen innskrevet (vis-surrogate/crop_circle.py), så 100 % treffer .disc
   eksakt. Skjermbildene var opprinnelig hverken kvadratiske eller like store
   — 1574x1484, 1530x1470, ... — og sirkelen lå tilfeldig i ramma. Da måtte
   bildet skaleres for å dekke ruta, og resultatet var en sirkel som satt
   skjevt og var litt strukket. Legger du inn et nytt skjermbilde: kjør det
   gjennom crop_circle.py først, ikke kompenser med width/height her. */
.sg .ut { display: flex; flex-direction: column; align-items: center; gap: 12px; }
.sg .panel { position: relative; width: 292px; height: 292px; }
.sg .disc { position: absolute; inset: 0; overflow: hidden; border-radius: 50%;
            border: 1px solid var(--rule); background: #fff; }
.sg .disc img { display: block; width: 100%; height: 100%; }
/* Retningen er TATT UT av figuren. Det sto en innstrømningspil på 45 grader
   med en etikett oppe til høyre for feltet, og en nordnål nede til høyre.
   Begge er borte. Feltet er fortsatt nordøst-kjøringen (felt-no.png) —
   retningen er bare ikke merket, så sliden sier «input: geometri, output:
   vindfelt» uten å gjøre et nummer av hvilken retning det er. */
</style>

<div class="sg">
  <div class="inn">
    <div class="raster">
      <figure>
        <img src="figures/modeller/predictions/input-hoyde.png" alt="Høyderaster over tomta">
        <figcaption>Høydeprofil<div class="ramp"></div></figcaption>
      </figure>
      <figure>
        <img src="figures/modeller/predictions/input-kategori.png" alt="Raster med overflateklasser: terreng, bygg og vegetasjon">
        <figcaption>Kategori
          <div class="key">
            <span><i style="background:#C98A2E"></i>Terreng</span>
            <span><i style="background:#6B4FD8"></i>Bygg</span>
            <span><i style="background:#1B7F5A"></i>Vegetasjon</span>
          </div>
        </figcaption>
      </figure>
    </div>
    <p class="lab">Input</p>
  </div>
  <svg class="pil" width="80" height="12" viewBox="0 0 80 12" aria-hidden="true">
    <path d="M0 6 H72" stroke="currentColor" stroke-width="2.4"/>
    <path d="M70 1 L79 6 L70 11 z" fill="currentColor"/></svg>
  <div class="nett">
    <img src="figures/modeller/modell-surrogat.svg" alt="Nevralt nett: tre lag noder bundet sammen av kanter">
    <p class="lab">Nevralt nett</p>
  </div>
  <svg class="pil" width="80" height="12" viewBox="0 0 80 12" aria-hidden="true">
    <path d="M0 6 H72" stroke="currentColor" stroke-width="2.4"/>
    <path d="M70 1 L79 6 L70 11 z" fill="currentColor"/></svg>
  <div class="ut">
    <div class="panel">
      <div class="disc">
        <img src="figures/modeller/predictions/felt-no.png" alt="Vindhastighet over tomta, 1,75 meter over bakken">
      </div>
    </div>
    <p class="lab">Output</p>
  </div>
</div>

<!-- Say: forrige slide sa at alle simuleringene ER treningsdataene, og
     viste nett-ikonet. Her er det samme nettet i bruk: hva som går inn, og
     hva som kommer ut. Én retning, stor nok til at salen ser feltet.

     Venstre: hele inngangen. Høyden på alt som står der, og hva det er —
     terreng, bygg eller vegetasjon. Ingen mesh, ingen randbetingelser. Og
     merk: ingen vindretning i inngangen.

     Høyre: vindfeltet. Lyst er skjermet, mettet er eksponert. Bilde inn,
     bilde ut — rammen som gjør den forståelig for en AI-sal.

     Retningen står ikke på sliden. Feltet er nordøst-kjøringen, så si det om
     noen spør — men figuren handler om inn og ut, ikke om retninger.

     Gjentakelsen sier du, den står ikke på sliden: det samme kjøres for alle
     åtte retningene i én batch — ikke åtte modeller — og vektes med vindrosen
     til komfortkartet de så på Gløshaugen-sliden.

     Har du tid til overs: 8 retninger x noen sekunder mot 8 x flere timer CFD.
     Det er hele poenget med at den kan stå på mens man tegner.

     Spør noen hvordan retningen kommer inn når den ikke er en inngang: vi
     roterer geometrien til nettets orientering, kjører, og roterer svaret
     tilbake. Det er med vilje ikke tegnet — det er et implementasjonsdetalj. -->
<!-- TODO ~0:40 -->


---

# Simulering eller estimat?

<style scoped>
/* SPREDNINGSPLOTT, bygd i CSS — ingen bildefil. To akser, to punkter:
   presisjon opp, ventetid til høyre. Poenget er at punktene ligger på
   DIAGONALEN: presisjon koster tid. Ingen av dem er «den beste» — de ligger
   på hver sin ende av den samme byttehandelen, og derfor brukes de til hver
   sin jobb.

   MÅLENE ER I PX mot en 1280x720-slide. Høyden er det trange: 720 px minus
   56 px toppmarg og 72 px bunnmarg gir 592 px, h1 tar ca. 81 px ved
   section-font 22 px, og inngangslinja ca. 70 px. Det er ca. 440 px igjen —
   derfor er plottet 330 px høyt pluss ca. 46 px til x-etikettene.

   Pilspissene er innebygde <svg>-er, og de krever --html=true. Marp Core
   slipper som standard bare gjennom en allowlist der div/img/p er med, men
   IKKE svg — uten flagget havner SVG-kilden på sliden som synlig tekst.
   Docker-kommandoen i README-en har flagget, så det er dekket.

   Punktene er plassert med left/bottom i px inne i .plot, ikke i prosent.
   Flytter du ett punkt, sjekk at kortene ikke møtes: kortene er ca. 130 px
   høye, og de to punktene står 180 px fra hverandre i høyden. Mindre
   avstand enn det, og kortene overlapper. */

section { font-size: 22px; }

.lead { margin: 0.2em 0 0; font-size: 0.9em; color: var(--muted); max-width: 52em; }

.kv { position: relative; width: 1090px; height: 376px; margin: 1.1em auto 0; }

/* Aksekorset ER to borders på .plot. Da er det nøyaktig plottets kanter
   punktene måles fra, og koordinatene kan ikke komme i utakt med aksene. */
.plot {
  position: absolute; left: 196px; top: 0; width: 880px; height: 330px;
  border-left: 2px solid var(--ink);
  border-bottom: 2px solid var(--ink);
}

.arr { position: absolute; color: var(--ink); }
.arr-y { left: -7px; top: -11px; }        /* på toppen av y-aksen */
.arr-x { right: -11px; bottom: -7px; }    /* på enden av x-aksen */

/* Aksenavnene står ved pilspissene, ikke midt på aksen: da leses de som
   retningen aksen peker — «mer presisjon oppover», «mer tid mot høyre». */
.ax-name { position: absolute; font-family: var(--display); font-weight: 700;
           font-size: 0.82em; letter-spacing: -0.01em; }
.ax-y { left: 10px; top: -8px; }
.ax-x { right: 0; bottom: -34px; }

/* Aksemerkene: verdien står der punktets hjelpelinje treffer aksen. Tida
   står DERFOR ikke på kortene — den sto begge steder først, og da ble
   «Sekunder» mot «1–2 timer» sagt to ganger i samme figur. Nå sier aksen
   det, i display-snittet og i svart, og kortet sier hva punktet brukes til. */
.tick { position: absolute; white-space: nowrap; }
.tick-y { right: calc(100% + 12px); text-align: right; transform: translateY(50%);
          font-size: 0.68em; line-height: 1.3; color: var(--muted); }
.tick-x { top: calc(100% + 12px); transform: translateX(-50%);
          font-family: var(--display); font-weight: 700; font-size: 0.95em;
          letter-spacing: -0.015em; }

/* Hjelpelinjene bort til aksene. Stiplet og lyse: de skal leses som
   avlesning, ikke som en tredje strek i figuren. */
.guide-h { position: absolute; border-top: 1px dashed var(--rule); left: 0; }
.guide-v { position: absolute; border-left: 1px dashed var(--rule); bottom: 0; }

.dot { position: absolute; width: 15px; height: 15px; border-radius: 50%;
       transform: translate(-50%, 50%); box-shadow: 0 0 0 3.5px var(--paper); }

/* Kortene: ikon og navn på samme linje, og under det JOBBEN punktet gjør.
   Jobben er det sliden handler om — «begge har verdi, men til ulike ting» —
   så den står i display-snittet, like stor som en klokke ville vært.
   Ikonene er de samme to som stigen og oppsummeringen bruker. */
.node { position: absolute; width: 300px; }
/* 64 px ikoner, samme mål som oppsummeringskortene i baklomma bruker. Ikke
   mindre: kantene i modell-surrogat.svg er 1,15 px i en 120-viewBox med 0,38
   i dekkevne, så under ca. 60 px forsvinner de og nettet blir en punktsky. */
.node .head { display: grid; grid-template-columns: 64px 1fr; gap: 0.6em;
              align-items: center; }
.node .head img { width: 64px; height: 64px; display: block; }
.node .head h3 { margin: 0; font-size: 1em; line-height: 1.15; }
.node .bruk { margin: 0.5em 0 0; }
.node .bruk b { display: block; font-family: var(--display); font-weight: 700;
                font-size: 1.25em; line-height: 1.1; letter-spacing: -0.015em; }
.node .bruk span { display: block; margin-top: 0.3em; font-size: 0.78em;
                   line-height: 1.35; color: var(--muted); }

/* SIMULERING: høyt oppe og langt ute — presis, men du venter.
   Punktet står på (680, 268) i plottet, og kortet henger til VENSTRE for
   det. Til høyre er det bare 200 px igjen, og kortet er 300 px bredt. */
.sim .dot { left: 680px; bottom: 268px; background: var(--ink); }
.sim .guide-h { bottom: 268px; width: 680px; }
.sim .guide-v { left: 680px; height: 268px; }
.sim .node { left: 348px; bottom: 268px; transform: translateY(50%);
             text-align: right; }
.sim .node .head { grid-template-columns: 1fr 64px; }

/* ESTIMATET: nede til venstre — mindre presisjon, men svaret kommer med en
   gang. Kortet henger til HØYRE for punktet, der det er plass. */
.est .dot { left: 120px; bottom: 88px; background: var(--accent); }
.est .guide-h { bottom: 88px; width: 120px; }
.est .guide-v { left: 120px; height: 88px; }
.est .node { left: 150px; bottom: 88px; transform: translateY(50%); }
.est .node .head h3,
.est .node .bruk b { color: var(--accent); }
</style>

<p class="lead">Begge svarer på det samme spørsmålet, og begge har verdi — men ikke til det samme. Forskjellen er hvor mye presisjon du får igjen for ventetiden, og det er den forskjellen som bestemmer hvor i prosessen de hører hjemme.</p>

<div class="kv">
<div class="plot">

  <svg class="arr arr-y" width="16" height="11" viewBox="0 0 16 11" aria-hidden="true">
    <path d="M8 0 L16 11 L0 11 z" fill="currentColor"/></svg>
  <svg class="arr arr-x" width="11" height="16" viewBox="0 0 11 16" aria-hidden="true">
    <path d="M11 8 L0 0 L0 16 z" fill="currentColor"/></svg>

  <div class="ax-name ax-y">Presisjon</div>
  <div class="ax-name ax-x">Ventetid</div>

  <div class="sim">
    <div class="guide-h"></div>
    <div class="guide-v"></div>
    <div class="tick tick-y" style="bottom: 268px">Etterprøvbar</div>
    <div class="tick tick-x" style="left: 680px">1–2 timer</div>
    <div class="dot"></div>
    <div class="node">
      <div class="head">
        <h3>Simulering</h3>
        <img src="figures/modeller/modell-cfd.svg" alt="">
      </div>
      <p class="bruk"><b>Dokumentasjon</b><span>Svaret som skal tåle å bli etterprøvd</span></p>
    </div>
  </div>

  <div class="est">
    <div class="guide-h"></div>
    <div class="guide-v"></div>
    <div class="tick tick-y" style="bottom: 88px">Omtrentlig<br>— med et avvik vi måler</div>
    <div class="tick tick-x" style="left: 120px">Sekunder</div>
    <div class="dot"></div>
    <div class="node">
      <div class="head">
        <img src="figures/modeller/modell-surrogat.svg" alt="">
        <h3>Estimat</h3>
      </div>
      <p class="bruk"><b>Iterering</b><span>Prøv tjue varianter før lunsj</span></p>
    </div>
  </div>

</div>
</div>

<!-- Say: sliden før viste hva modellen gjør. Denne svarer på det salen
     lurer på etterpå: skal den erstatte simuleringen? Nei.

     To akser. Oppover: presisjon. Mot høyre: hvor lenge du venter. Punktene
     ligger på diagonalen, og det er hele poenget — presisjon koster tid.

     Nede til venstre: estimatet. Sekunder, med et avvik vi måler. Det er
     ikke like presist, og det trenger det ikke å være, fordi det brukes til
     å ITERERE: prøve tjue varianter og se hvilken vei det går.

     Oppe til høyre: simuleringen. Én til to timer, etterprøvbar. Den brukes
     til å DOKUMENTERE — svaret som skal stå i rapporten, og som noen kan
     regne etter.

     Har du tid: pek på hjørnet oppe til VENSTRE, det tomme. Raskt OG
     nøyaktig finnes ikke ennå. Det er der forskningen står, og det er
     derfor estimatet er trent på simuleringene, ikke i stedet for dem. -->
<!-- TODO ~0:35 -->

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

