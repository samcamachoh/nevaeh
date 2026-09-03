from pathlib import Path

p = Path("index.html")
s = p.read_text()

old = '  var reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;'
new = '  var reduceQuery = window.matchMedia("(prefers-reduced-motion: reduce)");\n  function reducedMotion(){ return reduceQuery.matches; }'
assert old in s, "reduced-motion declaration not found"
s = s.replace(old, new, 1)

old_map = '''    /* Below 1200px the full-state viewBox shrinks the town labels out of
       legibility, so the map is reframed onto the service area instead of
       being stripped of them. Same footprint, sixteen towns named. */
    var mapEl = document.querySelector(".map");
    if (mapEl && window.matchMedia) {
      var wide = window.matchMedia("(min-width:1201px)");
      var frameMap = function(){
        var zoom = !wide.matches;
        mapEl.classList.toggle("is-zoomed", zoom);
        mapEl.setAttribute("viewBox", zoom ? "354 91 294 270" : "0 0 640 570");
      };
      frameMap();
      if (wide.addEventListener) wide.addEventListener("change", frameMap);
      else if (wide.addListener) wide.addListener(frameMap);
    }

'''
assert old_map in s, "responsive map block not found"
s = s.replace(old_map, "", 1)

marker = '''  /* ── Reveal on scroll ─────────────────────────────────────────────
     Containers marked data-stagger hand their children a --i so they
     arrive in sequence. data-live elements keep being observed, so a
     looping animation can be switched off once it scrolls away.     */
'''
new_map = '''  /* Responsive map framing is layout behavior and must not depend on
     IntersectionObserver support. */
  var mapEl = document.querySelector(".map");
  if (mapEl && window.matchMedia) {
    var wide = window.matchMedia("(min-width:1201px)");
    var frameMap = function(){
      var zoom = !wide.matches;
      mapEl.classList.toggle("is-zoomed", zoom);
      mapEl.setAttribute("viewBox", zoom ? "354 91 294 270" : "0 0 640 570");
    };
    frameMap();
    if (wide.addEventListener) wide.addEventListener("change", frameMap);
    else if (wide.addListener) wide.addListener(frameMap);
  }

'''
assert marker in s, "reveal marker not found"
s = s.replace(marker, new_map + marker, 1)

old_faq = '''    var running = null;

    summary.addEventListener("click", function(e){
      if (reduce) return;                  // let the browser just toggle it
      e.preventDefault();
      if (running) running.cancel();

      if (!item.open) {
        item.open = true;                  // render it, then grow into place
        running = wrap.animate(
          [{height:"0px", opacity:0}, {height:wrap.scrollHeight + "px", opacity:1}],
          {duration:320, easing:"cubic-bezier(.16,.72,.24,1)"});
        running.onfinish = function(){ running = null; };
      } else {
        running = wrap.animate(
          [{height:wrap.scrollHeight + "px", opacity:1}, {height:"0px", opacity:0}],
          {duration:250, easing:"cubic-bezier(.16,.72,.24,1)"});
        running.onfinish = function(){ item.open = false; running = null; };
      }
    });'''
new_faq = '''    var running = null;
    var desiredOpen = item.open;

    summary.addEventListener("click", function(e){
      if (reducedMotion()) return;         // let the browser just toggle it
      e.preventDefault();
      desiredOpen = !desiredOpen;
      if (running) running.cancel();

      if (desiredOpen) {
        item.open = true;                  // render it, then grow into place
        running = wrap.animate(
          [{height:"0px", opacity:0}, {height:wrap.scrollHeight + "px", opacity:1}],
          {duration:320, easing:"cubic-bezier(.16,.72,.24,1)"});
        running.onfinish = function(){ running = null; };
      } else {
        running = wrap.animate(
          [{height:wrap.scrollHeight + "px", opacity:1}, {height:"0px", opacity:0}],
          {duration:250, easing:"cubic-bezier(.16,.72,.24,1)"});
        running.onfinish = function(){
          if (!desiredOpen) item.open = false;
          running = null;
        };
      }
    });'''
assert old_faq in s, "FAQ animation block not found"
s = s.replace(old_faq, new_faq, 1)

old = '    function play(){ if (!raf && !reduce) raf = requestAnimationFrame(tick); }'
new = '    function play(){ if (!raf && !reducedMotion()) raf = requestAnimationFrame(tick); }'
assert old in s, "canvas play guard not found"
s = s.replace(old, new, 1)

old = '      if (reduce) draw(0); else play();'
new = '      if (reducedMotion()) draw(0); else play();'
assert old in s, "canvas start guard not found"
s = s.replace(old, new, 1)

old = '        if (reduce) return;'
new = '        if (reducedMotion()) return;'
assert old in s, "canvas observer guard not found"
s = s.replace(old, new, 1)

old = '''    start();

    /* The hero grows when the webfont swaps in or the viewport changes, and'''
new = '''    start();

    var onMotionChange = function(){
      stop();
      if (reducedMotion()) draw(0); else play();
    };
    if (reduceQuery.addEventListener) reduceQuery.addEventListener("change", onMotionChange);
    else if (reduceQuery.addListener) reduceQuery.addListener(onMotionChange);

    /* The hero grows when the webfont swaps in or the viewport changes, and'''
assert old in s, "canvas start marker not found"
s = s.replace(old, new, 1)
p.write_text(s)

r = Path("README.md")
t = r.read_text()
old_doc = '''`index.html` is fully self-contained. The typeface (Archivo) is embedded as a
base64 `@font-face` source, and the logo is an inline SVG path traced from the
PNG, so the page renders identically offline and on any host. Nothing is fetched
from a CDN.'''
new_doc = '''The site's own assets are self-contained in `index.html`. The typeface (Archivo)
is embedded as a base64 `@font-face` source, and the logo is an inline SVG path
traced from the PNG, so the page shell renders identically offline and on any
host. The inquiry form is the exception: its Typeform loader is fetched from
`embed.typeform.com` and requires a network connection.'''
assert old_doc in t, "README paragraph not found"
r.write_text(t.replace(old_doc, new_doc, 1))

Path(".github/scripts/apply_review_fixes.py").unlink()
