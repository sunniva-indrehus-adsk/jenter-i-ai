---
marp: true
theme: theme.css
paginate: true
math: katex
---

<!-- _class: title title-photo -->
<!-- _header: '24.09.2026' -->
<!-- paginate: false -->


# Jenter i AI


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
    <div class="frame portrait"><img src="figures/people/sunniva.png" alt="Sunniva"/></div>
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

     roles-holder «venstre» klemmer rollene inn i venstre halvdel, så boblene
     ikke legger seg over tomta. Arkitekten står i samme spalte her som på
     neste slide, så figuren ikke hopper når du klikker. -->

![](figures/tidligfase/hesthagen-flyfoto.jpg)

<div class="photo-credit">
  Flyfoto 2022 © Geovekst / Trondheim kommune · Kart © Kartverket, CC BY 4.0
</div>

<div class="roles-holder venstre">
<div class="roles">
<div class="role">
<div class="bubble"><ul>
<li>Hvor skal bygget stå, og hvor høyt kan det bli?</li>
<li>Blir det bra her (lys, støy, vind)?</li>
</ul></div>
<div class="figure"><img src="figures/tidligfase/rolle-arkitekt-lys.svg" alt=""><span class="name">Arkitekten</span></div>
</div>
</div>
</div>

<!-- Say: «først kommer arkitekten.» Les de tre spørsmålene, ikke ordrett — de
     står der for publikum, ikke for deg. -->
<!-- TODO ~0:20 -->

---

<!-- _class: demo overlay -->

<!-- Steg 3: utbyggeren kommer inn ved siden av, i høyre spalte av samme
     venstrestilte bærer. -->

![](figures/tidligfase/hesthagen-flyfoto.jpg)

<div class="photo-credit">
  Flyfoto 2022 © Geovekst / Trondheim kommune · Kart © Kartverket, CC BY 4.0
</div>

<div class="roles-holder venstre">
<div class="roles">
<div class="role">
<div class="bubble"><ul>
<li>Hvor skal bygget stå, og hvor høyt kan det bli?</li>
<li>Blir det bra her (lys, støy, vind)?</li>
</ul></div>
<div class="figure"><img src="figures/tidligfase/rolle-arkitekt-lys.svg" alt=""><span class="name">Arkitekten</span></div>
</div>
<div class="role fig-hoyre">
<div class="bubble"><ul>
<li>Går regnestykket opp?</li>
<li>Hva koster det å ombestemme seg om tre måneder?</li>
</ul></div>
<div class="figure"><img src="figures/tidligfase/rolle-utbygger-lys.svg" alt=""><span class="name">Utbyggeren</span></div>
</div>
</div>
</div>

<!-- Say: «og så kommer den som betaler.» Arkitekten spør om form, utbyggeren om
     risiko — begge trenger svar før noe er tegnet ferdig. Punchlinja «noen få
     uker der nesten alt avgjøres» sier du her, i stedet for å vise den. -->
<!-- TODO ~0:25 -->

---

<!-- _class: demo overlay logo-card -->

<!-- Logokortet fra filmen (1 s). Det rammer inn Forma-delen: ett foran videoen,
     ett etter vind- og AI-bildene. Marp-klassen logo-card skjuler vår egen
     Autodesk-logo nederst til venstre, siden kortet alt har en midt i bildet. -->

![](figures/video/stills/logo.jpg)

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
    <img src="figures/people/sunniva.png" alt="Sunniva">
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
   kortene står like store og på samme linje som uten markeringen. Fargen er
   hentet fra strømlinjene i vindbildet selv (#0A42D7, plukket fra kjernen av
   linjene), så markeringen peker på bildet i stedet for å konkurrere med det. */
.cols-3 .card.ring {
  position: relative;
  outline: 3px solid #0A42D7;
  outline-offset: 3px;
}
</style>

<div class="working-on">
  <div class="faces">
    <img src="figures/people/vilde-3.jpg" alt="Vilde">
    <img src="figures/people/sunniva.png" alt="Sunniva">
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

<img src="figures/vind/windcomfortgløs.png" alt="Komfortkart for vind over Gløshaugen, sett på skrå: uterommene mellom byggene er i hovedsak grønne, med gule flater i de åpne partiene og enkelte oransje felt">

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

     Prosentene i .pin-ene er lest av fargene i windcomfortgløs.png og
     verifisert mot pikslene: ring 1 og 3 ligger på Rusle (gult), ring 2 på
     Sitte (lysegrønt). Byttes bildet, må de sjekkes på nytt. -->

# Vindkomfort

<div class="use">

<div class="map">

<img src="figures/vind/windcomfortgløs.png" alt="Komfortkart for vind over Gløshaugen, sett på skrå: uterommene mellom byggene er i hovedsak grønne, med gule flater i de åpne partiene og enkelte oransje felt">

<div class="pin" style="left: 11%; top: 16%;">
  <span class="dot"></span>
  <span class="lbl"><b>Åpent felt</b><span>Ingenting bremser vinden — her går du forbi.</span></span>
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

     Det åpne feltet først: ingenting står i veien, så vinden får fart. Gult
     betyr at det er fint å gå gjennom, ikke å bli sittende. -->
<!-- TODO ~0:12 -->

---
<!-- _class: comfort-map -->

<!-- Trinn 3 av 4: første og andre merkelapp. Alt utenom .pin-ene skal være
     identisk med de andre tre trinnene — se kommentaren på trinn 2. -->

# Vindkomfort

<div class="use">

<div class="map">

<img src="figures/vind/windcomfortgløs.png" alt="Komfortkart for vind over Gløshaugen, sett på skrå: uterommene mellom byggene er i hovedsak grønne, med gule flater i de åpne partiene og enkelte oransje felt">

<div class="pin" style="left: 11%; top: 16%;">
  <span class="dot"></span>
  <span class="lbl"><b>Åpent felt</b><span>Ingenting bremser vinden — her går du forbi.</span></span>
</div>

<div class="pin" style="left: 57%; top: 40%;">
  <span class="dot"></span>
  <span class="lbl"><b>I le mellom byggene</b><span>Lunt nok til å sitte. Her kan uterommet ligge.</span></span>
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

<img src="figures/vind/windcomfortgløs.png" alt="Komfortkart for vind over Gløshaugen, sett på skrå: uterommene mellom byggene er i hovedsak grønne, med gule flater i de åpne partiene og enkelte oransje felt">

<div class="pin" style="left: 11%; top: 16%;">
  <span class="dot"></span>
  <span class="lbl"><b>Åpent felt</b><span>Ingenting bremser vinden — her går du forbi.</span></span>
</div>

<div class="pin" style="left: 57%; top: 40%;">
  <span class="dot"></span>
  <span class="lbl"><b>I le mellom byggene</b><span>Lunt nok til å sitte. Her kan uterommet ligge.</span></span>
</div>

<div class="pin" style="left: 21%; top: 58%;">
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

/* Tre trinn i oppskriften. De to første er ingrediensene og det tredje er
   resultatet — derfor et plusstegn mellom 1 og 2, og en pil inn mot 3.
   Skiltene er egne kolonner i rutenettet og ikke marger, så kortene blir like
   brede uansett hvor mye tekst de har. */
.recipe {
  display: grid;
  grid-template-columns: 1fr 34px 1fr 46px 1fr;
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
  min-height: 280px;
}
/* Det siste kortet er svaret, ikke enda en ingrediens. Aksentblå topplinje og
   lys flate, samme grep som .panel.ai og .card.ai ellers i decket. */
.recipe .card.out { border-top-color: var(--accent); background: var(--accent-soft); }

/* Miniatyrene: fast høyde og overflow: hidden, så de tre boksene er like store
   uansett hvilket format kildefila har. 185 px er den naturlige høyden til de
   to liggende figurene i en 282 px bred kortspalte — da slipper de å beskjæres
   i det hele tatt, og bare vindrosen trenger et utsnitt. */
.recipe .thumb {
  position: relative;
  height: 185px;
  overflow: hidden;
  margin-bottom: 0.9em;
}
.recipe .thumb img { position: absolute; top: 0; left: 0; width: 100%; display: block; }
/* Vindrosefila er stående og har fartsfordelingen under selve rosen. Her skal
   bare rosen vises: bildet skaleres etter høyden (167 % ≈ rosen fyller de
   øverste 58 % av fila), sentreres, og resten klippes av overflow: hidden. */
.recipe .thumb.rose img {
  width: auto;
  height: 174%;
  left: 50%;
  top: -4%;
  transform: translateX(-50%);
}

.recipe h3 { font-size: 1.05em; margin: 0 0 0.4em; }
.recipe .card.out h3 { color: var(--accent); }
.recipe p { margin: 0; font-size: 0.86em; line-height: 1.45; color: var(--muted); }

/* Plusstegnet står for «og», pila for «blir til» — samme skille som på
   result-build-slidene, der de to tegnene alt brukes med den betydningen. */
.recipe .plus {
  align-self: center;
  text-align: center;
  font-family: var(--display);
  font-weight: 700;
  font-size: 1.5em;
  line-height: 1;
}
.recipe .arr { align-self: center; position: relative; height: 3px; background: var(--ink); }
.recipe .arr::after {
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

# Hvordan beregner vi vindkomfort?

<div class="recipe">

<div class="card">
  <div class="thumb"><img src="figures/vind/vindretninger-plan.svg" alt="Tomta sett ovenfra, med piler som peker inn mot den fra åtte vindretninger"></div>
  <h3>Simulering</h3>
  <p>Vi simulerer hvordan vinden beveger seg mellom byggene når den kommer fra åtte ulike retninger.</p>
</div>

<div class="plus">+</div>

<div class="card">
  <div class="thumb rose"><img src="figures/vind/vindrose.png" alt="Vindrose for stedet: åtte sektorer med hvor stor andel av tiden det blåser fra hver retning, sørvest størst med 22 prosent"></div>
  <h3>Historiske data</h3>
  <p>Målt vindhastighet og vindretning for stedet: hvor ofte det blåser fra hver retning, og hvor hardt.</p>
</div>

<div class="arr"></div>

<div class="card out">
  <div class="thumb"><img src="figures/vind/windcomfortgløs.png" alt="Komfortkart for vind over Gløshaugen: grønt mellom byggene, gult i de åpne partiene"></div>
  <h3>Vindkomfort</h3>
  <p>Til sammen gir de hvor komfortabelt det er, sted for sted på tomta.</p>
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

<!-- Kopi av trinn 2 (slide 20) — flata skal være IDENTISK med den, ellers
     hopper stigen når du kommer tilbake til den her. Retter du et kort på
     slide 20, rett det samme her.

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
  <div class="frame"><img src="figures/people/sunniva.png" alt="Sunniva"/></div>
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

---
<!-- ──────────────────────────────────────────────────────────────────────
     BAKLOMMA. Alt under denne linja er utenfor taletiden.

     Her ligger to sett slides:

     1. «Fra vind: komfortabelhet» (tre trinn). Hoveddecket bruker nå
        «Vindkomfort» (to trinn) i stedet — de sier mye av det samme, men
        «Vindkomfort» viser kartet over hele tomta med de påpekte stedene,
        der «Fra vind» har komfortskalaen og kartet av hovedbygget.
        «Hvordan beregner vi vindkomfort?», som lå her, står nå i hovedløpet
        rett etter «Vindkomfort».

     2. To av modell-slidene som sto i hovedløpet mellom «Tusenvis av
        simuleringer» og de 15 rutene: «To modeller, ett svar» og
        «Surrogatmodellen». Den tredje, «Maskinlæringsmodellen», står nå
        som siste innholdsslide i hovedløpet i stedet — etter de 15 rutene,
        rett før «Vi står på stand».
        NB: det ligger to slides som heter «Surrogatmodellen» her — main sin
        boksfigur med treningsløkka, og vår pipeline-skisse lenger ned.

     3. Blokka som alt lå i baklomma: CFD-ligningen, CFD mot surrogat og
        pipeline-skissen. Kommentaren under forklarer rekkefølgen.

     Skal noe av dette opp i hoveddecket igjen, må du sjekke at det ikke
     dublerer main sin «To modeller, ett svar» eller «Surrogatmodellen».
     ────────────────────────────────────────────────────────────────────── -->
<!-- _class: result-build -->

# Fra vind: komfortabelhet

<div class="build">

<div></div>

<div></div>

<div class="mid">
  <div class="scale-strip">
    <div class="kicker">Komfortskalaen — Lawson LDDC</div>
    <div class="row">
      <div><span class="sw" style="background:#B2F8DA"></span><b>Sitte</b><span class="t">under 2,5 m/s</span></div>
      <div><span class="sw" style="background:#55DCA2"></span><b>Stå</b><span class="t">over 2,5 m/s</span></div>
      <div><span class="sw" style="background:#FED52A"></span><b>Rusle</b><span class="t">over 4 m/s</span></div>
      <div><span class="sw" style="background:#FFA900"></span><b>Gå</b><span class="t">over 6 m/s</span></div>
      <div><span class="sw" style="background:#FF463A"></span><b>Ukomf.</b><span class="t">over 8 m/s</span></div>
    </div>
  </div>
  <img src="figures/vind/gløshaugen-komfor-plot.png" alt="Komfortkart for vind rundt hovedbygget på Gløshaugen">
  <div class="figcap">Komfortkart for vind, hovedbygget på Gløshaugen.</div>
</div>

<div></div>

<div></div>

</div>

<!-- Say: dette er svaret arkitekten ser. Ingen modell, ingen ligning — bare
     resultatet, og fargene som sier hva det betyr. La det stå litt.
     De to neste slidene legger på hvor svaret kommer fra. -->
<!-- TODO ~0:30 -->

---

<!-- _class: result-build -->

# Fra vind: komfortabelhet

<div class="build">

<div class="panel">
  <img src="figures/modeller/modell-cfd.svg" alt="">
  <p class="h">Fysikkmodellen</p>

$$
\begin{aligned}
(\mathbf{U}\cdot\nabla)\mathbf{U} \;=\;& -\nabla p \\
&+\; \nabla\cdot\big[(\nu+\nu_t)\big(\nabla\mathbf{U}+\nabla\mathbf{U}^{\top}\big)\big] \\
&-\; c_d\,a\,\lvert\mathbf{U}\rvert\,\mathbf{U} \\[0.3em]
\nabla\cdot\mathbf{U} \;=\;& \;0
\end{aligned}
$$

  <p class="t">Timer per iterasjon.</p>
</div>

<div class="arr to-right"></div>

<div class="mid">
  <div class="scale-strip">
    <div class="kicker">Komfortskalaen — Lawson LDDC</div>
    <div class="row">
      <div><span class="sw" style="background:#B2F8DA"></span><b>Sitte</b><span class="t">under 2,5 m/s</span></div>
      <div><span class="sw" style="background:#55DCA2"></span><b>Stå</b><span class="t">over 2,5 m/s</span></div>
      <div><span class="sw" style="background:#FED52A"></span><b>Rusle</b><span class="t">over 4 m/s</span></div>
      <div><span class="sw" style="background:#FFA900"></span><b>Gå</b><span class="t">over 6 m/s</span></div>
      <div><span class="sw" style="background:#FF463A"></span><b>Ukomf.</b><span class="t">over 8 m/s</span></div>
    </div>
  </div>
  <img src="figures/vind/gløshaugen-komfor-plot.png" alt="Komfortkart for vind rundt hovedbygget på Gløshaugen">
  <div class="figcap">Komfortkart for vind, hovedbygget på Gløshaugen.</div>
</div>

<div></div>

<div></div>

</div>

<!-- Say: «dette er hvordan vi FAKTISK regner det ut.» Ligningen er den
     stasjonære RANS-en simpleFoam løser, med vårt eget vegetasjonsledd. Ikke gå
     gjennom leddene her — den annoterte versjonen kommer på Fysikkmodell-sliden.
     Poenget nå er bare: timer. -->
<!-- TODO ~0:25 -->

---

<!-- _class: result-build -->

# Fra vind: komfortabelhet

<div class="build">

<div class="panel">
  <img src="figures/modeller/modell-cfd.svg" alt="">
  <p class="h">Fysikkmodellen</p>

$$
\begin{aligned}
(\mathbf{U}\cdot\nabla)\mathbf{U} \;=\;& -\nabla p \\
&+\; \nabla\cdot\big[(\nu+\nu_t)\big(\nabla\mathbf{U}+\nabla\mathbf{U}^{\top}\big)\big] \\
&-\; c_d\,a\,\lvert\mathbf{U}\rvert\,\mathbf{U} \\[0.3em]
\nabla\cdot\mathbf{U} \;=\;& \;0
\end{aligned}
$$

  <p class="t">Timer per iterasjon.</p>
</div>

<div class="arr to-right"></div>

<div class="mid">
  <div class="scale-strip">
    <div class="kicker">Komfortskalaen — Lawson LDDC</div>
    <div class="row">
      <div><span class="sw" style="background:#B2F8DA"></span><b>Sitte</b><span class="t">under 2,5 m/s</span></div>
      <div><span class="sw" style="background:#55DCA2"></span><b>Stå</b><span class="t">over 2,5 m/s</span></div>
      <div><span class="sw" style="background:#FED52A"></span><b>Rusle</b><span class="t">over 4 m/s</span></div>
      <div><span class="sw" style="background:#FFA900"></span><b>Gå</b><span class="t">over 6 m/s</span></div>
      <div><span class="sw" style="background:#FF463A"></span><b>Ukomf.</b><span class="t">over 8 m/s</span></div>
    </div>
  </div>
  <img src="figures/vind/gløshaugen-komfor-plot.png" alt="Komfortkart for vind rundt hovedbygget på Gløshaugen">
  <div class="figcap">Komfortkart for vind, hovedbygget på Gløshaugen.</div>
</div>

<div class="arr ai to-left"></div>

<div class="panel ai">
  <img src="figures/modeller/modell-surrogat.svg" alt="">
  <p class="h">Surrogatmodellen</p>
  <p class="d">Nevralt nett, trent på ferdige fysikkmodell-kjøringer.</p>
  <p class="t">Sekunder per iterasjon.</p>
</div>

</div>

<!-- Say: «og dette er den andre veien til det samme bildet.» Begge pilene
     peker inn mot samme kart — det er hele argumentet. Så: timer mot sekunder,
     og hvorfor det avgjør hvem som kan bruke modellen. -->
<!-- TODO ~0:30 -->

---

# To modeller, ett svar

<style scoped>
section { font-size: 22px; }

.lead { margin: 0.2em 0 0; font-size: 0.9em; color: var(--muted); max-width: 52em; }

/* 300 px sider og ikke 200: sidene bærer nå egenskapene fra «Hva skiller dem»,
   ikke bare en tidsangivelse. Det gjør kartet i midten mindre, men til gjengjeld
   står forskjellene og det felles svaret på samme slide. */
.trio {
  display: grid;
  grid-template-columns: 300px 1fr 300px;
  gap: 1.4em;
  align-items: start;
  margin-top: 1.1em;
}

.trio .card { border-top-width: 3px; padding: 0.8em 0.9em 0.9em; }
.trio .card.ai { border-top-color: var(--accent); background: var(--accent-soft); }

/* Ikon og navn på samme linje sparer høyden en egen ikonrad ville tatt. */
.trio .head { display: grid; grid-template-columns: 64px 1fr; gap: 0.7em; align-items: center; }
.trio .head img { width: 64px; height: 64px; display: block; }
.trio .head h3 { margin: 0; font-size: 1em; line-height: 1.15; }
.trio .card.ai .head h3 { color: var(--accent); }

/* Tiden er den største forskjellen mellom de to, så den får display-snittet og
   egen linje. Resten av egenskapene står under, i mindre skrift. */
.trio .clock {
  font-family: var(--display);
  font-weight: 700;
  font-size: 1.45em;
  line-height: 1;
  letter-spacing: -0.015em;
  margin: 0.7em 0 0;
}
.trio .card.ai .clock { color: var(--accent); }
.trio .clock span { font-family: var(--sans); font-weight: 400; font-size: 0.44em; color: var(--muted); margin-left: 0.4em; letter-spacing: 0; }

.trio ul { margin: 0.7em 0 0; padding-left: 1.1em; font-size: 0.82em; }
.trio li { margin: 0.32em 0; }

.trio .mid img { display: block; width: 100%; height: auto; }
.trio .mid .figcap { margin-top: 0.5em; text-align: center; }

/* Fargeforklaringen, samme som på komfort-sliden. Fargene og navnene er
   verifisert mot koden der — ikke funnet på her. */
.scale-strip { margin-bottom: 0.7em; }
.scale-strip .kicker { margin-bottom: 0.45em; font-size: 0.62em; }
.scale-strip .row { display: grid; grid-template-columns: repeat(5, max-content); justify-content: space-between; gap: 0.4em; }
.scale-strip .row > div { font-size: 0.56em; line-height: 1.25; white-space: nowrap; }
.scale-strip .sw {
  display: inline-block;
  width: 0.9em;
  height: 0.9em;
  border-radius: 2px;
  box-shadow: 0 0 0 1px rgba(0, 0, 0, 0.14);
  margin-right: 0.35em;
  vertical-align: -0.07em;
}
.scale-strip .t { display: block; color: var(--muted); font-size: 0.88em; margin-top: 0.12em; }
</style>

<p class="lead">Begge svarer på det samme spørsmålet — hvordan vinden oppfører seg mellom byggene. Forskjellen er hvor nøyaktig svaret blir, og hvor lenge du må vente på det.</p>

<div class="trio">

<div class="card">
  <div class="head">
    <img src="figures/modeller/modell-cfd.svg" alt="">
    <h3>Fullverdig CFD</h3>
  </div>
  <p class="clock">Timer<span>per kjøring</span></p>
  <ul>
    <li>Nøyaktig, og etterprøvbar</li>
    <li>Kjøres én gang, til slutt</li>
    <li><b>Dokumenterer</b> et valg som alt er tatt</li>
  </ul>
</div>

<div class="mid">
  <div class="scale-strip">
    <div class="kicker">Komfortskalaen — Lawson LDDC</div>
    <div class="row">
      <div><span class="sw" style="background:#B2F8DA"></span><b>Sitte</b><span class="t">under 2,5 m/s</span></div>
      <div><span class="sw" style="background:#55DCA2"></span><b>Stå</b><span class="t">over 2,5 m/s</span></div>
      <div><span class="sw" style="background:#FED52A"></span><b>Rusle</b><span class="t">over 4 m/s</span></div>
      <div><span class="sw" style="background:#FFA900"></span><b>Gå</b><span class="t">over 6 m/s</span></div>
      <div><span class="sw" style="background:#FF463A"></span><b>Ukomf.</b><span class="t">over 8 m/s</span></div>
    </div>
  </div>
  <img src="figures/vind/gløshaugen-komfor-plot.png" alt="Komfortkart for vind rundt hovedbygget på Gløshaugen">
  <div class="figcap">Samme komfortkart — uansett hvilken av dem som regnet det ut.</div>
</div>

<div class="card ai">
  <div class="head">
    <img src="figures/modeller/modell-surrogat.svg" alt="">
    <h3>Surrogatmodellen</h3>
  </div>
  <p class="clock">Sekunder<span>per kjøring</span></p>
  <ul>
    <li>Omtrentlig, med et avvik vi måler</li>
    <li>Kjøres hele tiden, mens man tegner</li>
    <li><b>Tar</b> valget, sammen med arkitekten</li>
  </ul>
</div>

</div>

<!-- Say: les inngangslinja først — den gjør at de to sidene leses som to
     nøyaktighetsnivåer for samme svar, og ikke som to ulike verktøy.
     Pek så på «Timer» mot «Sekunder». Det er den forskjellen som avgjør hvem
     som kan bruke modellen, og når. Kartet i midten er beviset på at de svarer
     på det samme. -->
<!-- TODO ~0:45 -->

---

# Surrogatmodellen

<style scoped>
/* Figuren er 2,67:1, så bredden styrer høyden: 79 % av tekstbredden gir ca.
   340 px. Da er det ca. 30 px klaring ned til bunnmargen etter callouten —
   skru opp prosenten, og callouten legger seg oppå logoen. */
img { display: block; margin: 0.8em auto 0; width: 79%; }
.callout { margin-top: 1.1em; }
</style>

<!--
FIGUREN ER VERIFISERT MOT KODEN i spacemakerai/wind-surrogate. Det viktigste
funnet: vindretningen er IKKE en inngang til nettet. Geometrien roteres i
stedet, og for komfort kjøres alle åtte retninger som én batch:

  lib/prediction.py:53-61   predict(): rotate(-direction) → nett → rotate(+direction)
  lib/prediction.py:64-86   predict_comfort(): åtte rotasjoner i én batch,
                            deretter vektet med vindrosen
  lib/constants.py:35       WIND_DIRECTIONS = [0,45,...,315]
  lib/constants.py:37       GROUND_MEASUREMENT_HEIGHT = 1.75 m
  lib/constants.py:22-31    200x200 px site i 500x500 px kontekst, 1,5 m/px
  lib/utils/model.py        ONNX Runtime, assets/latest.onnx
  lambdas/handler_trigger_data_generation.py
                            treningsdata hentes løpende fra SUCCEEDED-analyser
                            i wind-analysis-backend-prod

Detaljene står i SVG-filens egen header, og manuset i Say-kommentaren nederst.
(Ikke skriv en HTML-kommentar inni denne: den ytre slutter ved det første
sluttmerket, og resten lekker ut som brødtekst.)
-->
<img src="figures/modeller/surrogat-pipeline.svg" alt="Terreng og bygninger som høydekart inn, nevralt nett som roterer geometrien for åtte vindretninger, åtte vindfelt ut, vektet med vindrosen til et komfortkart — trent på ferdige CFD-kjøringer">

<div class="callout">

Modellen har sett så mange løsninger at den kjenner igjen svaret.

</div>

<div class="todo">Gir skissen mening?</div>

<!-- Say: rammen som gjør det forståelig for en AI-sal: det er bilde-til-bilde.
     Inn: terreng og bygninger som høydekart. Ut: et hastighetsfelt.

     De to poengene som er verdt tiden:

     1. Nettet vet ikke hva en vindretning er. Vi ROTERER geometrien i stedet,
        kjører nettet, og roterer svaret tilbake. Åtte retninger blir åtte
        rotasjoner i én batch. Samme oppskrift som CFD-en — «gjenta for hver
        retning, vekt med vindrosen» — men åtte nettverkskjøringer i stedet for
        åtte timelange simuleringer.

     2. Treningsdataene er kundenes egne CFD-analyser. En lambda plukker opp
        ferdige kjøringer fra produksjon og gjør dem til treningseksempler. Hver
        gang noen betaler for den dyre analysen, blir den et eksempel til den
        raske. Det er derfor det er treningsdataene, ikke nettverket, som er
        arbeidet. -->
<!-- TODO ~1:05 -->

---

<!-- ─────────────────────────────────────────────────────────────────
     BAKLOMME — ikke en del av hovedløpet.

     Tre slides som sto mellom stigen og «Arkitekten bruker begge»:
       «Slik regner vi det ut» (CFD-ligningen, 1–2 timer)
       «For lenge når du drodler» (CFD mot surrogat)
       «Surrogatmodellen» (skissen av pipelinen)

     De hører sammen og må flyttes som én blokk: «For lenge når du
     drodler» innfører surrogatmodellen, og «Surrogatmodellen» tegner
     pipelinen.

     NB: den fjerde sliden i blokka — surrogat-figuren, den konkrete
     inn/ut-versjonen — er FLYTTET UT og står nå i hovedløpet som
     slide 26, rett etter «Tusenvis av simuleringer». Den lener seg
     derfor ikke lenger på skissen, og den står ikke og venter på at
     disse tre skal hentes fram. Tas de inn igjen, kommer skissen
     ETTER den konkrete figuren — vurder om det er rekkefølgen du vil.

     Til sammen ca. 2:00 av taletiden. Skal de tilbake, hører de hjemme
     rett etter den tredje stige-sliden. -->



<!-- _class: result-build -->

# Slik regner vi det ut

<style scoped>
.lead { margin: 0.2em 0 0; font-size: 0.82em; color: var(--muted); max-width: 52em; }
</style>

<p class="lead">En simulering av selve fysikken — hvordan luft beveger seg mellom byggene. Én til to timer per kjøring.</p>

<div class="build">

<div class="panel">
  <img src="figures/modeller/modell-cfd.svg" alt="">
  <p class="h">Fysikkmodellen</p>

$$
\begin{aligned}
(\mathbf{U}\cdot\nabla)\mathbf{U} \;=\;& -\nabla p \\
&+\; \nabla\cdot\big[(\nu+\nu_t)\big(\nabla\mathbf{U}+\nabla\mathbf{U}^{\top}\big)\big] \\
&-\; c_d\,a\,\lvert\mathbf{U}\rvert\,\mathbf{U} \\[0.3em]
\nabla\cdot\mathbf{U} \;=\;& \;0
\end{aligned}
$$

  <p class="t">1–2 timer per kjøring.</p>
</div>

<div class="arr to-right"></div>

<div class="mid">
  <div class="scale-strip">
    <div class="kicker">Komfortskalaen — Lawson LDDC</div>
    <div class="row">
      <div><span class="sw" style="background:#B2F8DA"></span><b>Sitte</b><span class="t">under 2,5 m/s</span></div>
      <div><span class="sw" style="background:#55DCA2"></span><b>Stå</b><span class="t">over 2,5 m/s</span></div>
      <div><span class="sw" style="background:#FED52A"></span><b>Rusle</b><span class="t">over 4 m/s</span></div>
      <div><span class="sw" style="background:#FFA900"></span><b>Gå</b><span class="t">over 6 m/s</span></div>
      <div><span class="sw" style="background:#FF463A"></span><b>Ukomf.</b><span class="t">over 8 m/s</span></div>
    </div>
  </div>
  <img src="figures/vind/windcomfortgløs.png" alt="Komfortkart for vind over Gløshaugen: grønt mellom byggene, gult i de åpne partiene">
  <div class="figcap">Komfortkart for vind, Gløshaugen.</div>
</div>

<div></div>

<div></div>

</div>

<!-- Say: «og dette er hvordan vi faktisk regner det ut.» Ligningen er den
     stasjonære RANS-en simpleFoam løser, med vårt eget vegetasjonsledd. Ikke gå
     gjennom leddene her — den annoterte versjonen kommer på Fysikkmodell-sliden.
     Poenget nå er bare: dette er en kompleks fysikkmodell, og den tar én til to
     timer. Si tallet sakte — det er oppsettet til neste slide. -->
<!-- TODO ~0:25 -->

---


<!-- _class: result-build -->

# For lenge når du drodler

<style scoped>
.lead { margin: 0.2em 0 0; font-size: 0.82em; color: var(--muted); max-width: 52em; }
</style>

<p class="lead">Derfor bygget vi surrogatmodellen: trent på resultatene fra tusenvis av simuleringer, og gir samme kart på sekunder.</p>

<div class="build">

<div class="panel">
  <img src="figures/modeller/modell-cfd.svg" alt="">
  <p class="h">Fysikkmodellen</p>

$$
\begin{aligned}
(\mathbf{U}\cdot\nabla)\mathbf{U} \;=\;& -\nabla p \\
&+\; \nabla\cdot\big[(\nu+\nu_t)\big(\nabla\mathbf{U}+\nabla\mathbf{U}^{\top}\big)\big] \\
&-\; c_d\,a\,\lvert\mathbf{U}\rvert\,\mathbf{U} \\[0.3em]
\nabla\cdot\mathbf{U} \;=\;& \;0
\end{aligned}
$$

  <p class="t">1–2 timer per kjøring.</p>
</div>

<div class="arr to-right"></div>

<div class="mid">
  <div class="scale-strip">
    <div class="kicker">Komfortskalaen — Lawson LDDC</div>
    <div class="row">
      <div><span class="sw" style="background:#B2F8DA"></span><b>Sitte</b><span class="t">under 2,5 m/s</span></div>
      <div><span class="sw" style="background:#55DCA2"></span><b>Stå</b><span class="t">over 2,5 m/s</span></div>
      <div><span class="sw" style="background:#FED52A"></span><b>Rusle</b><span class="t">over 4 m/s</span></div>
      <div><span class="sw" style="background:#FFA900"></span><b>Gå</b><span class="t">over 6 m/s</span></div>
      <div><span class="sw" style="background:#FF463A"></span><b>Ukomf.</b><span class="t">over 8 m/s</span></div>
    </div>
  </div>
  <img src="figures/vind/windcomfortgløs.png" alt="Komfortkart for vind over Gløshaugen: grønt mellom byggene, gult i de åpne partiene">
  <div class="figcap">Komfortkart for vind, Gløshaugen.</div>
</div>

<div class="arr ai to-left"></div>

<div class="panel ai">
  <img src="figures/modeller/modell-surrogat.svg" alt="">
  <p class="h">Surrogatmodellen</p>
  <p class="d">Nevralt nett, trent på tusenvis av ferdige simuleringer.</p>
  <p class="t">Sekunder per kjøring.</p>
</div>

</div>

<!-- Say: her er svingen. «Én til to timer er greit når beslutningen er tatt.
     Men arkitekten sitter og drodler — da er det for lenge.»

     Så den andre veien til det samme bildet: en maskinlæringsmodell trent på
     resultatene fra tusenvis av simuleringer. Den har lært hvordan vinden
     beveger seg på en tomt, og gir et estimat på sekunder.

     Begge pilene peker inn mot samme kart — det er hele argumentet. -->
<!-- TODO ~0:30 -->

---


# Surrogatmodellen

<style scoped>
/* Figuren er 2,67:1, så bredden styrer høyden: 79 % av tekstbredden gir ca.
   340 px. Da er det ca. 30 px klaring ned til bunnmargen etter callouten —
   skru opp prosenten, og callouten legger seg oppå logoen. */
img { display: block; margin: 0.8em auto 0; width: 79%; }
.callout { margin-top: 1.1em; }
</style>

<!--
FIGUREN ER VERIFISERT MOT KODEN i spacemakerai/wind-surrogate. Det viktigste
funnet: vindretningen er IKKE en inngang til nettet. Geometrien roteres i
stedet, og for komfort kjøres alle åtte retninger som én batch:

  lib/prediction.py:53-61   predict(): rotate(-direction) → nett → rotate(+direction)
  lib/prediction.py:64-86   predict_comfort(): åtte rotasjoner i én batch,
                            deretter vektet med vindrosen
  lib/constants.py:35       WIND_DIRECTIONS = [0,45,...,315]
  lib/constants.py:37       GROUND_MEASUREMENT_HEIGHT = 1.75 m
  lib/constants.py:22-31    200x200 px site i 500x500 px kontekst, 1,5 m/px
  lib/utils/model.py        ONNX Runtime, assets/latest.onnx
  lambdas/handler_trigger_data_generation.py
                            treningsdata hentes løpende fra SUCCEEDED-analyser
                            i wind-analysis-backend-prod

Detaljene står i SVG-filens egen header, og manuset i Say-kommentaren nederst.
(Ikke skriv en HTML-kommentar inni denne: den ytre slutter ved det første
sluttmerket, og resten lekker ut som brødtekst.)
-->
<img src="figures/modeller/surrogat-pipeline.svg" alt="Terreng og bygninger som høydekart inn, nevralt nett som roterer geometrien for åtte vindretninger, åtte vindfelt ut, vektet med vindrosen til et komfortkart — trent på ferdige CFD-kjøringer">

<div class="callout">

Modellen har sett så mange løsninger at den kjenner igjen svaret.

</div>

<div class="todo">Gir skissen mening?</div>

<!-- Say: rammen som gjør det forståelig for en AI-sal: det er bilde-til-bilde.
     Inn: terreng og bygninger som høydekart. Ut: et hastighetsfelt.

     De to poengene som er verdt tiden:

     1. Nettet vet ikke hva en vindretning er. Vi ROTERER geometrien i stedet,
        kjører nettet, og roterer svaret tilbake. Åtte retninger blir åtte
        rotasjoner i én batch. Samme oppskrift som CFD-en — «gjenta for hver
        retning, vekt med vindrosen» — men åtte nettverkskjøringer i stedet for
        åtte timelange simuleringer.

     2. Treningsdataene er kundenes egne CFD-analyser. En lambda plukker opp
        ferdige kjøringer fra produksjon og gjør dem til treningseksempler. Hver
        gang noen betaler for den dyre analysen, blir den et eksempel til den
        raske. Det er derfor det er treningsdataene, ikke nettverket, som er
        arbeidet. -->
<!-- TODO ~1:05 -->

---

<!-- ─────────────────────────────────────────────────────────────────
     BAKLOMME 2 — ikke en del av hovedløpet.

     Tre slides som sto mellom stigen og «Den kjører mens du tegner»:
       «Arkitekten bruker begge» (CFD mot surrogat, egenskap for egenskap)
       «Regulering av Hesthagen» (case-skilleark)
       «Hesthagen — fra parkeringsplass til bygg»

     De to siste hører sammen: skillearket annonserer caset.

     NB: «Den kjører mens du tegner» står fortsatt i hovedløpet, og
     rutene der er klippet fra Hesthagen-modellen. Uten caset må du
     fortelle den sliden uten å lene deg på at salen kjenner tomta.

     Til sammen ca. 1:20 av taletiden. -->



# Arkitekten bruker begge

<style scoped>
section { font-size: 22px; }

.lead { margin: 0.2em 0 0; font-size: 0.9em; color: var(--muted); max-width: 52em; }

/* 300 px sider og ikke 200: sidene bærer nå egenskapene fra «Hva skiller dem»,
   ikke bare en tidsangivelse. Det gjør kartet i midten mindre, men til gjengjeld
   står forskjellene og det felles svaret på samme slide. */
.trio {
  display: grid;
  grid-template-columns: 300px 1fr 300px;
  gap: 1.4em;
  align-items: start;
  margin-top: 1.1em;
}

.trio .card { border-top-width: 3px; padding: 0.8em 0.9em 0.9em; }
.trio .card.ai { border-top-color: var(--accent); background: var(--accent-soft); }

/* Ikon og navn på samme linje sparer høyden en egen ikonrad ville tatt. */
.trio .head { display: grid; grid-template-columns: 64px 1fr; gap: 0.7em; align-items: center; }
.trio .head img { width: 64px; height: 64px; display: block; }
.trio .head h3 { margin: 0; font-size: 1em; line-height: 1.15; }
.trio .card.ai .head h3 { color: var(--accent); }

/* Tiden er den største forskjellen mellom de to, så den får display-snittet og
   egen linje. Resten av egenskapene står under, i mindre skrift. */
.trio .clock {
  font-family: var(--display);
  font-weight: 700;
  font-size: 1.45em;
  line-height: 1;
  letter-spacing: -0.015em;
  margin: 0.7em 0 0;
}
.trio .card.ai .clock { color: var(--accent); }
.trio .clock span { font-family: var(--sans); font-weight: 400; font-size: 0.44em; color: var(--muted); margin-left: 0.4em; letter-spacing: 0; }

.trio ul { margin: 0.7em 0 0; padding-left: 1.1em; font-size: 0.82em; }
.trio li { margin: 0.32em 0; }

/* Samme grunn som i result-build: kartet er 1,287:1, og ved full spaltebredde
   havner bildeteksten i logoen. Her er spalten lavere, så taket er 320 px. */
.trio .mid img { display: block; max-height: 320px; max-width: 100%; width: auto; margin: 0 auto; }
.trio .mid .figcap { margin-top: 0.5em; text-align: center; }

/* Fargeforklaringen, samme som på komfort-sliden. Fargene og navnene er
   verifisert mot koden der — ikke funnet på her. */
.scale-strip { margin-bottom: 0.7em; }
.scale-strip .kicker { margin-bottom: 0.45em; font-size: 0.62em; }
.scale-strip .row { display: grid; grid-template-columns: repeat(5, max-content); justify-content: space-between; gap: 0.4em; }
.scale-strip .row > div { font-size: 0.56em; line-height: 1.25; white-space: nowrap; }
.scale-strip .sw {
  display: inline-block;
  width: 0.9em;
  height: 0.9em;
  border-radius: 2px;
  box-shadow: 0 0 0 1px rgba(0, 0, 0, 0.14);
  margin-right: 0.35em;
  vertical-align: -0.07em;
}
.scale-strip .t { display: block; color: var(--muted); font-size: 0.88em; margin-top: 0.12em; }
</style>

<p class="lead">De to brukes om hverandre: estimatet mens ideene står på skissestadiet, simuleringen når valget skal tas og dokumenteres. Samme spørsmål, to nivåer av nøyaktighet — og to helt ulike ventetider.</p>

<div class="trio">

<div class="card">
  <div class="head">
    <img src="figures/modeller/modell-cfd.svg" alt="">
    <h3>Fullverdig CFD</h3>
  </div>
  <p class="clock">1–2 timer<span>per kjøring</span></p>
  <ul>
    <li>Nøyaktig, og etterprøvbar</li>
    <li>Kjøres ved de viktige beslutningene</li>
    <li><b>Dokumenterer</b> valget som er tatt</li>
  </ul>
</div>

<div class="mid">
  <div class="scale-strip">
    <div class="kicker">Komfortskalaen — Lawson LDDC</div>
    <div class="row">
      <div><span class="sw" style="background:#B2F8DA"></span><b>Sitte</b><span class="t">under 2,5 m/s</span></div>
      <div><span class="sw" style="background:#55DCA2"></span><b>Stå</b><span class="t">over 2,5 m/s</span></div>
      <div><span class="sw" style="background:#FED52A"></span><b>Rusle</b><span class="t">over 4 m/s</span></div>
      <div><span class="sw" style="background:#FFA900"></span><b>Gå</b><span class="t">over 6 m/s</span></div>
      <div><span class="sw" style="background:#FF463A"></span><b>Ukomf.</b><span class="t">over 8 m/s</span></div>
    </div>
  </div>
  <img src="figures/vind/windcomfortgløs.png" alt="Komfortkart for vind over Gløshaugen: grønt mellom byggene, gult i de åpne partiene">
  <div class="figcap">Samme komfortkart — uansett hvilken av dem som regnet det ut.</div>
</div>

<div class="card ai">
  <div class="head">
    <img src="figures/modeller/modell-surrogat.svg" alt="">
    <h3>Surrogatmodellen</h3>
  </div>
  <p class="clock">Sekunder<span>per kjøring</span></p>
  <ul>
    <li>Et estimat, med et avvik vi måler</li>
    <li>Kjøres hele tiden, mens man tegner</li>
    <li><b>Itererer</b> seg fram til valget</li>
  </ul>
</div>

</div>

<!-- Say: oppsummeringen av hele vinddelen, og den skal ikke leses som «velg
     én». Arkitekten bruker begge, om hverandre: estimatet for å prøve ti ideer
     på en ettermiddag, simuleringen når noe skal bestemmes og dokumenteres.

     Pek på «1–2 timer» mot «Sekunder», og på kartet i midten: det er beviset på
     at de svarer på det samme spørsmålet. -->
<!-- TODO ~0:45 -->

---


# Regulering av Hesthagen
## Case
<!-- TODO ~0:10 -->

---


# Hesthagen — fra parkeringsplass til bygg

<style scoped>
section { font-size: 22px; }
/* Kartfila er 1000x625 (1,6:1), som i denne spalten blir ca. 349 px høyt — akkurat
   lavt nok til at callouten under ikke havner i logoen. */
.cols-2 img { display: block; width: 100%; height: auto; }
</style>

<div class="cols-2">

<div>

<div class="kicker">Tomta og planen</div>

- Brukt som NTNU-parkering mellom Klæbuveien og Gløshaugen
- En del av **NTNUs samlokaliseringstrategi**
- Fem etasjers hus der bilene står i dag
- Torg, trapp, gangbru og en offentlig plass rundt bygget

</div>

<div>

<!--
BRUK -ring-fila her, ikke hesthagen-kart.png. Den røde ringen rundt tomta er
brent inn i derivatfila; kildekartet har ingen ring. Marp klarte ikke å legge
ringen på i inline SVG (hver slide rendres inne i sin egen <svg>, og en nøstet
SVG med ekstern <image> falt ut av eksporten), så den ligger i PNG-en.

Skal ringen flyttes: skriptet står i README under «Kartet med ring».
-->
<img src="figures/hesthagen/hesthagen-kart-ring.png" alt="Kart over Hesthagen mellom Klæbuveien og Gløshaugen, med tomta som reguleres ringet inn i rødt">
<div class="figcap"><span class="figref">Figur</span> Hesthagen, mellom Klæbuveien og Gløshaugen. Rød ring: tomta som reguleres. Kart: © <a href="https://www.kartverket.no/">Kartverket</a>, CC BY 4.0.</div>

</div>

</div>

<div class="callout">

Mye av det planen lover, er uterom.
</div>


<!-- Say: «dette er tomta, og halve salen har parkert der.» Gjør det lokalt før
     du gjør det teknisk, og les callouten sakte — det er svingen inn til
     vindanalysen.

     Detaljregulering r20200032, vedtatt av bystyret 2. mars 2023. Kildene lå på
     sliden før, men 0,58em på projektor leser ingen — ta dem muntlig om noen
     spør:
       https://www.trondheim.kommune.no/aktuelt/kunngjoring-arealplan/arkiv-vedtatte-planer/eldre/20232/Hesthagen-og-del-av-Hogskoleparken-gnr-bnr-405-39-405-177-405-101-mfl-detaljregulering-r20200032/
       https://www.adressa.no/nyheter/trondheim/i/3MOkAP/naa-starter-det-enorme-byggeprosjektet-i-trondheim
-->
<!--
FIGUR: sliden tåler en massevolum-render i stedet for kartet. Lag den i Forma fra
reguleringskartet og eksporter selv — IKKE klipp ut illustrasjonene fra
planbeskrivelsen. De er forslagsstillerens, og repoet er offentlig (se «Ikke
bruk» i README).
-->
<!-- TODO ~0:50 -->

---
<!-- Main sin bakte fullbleed-versjon av surrogat-figuren. Hoveddecket bruker
     nå «Maskinlæringsmodellen» i stedet: samme innhold, men bygd i CSS av
     ekte skjermbilder, så etikettene arver temaets skrift og farger og kan
     rettes uten å rendre en PNG på nytt. Vil du ha den bakte tilbake, bytt
     de to. -->

<style scoped>
/* Bare figuren: ingen tittel, ingen callout. Figuren er 1,64:1 og sliden 16:9,
   så høyden er det som begrenser — max-height styrer, og width: auto lar
   bredden følge. justify-content sentrerer den i høyden når h1-en er borte.
   Figuren har INPUT/OUTPUT og retningene skrevet inn i seg, så den forklarer
   seg selv; teksten står i Say-notatet under. */
section { justify-content: center; }
img { display: block; margin: 0 auto; max-height: 100%; max-width: 100%; width: auto; }
</style>

<img src="figures/modeller/surrogatmodell.png" alt="Inn: høydeprofil og kategorikart over tomta, med terreng, bygninger og vegetasjon. Ut: åtte vindfelt, ett for hver av de åtte vindretningene fra nord til nordvest">

<!-- Say: den konkrete versjonen av skissen på forrige slide. Pek på de to
     bildene til venstre: høyden på alt som står der, og hva det er — terreng,
     bygning eller vegetasjon. Det er hele inngangen. Ingen mesh, ingen
     randbetingelser.

     Til høyre: åtte felt, ett per retning. Understrek at det ikke er åtte
     modeller — det er én modell kjørt åtte ganger på rotert geometri, og de
     vektes med vindrosen til det komfortkartet de så på Gløshaugen-sliden.

     Har du tid til overs: 8 retninger x noen sekunder mot 8 x flere timer CFD.
     Det er hele poenget med at den kan stå på mens man tegner. -->
<!-- TODO ~0:40 -->
