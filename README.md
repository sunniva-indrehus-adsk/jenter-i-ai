# Jenter i AI

> _Kort pitch for foredraget her._

Foredrag for **Jenter i AI**. Slides på norsk.

## Kjøre slidene

Ingen byggesteg — `talk/slides.md` redigeres direkte.

> **Kjør fra `talk/`, ikke fra rota.** Både `--theme theme.css` og katalogen som
> serveres (`.`) tolkes relativt til der du står. Står du i rota finner ikke Marp
> `theme.css`, og slidene rendres med standardtemaet — de blir stygge, men det er
> ingen feilmelding som forteller deg det.

```bash
cd talk

# Watch mode (live reload på http://localhost:8080/slides.md)
docker run --rm --init -v "$PWD":/home/marp/app -e LANG=$LANG -p 8080:8080 -p 37717:37717 \
  marpteam/marp-cli:v3.2.0 \
  --theme theme.css --watch -s --html=true .
```

Hver linje slutter med backslash `\` — det må være **siste tegn på linja** (ingen
mellomrom etter), ellers splitter zsh kommandoen og du får feil som
`flag needs an argument: 'e'`.

Åpne <http://localhost:8080/slides.md>. Stopp serveren med `Ctrl-C`.

Vil du heller kjøre uten å bytte katalog, pek mountet rett på `talk/`:

```bash
docker run --rm --init -v "$PWD/talk":/home/marp/app -e LANG=$LANG -p 8080:8080 -p 37717:37717 \
  marpteam/marp-cli:v3.2.0 \
  --theme theme.css --watch -s --html=true .
```

Har du `marp` installert lokalt, får du Artifakt i stedet for Inter:

```bash
cd talk && marp --theme theme.css --html -w slides.md
```

### Feilsøking

| Symptom | Årsak |
| --- | --- |
| Slidene har hvit bakgrunn og serif-tekst, ingen logo | Temaet ble ikke funnet — du kjørte fra rota i stedet for `talk/` |
| `Bind for 0.0.0.0:8080 failed: port is already allocated` | En gammel container kjører. `docker ps`, så `docker stop <navn>` |
| Endringer i `slides.md` slår ikke gjennom | Watch-modus følger bare den monterte katalogen — sjekk at mountet peker på `talk/` |

Sjekk hva som faktisk serveres:

```bash
curl -s http://localhost:8080/slides.md | grep -c 0696D7   # 1 = temaet er med, 0 = ikke
```

### Figurer

Statiske figurer ligger som frittstående SVG-er i `talk/figures/illustrations/`,
nummerert etter rekkefølgen i decket (`01-…svg`, `02-…svg`). Portretter i
`talk/figures/people/`.

```markdown
![](figures/illustrations/01-eksempel.svg)
```

eller, for å styre størrelsen:

```html
<img src="figures/illustrations/01-eksempel.svg" width="90%">
```

For animerte SVG-er med SMIL (`<animate>` / `<animateMotion>`), bruk `<object>`
i stedet for `<img>` — da kjører nettleseren dem som et levende dokument:

```html
<object data="figures/illustrations/01-eksempel.svg" type="image/svg+xml" width="90%"></object>
```

Interaktive widgets som trenger CSS-søskenselektorer må ligge inline i sliden —
de kan ikke flyttes ut, fordi CSS-en bor utenfor SVG-en.

### Eksportere til fil

Hver linje slutter med backslash `\` — det må være **siste tegn på linja** (ingen
mellomrom etter), ellers splitter zsh kommandoen og du får feil som
`flag needs an argument: 'e'`.

Frittstående HTML:

```bash
docker run --rm -v "$PWD":/home/marp/app/ -e MARP_USER="$(id -u):$(id -g)" -e LANG=$LANG \
    marpteam/marp-cli:v3.2.0 \
    --theme theme.css --allow-local-files --html slides.md -o slides.html
```

PDF:

```bash
docker run --rm -v "$PWD":/home/marp/app/ -e MARP_USER="$(id -u):$(id -g)" -e LANG=$LANG \
    marpteam/marp-cli:v3.2.0 \
    --theme theme.css --allow-local-files --html slides.md --pdf
```

## Autodesk-profil

Temaet (`talk/theme.css`) etterligner Autodesks visuelle profil:

| Element | Valg |
| --- | --- |
| Typografi | **Inter** (åpen) — eller **Artifakt** hvis du har den installert |
| Farger | Autodesk-svart `#000000` på hvit `#FFFFFF`, grå `#6E6E6E` til sekundærtekst |
| Aksent | Autodesk-blå `#0696D7` — kulepunkter, lenker, `.kicker`, `.callout` |
| Logo | Hvit lockup øverst til venstre på tittel- og `section`-slidene, svart nede til venstre ellers |
| Sidetall | Nede til høyre, grått |

Alt er sjekket inn, så en fersk klone rendrer identisk. Ingenting hentes fra
nett under bygging.

### Logo

`talk/figures/logos/autodesk-logo-black.svg` og `-white.svg` er
[Autodesks primærlogo fra 2021][logo], hentet fra Wikimedia Commons. Filen er
**public domain** der — den består bare av enkle geometriske former og tekst, og
kommer ikke over terskelen for verkshøyde. Den hvite varianten er samme fil med
`fill` byttet til `#FFFFFF`; kilde og lisens står som kommentar i begge filene.

Navnet og logoen er fortsatt et registrert varemerke til Autodesk. Her brukes de
til å vise hvor foredragsholderne jobber, som er vanlig, beskrivende bruk.

[logo]: https://commons.wikimedia.org/wiki/File:Autodesk_Logo_2021.svg

### Skrifter

Autodesks merkevareskrift er **Artifakt**, men den er lisensiert og kan ikke
sjekkes inn. Temaet løser det med en to-trinns stakk:

1. `'Artifakt Element'` / `'Artifakt Legend'` — treffer hvis du har skriften
   installert lokalt (den ligger i `/Library/Fonts` på en Autodesk-Mac).
2. `'Inter'` — pakket med i `talk/fonts/Inter-latin.woff2` (48 kB, variabel
   vekt 100–900) under [SIL Open Font License 1.1][ofl]. Lisensteksten ligger i
   `talk/fonts/Inter-OFL.txt`, som OFL krever.

Inter er en nær nok neo-grotesk til at decket ser likt ut uansett hvilken av de
to som slår til. Docker-eksport bruker Inter, siden containeren ikke ser
systemfontene dine.

[ofl]: https://openfontlicense.org/

> Portrettene i `talk/figures/people/` blir offentlige når repoet publiseres.
> Sjekk at alle avbildede er med på det.

## Slidetyper

| Klasse | Bruk |
| --- | --- |
| `<!-- _class: title -->` | Tittel- og avslutningsslide — svart bakgrunn, hvit lockup. `#` tittel, `##` undertittel, `###` arrangement (settes i versaler) |
| `<!-- _class: title title-photo -->` | Som over, men lys: full-bleed render i bakgrunnen og svart tekst |
| `<!-- _class: section -->` | Kapittelskille — svart, venstrejustert `#` + `##` |
| `<!-- _class: statement -->` | Én stor påstand midt på hvit bakgrunn |
| _(ingen)_ | Vanlig innholdsslide — overskrift med strek under, innhold under |

### Tittelslide med bilde

`title-photo` legger en render i full bredde bak tittelen. Bildet er lyst, så
sliden snus fra svart til hvit og teksten settes i svart. En myk hvit gradient i
nedre venstre hjørne holder tittelen leselig uansett hvor strømlinjene faller,
uten å vaske ut attribusjonen nede til høyre.

Standardbildet er `gløshaugen-streamlines.png`. Bytt det per slide:

```markdown
<!-- _class: title title-photo -->

<style scoped>
section { --photo: url('figures/illustrations/en-annen-render.png'); }
</style>
```

Renderen fra Forma har allerede en «Autodesk Forma»-lockup øverst til venstre,
så temaets egen logo er skrudd av på denne slidetypen — ellers hadde det blitt
to logoer.

## Byggeklosser

```html
<div class="cols-2"> … </div>     <!-- to like spalter -->
<div class="cols-3"> … </div>     <!-- tre kort på rad, lik høyde -->
<div class="card"><h3>…</h3><p>…</p></div>
<div class="callout"> … </div>    <!-- blå ramme til venstre -->
<div class="kicker">Stikkord</div>
<div class="who-row">            <!-- portretter -->
  <div class="who"><img src="figures/people/sunniva.png"/><span>Sunniva</span></div>
</div>
<div class="figcap"><span class="figref">Figur 1</span> Bildetekst.</div>
```

## Konvensjoner

- `<style scoped>` i sliden for layout som bare gjelder den ene sliden.
- `<!-- Say: … -->` for manus, `<!-- TODO ~M:SS -->` for tidsbudsjett per slide.
- Matte er KaTeX (`math: katex` i frontmatter).
- **Eksporter alltid til `talk/`.** Logoen hentes med en relativ `url()` i
  temaet, så en HTML-fil som havner utenfor `talk/` mister merket i hjørnet.

## Kilder

_Pekere til kildemateriale her._
