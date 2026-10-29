# The Augmented Forest

A 20-minute recap of Kent Beck's closing keynote at GOTO Copenhagen 2026,
*The Augmented Forest* (on stage: *The Forest Genie*): forests, deserts,
genies, and features vs. futures.

The deck is Marp markdown, in `talk/augmented-forest.md`, with the Autodesk
theme in `talk/theme.css`. Speaker notes are the `<!-- Say: -->` comments on
each slide.

## Running the slides

Run from `talk/`, not the repo root: both `--theme theme.css` and the served
directory are relative to where you stand. From the root, Marp silently falls
back to its default theme.

```bash
cd talk
docker run --rm --init -v "$PWD":/home/marp/app -e LANG=$LANG -p 8080:8080 -p 37717:37717 \
  marpteam/marp-cli:v3.2.0 \
  --theme theme.css --watch -s --html=true .
```

Open <http://localhost:8080/augmented-forest.md>. Stop with `Ctrl-C`.

With `marp` installed locally:

```bash
cd talk && marp --theme theme.css --html -w augmented-forest.md
```

## Figures

| Folder | What |
| --- | --- |
| `figures/augmented-forest/` | Everything the deck uses: the flat SVG illustrations (desert, forest, genie, icons) and the cropped photos |
| `figures/illustrations/` | The original, uncropped conference photos and Nick's headshot |
| `figures/logos/` | Autodesk logo, black and white, used by the theme |

The Kent Beck portrait (`kent-portrait-hat.jpg`) is from kentbeck.com, photo
by Robert Opiyo. Ask before using it outside internal talks.

## Publishing

`.github/workflows/publiser-slides.yml` builds HTML and PDF on every push to
`main` and publishes them to GitHub Pages (`gh-pages` branch).
