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

## Hvorfor vi ga opp presisjon i vindberegninger — og fikk noe bedre igjen

### Jenter i AI

<!-- Say: les tittelen høyt. «Det høres ut som en innrømmelse. Det er en
     designbeslutning, og vi skal vise dere hvorfor.» -->
<!-- TODO ~0:20 -->

---

<!-- paginate: true -->

# Jente i Autodesk

<div class="person">

<div>

<div class="kicker">Vilde</div>

- **Indøk på NTNU**, med spesialisering mot programmering
- **Konsulent** først: ny kunde, ny kodebase, ofte — leverer, og går videre
- **Utvikler** nå: gøyere å bygge produktet enn å lage slides om det

</div>

<div class="person-photo">
  <div class="frame"><img src="figures/people/vilde.jpg" alt="Vilde"/></div>
  <span>Vilde</span>
</div>

</div>

<div class="callout">

Det som overførte seg fra konsulentårene: å høre hva kunden **egentlig** spør om. Det som måtte læres på nytt: at koden ikke leveres — den eies, i årevis.

</div>

<!-- Say: la Vilde fortelle selv. Poenget for publikum: det finnes flere veier inn,
     og «jeg gikk ikke datateknikk» er ikke en sperre. -->
<!-- TODO ~1:20 -->

---

# Jente i Autodesk
<div class="person">

<div>

<div class="kicker">Sunniva</div>

- **Fysmat på NTNU**, så forskning: numerikk — å gjøre ligninger om til kode
- Skrev et paper som kanskje fem mennesker i verden har lest
- Nå: de samme ligningene, i et verktøy tusenvis av arkitekter åpner hver dag

</div>

<div class="person-photo">
  <div class="frame"><img src="figures/people/sunniva.png" alt="Sunniva"/></div>
  <span>Sunniva</span>
</div>

</div>

<div class="callout">

Det er den samme jobben. Forskjellen er hvor mange som får noe ut av den.

</div>

<!-- Say: kort og personlig. Ikke fortell hele doktorgraden — fortell hvorfor du
     byttet. -->
<!-- TODO ~1:20 -->

---

<!-- _class: section -->

# Hva vi bygger

## Autodesk Forma — tidligfase for by- og stedsutvikling

<!-- TODO ~0:10 -->

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

# Tidligfasen: alt er åpent, ingenting er tegnet

<div class="cols-2">

<div>

<div class="kicker">Arkitekten lurer på</div>

- Hvor mange kvadratmeter får jeg plass til her?
- Hvor skal bygget stå, og hvor høyt kan det bli?
- Blir det bra å være her — sol, lys, luft, lyd?

</div>

<div>

<div class="kicker">Utbyggeren lurer på</div>

- Går regnestykket opp?
- Hva må vi dokumentere for kommunen?
- Hva koster det å ombestemme seg om tre måneder?

</div>

</div>

<div class="callout">

Tidligfasen er noen få uker der nesten ingenting er bestemt — og der nesten alt avgjøres.

</div>

<!-- Say: dette er rammen for hele resten av talken. Alt vi bygger, bygges for
     disse ukene. -->
<!-- TODO ~0:50 -->

---

# Produktreisen

<style scoped>
.cols-3 .card p { font-size: 0.85em; }
</style>

<div class="cols-3">

<div class="card">
<h3>1. Tegne</h3>
<p>Volumer, gater, høyder. Grovt og raskt, rett i nettleseren — ingen installasjon, ingen modell å arve.</p>
</div>

<div class="card">
<h3>2. Hente inn verden</h3>
<p>Terreng, nabobygg, veier, klimadata. Bestilles for tomta, i stedet for å modelleres i hånd.</p>
</div>

<div class="card">
<h3>3. Analysere</h3>
<p>Sol, dagslys, støy, vind, karbon. På forslaget du tegnet for tretti sekunder siden.</p>
</div>

</div>

<div class="callout">

Og så om igjen. Et prosjekt er ikke en fase man leverer og går fra — det er en modell noen eier i årevis.

</div>

<!-- Say: nevn at dette er forskjellen fra konsulentmodellen Vilde kom fra.
     Kuttkandidat hvis tiden blir knapp — slå den sammen med sliden før. -->
<!-- TODO ~0:50 -->

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

<div class="figcap">Alle seks kjørt på samme tomt: hovedbygget på Gløshaugen.</div>

<!-- Say: seks analyser, samme modell, samme ettermiddag. Pek på vind — «den ene
     nederst til høyre er den vi skal snakke om resten av tiden.» -->
<!-- TODO ~0:40 -->

---

# Én analyse, eller hundre?

<div class="cols-2">

<div>

<div class="kicker">Hvis analysen tar en time</div>

- Du kjører den når du er ferdig
- Den blir dokumentasjon
- Den bekrefter valget ditt — eller knuser det, for sent

</div>

<div>

<div class="kicker">Hvis analysen tar fem sekunder</div>

- Du kjører den mens du tegner
- Den blir et tegneverktøy
- Den former bygget, i stedet for å godkjenne det

</div>

</div>

<div class="callout">

Dette er hele talken på én slide: **en analyse som ikke rekker å bli brukt, er ikke verdt nøyaktigheten sin.**

</div>

<!-- Say: her setter du opp betalingen som kommer helt til slutt. Ikke avslør
     løsningen ennå. -->
<!-- TODO ~0:40 -->

---

<!-- _class: section -->

# Regulering av Hesthagen

## Parkeringsplassen dere går forbi på vei opp til Gløshaugen

<!-- TODO ~0:10 -->

---

# Hesthagen — fra parkering til byggeplass

<div class="cols-2">

<div>

<div class="kicker">Tomta</div>

- Nedlagt NTNU-parkering mellom Klæbuveien og Gløshaugen
- Del av **NTNU Campussamling**; Statsbygg er byggherre
- Detaljregulering **r20200032**, vedtatt av bystyret 2. mars 2023
- Trolig Trondheims største byggeprosjekt det neste tiåret
- Nesten ingen bilparkering igjen: seks HC-plasser i Klæbuveien

<div class="sources">

<span class="src-label">Kilder</span><br>
Trondheim kommune, <a href="https://www.trondheim.kommune.no/aktuelt/kunngjoring-arealplan/arkiv-vedtatte-planer/eldre/20232/Hesthagen-og-del-av-Hogskoleparken-gnr-bnr-405-39-405-177-405-101-mfl-detaljregulering-r20200032/">vedtatt detaljregulering</a> og <a href="https://www.trondheim.kommune.no/globalassets/10-bilder-og-filer/10-byutvikling/byplankontoret/1c_vedtatt-plan/2023/campus_hesthagen-og-del-av-hogskoleparken-gnrbnr-40539-405177-405101-m.fl.-detaljregulering--r20200034/planbeskrivelse.pdf">planbeskrivelse (PDF)</a><br>
Adresseavisen, <a href="https://www.adressa.no/nyheter/trondheim/i/3MOkAP/naa-starter-det-enorme-byggeprosjektet-i-trondheim">«Nå starter det enorme byggeprosjektet i Trondheim»</a>

</div>

</div>

<div>
<img src="figures/illustrations/hesthagen-kart.png" alt="Kart over Hesthagen mellom Klæbuveien og Gløshaugen">
<div class="figcap"><span class="figref">Figur</span> Hesthagen, mellom Klæbuveien og Gløshaugen. Kart: © <a href="https://www.kartverket.no/">Kartverket</a>, CC BY 4.0.</div>
</div>

</div>

<!-- Say: «dette er tomta, og halve salen har parkert der.» Gjør det lokalt før
     du gjør det teknisk. -->
<!-- TODO ~0:50 -->

---

# Hva planen faktisk tillater

<div class="cols-2">

<div>

<div class="kicker">Tomt 6B — bygget</div>

- Ny kvartalsstruktur på dagens parkeringsplass
- Fem etasjer og kjeller, trappet ned til fire mot Klæbuveien
- Stor transparens i fasadene i første og andre etasje

</div>

<div>

<div class="kicker">Tomt 6B — uterommene</div>

- Torg i krysset Klæbuveien / Gløshaugveien
- Delvis overbygget trapp opp mot Gløshaugen-platået
- Gangbru fra Sem Sælands vei, gjennom parken
- Offentlig tilgjengelig plass sør for bygget

</div>

</div>

<div class="callout">

Fire av sju punkter handler om uterom. Det er der folk skal være — og det er der vinden bor.

</div>

<!-- Say: dette er svinget inn til vindanalysen. Les det siste punktet sakte. -->
<!--
FIGUR: denne sliden tåler en massevolum-render ved siden av teksten.
Lag den i Forma fra reguleringskartet og eksporter selv — IKKE klipp ut
illustrasjonene fra planbeskrivelsen. De er forslagsstillerens, og repoet er
offentlig (se «Ikke bruk» i README). figures/illustrations/hesthagen-regulering.png
er et slikt skjermbilde og bør ikke ende opp på en slide.
-->
<!-- TODO ~0:40 -->

---

<!-- _class: statement -->

# Et torg ingen vil sitte på, er ikke et torg. Det er en snarvei.

<!-- Say: pause. Så: «hvordan vet man det, før det er bygget?» -->
<!-- TODO ~0:20 -->

---

# Vindkomfort: samme vind, ulik opplevelse

<style scoped>
.wind { display: grid; grid-template-columns: 1.35fr 1fr; gap: 1.5em; align-items: start; }
/* Bildet er 2460x1606 — uten høydetak presser det callouten ned i logoen. */
.wind img { height: 430px; width: 100%; object-fit: cover; object-position: center 45%; }
.scale { list-style: none; margin: 0.2em 0 0 0; padding: 0; font-size: 0.78em; }
.scale li { display: grid; grid-template-columns: 1em 1fr; gap: 0.75em; margin: 0.5em 0; align-items: baseline; }
.scale .sw { width: 1em; height: 1em; border-radius: 2px; box-shadow: 0 0 0 1px rgba(0,0,0,0.12); }
.scale b { font-weight: 700; }
.scale span.txt { color: var(--muted); font-size: 0.9em; display: block; }
.wind .callout { font-size: 0.82em; margin-top: 1.1em; }
</style>

<div class="wind">

<div>
<img src="figures/illustrations/gløshaugen-komfor-plot.png" alt="Komfortkart for vind rundt hovedbygget på Gløshaugen">
<div class="figcap"><span class="figref">Figur</span> Komfortkart for vind, hovedbygget på Gløshaugen. Egen Forma-analyse.</div>
</div>

<div>

<div class="kicker">Komfortskalaen</div>

<ul class="scale">
<li><span class="sw" style="background:#75CD9B"></span><span><b>Sitte i ro</b><span class="txt">Behagelig å bli sittende ute</span></span></li>
<li><span class="sw" style="background:#EACA41"></span><span><b>Stå og vente</b><span class="txt">Greit i noen minutter</span></span></li>
<li><span class="sw" style="background:#E5A32B"></span><span><b>Gå forbi</b><span class="txt">Fint å passere, ikke å oppholde seg</span></span></li>
<li><span class="sw" style="background:#DE533E"></span><span><b>Ubehagelig</b><span class="txt">Her går man en annen vei</span></span></li>
</ul>

<div class="callout">

Skalaen spør ikke «hvor mye blåser det», men «hvor ofte blåser det for mye til det du skal gjøre her».

</div>

</div>

</div>

<!-- Say: pek på de oransje flekkene ved bygningshjørnene. Det er der vinden
     akselererer — og der arkitekten hadde tenkt en benk. -->
<!-- TODO: verifiser at fargene og kategorinavnene her matcher legenden i appen
     (fargekodene er plukket rett ut av PNG-en, men navnene er mine). -->
<!-- TODO ~1:10 -->

---

<!-- _class: section -->

# Hvorfor tar dette tid?

## Fysikken, og regningen

<!-- TODO ~0:10 -->

---

# Ligningen bak et vindkart

$$
\frac{\partial \mathbf{u}}{\partial t} + (\mathbf{u}\cdot\nabla)\mathbf{u}
= -\frac{1}{\rho}\nabla p + \nu\nabla^{2}\mathbf{u},
\qquad
\nabla\cdot\mathbf{u} = 0
$$

<div class="cols-2">

<div>

<div class="kicker">Hva som står der</div>

- $\mathbf{u}$ — vindens hastighet, i hvert punkt
- $p$ trykk, $\rho$ tetthet, $\nu$ hvor seig luften er
- Første ligning: Newtons andre lov, for en luftpakke
- Andre ligning: luft blir ikke borte

</div>

<div>

<div class="kicker">Hva som er problemet</div>

- Ingen formel gir deg $\mathbf{u}$ for et bykvartal
- Vi må regne oss frem — punkt for punkt, steg for steg
- Det er dette «numerikk» betyr, og det var jobben min

</div>

</div>

<!-- Say: ikke gå gjennom ligningen ledd for ledd. Poenget er ett: den kan ikke
     løses, bare regnes. Salen er teknisk — de tåler å se den, men ikke å bli
     forelest om den. -->
<!-- TODO ~1:00 -->

---

# Fra ligning til regning: diskretisering

<style scoped>
.bignum { border-left: 3px solid var(--ink); padding-left: 0.9em; margin-top: 0.6em; }
.bignum .n { display: block; font-family: var(--display); font-weight: 700; font-size: 2.1em; line-height: 1.05; letter-spacing: -0.02em; }
.bignum .u { display: block; color: var(--muted); font-size: 0.82em; margin-top: 0.35em; }
</style>

<div class="cols-2">

<div>

<div class="kicker">Slik gjøres det</div>

- Legg en boks rundt tomta, og del boksen i celler
- Millioner av celler for et bykvartal
- Løs ligningene i hver celle, om og om igjen, til svaret slutter å endre seg
- Gjenta for hver vindretning, og vekt med vindstatistikken for stedet

</div>

<div>

<div class="kicker">Prislappen</div>

<div class="bignum">
<span class="n">Timer</span>
<span class="u">per alternativ — på mange kjerner, for én tomt, for én utforming</span>
</div>

<div class="callout">

Arkitekten har ikke timer. Arkitekten har tiden det tar å dra i et hjørne.

</div>

</div>

</div>

<!-- Say: her er det verdt å si høyt at det ikke er kode som er treg — det er
     problemet. Flere celler og flere retninger er den eneste veien til et
     nøyaktigere svar. -->
<!-- TODO: bytt «Timer» mot det faktiske tallet fra vårt CFD-oppsett, og sett
     inn antall celler + antall vindretninger. Konkrete tall slår «timer». -->
<!-- TODO ~1:00 -->

---

<!-- _class: section -->

# AI-svaret

## En modell som har sett nok CFD til å gjette godt

<!-- TODO ~0:10 -->

---

# Surrogatmodellen

<style scoped>
/* 74 %, ikke 100 %: figuren er bred og lav, og callouten under trenger plassen. */
img { display: block; margin: 0.6em auto 0; width: 74%; }
</style>

<img src="figures/illustrations/02-surrogat-pipeline.svg" alt="Geometri og vindretning inn, nevralt nett, vindfelt ut — trent på ferdige CFD-kjøringer">

<div class="callout">

Modellen løser ingen ligninger. Den har sett så mange løsninger at den kjenner igjen svaret.

</div>

<!-- Say: rammen som gjør det forståelig for en AI-sal: det er bilde-til-bilde.
     Inn: geometrien som et høydekart. Ut: et hastighetsfelt. Nettverket er
     kjedelig — det er treningsdataene som er hele arbeidet, og de er dyre,
     fordi hvert eksempel ER en full CFD-kjøring. -->
<!-- TODO: hvis tallene kan deles: hvor mange CFD-kjøringer ligger i
     treningssettet, og hvor lang tid tok det å generere dem? -->
<!-- TODO ~1:10 -->

---

# Hva vi ga opp, og hva vi fikk

<style scoped>
.cols-2 { gap: 1.4em; }
.card { border-top-width: 3px; }
.card.ai { border-top-color: var(--accent); background: var(--accent-soft); }
.card ul { font-size: 0.88em; margin-top: 0.4em; }
.card li { margin: 0.35em 0; }
</style>

<div class="cols-2">

<div class="card">

<h3>Fullverdig CFD</h3>

- Nøyaktig, og etterprøvbar
- Timer per kjøring
- Kjøres én gang, til slutt
- **Dokumenterer** et valg som alt er tatt

</div>

<div class="card ai">

<h3>Surrogatmodellen</h3>

- Omtrentlig, med et avvik vi måler
- Sekunder per kjøring
- Kjøres hele tiden, mens man tegner
- **Tar** valget, sammen med arkitekten

</div>

</div>

<div class="callout">

Begge finnes i Forma. Den raske former bygget; den nøyaktige signerer det.

</div>

<!-- Say: viktig nyanse — vi erstatter ikke CFD, vi flytter den bakover i
     prosessen. Vær ærlig om avviket hvis noen spør; ikke selg det som gratis. -->
<!-- TODO ~0:50 -->

---

<!-- _class: statement -->

# Mer brukt, men mindre nøyaktig.

## En modell som er litt feil og alltid tilgjengelig, endrer flere bygg enn en som er riktig og kommer for sent.

<!-- Say: dette er betalingen for tittelen. Si den, og hold pausen. -->
<!-- TODO ~0:20 -->

---

# Hva nå?

<div class="cols-2">

<div>

<div class="kicker">Prøv det selv</div>

- **Autodesk Forma** — kjører i nettleseren, ingen installasjon
- Studenttilgang via **Autodesk Education**
- Bygg tomta di, kjør vindanalysen, dra i et hjørne

</div>

<div>

<div class="kicker">Hvis dette hørtes gøy ut</div>

- Vi sitter i Trondheim — kom og spør om hvordan det er
- Numerikk, ML og frontend i samme kodebase
- Ingen av oss gikk datateknikk

</div>

</div>

<div class="callout">

Spørsmålet vi begge fikk, og som du kan hoppe over: «er jeg teknisk nok til dette?»

</div>

<!-- TODO: sjekk hva som faktisk er riktig å si om studenttilgang til Forma før
     du lover det fra scenen, og om vi har lov til å nevne rekruttering. -->
<!-- TODO ~0:30 -->

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

<!-- TODO ~0:20 -->
