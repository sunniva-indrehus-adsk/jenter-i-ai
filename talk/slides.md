---
marp: true
theme: theme.css
paginate: true
math: katex
---

<!-- _class: title title-photo -->
<!-- _header: '24.09.2026' -->
<!-- paginate: false -->

# Mer brukt, men mindre nøyaktig

### Jenter i AI

---

# Fra indøk til Autodesk

<div class="person">

<div>

<div class="kicker">Ville bygge produkt i stedet for slides</div>

- Internship som utvikler under studiene
- Bruke kode til å løse komplekse problemer
- Jobbe i en produktorganisasjon

</div>

<div class="person-photo">
  <div class="frame"><img src="figures/people/vilde.jpg" alt="Vilde"/></div>
  <span>Vilde</span>
</div>

</div>

<div class="callout">

Det er spennende å kombinere matematikk, algoritmer og programvareutvikling for å bidra til en mer bærekraftig verden.</em>

</div>

<!-- Say: la Vilde fortelle selv — 2 min. Poenget for publikum: det finnes flere veier inn. -->
<!-- TODO ~2:00 -->


---

<!-- paginate: true -->

# Fra fysmat til Autodesk


<div class="person">

<div>

- Fysiker som ble programmerer
- Jobber med *…* i Forma hos Autodesk
- Kort om veien hit

</div>

<div class="person-photo">
  <div class="frame"><img src="figures/people/sunniva.png" alt="Sunniva"/></div>
  <span>Sunniva</span>
</div>

</div>

<!-- Say: kort og personlig — 1 min, ikke mer. -->

---

<!-- _class: demo -->

<!--
«What is Forma Site Design» fra YouTube. Marp trenger --html=true for at
<iframe> skal rendres; det ligger allerede i kommandoen i README.

Embedden krever nett i salen, og den fungerer ikke i PDF-eksport. Last ned en
lokal kopi som reserve og bytt iframe-en (og skriptet) mot:
  <video src="figures/video/forma-demo.mp4" controls muted playsinline></video>
CSS-en i theme.css håndterer begge.

start=18 og end=74: klippet går fra 0:18 til 1:14 — 56 sekunder, spilt i vanlig
hastighet. Bruker du den lokale reservefila i stedet, blir det #t=18,74 på
slutten av src.

rel=0 og modestbranding=1 demper YouTubes egne forslag. autoplay=1 krever
mute=1 — nettlesere blokkerer autoplay med lyd. Lyden skal av uansett.

Tittelkortet «Autodesk Forma» ligger over videoen de første 5 sekundene og fader
ut. Teksten står i .demo-intro-diven under, utseendet i theme.css, og de 5
sekundene i setTimeout-en i skriptet.

cc_load_policy=0 og iv_load_policy=3 ber om ingen undertekster og ingen
annotasjoner. cc_load_policy er bare et hint — er undertekster slått på i din
egen YouTube-konto vinner den, så sjekk CC-knappen i spilleren før du går på.
-->

<iframe
  id="forma-demo"
  src="https://www.youtube-nocookie.com/embed/1ovhhMWpohw?start=18&end=74&rel=0&modestbranding=1&playsinline=1&cc_load_policy=0&iv_load_policy=3"
  data-autoplay-src="https://www.youtube-nocookie.com/embed/1ovhhMWpohw?start=18&end=74&rel=0&modestbranding=1&playsinline=1&cc_load_policy=0&iv_load_policy=3&autoplay=1&mute=1"
  title="What is Forma Site Design"
  allow="autoplay; encrypted-media; picture-in-picture; fullscreen"
  referrerpolicy="strict-origin-when-cross-origin"></iframe>



<div class="demo-intro">
  <img src="figures/logos/autodesk-forma-logo.png" alt="Autodesk Forma"/>
</div>

<script>
  // Autoplay og tittelkortet trigges når sliden BLIR AKTIV, ikke ved sidelast:
  // Marp holder alle slides i DOM samtidig, så autoplay=1 rett i src ville
  // spilt videoen ferdig lenge før du kom hit.
  //
  // Derfor to URL-er. src er uten autoplay og fullt spillbar — svikter skriptet,
  // står du igjen med en vanlig video du trykker play på, ikke en svart slide.
  // data-autoplay-src er den samme med autoplay=1&mute=1, og byttes inn av
  // skriptet. (mute=1 er påkrevd; nettlesere blokkerer autoplay med lyd.)
  //
  // Dette må gjøres i JS, ikke CSS: Marpit prefikser alle selektorer — også i en
  // global style-blokk — med section-scopet, mens aktiv-klassen bespoke-marp-active
  // ligger på svg-elementet OVER section, altså utenfor rekkevidde derfra.
  //
  // VIKTIG: ingen bruk av tegnet «større enn» i denne blokka. Marp escaper det
  // til en HTML-entitet inne i inline-script, og da knekker JS-en. Derfor
  // function () i stedet for pilfunksjoner, og === i stedet for sammenligninger.
  (function () {
    const frame = document.getElementById('forma-demo');
    if (!frame) return;
    const intro = frame.parentElement.querySelector('.demo-intro');
    const idleSrc = frame.src;
    const slide = frame.closest('svg');
    let timer;
    function activate() {
      frame.src = frame.dataset.autoplaySrc; // Ny src = starter forfra.
      if (!intro) return;
      intro.classList.remove('is-hidden');
      clearTimeout(timer);
      timer = setTimeout(function () { intro.classList.add('is-hidden'); }, 4000);
    }
    function deactivate() {
      frame.src = idleSrc; // Stopper avspilling når du går videre.
      clearTimeout(timer);
      if (intro) intro.classList.add('is-hidden');
    }
    // Bespoke legger på klassene sine ETTER at denne script-taggen er parset, så
    // svg-en er ennå ikke merket når vi kommer hit. Poll litt før vi gir opp.
    let tries = 0;
    (function waitForBespoke() {
      // Statisk eksport (PDF): ingen bespoke, la src stå spillbar som den er.
      if (!slide || tries++ === 40) return;
      if (!slide.classList.contains('bespoke-marp-slide')) {
        setTimeout(waitForBespoke, 50);
        return;
      }
      let wasActive = slide.classList.contains('bespoke-marp-active');
      if (wasActive) activate();
      else if (intro) intro.classList.add('is-hidden');
      new MutationObserver(function () {
        const isActive = slide.classList.contains('bespoke-marp-active');
        if (isActive === wasActive) return;
        wasActive = isActive;
        if (isActive) activate(); else deactivate();
      }).observe(slide, { attributes: true, attributeFilter: ['class'] });
    })();
  })();
</script>

---

# Analyser i Autodesk Forma

<style scoped>
.cols-3 .card {
  padding: 0;
  overflow: hidden;
  align-self: start;
  border-top: 1px solid var(--rule);
}
.cols-3 .card img {
  display: block;
  width: 100%;
  height: 7em;
  object-fit: cover;
}
.cols-3 .card .figcap {
  padding: 0.5em 0.7em;
  margin: 0;
}
</style>

<div class="cols-3">

<div class="card">
<img src="figures/illustrations/analyses/noise.png" alt="Støy">
<div class="figcap"><span class="figref">Støy</span></div>
</div>

<div class="card">
<img src="figures/illustrations/analyses/solar-energy.png" alt="Solenergi">
<div class="figcap"><span class="figref">Solenergi</span></div>
</div>

<div class="card">
<img src="figures/illustrations/analyses/daylight.png" alt="Dagslys">
<div class="figcap"><span class="figref">Dagslys</span></div>
</div>

<div class="card">
<img src="figures/illustrations/analyses/microclimate.png" alt="Mikroklima">
<div class="figcap"><span class="figref">Mikroklima</span></div>
</div>

<div class="card">
<img src="figures/illustrations/analyses/sun.png" alt="Sol">
<div class="figcap"><span class="figref">Sol</span></div>
</div>

<div class="card">
<img src="figures/illustrations/analyses/wind.png" alt="Vind">
<div class="figcap"><span class="figref">Vind</span></div>
</div>

</div>

---

<!-- _class: section -->

# Regulering av Hesthaugen


---

# Hesthagen — fra parkering til byggeplass

<div class="cols-2">

<div>

<div class="kicker">Tomta</div>

- Nedlagt NTNU-parkering mellom Klæbuveien og Gløshaugen
- Detaljregulert av Trondheim kommune (R20200034)
- …

<div class="sources">

<span class="src-label">Kilder</span><br>
Trondheim kommune, <a href="https://www.trondheim.kommune.no/aktuelt/kunngjoring-arealplan/arkiv-vedtatte-planer/eldre/20232/Hesthagen-og-del-av-Hogskoleparken-gnr-bnr-405-39-405-177-405-101-mfl-detaljregulering-r20200032/">vedtatt detaljregulering</a> og <a href="https://www.trondheim.kommune.no/globalassets/10-bilder-og-filer-eksternt/10-byutvikling/byplankontoret/1c_vedtatt-plan/2023/campus_hesthagen-og-del-av-hogskoleparken-gnrbnr-40539-405177-405101-m.fl.-detaljregulering--r20200034/planbeskrivelse.pdf">planbeskrivelse (PDF)</a><br>
Adresseavisen, <a href="https://www.adressa.no/nyheter/trondheim/i/3MOkAP/naa-starter-det-enorme-byggeprosjektet-i-trondheim">«Nå starter det enorme byggeprosjektet i Trondheim»</a>

</div>

</div>

<div>
<img src="figures/illustrations/hesthagen-kart.png" alt="Kart over Hesthagen mellom Klæbuveien og Gløshaugen">
<div class="figcap"><span class="figref">Figur</span> Hesthagen, mellom Klæbuveien og Gløshaugen. Kart: © <a href="https://www.kartverket.no/">Kartverket</a>, CC BY 4.0.</div>
</div>

</div>

---

<!-- _class: statement -->

# En påstand som fortjener hele sliden

---

# En likning, om det trengs

$$
E = \int_{\Omega} L(\omega)\,\cos\theta\,\mathrm{d}\omega
$$

<!-- KaTeX er slått på i frontmatter (math: katex). -->

---

<!-- _class: section -->

# Del 2

## …

---

<!-- _class: section -->

# Del 3

## …

---

# Hva nå?

<div class="cols-2">

<div>

<div class="kicker">Kom i gang</div>

- Ressurs 1 — …
- Ressurs 2 — …

</div>

<div>

<div class="kicker">Ta kontakt</div>

- …

</div>

</div>



---

# Takk for oppmerksomheten!

<style scoped>
.people-row {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 1.4em;
  margin-top: 1.2em;
}
.people-row .person-photo .frame { width: 190px; height: 190px; }
</style>

<div class="people-row">

<div class="person-photo">
  <div class="frame"><img src="figures/people/vilde.jpg" alt="Vilde"/></div>
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

<div class="callout">

Vi står på stand — kom og spør oss om alt vi ikke fikk plass til her!

</div>
