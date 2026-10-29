---
marp: true
theme: theme.css
paginate: true
---

<!--
THE AUGMENTED FOREST: a 20-minute recap of Kent Beck's GOTO Copenhagen 2026
keynote (Fri 2 Oct, TAP1 Main Stage). Thirteen slides, about 1.5 minutes each,
with time left for questions. The slides carry pictures; the speaker notes
("Say:") carry the story.

Same theme as the "Jenter i AI" deck (theme.css). The illustrations are flat
SVGs in figures/augmented-forest/, drawn for this deck in one palette:
forest green, desert sand, and Autodesk blue for the genie.
-->

<style>
:root {
  --forest: #2E7D4F;
  --desert: #C08A2E;
}

/* Big illustration with a label underneath. Used on most slides. */
.scene { display: flex; flex-direction: column; align-items: center; text-align: center; }
.scene img { display: block; width: 100%; height: auto; }
.scene .label {
  font-family: var(--display);
  font-weight: 700;
  font-size: 1.25em;
  margin-top: 0.15em;
}
.scene .tag { color: var(--muted); font-size: 0.8em; margin-top: 0.1em; }
.forest-c { color: var(--forest); }
.desert-c { color: var(--desert); }
.genie-c  { color: var(--accent); }

/* Three icons with a short label each. */
.icons {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 2em;
  margin-top: 1.4em;
  text-align: center;
}
.icons img { width: 170px; height: 170px; display: block; margin: 0 auto 0.5em; }
.icons b { display: block; font-family: var(--display); font-size: 1.15em; }
.icons span { color: var(--muted); font-size: 0.8em; }

.big-quote {
  font-family: var(--display);
  font-weight: 700;
  font-size: 1.6em;
  line-height: 1.25;
  letter-spacing: -0.01em;
}
.attrib { color: var(--muted); font-size: 0.7em; margin-top: 0.6em; }
</style>

<!-- _class: title title-photo -->
<!-- _header: 'GOTO Copenhagen 2026 · recap' -->
<!-- _paginate: false -->

<!-- White title slide: title-photo gives black type, the black Autodesk logo
     and a blue eyebrow. --photo: none drops the photo, so only the theme's
     white corner gradients are left, white on white. -->
<style scoped>
section { --photo: none; }
/* The dense forest-more.svg, the forest after the genie. 440 px wide and
   ending above the title, with the lamp in its bottom RIGHT corner: the
   one-line title runs to about x 760, and a lamp on the left ran into it. */
.hero { position: absolute; right: 64px; top: 104px; width: 440px; }
.hero img { display: block; width: 100%; }
.hero .lamp { position: absolute; width: 40%; right: -6%; bottom: -10%; }
h1 { white-space: nowrap; max-width: none; }
h2, h3 { max-width: 560px; }
</style>

<div class="hero">
  <img src="figures/augmented-forest/forest-more.svg" alt="">
  <img class="lamp" src="figures/augmented-forest/genie.svg" alt="">
</div>

### Kent Beck's keynote, retold

# The Augmented Forest

## Forests, deserts and genies

<!-- Say (0:30): Introduce yourself in one sentence. "The closing keynote at
     GOTO Copenhagen this year was Kent Beck: creator of XP, TDD, co-author of
     the Agile Manifesto. I've been thinking about it since, so here it is in
     twenty minutes." -->

---

# GOTO Copenhagen 2026

<style scoped>
/* The team on the left, GOTO on the right, both 418 px tall. 418 px is the
   selfie's own 4:3 height at 558 px wide, so it isn't cropped: there are
   faces right at both edges. The gotopia screenshot (1256 x 1064) is shown
   whole at the same height. */
.opening { display: grid; grid-template-columns: 558px auto; justify-content: space-between; gap: 1.4em; margin-top: 0.4em; }
.opening img { display: block; width: 100%; height: 418px; object-fit: cover; border-radius: 4px; }
.opening .gotopia img { width: auto; height: 418px; object-fit: contain; box-shadow: 0 1px 6px rgba(0, 0, 0, 0.15); }
.opening .figcap { margin-top: 0.35em; }

/* Nick wasn't in the selfie, so his headshot is added in. Placed and sized
   in percent of the selfie so it scales with it: he sits at the far side
   of the table in the middle, between the two men, with two people to his
   left and three to his right. At 11% of the photo's width his face is the
   size of his neighbours', and his head is level with theirs. No ring: a soft
   radial mask fades the edge into the wall behind, so he reads as part of
   the photo rather than a badge on top of it. */
.opening .group { position: relative; }
.opening .group .nick {
  position: absolute;
  left: 37.5%;
  top: 38%;
  width: 11%;
  aspect-ratio: 1;
  height: auto;
  border-radius: 0;
  object-fit: cover;
  object-position: center 40%;
  -webkit-mask-image: radial-gradient(circle at 50% 48%, #000 55%, transparent 71%);
  mask-image: radial-gradient(circle at 50% 48%, #000 55%, transparent 71%);
}
</style>

<div class="opening">
  <div class="group">
    <img src="figures/augmented-forest/goto-selfie.jpg" alt="Selfie with colleagues at GOTO Copenhagen 2026">
    <img class="nick" src="figures/augmented-forest/nick-headshot.png" alt="Nick">
    <div class="figcap">At GOTO Copenhagen 2026</div>
  </div>
  <div class="gotopia">
    <img src="figures/augmented-forest/gotopia-sessions.jpg" alt="Screenshot of conference sessions on gotopia.tech, with goto; and YOW! talk thumbnails">
    <div class="figcap">GOTO talks on <a href="https://gotopia.tech/sessions?page=0">gotopia.tech</a></div>
  </div>
</div>

<!-- Say (1:00): Start with the selfie: who you went with, and what the
     conference was like. Then point right: GOTO runs conferences in several
     cities (and YOW! in Australia), and most talks end up free on
     gotopia.tech, so everyone here can watch them afterwards. -->

---

# Kent Beck

<style scoped>
.bio { display: grid; grid-template-columns: 300px 1fr; gap: 2.4em; align-items: center; margin-top: 0.4em; }
.bio .portrait { width: 300px; height: 300px; border-radius: 50%; overflow: hidden; box-shadow: 0 0 0 8px var(--paper), 0 0 0 9px var(--rule); }
.bio .portrait img { width: 100%; height: 100%; object-fit: cover; display: block; }
.bio ul { margin: 0; padding-left: 1.1em; font-size: 0.86em; line-height: 1.4; }
.bio li { margin: 0 0 0.55em; }
.bio li strong { font-family: var(--display); font-size: 1.12em; }
.bio li .d { display: block; color: var(--muted); }
.bio .figcap { text-align: center; margin-top: 1em; }
</style>

<div class="bio">
<div>
  <div class="portrait"><img src="figures/augmented-forest/kent-portrait-hat.jpg" alt="Kent Beck smiling, in a blue fedora and a bow tie"></div>
  <div class="figcap">Photo: Robert Opiyo, via kentbeck.com</div>
</div>
<div>

- **[Extreme Programming](https://en.wikipedia.org/wiki/Extreme_programming)**
  <span class="d">Created on Chrysler's C3 project, 1996 · <em>Extreme Programming Explained</em>, 1999</span>
- **[Test-driven development](https://en.wikipedia.org/wiki/Test-driven_development)**
  <span class="d"><em>Test-Driven Development: By Example</em>, 2002</span>
- **[Agile Manifesto](https://agilemanifesto.org)**
  <span class="d">One of the 17 original signatories · Snowbird, Utah, February 2001</span>
- **[Tidy First?](https://newsletter.kentbeck.com)**
  <span class="d">Book (O'Reilly, 2023) and newsletter · codes with genies every day</span>

</div>
</div>

<!-- Say (1:00): Most of the room knows the name, so keep this quick. The
     point to make: this isn't an AI hype person. It's someone who has spent
     forty years on how to change code safely, and who now spends his days
     coding with AI agents and writing about what he finds. -->

---

# Beck's keynote

<style scoped>
/* The stage photo on its own, as large as the slide allows under the title
   (1800 x 1463, so 470 px tall is 578 px wide), centred. */
.stage { display: flex; flex-direction: column; align-items: center; margin-top: -0.2em; }
.stage img { display: block; height: 470px; width: auto; border-radius: 4px; }
.stage .figcap { margin-top: 0.4em; }
</style>

<div class="stage">
  <img src="figures/augmented-forest/kent-forest-genie.jpg" alt="Kent Beck on stage in front of his handwritten title slide: The Forest Genie">
  <div class="figcap">GOTO Copenhagen, 2 October 2026 on stage</div>
</div>

<!-- Say (1:00): The program said "The Augmented Forest", but his handwritten
     first slide said "The Forest Genie". Closing keynote on the Friday.

     Background: the Forest & Desert metaphor is from Beth Andres-Beck and
     Kent Beck (Øredev 2024). The genie is Kent's word for AI coding agents,
     used since spring 2025. The keynote's question was: AI makes programming
     more fun and harder at the same time. How do we keep up, still get work
     done, and explain it to people who don't code? -->
---

# Two landscapes

<style scoped>
.pair { display: grid; grid-template-columns: 1fr 1fr; gap: 3em; margin-top: 0.4em; }
.pair .scene img { width: 92%; }
.words { font-size: 0.85em; margin-top: 0.5em; color: var(--ink); }
.runs { font-family: var(--display); font-weight: 700; font-size: 1.3em; margin-top: 0.4em; }
</style>

<div class="pair">
  <div class="scene">
    <img src="figures/augmented-forest/desert.svg" alt="Desert">
    <div class="words">Deadlines · bugs · painful on-call · change is the enemy</div>
    <div class="runs desert-c">Runs on fear</div>
  </div>
  <div class="scene">
    <img src="figures/augmented-forest/forest.svg" alt="Forest">
    <div class="words">Small safe steps · tests · rare bugs · change is expected</div>
    <div class="runs forest-c">Runs on trust</div>
  </div>
</div>

<!-- Say (2:00): Desert first, because most of us have been there. "We travel
     by force of will under an oppressive heat." Little margin, no time to look
     back, estimates rule, metrics used to control people.

     The forest is resource-rich and self-renewing: today's work makes
     tomorrow easier. Tests, pairing, refactoring, continuous release. On-call
     is "no big deal" because there are so few bugs.

     Land on the bottom line. Kent's view: the single most important
     difference is trust vs fear. Trust in each other, in yourself, in the
     software and in the future.

     Why the metaphor matters (Beth Andres-Beck): "This architecture you've
     described sounds like a lush forest, but we are living in the desert."
     Advice doesn't carry over. Forest advice ("write tests, pair") misfires in
     the desert, where there's no slack. Desert advice ("more estimates, more
     review layers") makes no sense in the forest. Getting from desert to
     forest takes small, safe steps the whole community takes: "No developer
     can do it alone, and no amount of technology will get us there." -->

---

# Features vs. Futures

<style scoped>
/* Full-bleed: the photo IS the slide. A 16:9 crop of IMG_4067 (2560 x 1440,
   2x the slide), so it covers the whole page without distortion. The title
   sits on the dark rigging top left, so it turns white. The Autodesk logo
   is hidden here: bottom left is exactly where Kent stands, and the logo
   landed on his hand. The page number turns light to stay readable. */
section {
  background: #000 url('figures/augmented-forest/kent-features-futures-wide.jpg') center / cover no-repeat;
}
section h1 { color: #fff; border-bottom-color: rgba(255, 255, 255, 0.85); max-width: 420px; text-shadow: 0 1px 6px rgba(0, 0, 0, 0.6); }
section::before { display: none; }
section::after { color: rgba(255, 255, 255, 0.8); }
.credit { position: absolute; right: 96px; bottom: 30px; font-size: 15px; color: rgba(255, 255, 255, 0.85); text-shadow: 0 1px 4px rgba(0, 0, 0, 0.8); }
</style>

<div class="credit">Kent Beck, GOTO Copenhagen 2026</div>

<!-- Say (1:45): Kent's older idea, and the lens for the rest of the talk. Software is
     valuable in two ways: the features it has today, and the options it keeps
     open for what it could do next. Every feature spends some of those
     options, so the system gets stiffer over time, unless you put options
     back with tidying, tests and structure.

     Point at the chart in the photo. Kent's own names for the two lines
     (from his post "Earn And Learn"): the blue curve is the Finish Line
     Game, spending futures on features and betting the product ships before
     the futures run out. The red staircase is the Compounding Game,
     alternating features with tidying so both keep growing. The desert plays
     the first game, the forest the second.

     The video card links to the full ShipSummit talk. Its thumbnail asks
     "Do Unit Tests Still Matter?", worth a laugh with this audience.

     Features are easy to see and count, so they win. Futures sit below the
     surface, so they get skipped.

     The genie is great at features and no good at managing futures. The line
     at the bottom is Kent's: it used to take a hundred people ten years to
     reach the point where there are no options left. With a genie, one
     person can get there in a week. Leave that hanging: the genie is next. -->

---

# Features vs. Futures

<style scoped>
/* Slide 6's full-bleed photo again, now annotated. Positions are in slide
   pixels on the 1280 x 720 page, measured on kent-features-futures-wide.jpg:
   Kent's handwritten FUTURES sits at about x 505-590, y 360-415, and
   FEATURES at x 640-790, y 488-555. Each word gets a ring and a card:
   dashed gold for the invisible, solid blue for the visible. */
section {
  background: #000 url('figures/augmented-forest/kent-features-futures-wide.jpg') center / cover no-repeat;
}
section h1 { color: #fff; border-bottom-color: rgba(255, 255, 255, 0.85); width: fit-content; max-width: none; white-space: nowrap; text-shadow: 0 1px 6px rgba(0, 0, 0, 0.6); }
section::before { display: none; }
section::after { color: rgba(255, 255, 255, 0.8); }

.quote { position: absolute; left: 64px; top: 146px; width: 400px; color: #fff; font-family: var(--display); font-weight: 700; font-size: 22px; line-height: 1.3; text-shadow: 0 1px 6px rgba(0, 0, 0, 0.8); }
.quote span { display: block; margin-top: 0.4em; font-family: var(--sans); font-weight: 400; font-size: 15px; color: rgba(255, 255, 255, 0.8); }

.ring { position: absolute; border-radius: 50%; }
.ring.inv { left: 488px; top: 342px; width: 120px; height: 86px; border: 4px dashed #F2C14E; }
.ring.vis { left: 622px; top: 474px; width: 188px; height: 94px; border: 4px solid var(--accent); }

.link { position: absolute; height: 0; border-top: 3px solid; }
.link.inv { left: 452px; top: 385px; width: 36px; border-color: #F2C14E; border-top-style: dashed; }
.link.vis { left: 810px; top: 521px; width: 26px; border-color: var(--accent); }

.card { position: absolute; box-sizing: border-box; background: rgba(255, 255, 255, 0.96); border: 0; border-left: 5px solid; border-radius: 4px; padding: 12px 16px; box-shadow: 0 4px 16px rgba(0, 0, 0, 0.35); }
.card .kicker { margin: 0 0 2px; font-size: 15px; }
.card b { display: block; font-family: var(--display); font-size: 24px; line-height: 1.15; }
.card p { margin: 4px 0 0; color: #444; font-size: 15px; line-height: 1.4; }
.card.inv { left: 64px; top: 320px; width: 388px; border-left-color: #F2C14E; }
.card.inv .kicker { color: #A87A1E; }
.card.vis { left: 836px; top: 462px; width: 300px; border-left-color: var(--accent); }
</style>

<div class="ring inv"></div><div class="link inv"></div>
<div class="card inv">
  <div class="kicker">Invisible</div>
  <b>Futures</b>
  <p>Understanding, simplification, teaching, enabling abstractions. Nobody gets credit for it.</p>
</div>

<div class="ring vis"></div><div class="link vis"></div>
<div class="card vis">
  <div class="kicker">Visible</div>
  <b>Features</b>
  <p>What users see, what gets counted and credited.</p>
</div>

<!-- Say (1:30): From Kent's post "Mathematicians, Here's a Way To Think About
     Your Existential Crisis" (September 2026). Programming, like maths, has a
     visible part (features; for mathematicians, proofs) and a much larger
     invisible part: "understanding, education, simplification, enabling
     abstractions."

     "If all we work on is the visible part, progress on that visible part
     slows to a crawl." And "nobody gets credit for the invisible work".

     Same photo as the slide before, now marked up: futures are the invisible
     axis, features the visible one. The blue curve is what happens when only
     the visible axis gets attention.

     Hand-off to the genie: "The visible stuff is better done by machine. The
     invisible stuff is, well, invisible." So who tends the roots? -->

---

# The Genie

<style scoped>
.g { display: grid; grid-template-columns: 0.85fr 1.15fr; gap: 2em; align-items: center; margin-top: -0.4em; }
.g .big-quote { font-size: 1.35em; }
/* GitHub's contribution graph, cropped to February-July 2026 from a 2x
   screenshot of github.com/kentbeck (678 x 236). */
.g .gh { margin-top: 1.1em; }
.g .gh img { display: block; width: 100%; height: auto; }
.g .gh .figcap { margin-top: 0.4em; }
</style>

<div class="g">
<img src="figures/augmented-forest/genie.svg" alt="Genie lamp with blue smoke">
<div>
<div class="big-quote">"Sometimes it's useful, and sometimes it's damaging."</div>
<div class="attrib">Kent Beck on AI coding agents</div>
<div class="gh">
  <img src="figures/augmented-forest/kent-github-feb-jul.png" alt="Kent Beck's GitHub contribution graph, February to July 2026, densest in March and April">
  <div class="figcap"><strong>Kent's GitHub contributions, Feb–Jul 2026:</strong> 495 on 54 days, 301 of them in April. Each square is one day; the greener, the more commits, pull requests, issues and reviews that day. Source: <a href="https://github.com/kentbeck">github.com/kentbeck</a></div>
</div>
</div>
</div>

<!-- Say (1:30): Why "genie" and not "assistant"? A genie grants wishes. It's
     powerful, eager to please, and unpredictable: you get what you asked for,
     which isn't always what you meant.

     Kent's name for working with it properly is "augmented coding", as
     opposed to vibe coding. In vibe coding you only care whether it works.
     In augmented coding you still care about the code: tested, tidy,
     understood. Same values as before, more leverage.

     The graph: proof he's not talking theory. This is what coding with
     genies every day looks like on his GitHub, with the burst in March and
     April. Numbers read from his public profile on 29 October 2026; the
     graph only counts work on GitHub, not everything he does. -->

---

# How genies misbehave

<div class="icons">
  <div><img src="figures/augmented-forest/icon-cheat.svg" alt=""><b>It cheats</b><span>deletes the failing test</span></div>
  <div><img src="figures/augmented-forest/icon-overreach.svg" alt=""><b>It overreaches</b><span>grants wishes you didn't make</span></div>
  <div><img src="figures/augmented-forest/icon-tarpit.svg" alt=""><b>It degrades</b><span>the genie tarpit</span></div>
</div>

<!-- Say (1:45): All three are from Kent's own experience.
     Cheats: you asked for green tests, so deleting the failing one counts.
     Overreaches: extra features, extra abstractions, rewrites nobody asked for.
     Degrades: "a degraded facsimile of the mediocre code it trained on".
     Complexity piles up until the genie itself gets stuck in it. That's the
     serious one: the genie makes the code harder to change, and harder-to-
     change code makes the genie worse. It's the features-and-futures curve
     from two slides back, sliding down to zero options at genie speed.

     If Kent showed a live example here, tell it. -->

---

# Taming the genie

<div class="icons">
  <div><img src="figures/augmented-forest/icon-tests.svg" alt=""><b>Tests</b><span>the wish, written down</span></div>
  <div><img src="figures/augmented-forest/icon-steps.svg" alt=""><b>Small steps</b><span>short leash, cheap to undo</span></div>
  <div><img src="figures/augmented-forest/icon-eye.svg" alt=""><b>Watch it</b><span>read the diff</span></div>
</div>



<!-- Say (1:45): Kent calls TDD a superpower with agents: the test is the
     wish, written so the genie can't misread it. Small steps keep it on a
     short leash. Read the diff, especially changes to tests.
     One more: asking for code "like Kent Beck" improved the style but not the
     architecture. Design took explicit constraints.

     Then pause on the bottom line. This is the turning point of the talk. -->

---

# The genie intensifies

<style scoped>
/* No captions. The landscapes stack in two columns, before on the left and
   after on the right, with ONE genie in the middle between them: "+ genie ="
   spans both rows. All pictures the same size (the SVGs are all 4:3), so
   nothing but the content changes between before and after. */
.amp { display: grid; grid-template-columns: 270px 50px 270px 50px 270px; grid-template-rows: auto auto; justify-content: center; align-items: center; column-gap: 0.6em; row-gap: 1.2em; margin-top: 0.4em; }
.amp img { display: block; width: 270px; height: auto; }
.amp .mid { grid-row: 1 / span 2; }
.amp .op { font-family: var(--display); font-weight: 700; font-size: 1.8em; color: var(--muted); text-align: center; }
</style>

<div class="amp">
  <img src="figures/augmented-forest/desert.svg" alt="Desert" style="grid-column:1; grid-row:1">
  <img src="figures/augmented-forest/forest.svg" alt="Forest" style="grid-column:1; grid-row:2">
  <div class="op mid" style="grid-column:2">+</div>
  <img class="mid" src="figures/augmented-forest/genie.svg" alt="Genie" style="grid-column:3">
  <div class="op mid" style="grid-column:4">=</div>
  <img src="figures/augmented-forest/desert-more.svg" alt="The desert swallowed by dunes" style="grid-column:5; grid-row:1">
  <img src="figures/augmented-forest/forest-more.svg" alt="The forest grown dense" style="grid-column:5; grid-row:2">
</div>

<!-- Say (2:00): This is the thesis from the keynote abstract: AI intensifies
     both experiences. The genie isn't a landscape. It amplifies whatever
     landscape it lands in.

     In the desert: more code, faster, under the same pressure. No tests to
     catch a wish gone wrong, reviewers drowning in diffs, tangled code, the
     tarpit.

     In the forest: tests turn every wish into a checkable contract, small
     steps are cheap to throw away, tidy code is easier for the genie to read
     too, and experiments become almost free.

     The slide has no captions on purpose. Say them: "more code, more sand"
     and "faster learning, more forest".

     The genie is identical in both rows. Only the soil differs. Forest
     practices used to be "nice to have when we find time". With a genie,
     they're the leash.

     For non-programmers: "We bought the genie, why aren't we faster?"
     "Because we put it in the desert." -->

---

# Five principles

<style scoped>
/* The photo alone, centred, as large as the slide allows under the title:
   1800 x 1350 is 4:3, so 480 px tall is 640 px wide. */
.pr { display: flex; justify-content: center; margin-top: -0.2em; }
.pr .photo img { display: block; height: 480px; width: auto; border-radius: 4px; }
.pr ol { margin: 0; padding-left: 1.3em; font-family: var(--display); font-weight: 700; font-size: 1.3em; line-height: 1.75; }
.pr ol li::marker { color: var(--forest); }
</style>

<div class="pr">
<div class="photo"><img src="figures/augmented-forest/kent-principles.jpg" alt="Kent Beck on stage in front of his handwritten list of principles"></div>


</div>

<!-- Say (1:45): Kent's handwritten list, as he showed it. These are how to
     grow the forest when you have a genie: use it to automate the toil, but
     keep the people connected, keep the choices visible, and keep learning.

     Spend the most time on "preserve struggle". The genie can take away the
     struggle that's how we learn, and a team that stops learning slides
     back towards the desert. (Fill in what Kent said about each one; the
     photo only shows the words.)

     Then turn it back to the room:
       Ask   - where are we forest, and where desert?
       Check - would our tests catch a wish gone wrong?
       Plant - one small, safe step this sprint: a test, a tidying, a
               smaller slice. -->

---



# Further deep dive

<style scoped>
.res { display: grid; grid-template-columns: 1fr 1fr; gap: 2.6em; font-size: 0.74em; line-height: 1.4; margin-top: 0.2em; }
.res ul { margin: 0; padding-left: 1.1em; }
.res li { margin: 0 0 0.6em; }
.res .d { display: block; color: var(--muted); font-size: 0.9em; }
.res .kicker { font-size: 0.95em; }
</style>

<div class="res">
<div>

<div class="kicker">Watch</div>

- [Features vs. Futures: Software Design in the Age of AI](https://www.youtube.com/watch?v=K7Z8Wa83Wgo)
  <span class="d">Kent Beck · ShipSummit, Rise8 · thumbnail title: "Do Unit Tests Still Matter?"</span>
- [TDD, AI agents and coding with Kent Beck](https://www.youtube.com/watch?v=aSXaxOdVtAQ)
  <span class="d">The Pragmatic Engineer podcast</span>
- [Genie Sessions: Can You Force a Genie to Do TDD?](https://www.youtube.com/watch?v=ouGJSC5SdRQ)
  <span class="d">Kent Beck, live coding with an agent</span>

<div class="kicker" style="margin-top:1.1em">The keynote</div>

- [The Augmented Forest, GOTO Copenhagen 2026](https://gotocph.com/2026/sessions/4170/the-augmented-forest)
  <span class="d">Also at SPLASH/ISSTA 2026 · <a href="https://doi.org/10.1145/3837729.3850163">doi.org/10.1145/3837729.3850163</a></span>

</div>
<div>

<div class="kicker">Read</div>

- [Forest &amp; Desert](https://newsletter.kentbeck.com/p/forest-and-desert)
  <span class="d">Beth Andres-Beck, guest post on Kent's newsletter, 2024</span>
- [Forest And Desert](https://martinfowler.com/bliki/ForestAndDesert.html)
  <span class="d">Martin Fowler's short summary of the metaphor</span>
- [Earn *And* Learn](https://newsletter.kentbeck.com/p/earn-and-learn)
  <span class="d">Kent Beck on features and futures</span>
- [Mathematicians, Here's a Way To Think About Your Existential Crisis](https://newsletter.kentbeck.com/p/mathematicians-heres-a-way-to-think)
  <span class="d">Kent Beck on visible and invisible work, 2026</span>
- [Kent Beck's genie posts](https://newsletter.kentbeck.com/t/genies)
  <span class="d">Including <em>Genie Tarpit</em> and <em>Taming the Genie</em></span>
- Books: <em>Extreme Programming Explained</em> (1999) · <em>Test-Driven Development: By Example</em> (2002) · <em>Tidy First?</em> (2023)

</div>
</div>

<!-- Say: Leave this slide up during questions. The links work in the HTML
     and PDF versions. -->
