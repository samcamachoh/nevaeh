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

- `hello@nevaehcoffee.com`
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

The dark sections (hero, service-area map, inquiry form) are a fixed register
rather than a theme inversion — the brand run in reverse, cream and camel on
espresso. The page also supports the visitor's light/dark preference: all colors
are CSS custom properties defined on `:root`, redefined under
`prefers-color-scheme: dark` and `[data-theme="dark"]`.

The Central Florida map is hand-plotted SVG. Coastline points come from real
longitude/latitude converted with `x = (lon + 87.7) / 7.8 * 620` and
`y = (31.1 - lat) / 6.7 * 560`; the dashed ellipse is a 90-mile radius around
Orlando.

## Not built yet

Testimonials and a photo gallery were deliberately left out — both need real
content. A gallery of actual bar setups is likely the highest-value addition for
booking weddings.
