# Nevaeh Coffee Company

Marketing site for Nevaeh Coffee Company — a mobile espresso bar serving weddings
and events across Central Florida.

**Live preview:** open `index.html` in any browser. No build step, no dependencies,
no server required.

## Structure

Six sections: hero, what we do (event types), the bar (drinks and how it works),
where we travel (Central Florida map with a 90-mile radius), FAQ, and the inquiry
form.

## What's here

| File | What it is |
| --- | --- |
| `index.html` | The entire site — markup, styles, and scripts in one file |
| `Nevaeh (1).png` | The original logo artwork |

`index.html` is fully self-contained. The typeface (Archivo) is embedded as a
base64 `@font-face` source, and the logo is an inline SVG path traced from the
PNG, so the page renders identically offline and on any host. Nothing is fetched
from a CDN.

## Deploying

Any static host works, since the whole site is one file:

- **GitHub Pages** — Settings → Pages → deploy from `main`, root folder
- **Netlify / Vercel** — drag the folder in, or connect this repo; no build command
- **Any web host** — upload `index.html` as the site root

## Before going live

Three things still need real values.

**1. The inquiry form needs a Formspree form ID.** This is a one-line change.

1. Sign up at [formspree.io](https://formspree.io) — the free plan covers 50
   submissions a month, which is plenty for event inquiries
2. Create a form; Formspree gives you an ID that looks like `xbjnvqwe`
3. In `index.html`, find the `<form>` tag and swap the placeholder into the
   action:

```html
<form class="form" id="inqForm" novalidate
      action="https://formspree.io/f/xbjnvqwe" method="POST">
```

That's the only edit. Formspree will email you the first time a submission
comes in, to confirm the address.

The form posts over `fetch` so the visitor stays on the page and sees the
confirmation panel rather than being bounced to Formspree. Two hidden fields do
work behind the scenes: `_subject` sets the email subject to
`Coffee bar inquiry — {name} — {date}` so inquiries are scannable in an inbox,
and `_gotcha` is a spam trap that bots fill in and people never see.

Until a real ID is in place — and if a send ever fails — the form still
validates, shows the visitor their details, and offers a pre-filled email link.
It never tells anyone their inquiry was sent when it wasn't.

**2. Contact details are placeholders.** Search `index.html` and replace:

- `wearenevaehco@gmail.com`
- `(407) 555-0134` — currently a reserved fictional number, not a working line

**3. There is no pricing on the site**, by design — you don't have rates set yet.
The FAQ and the inquiry section both say every event is quoted individually. When
you're ready to publish rates, that's the place to change the wording.

## Design notes

Type is one family in two roles: Archivo, a variable grotesk covering 400–700.
Display text (the wordmark, headings, the facts strip) runs at 600 with tight
negative tracking; body copy is 400. Both roles read from their own token
(`--f-display`, `--f-body`, aliased to `--f-sans`) so either can move
independently, and `--display-tracking` holds the heading letter-spacing.

The palette is built from the two colors in the logo: the cream `#F1F3E8` and the
camel `#CBA98A`. The camel is darkened to `#8C6035` for text and buttons on cream
so it stays legible; at full strength it's used on the dark bands.

The hero art is a canvas field, not a photograph: value noise, twisted around a
point off to the right and folded back on itself so it draws thin bright veins,
which reads as milk turning into a shot. It renders into a buffer about a
seventh of the page width and scales up under a CSS blur, so the per-pixel cost
stays small; the polar table it samples through is rebuilt only on resize.

Two scrims sit over it — a column that keeps the copy off the veins, and the
fade down into the facts strip. Those are measured rather than guessed: sampling
the composited backdrop under the real glyph rects across frames, the headline
holds 11:1, the body copy 6.4:1 and the eyebrow 8:1 on desktop, with the tightest
case (tablet body copy) at 4.8:1. Below 900px the copy runs full width, so there
is no side to push the pour to and it is damped everywhere instead.

The dark sections (hero, service-area map, inquiry form) are a fixed register
rather than a theme inversion — the brand run in reverse, cream and camel on
espresso. The page also supports the visitor's light/dark preference: all colors
are CSS custom properties defined on `:root`, redefined under
`prefers-color-scheme: dark` and `[data-theme="dark"]`.

## Motion

Everything moves through one small system, and all of it is optional.

Blocks marked `data-reveal` start faded and offset and settle into place when
they scroll in; a container marked `data-stagger` hands each child a `--i` so
its rows arrive in sequence. The hidden start states only exist under `html.js`,
a class added by an inline script in the head that first checks for
`IntersectionObserver` — so with scripts off, blocked, or too old, the page
renders fully visible rather than blank. Reveal observers fire on any
intersection rather than a percentage, since an element taller than the viewport
can never expose a fixed fraction of itself.

Other pieces: the header carries a scroll-progress hairline and highlights the
nav link for the section you're in; the coastline draws itself and the 90-mile
radius opens around Orlando before the pins land; FAQ answers animate open and
shut (`<details>` can't transition, so the answer sits in a wrapper the script
animates, and the close is deferred until it finishes collapsing); the
confirmation panel and its recap rows fade in.

Under `prefers-reduced-motion: reduce` every reveal resolves to its finished
state, the looping animations stop, the FAQ falls back to the browser's own
instant toggle, and the hero canvas paints one static frame. The progress
hairline stays — it reports position rather than decorating. Transitions stick
to `opacity` and `transform` so they run on the compositor, the hero canvas
stops drawing whenever it scrolls off screen, and the scroll handler paints at
most once a frame.

The Central Florida map is hand-plotted SVG. Coastline points come from real
longitude/latitude converted with `x = (lon + 87.7) / 7.8 * 620` and
`y = (31.1 - lat) / 6.7 * 560`; the dashed ellipse is a 90-mile radius around
Orlando.

## Not built yet

Testimonials and a photo gallery were deliberately left out — both need real
content. A gallery of actual bar setups is likely the highest-value addition for
booking weddings.
