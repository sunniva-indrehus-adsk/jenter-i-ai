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
<div class="kicker">Kontekst</div>
Velg geolokasjon
</div>

---

<!-- _class: demo flipbook eget-merke -->

![](figures/site-design/bestill-data.png)

<div class="demo-label">
<div class="kicker">Kontekst</div>
Bestill data
</div>

---

<!-- _class: demo flipbook eget-merke -->

![](figures/site-design/sett-kontekst.png)

<div class="demo-label">
<div class="kicker">Sett kontekst</div>
Jobb i nettleseren
</div>

---

<!-- _class: demo flipbook eget-merke -->

![](figures/site-design/vis-hesthagen-med-data.png)

<div class="demo-label">
<div class="kicker">Utforsk</div>
Begynn å utforske din tomt
</div>

---

<!-- _class: demo flipbook eget-merke -->

![](figures/site-design/hesthagen-med-tegning.png)

<div class="demo-label">
<div class="kicker">Tegn</div>
Iterer over forslaget
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

---

# Den kjører mens du tegner

<style scoped>
.ph {
  height: 400px;
  display: flex;
  align-items: center;
  justify-content: center;
  background: repeating-linear-gradient(45deg, #F4F4F4 0 12px, #EDEDED 12px 24px);
  color: var(--muted);
  font-size: 0.85em;
  text-align: center;
  padding: 0 3em;
  margin-top: 0.6em;
}
</style>

<div class="ph">
Opptak fra Hesthagen-modellen i Forma: flytt et volum, og se vindfeltet regne
seg om.<br>Skjermopptak → figures/video/hesthagen-demo.mp4
</div>

<div class="todo">
Mangler opptaket. Ta det opp selv fra Forma på Hesthagen-prosjektet — 10–15
sekunder holder, og det tåler å gå på loop. Legg fila i talk/figures/video/ (den
er gitignorert) og bruk tools/flipbook.sh --shots for å lage PDF-bildene, samme
oppskrift som forma-demo. Se README, «To sett bilder».
</div>

<!-- Say: dette er hele poenget, demonstrert. Ikke forklar mens den kjører —
     la dem se at tallet endrer seg i det volumet flyttes. -->
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
