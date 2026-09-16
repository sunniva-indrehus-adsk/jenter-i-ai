# tools/

**Ingenting her trengs for å bygge decket.** Slidene bygges med to
docker-kommandoer rett fra `talk/slides.md` — se README i rota, «Bygge».

Det som ligger her, er oppskriften på én figur. Figuren selv er sjekket inn, så
skriptene kjøres bare hvis den skal lages på nytt.

| Fil | Lager |
| --- | --- |
| `hesthagen_slide4.py` | `talk/figures/tidligfase/hesthagen-flyfoto*.jpg` — bakgrunnen på slide 3, 4 og 5 |
| `hesthagen_geo.py` | biblioteket det bruker: koordinatomregning og WMS-kall mot Trondheim kommune og Kartverket |

```bash
python3 tools/hesthagen_slide4.py            # alle fem variantene
python3 tools/hesthagen_slide4.py flyfoto    # bare den som er i bruk
```

Krever nett (WMS-kall) og `pillow`.

**Endrer du innrammingen, må to tall sjekkes på nytt.** `ROLLER`-ramma bestemmer
hvor tomtegrensa lander i slide-piksler, og rollefigurene på slide 4 og 5 er
posisjonert for å holde seg unna den røde streken — grensa er x=699. Skriptet
skriver ut hvor tomta havner. Se `section.overlay .roles-holder.venstre` i
`talk/theme.css` og «Tidligfase-bildet» i README for regnestykket.

## Slettede skript

Disse fantes, men er fjernet — de var engangsverktøy, og det de gjorde står nå
som kommandoer i README i stedet:

| Var | Erstattet av |
| --- | --- |
| `build-deck.sh` | de to docker-kommandoene under «Bygge» |
| `flipbook.sh` | ffmpeg-kommandoene under «Hente ruter ut av et skjermopptak» |
| `grab-forma.sh` | `screencapture` under «Skjermbilder rett fra Forma» |
| `inject_film.py` | ingenting — videoen er ute av decket, så decket har bare én utgave |
