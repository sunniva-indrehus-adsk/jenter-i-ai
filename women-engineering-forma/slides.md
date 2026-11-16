---
marp: true
theme: theme.css
paginate: true
math: katex
lang: en
---

<!-- _class: title title-photo -->
<!-- _header: 'November 17, 2026' -->
<!-- paginate: false -->

<!-- TITLE SLIDE, English version (Women engineering Forma, November 17, 2026).
     Translated from the Jenter i AI deck of September 24, 2026, which still
     lives unchanged in jenter-i-ai/slides.md.

     No title text: the "Who run the world? Girls!" image (figures/logos/
     girls.png) bottom right is the event mark, in place of the Jenter i AI
     logo.

     The white layers the theme puts in the two bottom corners
     (section.title-photo in theme.css) existed to give the JiA logo and the
     title a calm surface. Neither is here, so background-image is overridden
     to the photo alone. The girls image is opaque and carries itself.

     paginate: false is set here without an underscore, so it carries on
     down until "# Women in Autodesk" turns it back on. -->

<style scoped>
section {
  --photo: url('figures/analyser/wind.png');
  background-image: var(--photo);
  background-size: cover;
  background-position: center;
  background-repeat: no-repeat;
}

/* Absolutely positioned, not in the flow: section.title is a flex column that
   packs to the bottom left. 64 px from the right is --margin-x, the same
   margin as the Autodesk logo top left. The image is 582 x 582, so 230 px is
   a 2.5x downscale and stays sharp on a large screen. */
.event-logo {
  position: absolute;
  right: var(--margin-x);
  bottom: 52px;
  line-height: 0;
}
.event-logo img {
  height: 230px;
  width: auto;
  display: block;
  border-radius: 14px;
  box-shadow: 0 6px 24px rgba(0, 0, 0, 0.18);
}
</style>

<div class="event-logo">
  <img src="figures/logos/girls.png" alt="Who run the world? Girls!">
</div>

---

<!-- paginate: true -->

# Women in Autodesk

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
    <div class="frame family"><img src="figures/people/vilde-2.jpg" alt="Vilde on the beach volleyball court"/></div>
    <div class="frame portrait"><img src="figures/people/vilde-3.jpg" alt="Vilde"/></div>
  </div>
  <div class="kicker">Vilde</div>
</div>

<div class="jente sunniva">
  <div class="photo-cluster">
    <div class="frame family"><img src="figures/people/sunniva-2.jpg" alt="Sunniva with family"/></div>
    <div class="frame portrait"><img src="figures/people/sunniva-color.jpg" alt="Sunniva"/></div>
  </div>
  <div class="kicker">Sunniva</div>
</div>

</div>

<!--
KEPT FOR REFERENCE: the bullets and callouts from the two old slides.
Not deleted, because they are real content — but they are no longer on the
slide and are told out loud instead. If you want them back on the slide:

  Vilde
  - From Industrial Economics and Technology Management (NTNU) to Autodesk
  - Internship as a developer during my studies
  - Fun to build product instead of slides
  - Working in a product organization
  callout: Working for a more sustainable world with code and math.

  Sunniva
  - From Physics and Mathematics (NTNU) to Autodesk — turning equations into code
  - Then: wrote a paper that maybe five people in the world have read
  - Now: still equations, in a tool thousands of architects open every day
  callout: Same kind of work, but a bigger impact in the real world.
-->

<!-- Say: each of you tells your own story, briefly. The point for the
     audience is that there are many ways in — industrial economics and
     physics, not computer science — and that "I didn't study computer
     science" is not a barrier. The bullets are no longer on the slide, so
     they have to be said. -->
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
  <div class="kicker">Early stage</div>
  <h1>The art of filling a site</h1>
</div>

<div class="photo-credit">
  Aerial photo 2022 © Geovekst/Trondheim kommune · Map © Kartverket, CC BY 4.0
</div>

<!-- Say: let the picture stand for a moment before you say anything. An
     empty block, cars where half the room has parked, no lines drawn. Then:
     "and this is where the questions begin." -->
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

       - Where should the building go, and how tall can it be?
       - Will it be a good place to be (light, noise, wind)?

     Skal de tilbake på flata, står oppskriften i theme.css over
     «section.overlay .bubble». -->

![](figures/tidligfase/hesthagen-flyfoto.jpg)

<div class="photo-credit">
  Aerial photo 2022 © Geovekst/Trondheim kommune · Map © Kartverket, CC BY 4.0
</div>

<div class="roles-holder venstre">
<div class="roles">
<div class="role">
<div class="figure"><img src="figures/tidligfase/rolle-arkitekt-lys.svg" alt=""><span class="name">The architect</span></div>
</div>
</div>
</div>

<!-- Say: "first comes the architect." Nothing is written on the slide, so
     the questions MUST be said — the two above, in your own order. Wait until
     the figure has stood for a moment; it is big enough to carry the pause. -->
<!-- TODO ~0:20 -->

---

<!-- _class: demo overlay -->

<!-- Steg 3: utbyggeren kommer inn ved siden av, i spalte 2 av samme
     venstrestilte bærer. Arkitekten rører seg ikke — samme spalte, samme
     figurhøyde som på forrige slide.

     UTBYGGERENS SPØRSMÅL sto i en snakkeboble her før, som arkitektens. Begge
     er tatt ut av samme grunn; se kommentaren på forrige slide. Tatt vare på:

       - Do the numbers add up?
       - What does it cost to change our minds in three months? -->

![](figures/tidligfase/hesthagen-flyfoto.jpg)

<div class="photo-credit">
  Aerial photo 2022 © Geovekst/Trondheim kommune · Map © Kartverket, CC BY 4.0
</div>

<div class="roles-holder venstre">
<div class="roles">
<div class="role">
<div class="figure"><img src="figures/tidligfase/rolle-arkitekt-lys.svg" alt=""><span class="name">The architect</span></div>
</div>
<div class="role">
<div class="figure"><img src="figures/tidligfase/rolle-utbygger-lys.svg" alt=""><span class="name">The developer</span></div>
</div>
</div>
</div>

<!-- Say: "and then comes the one who pays." The architect asks about form,
     the developer about risk — both need answers before anything is fully
     drawn. Their questions are no longer on the slide, so the two above must
     be said. Land the punchline here: "a few weeks where almost everything
     is decided." -->
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

<!-- Say: don't stay here. Click on right away — the card is a stage
     direction, not a slide. -->
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
<div class="kicker">The place</div>
Choose an address
</div>

---

<!-- _class: demo flipbook eget-merke -->

![](figures/site-design/bestill-data.png)

<div class="demo-label">
<div class="kicker">Context</div>
Choose relevant data
</div>

---

<!-- _class: demo flipbook eget-merke -->

![](figures/site-design/sett-kontekst.png)

<div class="demo-label">
<div class="kicker">The foundation</div>
Put the site in context with its surroundings
</div>

---

<!-- _class: demo flipbook eget-merke -->

![](figures/site-design/vis-hesthagen-med-data.png)

<div class="demo-label">
<div class="kicker">The site</div>
Plan
</div>

---

<!-- _class: demo flipbook eget-merke -->

![](figures/site-design/hesthagen-med-tegning.png)

<div class="demo-label">
<div class="kicker">Proposal</div>
Iterate on the design
</div>

---

# Analyses in Autodesk Forma

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
<img src="figures/analyser/noise.png" alt="Noise">
<div class="figcap"><span class="figref">Noise</span></div>
</div>

<div class="card">
<img src="figures/analyser/solar-energy.png" alt="Solar energy">
<div class="figcap"><span class="figref">Solar energy</span></div>
</div>

<div class="card">
<img src="figures/analyser/daylight.png" alt="Daylight">
<div class="figcap"><span class="figref">Daylight</span></div>
</div>

<div class="card">
<img src="figures/analyser/microclimate.png" alt="Microclimate">
<div class="figcap"><span class="figref">Microclimate</span></div>
</div>

<div class="card">
<img src="figures/analyser/sun.png" alt="Sun">
<div class="figcap"><span class="figref">Sun</span></div>
</div>

<div class="card">
<img src="figures/analyser/wind.png" alt="Wind">
<div class="figcap"><span class="figref">Wind</span></div>
</div>

</div>


<!-- Say: six analyses, same model, same afternoon. Let them see the breadth
     here — don't point at any single one yet. The next slide is the same,
     with wind highlighted, and that's where you make the choice for them. -->
<!-- TODO ~0:40 -->

---

# Analyses in Autodesk Forma

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
<img src="figures/analyser/noise.png" alt="Noise">
<div class="figcap"><span class="figref">Noise</span></div>
</div>

<div class="card">
<img src="figures/analyser/solar-energy.png" alt="Solar energy">
<div class="figcap"><span class="figref">Solar energy</span></div>
</div>

<div class="card">
<img src="figures/analyser/daylight.png" alt="Daylight">
<div class="figcap"><span class="figref">Daylight</span></div>
</div>

<div class="card">
<img src="figures/analyser/microclimate.png" alt="Microclimate">
<div class="figcap"><span class="figref">Microclimate</span></div>
</div>

<div class="card">
<img src="figures/analyser/sun.png" alt="Sun">
<div class="figcap"><span class="figref">Sun</span></div>
</div>

<div class="card ring">
<img src="figures/analyser/wind.png" alt="Wind">
<div class="figcap"><span class="figref">Wind</span></div>
</div>

</div>


<!-- Say: "and this is the one we'll spend the rest of our time on." Hold on
     the frame for a moment before moving on — this is where the wind story
     begins. Don't explain why wind yet; that comes on the next slide. -->
<!-- TODO ~0:15 -->

---

<!-- _class: comfort-map -->

<!-- Trinn 1 av 4: kartet alene. Merkelappene kommer én av gangen på de tre
     neste slidene, som er identiske bortsett fra dem — samme grep som
     rollekortene på tomt-sliden og stigen lenger bak. Marp har ingen
     fragmenter, så oppbygging gjøres ved å duplisere sliden.

     Bildet, skalaen og alt annet MÅ være likt på alle fire, ellers hopper det
     når du klikker. Retter du noe her, rett det samme på trinn 2–4. -->

# Wind comfort

<div class="use">

<div class="map">

<img src="figures/vind/windcomfortgløs2.png" alt="Wind comfort map over Gløshaugen, seen at an angle: the outdoor spaces between the buildings are mostly green, with yellow areas in the open parts and a few orange patches">

</div>

<div class="side">

<div class="legend">
<div class="kicker">Comfort scale</div>

<div class="row"><span class="sw" style="background:#B2F8DA"></span><div><b>Sitting</b><span class="t">below 2.5 m/s</span></div></div>
<div class="row"><span class="sw" style="background:#55DCA2"></span><div><b>Standing</b><span class="t">above 2.5 m/s</span></div></div>
<div class="row"><span class="sw" style="background:#FED52A"></span><div><b>Strolling</b><span class="t">above 4 m/s</span></div></div>
<div class="row"><span class="sw" style="background:#FFA900"></span><div><b>Walking</b><span class="t">above 6 m/s</span></div></div>
<div class="row"><span class="sw" style="background:#FF463A"></span><div><b>Uncomfortable</b><span class="t">above 8 m/s</span></div></div>
</div>
</div>

</div>

<!-- Say: let the map stand alone for a moment. "This is the answer — one map
     of the whole site." Give the room time to see the colors and recognize
     the place before you start explaining. Then click, and the labels
     appear. -->
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

# Wind comfort

<div class="use">

<div class="map">

<img src="figures/vind/windcomfortgløs2.png" alt="Wind comfort map over Gløshaugen, seen at an angle: the outdoor spaces between the buildings are mostly green, with yellow areas in the open parts and a few orange patches">

<div class="pin" style="left: 21%; top: 15%;">
  <span class="dot"></span>
  <span class="lbl"><b>Open area</b><span>Nothing slows the wind down.</span></span>
</div>

</div>

<div class="side">

<div class="legend">
<div class="kicker">Comfort scale</div>

<div class="row"><span class="sw" style="background:#B2F8DA"></span><div><b>Sitting</b><span class="t">below 2.5 m/s</span></div></div>
<div class="row"><span class="sw" style="background:#55DCA2"></span><div><b>Standing</b><span class="t">above 2.5 m/s</span></div></div>
<div class="row"><span class="sw" style="background:#FED52A"></span><div><b>Strolling</b><span class="t">above 4 m/s</span></div></div>
<div class="row"><span class="sw" style="background:#FFA900"></span><div><b>Walking</b><span class="t">above 6 m/s</span></div></div>
<div class="row"><span class="sw" style="background:#FF463A"></span><div><b>Uncomfortable</b><span class="t">above 8 m/s</span></div></div>
</div>
</div>

</div>

<!-- Say: here you read the map for the room, one place at a time. Three
     places, no more — they'll see the rest themselves.

     The open area first: nothing is in the way, so the wind picks up speed.
     Yellow means it's fine to walk through, not to sit down and stay. -->
<!-- TODO ~0:12 -->

---
<!-- _class: comfort-map -->

<!-- Trinn 3 av 4: første og andre merkelapp. Alt utenom .pin-ene skal være
     identisk med de andre tre trinnene — se kommentaren på trinn 2. -->

# Wind comfort

<div class="use">

<div class="map">

<img src="figures/vind/windcomfortgløs2.png" alt="Wind comfort map over Gløshaugen, seen at an angle: the outdoor spaces between the buildings are mostly green, with yellow areas in the open parts and a few orange patches">

<div class="pin" style="left: 21%; top: 15%;">
  <span class="dot"></span>
  <span class="lbl"><b>Open area</b><span>Nothing slows the wind down.</span></span>
</div>

<div class="pin" style="left: 62%; top: 51%;">
  <span class="dot"></span>
  <span class="lbl"><b>Sheltered by buildings</b><span>The surrounding buildings block the wind.</span></span>
</div>

</div>

<div class="side">

<div class="legend">
<div class="kicker">Comfort scale</div>

<div class="row"><span class="sw" style="background:#B2F8DA"></span><div><b>Sitting</b><span class="t">below 2.5 m/s</span></div></div>
<div class="row"><span class="sw" style="background:#55DCA2"></span><div><b>Standing</b><span class="t">above 2.5 m/s</span></div></div>
<div class="row"><span class="sw" style="background:#FED52A"></span><div><b>Strolling</b><span class="t">above 4 m/s</span></div></div>
<div class="row"><span class="sw" style="background:#FFA900"></span><div><b>Walking</b><span class="t">above 6 m/s</span></div></div>
<div class="row"><span class="sw" style="background:#FF463A"></span><div><b>Uncomfortable</b><span class="t">above 8 m/s</span></div></div>
</div>
</div>

</div>

<!-- Say: the sheltered zone between the buildings: this is where the outdoor
     space should go. Light green is "sitting" — your coffee stays put. Put it
     up against the open area you just talked about; the contrast is the
     whole point. -->
<!-- TODO ~0:10 -->

---
<!-- _class: comfort-map -->

<!-- Trinn 4 av 4: alle tre merkelappene på. Alt utenom .pin-ene skal være
     identisk med de andre tre trinnene — se kommentaren på trinn 2. -->

# Wind comfort

<div class="use">

<div class="map">

<img src="figures/vind/windcomfortgløs2.png" alt="Wind comfort map over Gløshaugen, seen at an angle: the outdoor spaces between the buildings are mostly green, with yellow areas in the open parts and a few orange patches">

<div class="pin" style="left: 21%; top: 15%;">
  <span class="dot"></span>
  <span class="lbl"><b>Open area</b><span>Nothing slows the wind down.</span></span>
</div>

<div class="pin" style="left: 62%; top: 51%;">
  <span class="dot"></span>
  <span class="lbl"><b>Sheltered by buildings</b><span>The surrounding buildings block the wind.</span></span>
</div>

<div class="pin" style="left: 22%; top: 74%;">
  <span class="dot"></span>
  <span class="lbl"><b>Between two buildings</b><span>The wind is squeezed through and speeds up.</span></span>
</div>

</div>

<div class="side">

<div class="legend">
<div class="kicker">Comfort scale</div>

<div class="row"><span class="sw" style="background:#B2F8DA"></span><div><b>Sitting</b><span class="t">below 2.5 m/s</span></div></div>
<div class="row"><span class="sw" style="background:#55DCA2"></span><div><b>Standing</b><span class="t">above 2.5 m/s</span></div></div>
<div class="row"><span class="sw" style="background:#FED52A"></span><div><b>Strolling</b><span class="t">above 4 m/s</span></div></div>
<div class="row"><span class="sw" style="background:#FFA900"></span><div><b>Walking</b><span class="t">above 6 m/s</span></div></div>
<div class="row"><span class="sw" style="background:#FF463A"></span><div><b>Uncomfortable</b><span class="t">above 8 m/s</span></div></div>
</div>
</div>

</div>

<!-- Say: the passage between two buildings: the wind is squeezed through a
     narrower cross-section and speeds up. It's the effect people feel without
     being able to explain it, and the only way to fix it is to change the
     buildings — not to put up a screen afterwards.

     The point to land, now that all three are showing: the architect doesn't
     need the numbers. They need to see where it's green before the volumes
     are locked. -->
<!-- TODO ~0:15 -->

---

<!-- _class: ladder -->

# How does the architect analyze wind?

<div class="steps">

<div class="card past">
  <div class="kicker">Before</div>
  <img src="figures/modeller/modell-ekspert.svg" alt="">
  <p class="name">Wind expert</p>
  <p class="clock">Weeks</p>
</div>

<div></div>

<div></div>

</div>

<!-- Say: before, you had to hire someone. Wind analysis was a consulting
     service: you ordered it, and you waited. It came late in the project, it
     came once, and it told you whether what you had already decided was
     okay. -->
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

# How do we calculate wind comfort?

<div class="recipe">

<div class="card">
  <h3>Simulation</h3>
  <div class="thumb dirs">
    <img class="site" src="figures/gløshaugenfromabove.png" alt="">
    <img src="figures/vind/vindretninger-plan.svg" alt="Gløshaugen seen from above, with arrows pointing in towards the site from eight wind directions">
  </div>
</div>

<div class="plus">+</div>

<div class="card">
  <h3>Historical data</h3>
  <div class="thumb rose"><img src="figures/vind/vindrose.png" alt="Wind rose for the site: eight sectors showing the share of time the wind blows from each direction, with southwest the largest at 22 percent"></div>
</div>

</div>

<!-- Say: the recipe, before the figures on the next slide.

     The two cards are the ingredients, and the comfort map you just saw is
     the answer — read the plus sign out loud, so the room follows the sum.

     The point worth stopping on: the simulation alone says nothing about
     comfort. It says what the wind DOES if it comes from the northwest. Only
     when you know how often it actually does that can you say whether a
     place is sheltered. That's why the historical data is not a detail —
     without it you have eight pictures and no conclusion. -->
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
  <h1>Simulation in Forma</h1>
  <div class="mhead-row">
    <img src="figures/modeller/modell-cfd.svg" alt="">
    <p class="sub">Physics model</p>
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
  <img src="figures/vind/streamlines.png" alt="Streamlines from a wind simulation with wind from the southeast: blue paths that split around the main building, speed up past the gable and curl into vortices behind the buildings">
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

<!-- Say: here is the simulation.

     Start with the picture, not the equation: this is one direction — wind
     from the southeast — and every blue line is the path a parcel of air
     takes. Follow one of them with your hand: it splits around the main
     building, shoots past the gable, and behind the buildings it curls up
     into vortices. THIS is what the simulation calculates, point by point in
     the air above the site.

     Say "one direction" clearly — the picture shows southeast, and that's the
     whole point about the cost: multiply it. Work it out out loud: eight
     directions, an hour or two each, for the one comfort map they've already
     seen.

     Then the equations, and only as a gesture: this is the physics it solves.
     Don't go through the terms. The only thing you might point at is the last
     term — trees and vegetation slowing the wind — which is our own addition.

     Now the room has the number they need for the next step: eight
     directions x a couple of hours, every time you move a volume. -->
<!-- TODO ~0:30 -->
---

<!-- _class: ladder -->

# How does the architect analyze wind?

<div class="steps">

<div class="card past">
  <div class="kicker">Before</div>
  <img src="figures/modeller/modell-ekspert.svg" alt="">
  <p class="name">Wind expert</p>
  <p class="clock">Weeks</p>
</div>

<div></div>

<div></div>

</div>

<!-- Say: before, you had to hire someone. Wind analysis was a consulting
     service: you ordered it, and you waited. It came late in the project, it
     came once, and it told you whether what you had already decided was
     okay. -->
<!-- TODO ~0:10 -->

---

<!-- _class: ladder -->

# How does the architect analyze wind?

<div class="steps">

<div class="card past">
  <div class="kicker">Before</div>
  <img src="figures/modeller/modell-ekspert.svg" alt="">
  <p class="name">Wind expert</p>
  <p class="clock">Weeks</p>
</div>

<div class="card">
  <div class="kicker">With Forma</div>
  <img src="figures/modeller/modell-cfd.svg" alt="">
  <p class="name">Simulation <span class="sub">Physics model</span></p>
  <p class="clock">Hours</p>
</div>

<div></div>

</div>

<!-- Say: the simulation in the tool was the really big step, and it's worth
     saying why: it's easy to use. You don't set up a mesh, you don't specify
     boundary conditions — you press a button, on the geometry you've already
     drawn.

     That's what takes the expert out of the loop, not just that it's faster.
     The wind analysis in Forma made the information available to the
     architect directly. -->
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


<figure><img src="figures/video/iterations/hesthagen-001.jpg" alt="Closed block around a courtyard, the comfort map green inside the courtyard"></figure>

<figure><img src="figures/video/iterations/hesthagen-002.jpg" alt="Two angled wings, the comfort map redrawn"></figure>

<figure><img src="figures/video/iterations/hesthagen-003.jpg" alt="One long angled slab along the road"></figure>

<figure><img src="figures/video/iterations/hesthagen-004.jpg" alt="U-shape with a point block to the north, the courtyard green"></figure>

<figure><img src="figures/video/iterations/hesthagen-005.jpg" alt="Curved wing with a point block, the courtyard almost entirely green"></figure>

<figure><img src="figures/video/iterations/hesthagen-006.jpg" alt="Three freestanding volumes spread across the site"></figure>

<figure><img src="figures/video/iterations/hesthagen-007.jpg" alt="Slab and point block angled towards each other"></figure>

<figure><img src="figures/video/iterations/hesthagen-008.jpg" alt="L-shaped building with a point block, large green outdoor space"></figure>

<figure><img src="figures/video/iterations/hesthagen-009.jpg" alt="Curved slab with a point block, wide green courtyard"></figure>

<figure><img src="figures/video/iterations/hesthagen-010.jpg" alt="Two parallel slabs set diagonally across the site"></figure>

<figure><img src="figures/video/iterations/hesthagen-011.jpg" alt="Three parallel slabs"></figure>

<figure><img src="figures/video/iterations/hesthagen-012.jpg" alt="Three staggered slabs"></figure>

<figure><img src="figures/video/iterations/hesthagen-013.jpg" alt="Three small freestanding volumes, the comfort map almost entirely green"></figure>

<figure><img src="figures/video/iterations/hesthagen-014.jpg" alt="Six small point blocks in a grid"></figure>

<figure><img src="figures/video/iterations/hesthagen-015.jpg" alt="Staggered point blocks in two rows"></figure>

</div>

<!-- Say: don't read out the tiles. The title is no longer on the slide, so it
     has to be said: "the architect can quickly evaluate many alternatives —
     fifteen attempts, one afternoon." Then point at the courtyard in the
     first tile and compare it with one of the last: yellow turns green. The
     point isn't which proposal won, it's that you had time to try them all.

     Stills and not video: video doesn't play in PDF export, see the README.
     The images are cut from the screen recording of the Hesthagen model. -->
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
  <h3>What we have</h3>
  <p>Thousands of completed simulations.</p>
  <p class="big">Training data</p>
</div>

<div class="arr"></div>

<div class="card ai">
  <img src="figures/modeller/modell-surrogat.svg" alt="">
  <h3>What we could build</h3>
  <p>A model that recognizes how the wind moves.</p>
  <p class="big">Machine learning model</p>
</div>

</div>

<!-- Say: this is the turning point, and it's worth saying slowly.

     The simulation is expensive, but we've run it thousands of times — on
     real sites, in real projects. All those runs are sitting there as
     finished answers: this geometry gives this wind field.

     And that's exactly what a machine learning model needs. Thousands of
     pairs of questions and answers. So we trained a model on them, and it
     can predict how the wind moves — without calculating the physics at all.

     The point to stress if you only get to say one thing: the network isn't
     the hard part, the training data is. Every time a customer pays for the
     expensive analysis, it becomes an example for the fast one. -->
<!-- TODO ~0:35 -->
---
<div class="mhead">
  <h1>Estimate in Forma</h1>
  <div class="mhead-row">
    <img src="figures/modeller/modell-surrogat.svg" alt="">
    <p class="sub">Machine learning model</p>
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
          <img src="figures/modeller/predictions/input-hoyde.png" alt="Height raster of the site">
        </div>
        <figcaption>Height<div class="ramp"></div></figcaption>
      </figure>
      <figure>
        <div class="ring">
          <img src="figures/modeller/predictions/input-kategori.png" alt="Raster with surface classes: terrain, buildings and vegetation">
        </div>
        <figcaption>
          <div class="key">
            <span><i style="background:#FFFFFF"></i>Buildings</span>
            <span><i style="background:#CFCFCF"></i>Terrain</span>
            <span><i style="background:#1B7F5A"></i>Vegetation</span>
          </div>
        </figcaption>
      </figure>
    </div>
  </div>
  <svg class="pil steg2" width="48" height="12" viewBox="0 0 48 12" aria-hidden="true">
    <path d="M0 6 H40" stroke="currentColor" stroke-width="2.4"/>
    <path d="M38 1 L47 6 L38 11 z" fill="currentColor"/></svg>
  <div class="nett steg2">
    <p class="lab">Neural network</p>
    <img src="figures/modeller/modell-surrogat.svg" alt="Neural network: three layers of nodes connected by edges">
  </div>
  <svg class="pil steg3" width="48" height="12" viewBox="0 0 48 12" aria-hidden="true">
    <path d="M0 6 H40" stroke="currentColor" stroke-width="2.4"/>
    <path d="M38 1 L47 6 L38 11 z" fill="currentColor"/></svg>
  <div class="ut steg3">
    <p class="lab">Output</p>
    <div class="panel">
      <div class="disc">
        <img src="figures/modeller/predictions/felt-sv.png" alt="Wind speed over the site, 1.75 meters above the ground">
      </div>
    </div>
  </div>
</div>

<!-- Say: the previous slide said that all the simulations ARE the training
     data. Now we'll see the same network in use — but start with what goes
     IN.

     The entire input is this: the height of everything standing there, and
     what it is — building, terrain or vegetation. Two images of the site.

     No mesh. No boundary conditions. And note: no wind direction in the
     input — we'll come back to that if anyone asks. -->
<!-- TODO ~0:15 -->

---
<div class="mhead">
  <h1>Estimate in Forma</h1>
  <div class="mhead-row">
    <img src="figures/modeller/modell-surrogat.svg" alt="">
    <p class="sub">Machine learning model</p>
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
          <img src="figures/modeller/predictions/input-hoyde.png" alt="Height raster of the site">
        </div>
        <figcaption>Height<div class="ramp"></div></figcaption>
      </figure>
      <figure>
        <div class="ring">
          <img src="figures/modeller/predictions/input-kategori.png" alt="Raster with surface classes: terrain, buildings and vegetation">
        </div>
        <figcaption>
          <div class="key">
            <span><i style="background:#FFFFFF"></i>Buildings</span>
            <span><i style="background:#CFCFCF"></i>Terrain</span>
            <span><i style="background:#1B7F5A"></i>Vegetation</span>
          </div>
        </figcaption>
      </figure>
    </div>
  </div>
  <svg class="pil steg2" width="48" height="12" viewBox="0 0 48 12" aria-hidden="true">
    <path d="M0 6 H40" stroke="currentColor" stroke-width="2.4"/>
    <path d="M38 1 L47 6 L38 11 z" fill="currentColor"/></svg>
  <div class="nett steg2">
    <p class="lab">Neural network</p>
    <img src="figures/modeller/modell-surrogat.svg" alt="Neural network: three layers of nodes connected by edges">
  </div>
  <svg class="pil steg3" width="48" height="12" viewBox="0 0 48 12" aria-hidden="true">
    <path d="M0 6 H40" stroke="currentColor" stroke-width="2.4"/>
    <path d="M38 1 L47 6 L38 11 z" fill="currentColor"/></svg>
  <div class="ut steg3">
    <p class="lab">Output</p>
    <div class="panel">
      <div class="disc">
        <img src="figures/modeller/predictions/felt-sv.png" alt="Wind speed over the site, 1.75 meters above the ground">
      </div>
    </div>
  </div>
</div>

<!-- Say: then the two images go into the network. It's the same icon the
     room has seen on the ladder and on the bridge slide — it's the model
     that was trained on the thousands of simulations.

     It doesn't calculate the physics. It recognizes.

     If someone asks how the direction comes in when it isn't an input: we
     rotate the geometry to the network's orientation, run it, and rotate the
     answer back. It's deliberately not drawn — it's an implementation
     detail. -->
<!-- TODO ~0:10 -->

---
<div class="mhead">
  <h1>Estimate in Forma</h1>
  <div class="mhead-row">
    <img src="figures/modeller/modell-surrogat.svg" alt="">
    <p class="sub">Machine learning model</p>
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
          <img src="figures/modeller/predictions/input-hoyde.png" alt="Height raster of the site">
        </div>
        <figcaption>Height<div class="ramp"></div></figcaption>
      </figure>
      <figure>
        <div class="ring">
          <img src="figures/modeller/predictions/input-kategori.png" alt="Raster with surface classes: terrain, buildings and vegetation">
        </div>
        <figcaption>
          <div class="key">
            <span><i style="background:#FFFFFF"></i>Buildings</span>
            <span><i style="background:#CFCFCF"></i>Terrain</span>
            <span><i style="background:#1B7F5A"></i>Vegetation</span>
          </div>
        </figcaption>
      </figure>
    </div>
  </div>
  <svg class="pil steg2" width="48" height="12" viewBox="0 0 48 12" aria-hidden="true">
    <path d="M0 6 H40" stroke="currentColor" stroke-width="2.4"/>
    <path d="M38 1 L47 6 L38 11 z" fill="currentColor"/></svg>
  <div class="nett steg2">
    <p class="lab">Neural network</p>
    <img src="figures/modeller/modell-surrogat.svg" alt="Neural network: three layers of nodes connected by edges">
  </div>
  <svg class="pil steg3" width="48" height="12" viewBox="0 0 48 12" aria-hidden="true">
    <path d="M0 6 H40" stroke="currentColor" stroke-width="2.4"/>
    <path d="M38 1 L47 6 L38 11 z" fill="currentColor"/></svg>
  <div class="ut steg3">
    <p class="lab">Output</p>
    <div class="panel">
      <div class="disc">
        <img src="figures/modeller/predictions/felt-sv.png" alt="Wind speed over the site, 1.75 meters above the ground">
      </div>
    </div>
  </div>
</div>

<!-- Say: and out comes the wind field. Light is sheltered, saturated is
     exposed. Image in, image out — that's the whole frame.

     The field here is the southwest run, but the direction isn't on the
     slide. Only say it if someone asks; the figure is about in and out.

     You say the repetition, it isn't on the slide: the same thing runs for
     all eight directions in one batch — not eight models — and is weighted
     with the wind rose into the comfort map they saw on the Gløshaugen slide.

     If you have time to spare: 8 directions x a few seconds versus 8 x
     several hours of CFD. That's the whole point of it being able to run
     while you draw. -->
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

# How does the architect analyze wind?

<div class="steps">

<div class="card past">
  <div class="kicker">Before</div>
  <img src="figures/modeller/modell-ekspert.svg" alt="">
  <p class="name">Wind expert</p>
  <p class="clock">Weeks</p>
</div>

<div class="card">
  <div class="kicker">With Forma</div>
  <img src="figures/modeller/modell-cfd.svg" alt="">
  <p class="name">Simulation <span class="sub">Physics model</span></p>
  <p class="clock">Hours</p>
</div>

<div></div>

</div>

<!-- Say: a quick look back, don't repeat the mesh explanation from the first
     time. "Here's where we were: the expert took weeks, the simulation in the
     tool takes hours." Then click, and the third step appears. -->
<!-- TODO ~0:08 -->

---

<!-- _class: ladder -->

# How does the architect analyze wind?

<div class="steps">

<div class="card past">
  <div class="kicker">Before</div>
  <img src="figures/modeller/modell-ekspert.svg" alt="">
  <p class="name">Wind expert</p>
  <p class="clock">Weeks</p>
</div>

<div class="card">
  <div class="kicker">With Forma</div>
  <img src="figures/modeller/modell-cfd.svg" alt="">
  <p class="name">Simulation <span class="sub">Physics model</span></p>
  <p class="clock">Hours</p>
</div>

<div class="card ai">
  <div class="kicker">With Forma</div>
  <img src="figures/modeller/modell-surrogat.svg" alt="">
  <p class="name">Estimate <span class="sub">Machine learning model</span></p>
  <p class="clock">Seconds</p>
</div>

</div>

<!-- Say: and then the third step. Don't explain it here — they've already
     seen the simulation and the training data. Just point out that the
     estimate exists, and say "this is what we'll look at now." The next
     slide is the machine learning model.

     Land it out loud: when the answer arrives while you're drawing, the
     analysis becomes something you make decisions WITH in the design phase —
     not a report that confirms a choice that's already been made.

     The point to take away, if the room only remembers one thing: when
     something becomes a hundred times cheaper, it doesn't just change how
     fast it goes. It changes who gets to use it, and when in the process. -->
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

# Can you tell the difference?

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
    <img src="figures/simulation.png" alt="Wind comfort map over Gløshaugen from the simulation: green areas sheltered between the buildings, yellow patches over the open parts to the north">
  </div>
  <div class="head">
    <div class="who">
      <img src="figures/modeller/modell-cfd.svg" alt="">
      <div class="labels">
        <span class="name">Simulation</span>
        <span class="sub">Documentation · more precise</span>
      </div>
    </div>
    <span class="time">1–2 hours</span>
  </div>
</figure>

<figure class="est">
  <div class="shot">
    <img src="figures/estimate.png" alt="Wind comfort map over the same area from the machine learning model: the same green and yellow areas, but with softer transitions and a little more yellow to the north">
  </div>
  <div class="head">
    <div class="who">
      <img src="figures/modeller/modell-surrogat.svg" alt="">
      <div class="labels">
        <span class="name">Estimate</span>
        <span class="sub">Iterations · approximate</span>
      </div>
    </div>
    <span class="time">2–6 seconds</span>
  </div>
</figure>

</div>

<!-- Say: two maps of the same site. One took a couple of hours, the other
     arrived while you were drawing. Don't say which is which right away —
     let the room look at them for a few seconds first.

     The point isn't that they're identical, because they aren't: look at the
     open areas to the north, where the estimate adds a little more yellow,
     and at the edges between the zones, which are softer in the estimate.
     That's the approximation showing.

     The point is that the conclusion is the same. The outdoor space between
     the buildings is sheltered in both, and the open areas are exposed in
     both. If you're choosing where the entrance and the outdoor seating
     should go, you make the same choice from either one.

     The labels give use and precision in one line; the time is on the right.
     Say that the simulation is more precise but takes longer — seconds
     versus hours is visible without you having to read it out. -->
<!-- TODO ~0:30 -->
