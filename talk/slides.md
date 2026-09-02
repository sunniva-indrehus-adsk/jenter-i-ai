---
marp: true
theme: theme.css
paginate: true
math: katex
---

<!-- _class: title title-photo -->
<!-- _header: '24.09.2026' -->
<!-- paginate: false -->

# AI i Autodesk

## Jenter i AI



<!-- Say: les tittelen høyt. «Det høres ut som en innrømmelse. Det er en
     designbeslutning, og vi skal vise dere hvorfor.» -->
<!-- TODO ~0:20 -->

---

<!-- paginate: true -->

# Fra indøk til Autodesk

<style scoped>
/* Bildet er høyt portrett: en sentrert kvadratisk beskjæring hadde blitt mest
   himmel. 63 % skyver utsnittet ned så begge personene ligger i sirkelen, og
   scale(1.5) zoomer inn om samme senter så de to fyller sirkelen.
   Resten av .photo-cluster ligger i theme.css. */
.photo-cluster .family img { object-position: center 63%; transform: scale(1.5); }
</style>

<div class="person">

<div>

<div class="kicker">Vilde</div>

- Internship som utvikler under studiene
- Gøy å bygge produkt i stedet for slides
- Jobbe i en produktorganisasjon

</div>

<div class="photo-cluster">
  <div class="frame family"><img src="figures/people/vilde-2.jpg" alt="Vilde på sandvolleyballbanen"/></div>
  <div class="frame portrait"><img src="figures/people/vilde-3.jpg" alt="Vilde"/></div>
</div>

</div>

<div class="callout">

Jobbe for en mer bærekraftig verden med koding og matte.</em>

</div>

<!-- Say: la Vilde fortelle selv. Poenget for publikum: det finnes flere veier inn,
     og «jeg gikk ikke datateknikk» er ikke en sperre. -->
<!-- TODO ~1:20 -->

---

# Jente i Autodesk

<style scoped>
/* Den øverste fjerdedelen av familiebildet er bare hvit vegg, og hvitt mot hvit
   slide blir et hull. object-position skyver utsnittet ned så veggen forsvinner.
   68 %, ikke 85 %: sirkelen er smalest i toppen og bunnen, så ansiktene må ligge
   nær midthøyden for at de to ytterste ikke skal bli beskåret av masken.
   Resten av .photo-cluster ligger i theme.css. Den lille sirkelen er plassert
   der den lander på kjolen til barnet — det eneste stedet i dette bildet der
   den ikke dekker et ansikt. */
.photo-cluster .family img { object-position: center 68%; }
</style>

<div class="person">

<div>

<div class="kicker">Sunniva</div>

- **Fysmat på NTNU**, så forskning: numerikk — å gjøre ligninger om til kode
- Da: Skrev et paper som kanskje fem mennesker i verden har lest
- Nå: også ligniner i et verktøy tusenvis av arkitekter åpner hver dag

</div>

<div class="photo-cluster">
  <div class="frame family"><img src="figures/people/sunniva-2.jpg" alt="Sunniva med familien"/></div>
  <div class="frame portrait"><img src="figures/people/sunniva.png" alt="Sunniva"/></div>
</div>

</div>

<div class="callout">

Samme type jobb, men høyere påvirking "i den virkelige verden"

</div>

<div class="todo">tittel? </div>



---

<!-- _class: demo -->

<!--
«What is Forma Site Design» fra YouTube. Marp trenger --html=true for at
<iframe> skal rendres; det ligger allerede i kommandoen i README.

Embedden krever nett i salen, og den fungerer ikke i PDF-eksport. Last ned en
lokal kopi som reserve og bytt iframe-en (og skriptet) mot:
  <video src="figures/video/forma-demo.mp4" controls muted playsinline></video>
CSS-en i theme.css håndterer begge.

start=14 og end=74: klippet går fra 0:14 til 1:14 — 60 sekunder, spilt i vanlig
hastighet. Bruker du den lokale reservefila i stedet, blir det #t=14,74 på
slutten av src.

Hvorfor 14 og ikke 18: tittelkortet ligger over de første 5 sekundene, så de
fem første sekundene av klippet ser ingen. Starter vi på 0:14, er videoen kommet
til 0:19 når kortet er borte, og det er der klippet skal begynne for publikum.

rel=0 og modestbranding=1 demper YouTubes egne forslag. autoplay=1 krever
mute=1 — nettlesere blokkerer autoplay med lyd. Lyden skal av uansett.

controls=0 ligger BARE på data-autoplay-src: det er den som spilles i salen, og
uten den blinker YouTubes store play-knapp og kontrollinjen gjennom tittelkortet
(som er halvgjennomsiktig) i det videoen starter. Prisen er at du ikke kan pause
midt i klippet — gå videre til neste slide i stedet. src beholder kontrollene,
så reserveløsningen (og PDF-eksport, der skriptet ikke kjører) fortsatt har en
play-knapp å trykke på.

Tittelkortet «Autodesk Forma» ligger over videoen de første 5 sekundene og fader
ut. Teksten står i .demo-intro-diven under, utseendet i theme.css, og tidene i
setTimeout-en i skriptet. Kortet er helt dekkende hele tiden det ligger der, så
verken YouTubes spinner eller kontrollinjen synes gjennom mens videoen laster.

cc_load_policy=0 og iv_load_policy=3 ber om ingen undertekster og ingen
annotasjoner. cc_load_policy er bare et hint — er undertekster slått på i din
egen YouTube-konto vinner den, så sjekk CC-knappen i spilleren før du går på.
-->

<iframe
  id="forma-demo"
  src="https://www.youtube-nocookie.com/embed/1ovhhMWpohw?start=14&end=74&rel=0&modestbranding=1&playsinline=1&cc_load_policy=0&iv_load_policy=3"
  data-autoplay-src="https://www.youtube-nocookie.com/embed/1ovhhMWpohw?start=14&end=74&rel=0&modestbranding=1&playsinline=1&cc_load_policy=0&iv_load_policy=3&autoplay=1&mute=1&controls=0"
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
      timer = setTimeout(function () { intro.classList.add('is-hidden'); }, 5000);
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

<!-- Say: 60 sekunder klipp. Ikke snakk over hele — la den rulle, og kommenter
     bare det som skjer på slutten. -->
<!-- TODO ~1:00 -->

---

# Tidligfase: alt er åpent, ingenting er tegnet

<style scoped>
/* Sliden hadde ca. 135 px ubrukt plass nederst. Den går nå til luft. */
.cols-2 { gap: 2.4em; margin-top: 0.7em; }
.kicker { margin-bottom: 0.85em; }
li { margin: 0.7em 0; }
/* margin-top: auto virker fordi Marp gjør section til en flex-kolonne: auto
   spiser all resterende høyde, så callouten legger seg i bunnen uansett hvor
   mye tekst spaltene over har. Ingen magiske pikselverdier å vedlikeholde. */
.callout { margin-top: auto; }
</style>

<div class="cols-2">

<div>

<div class="kicker">Arkitekten lurer på</div>

- Hvor mange kvadratmeter får jeg plass til her?
- Hvor skal bygget stå, og hvor høyt kan det bli?
- Blir det bra her — sol, lys, luft, lyd?

</div>

<div>

<div class="kicker">Utbyggeren lurer på</div>

- Går regnestykket opp?
- Hva må vi dokumentere for kommunen?
- Hva koster det å ombestemme seg om tre måneder?

</div>

</div>

<div class="callout">

Noen få uker der nesten alt avgjøres.

</div>

<!-- Say: dette er rammen for hele resten av talken. Alt vi bygger, bygges for
     disse ukene. -->
<!-- TODO ~0:45 -->

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
  /* 6.6em, ikke 7: bildeteksten under rutenettet trenger luft mot logoen. */
  height: 6.6em;
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
<!-- TODO ~0:50 -->

---


# Vindkomfort

<style scoped>
.wind { display: grid; grid-template-columns: 1.35fr 1fr; gap: 1.5em; align-items: start; }
/* Kartet er høyere enn skalaen, så skalaen sentreres mot det i stedet for å
   henge i toppen med et tomrom under. align-self, ikke align-items: kartet skal
   fortsatt ligge i topp — det er det som setter høyden på raden. */
.wind > div:last-child { align-self: center; }
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

<div class="kicker">Komfortskalaen — Lawson LDDC</div>

<!--
FARGER OG NAVN ER HENTET FRA KODEN, ikke funnet på:

  wind-analysis-ui/src/analysis/surfaceResult/windColors.ts:15
      comfortColors = ["#B2F8DA","#55DCA2","#FED52A","#FFA900","#FF463A"]
  wind-analysis-ui/src/i18n/translations/nb-NO/texts.json
      comfort.labels = Sitte / Stå / Rusle / Gå / Ukomfortabelt
  wind-surrogate/wind/lib/comfort.py:77
      lawson_lddc: speed_thresholds [2.5, 4, 6, 8] m/s, 5 % for alle fire
  wind-surrogate/wind/lib/comfort.py:130-152
      compute_comfort(): klasse 0-4, én klasse per terskel som overskrides

Fem kategorier, ikke fire — klasse 0 er den roligste og har ingen terskel.
Samme palett i både CFD-appen og ML-webkomponenten.
-->
<ul class="scale">
<li><span class="sw" style="background:#B2F8DA"></span><span><b>Sitte</b><span class="txt">Under 2,5 m/s nesten hele året</span></span></li>
<li><span class="sw" style="background:#55DCA2"></span><span><b>Stå</b><span class="txt">Over 2,5 m/s mer enn 5 % av tiden</span></span></li>
<li><span class="sw" style="background:#FED52A"></span><span><b>Rusle</b><span class="txt">Over 4 m/s mer enn 5 % av tiden</span></span></li>
<li><span class="sw" style="background:#FFA900"></span><span><b>Gå</b><span class="txt">Over 6 m/s mer enn 5 % av tiden</span></span></li>
<li><span class="sw" style="background:#FF463A"></span><span><b>Ukomfortabelt</b><span class="txt">Over 8 m/s mer enn 5 % av tiden</span></span></li>
</ul>

</div>

</div>

<div class="todo">Bygge overgang til neste slide</div>

<!-- Say: pek på de oransje flekkene ved bygningshjørnene. Det er der vinden
     akselererer — og der arkitekten hadde tenkt en benk. -->
<!-- TODO ~1:10 -->

---

<!-- _class: section -->

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
<img src="figures/illustrations/hesthagen-kart-ring.png" alt="Kart over Hesthagen mellom Klæbuveien og Gløshaugen, med tomta som reguleres ringet inn i rødt">
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
# Fysikkmodellen

<style scoped>
section { font-size: 23px; }
/* Ligningen skal fylle mer av sliden — den er poenget her, ikke en fotnote. */
.katex-display { margin: 0.5em 0 0.35em; }
.katex-display > .katex { font-size: 1.25em; }
.eqname { text-align: center; color: var(--muted); font-size: 0.72em; line-height: 1.5; margin: 0 0 1.1em; }
.eqname strong { color: var(--ink); font-weight: 700; }
.eqname code { font-size: 0.9em; }
</style>

<!--
LIGNINGEN ER VERIFISERT MOT KODEN i spacemakerai/wind-analysis-backend:

  openfoam/UEqn.H          fvm::div(phi, U) + turbulence->divDevReff(U)
                           == -fvc::grad(p), pluss
                           fvm::Sp(0.2*leafAreaDensity*mag(U), U)
  openfoam/createFields.H  leser inn feltet leafAreaDensity
  openfoam/realizableKE.*  patchet realizable k–epsilon (Shih et al. 1995)
  openfoam/Dockerfile.openfoam  OpenFOAM v2306, solver simpleFoam
  README.md:87             «simpleFoam with custom realizableKE turbulence model»

Tre ting den forrige ligningen tok feil:
  1. Den hadde du/dt. simpleFoam har ingen ddt-term — vi løser det STASJONÆRE
     problemet, altså den ferdig utblåste tilstanden, ikke forløpet dit.
  2. Den hadde bare molekylær viskositet nu. Vi løser de REYNOLDS-MIDLEDE
     ligningene, der nu erstattes av nu + nu_t og nu_t kommer fra k–epsilon.
  3. Den manglet vegetasjonsleddet, som er vår egen endring av solveren.

c_d = 0,2 er hardkodet i UEqn.H, a er leafAreaDensity (bladarealtetthet).
Vil du droppe trærne fra sliden, er det ett \underbrace å slette.
-->
$$
\begin{aligned}
\underbrace{(\mathbf{U}\cdot\nabla)\mathbf{U}}_{\text{vinden flytter seg selv}}
\;&=\; -\nabla p
\;+\; \underbrace{\nabla\cdot\big[(\nu+\nu_t)\big(\nabla\mathbf{U}+\nabla\mathbf{U}^{\top}\big)\big]}_{\text{friksjon og turbulens}}
\;-\; \underbrace{c_d\,a\,\lvert\mathbf{U}\rvert\,\mathbf{U}}_{\text{trær}} \\[0.4em]
\nabla\cdot\mathbf{U} \;&=\; 0
\end{aligned}
$$

<div class="eqname"><strong>Reynolds-midlede Navier–Stokes-ligninger</strong> — stasjonære og inkompressible<br>lukket med <strong>realizable k–ε</strong> · løst i OpenFOAM med <code>simpleFoam</code></div>

<div class="cols-2">

<div>

<div class="kicker">Hva som står der</div>

- $\mathbf{U}$ — den **tidsmidlede** vinden, ikke vindkast
- Newtons andre lov for en luftpakke, pluss: luft blir ikke borte
- Ingen formel gir svaret — det må regnes ut, punkt for punkt. Det er dette «numerikk» betyr

</div>

<div>

<div class="kicker">Derfor tar det tid</div>

- Del tomta i celler: millioner av dem for et bykvartal
- Løs ligningene i hver celle, om og om igjen, til svaret står stille
- Gjenta for hver vindretning, og vekt med vindstatistikken for stedet

</div>

</div>



<div class="todo">gøy med matte eller stack overflow?</div>

<!-- Say: ikke gå gjennom ligningen ledd for ledd. Poenget er ett: den kan ikke
     løses, bare regnes — og det er ikke koden som er treg, det er problemet.
     Flere celler og flere retninger er den eneste veien til et bedre svar.

     Har du 20 sekunder til overs: siste ledd er vår egen endring av solveren.
     Trær er ikke vegger — de bremser vinden i forhold til hvor tett bladverket
     er (a = bladarealtetthet), og c_d = 0,2. Det er en fin illustrasjon av at
     «fysikkmodellen» ikke er noe man laster ned ferdig. -->
<!-- TODO ~1:20 -->

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
<img src="figures/illustrations/02-surrogat-pipeline.svg" alt="Terreng og bygninger som høydekart inn, nevralt nett som roterer geometrien for åtte vindretninger, åtte vindfelt ut, vektet med vindrosen til et komfortkart — trent på ferdige CFD-kjøringer">

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

# To vindmodeller

<style scoped>
.cols-2 { gap: 1.4em; }
.card { border-top-width: 3px; }
.card.ai { border-top-color: var(--accent); background: var(--accent-soft); }
.card ul { font-size: 0.84em; margin-top: 0.4em; }
.card li { margin: 0.3em 0; }
/* Punchlinja fra statement-sliden, flyttet inn hit: samme rolle, mindre type. */
.punch { margin-top: 4em; border-left: 3px solid var(--accent); padding-left: 0.9em; }
.punch .line {
  margin: 0;
  font-family: var(--display);
  font-weight: 700;
  font-size: 1.7em;
  line-height: 1.15;
  letter-spacing: -0.015em;
}
.punch .sub { margin: 0.25em 0 0; color: var(--muted); font-size: 0.82em; }
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

<div class="punch">
  <p class="sub">Surrogatmodellen gir arkitekten mulighet til å teste mange alternativer — mens det ennå går an å endre dem.</p>
</div>

<!-- Say: gå gjennom kortene raskt, kolonne mot kolonne, ikke punkt for punkt.
     Viktig nyanse: vi erstatter ikke CFD, vi flytter den bakover i prosessen.
     Vær ærlig om avviket hvis noen spør; ikke selg det som gratis.

     Så pause, snu deg mot punchlinja og si den — dette er betalingen for
     tittelen. Hold pausen etterpå, selv om sliden ikke lenger er tom. -->
<!-- TODO ~0:55 -->

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
