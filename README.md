# Nevaeh Coffee Company

Marketing site for Nevaeh Coffee Company — a mobile espresso bar serving weddings
and events across Central Florida.

**Live preview:** open `index.html` in any browser. No build step, no dependencies,
no server required.

## What's here

| File | What it is |
| --- | --- |
| `index.html` | The entire site — markup, styles, and scripts in one file |
| `Nevaeh (1).png` | The original logo artwork |

`index.html` is fully self-contained. The two typefaces (Instrument Serif and
Archivo) are embedded as base64 `@font-face` sources, and the logo is an inline
SVG path traced from the PNG, so the page renders identically offline and on any
host. Nothing is fetched from a CDN.

## Deploying

Any static host works, since the whole site is one file:

- **GitHub Pages** — Settings → Pages → deploy from `main`, root folder
- **Netlify / Vercel** — drag the folder in, or connect this repo; no build command
- **Any web host** — upload `index.html` as the site root

## Before going live

Three things still need real values.

**1. The inquiry form doesn't deliver anywhere yet.** A static page can't receive
submissions on its own. Right now the form validates, shows the visitor a recap of
what they entered, and offers a pre-filled email link. To have submissions arrive
in an inbox, point the form at a form service — look for the comment block above
`<form class="form" id="inqForm">` in `index.html`:

```html
<form action="https://formspree.io/f/YOUR_ID" method="POST">
```

Then remove the `e.preventDefault()` branch in the submit handler near the bottom
of the file.

**2. Contact details are placeholders.** Search `index.html` and replace:

- `hello@nevaehcoffee.com`
- `(407) 555-0134` — currently a reserved fictional number, not a working line

**3. Package pricing is illustrative.** The three tiers ($650 / $1,150 / $1,800),
their guest counts, hours, and inclusions were written to demonstrate the layout.
Replace them with real numbers in the `<section class="band pkgs">` block.

## Design notes

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
