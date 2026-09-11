<!-- _class: demo -->

<!-- Denne fila er BARE demo-sliden. tools/inject_film.py setter den inn i
     stedet for stillbildeserien når slides-film.md genereres — se README,
     «To utgaver av decket».

     Rediger innholdet i slides.md, ikke her. Her hører bare selve filmsliden. -->

<!--
«What is Forma Site Design» fra YouTube. Marp trenger --html=true for at
<iframe> skal rendres; det ligger allerede i kommandoen i README.

Embedden krever nett i salen, og den fungerer ikke i PDF-eksport. Last ned en
lokal kopi som reserve og bytt iframe-en (og skriptet) mot:
  <video src="figures/video/forma-demo.mp4" controls muted playsinline></video>
CSS-en i theme.css håndterer begge.

start=14 og end=63: klippet går fra 0:14 til 1:03 — 49 sekunder, spilt i vanlig
hastighet. Sluttpunktet er satt der med vilje: fra 1:03 går filmen over i Forma
Board og rapportoppsett, som vi ikke rekker å snakke om på 15 minutter. Klippet
slutter derfor på AI-prediksjonen, som er den vi bygger videre på. Bruker du den lokale reservefila i stedet, blir det #t=14,74 på
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
  src="https://www.youtube-nocookie.com/embed/1ovhhMWpohw?start=14&end=63&rel=0&modestbranding=1&playsinline=1&cc_load_policy=0&iv_load_policy=3"
  data-autoplay-src="https://www.youtube-nocookie.com/embed/1ovhhMWpohw?start=14&end=63&rel=0&modestbranding=1&playsinline=1&cc_load_policy=0&iv_load_policy=3&autoplay=1&mute=1&controls=0"
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
