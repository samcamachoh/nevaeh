# Nevaeh Coffee Company

Marketing site for Nevaeh Coffee Company — a mobile espresso bar serving weddings
and events across Central Florida.

**Live preview:** open `index.html` in any browser. No build step, no dependencies,
no server required.

## Structure

Six sections: hero, what we do (event types), the bar (drinks and how it works),
where we travel (Central Florida map with a 90-mile radius), FAQ, and the inquiry
section, which is a short section head over the Typeform embed. A menu ticker
runs between the event types and the bar.

## What's here

| File | What it is |
| --- | --- |
| `index.html` | The entire site — markup, styles, and scripts in one file |
| `Nevaeh (1).png` | The original logo artwork |
| `og-image.png` | 1200×630 social share card, generated from the logo and the embedded typeface |
| `apple-touch-icon.png` | 180×180 home-screen icon |
| `robots.txt` | Crawler rules; points at the sitemap |
| `sitemap.xml` | One URL, since there is one page |
| `CNAME` | Tells GitHub Pages to serve the site at `nevaeh-coffee.com` |

The site's own assets are self-contained in `index.html`. The typeface (Archivo)
is embedded as a base64 `@font-face` source, and the logo is an inline SVG path
traced from the PNG, so the page shell renders identically offline and on any
host. The inquiry form is the exception: its Typeform loader is fetched from
`embed.typeform.com` and requires a network connection.

## Deploying

Any static host works, since the whole site is one file:

- **GitHub Pages** — Settings → Pages → deploy from `main`, root folder. The
  `CNAME` file already claims `nevaeh-coffee.com`, so point that domain's DNS at
  GitHub (an `ALIAS`/`ANAME` on the apex to `samcamachoh.github.io`, or four `A`
  records to GitHub's Pages IPs) and tick **Enforce HTTPS** once the certificate
  issues.
- **Netlify / Vercel** — drag the folder in, or connect this repo; no build command
- **Any web host** — upload `index.html` as the site root

## Before going live

Three things still need real values.

**1. The inquiry form is a Typeform embed** (`01M08MGAQNE8WCJ1ZZADV67VXS`),
rendered by the loader script at the end of `index.html`. Responses go to the
Typeform account that owns the form — not to this repo and not to email unless
Typeform notifications are switched on there.

To change the questions, edit the form in Typeform; the site needs no change.
To swap in a different form, replace the ID in the `data-tf-live` attribute.

Note that the embed loads a third-party script, so the form only appears when
the page is served over http/https with a network connection. Opening
`index.html` straight off disk still renders the whole site, but that panel
stays empty.

**2. There is no phone number on the site.** Contact runs through the Typeform
and the email address in the footer. If you want a phone line listed, add it to
the footer's "Get in touch" column and, optionally, back into the inquiry
section.

**3. There is no pricing on the site**, by design — you don't have rates set yet.
The FAQ and the inquiry section both say every event is quoted individually. When
you're ready to publish rates, that's the place to change the wording.

## SEO

The site is one page targeting one job: people in Central Florida searching for a
mobile coffee or espresso bar for a wedding or event.

**Canonical host is `https://nevaeh-coffee.com`.** It is hard-coded in the
`<head>`, in `robots.txt`, in `sitemap.xml`, and throughout the JSON-LD. If the
domain ever changes, find-and-replace that string across those four files and
nothing else needs touching.

### What's in the page

- **Title and description** lead with the search terms rather than the brand —
  "Mobile Espresso Bar for Weddings & Events | Orlando, FL" (55 characters) over a
  147-character description. Both sit under the length where Google truncates.
- **Canonical link and a `robots` directive** that opts into large image previews
  and full-length snippets.
- **Open Graph and Twitter cards** with a real 1200×630 image, so a link pasted
  into a text, a Facebook group, or a planner's email renders as a card instead of
  a bare URL. Wedding referrals travel by link, so this is worth more here than it
  looks.
- **`geo.*` meta and coordinates** for the Orlando home base.
- **JSON-LD** in a single `@graph`, described below.
- **A section head on the inquiry band.** It used to be the bare Typeform, which
  meant the page's main conversion point was an iframe — no heading, no indexable
  copy, and nothing at all for a visitor without JavaScript. It now has an `h2`,
  a paragraph restating how quoting works, and a `<noscript>` fallback pointing at
  the email address.
- **`preconnect` to `embed.typeform.com`** and `defer` on its loader, so the
  third-party script costs less on first paint.

### Structured data

One `<script type="application/ld+json">` before `</head>` holding three linked
nodes:

| Node | What it does |
| --- | --- |
| `LocalBusiness` + `FoodEstablishment` | The business itself: name, email, founding year, logo, price range, the drink menu, and the six event types as an `OfferCatalog` |
| `WebSite` | Names the site, so Google can show "Nevaeh Coffee Company" as the site name in results |
| `WebPage` + `FAQPage` | The four FAQ entries, eligible for expandable results |

Two details worth knowing before editing it:

- **The FAQ and service entries are generated from the visible markup**, so the
  schema cannot drift from what a visitor reads. If you reword a FAQ answer in
  the HTML, reword it identically in the JSON-LD — Google treats a mismatch
  between schema and visible copy as a violation and will drop the rich result.
- **There is no street address, and that is correct.** A mobile business with no
  storefront declares locality and region only; the coverage is expressed as a
  `GeoCircle` with a 144,841-metre (90-mile) radius around Orlando, plus the
  sixteen towns named on the page.

### Deliberately left out

These would all be schema violations or fabrications as things stand, so they are
absent rather than guessed at:

- **`openingHoursSpecification`** — you book by date, not by walk-in hours. If you
  want to publish availability (say, "Saturdays, 6am–11pm"), add it to the
  `LocalBusiness` node and to the page copy at the same time.
- **`aggregateRating` / `review`** — self-declared review markup with no real
  reviews behind it is a manual-action risk. Once you have reviews on Google, they
  surface through the Business Profile anyway; do not hand-write them here.
- **`telephone`** — there is no phone number on the site. Add it to both the
  footer and the `LocalBusiness` node together if that changes.
- **`sameAs`** — fill this array with your Instagram, Facebook, and Google
  Business Profile URLs once they exist. It is how Google confirms that the site,
  the profile, and the social accounts are the same business, and it is probably
  the single highest-value line you can add to the schema.

### Off the site

For a local service business, the page is maybe a third of the work. The rest:

1. **Claim the Google Business Profile.** For a service-area business, set it to
   hide the address and declare the service area instead. This is the largest
   single ranking factor for "mobile coffee bar near me" style searches, and it
   feeds the map pack, which sits above the organic results.
2. **Keep NAP identical everywhere.** Name, address, phone — byte-for-byte the
   same string on the site, the Business Profile, and every directory. "Nevaeh
   Coffee Company", Orlando, FL. Inconsistency is the most common reason local
   rankings stall.
3. **Verify in Google Search Console**, submit `sitemap.xml`, and check the
   Rich Results Test for the FAQ markup.
4. **Get listed where planners actually look** — The Knot, WeddingWire, Zola,
   and the venue vendor lists for the places you already work. Venue backlinks
   are the most valuable ones available to a wedding vendor, and they are usually
   free for the asking once you have poured there.
5. **Ask for Google reviews after every event.** Volume and recency both count.
6. **Add photos.** A gallery of real setups is still the highest-value addition to
   this site, for booking and for search alike — image results and the Business
   Profile both reward it.

## Mobile

Most visitors arrive on a phone, so the phone layout is the one that gets
measured. Two things differ from the desktop page rather than just reflowing
into it.

Nothing floats over the page. A sticky booking bar was tried and removed — on a
page this length the routes to the form are the hero button, the nav, and the
footer link.

**The service-area map is reframed, not shrunk.** The full-state viewBox scales
the town labels to roughly half their stated size — 13px type lands at about
7px — so below 1200px they used to be hidden, leaving an unlabelled blob of
dots. Below that width the script now swaps the viewBox to `354 91 294 270`,
cropping to the service area itself: same footprint, all nine places named, and
the 90-mile circle filling the frame. The whole state is context a phone has no
room for; the circle is the part that answers "do you come to my venue?".
Without JavaScript the full map renders with labels hidden, as before.

**The event grid changes shape twice.** Three columns above 760px, two below,
and one below 360px — where two columns leave about 110px for text, which is
three words to a line with breaks mid-word. Single column costs 78px of height
there and is worth it; above 360px the columns hold enough that two-up is the
better trade, since narrow columns wrap more and the saving is real (measured at
145–210px).

Smaller corrections, each a measured problem rather than a guess: horizontal
reveals become vertical below 900px (a 30px offset is wider than the 20px gutter
a phone has to spare, and the page panned sideways until they settled); the
uppercase micro-labels come up from 10px; the facts strip tightens; and the hero
eyebrow's separators move from trailing to leading so a wrap does not leave one
dangling at the end of the line.

Tap targets were already at or above 44px and stayed there. The layout is clean
of horizontal overflow from 320px up.

## Design notes

Type is one family in two roles: Archivo, a variable grotesk covering 400–700.
Display text (the wordmark, headings, the facts strip) runs at 600 with tight
negative tracking; body copy is 400. Both roles read from their own token
(`--f-display`, `--f-body`, aliased to `--f-sans`) so either can move
independently, and `--display-tracking` holds the heading letter-spacing.

The palette is built from the two colors in the logo: the cream `#F1F3E8` and the
camel `#CBA98A`. The camel is darkened to `#8C6035` for text and buttons on cream
so it stays legible; at full strength it's used on the dark bands and on the menu
ticker, which is the one place it carries a whole band as a ground
(`--camel-band`, fixed in both themes like the nocturne sections). Espresso on
camel there holds 8.3:1.

Four things keep the page from reading as flat type on flat fills:

- **Grain.** One 140px noise tile, fixed over the whole page at 5% via
  `body::after`. Cream reads as paper rather than a blank fill, and the espresso
  bands pick up a film cast. No blend mode, one composited layer.
- **Warm light.** Each cream band carries a radial `--accent-wash` bloom off one
  top corner, the same light the hero pour throws.
- **The ticker.** Two identical sets of drink names side by side in a
  `width: max-content` row; the row travels exactly `-50%`, so the loop has no
  seam. Masked at both edges, paused on hover, stopped under reduced motion. It
  duplicates the chip lists below, so it is `aria-hidden`.
- **Index numerals.** The event cells number themselves with a CSS counter —
  `counter(offer, decimal-leading-zero)` on `::after`, no markup — set large and
  low-contrast behind the copy, and scaled with `clamp` so they do not swamp the
  two-up column on a phone.

Section heads set the heading against its copy in two columns above 900px, which
is what fills the measure on a wide screen; `:has(p)` keeps the FAQ head, which
has no paragraph, out of it.

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
Orlando. Below 1200px the script reframes it onto the service area — see
**Mobile** above.

## Not built yet

Testimonials and a photo gallery were deliberately left out — both need real
content. A gallery of actual bar setups is likely the highest-value addition for
booking weddings.
