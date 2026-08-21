# Accessibility Checklist (WCAG 2.1 AA target)

Public-facing legal content must be accessible. This is not optional for a government site.

## Structure
- [ ] Real heading hierarchy (`<h1>` → `<h2>` → `<h3>`), never skipped levels
- [ ] Semantic HTML elements (`<nav>`, `<main>`, `<article>`, `<section>`) — not `<div>` soup
- [ ] Lists use `<ul>`/`<ol>`, not manually typed dashes/numbers
- [ ] Tables use `<th>` with `scope` attributes for headers

## Navigation
- [ ] Fully keyboard-navigable (tab order logical, no keyboard traps)
- [ ] Skip-to-content link at top of page
- [ ] Visible focus indicators on all interactive elements

## Content
- [ ] Alt text on every image, map, and embedded chart
- [ ] Descriptive link text (never "click here")
- [ ] Sufficient color contrast (4.5:1 minimum for normal text)
- [ ] No content conveyed by color alone (e.g. "repealed" shown in red text should also say "Repealed" in words)

## Documents
- [ ] HTML is the primary/canonical format
- [ ] PDF offered only as a secondary download, and must itself be tagged/accessible (not a flat scanned image)
- [ ] Scanned historical documents get OCR + alt text describing the scan, plus a note that OCR text may contain errors

## Testing
- [ ] Test with an actual screen reader (VoiceOver, NVDA, or JAWS), not just automated checkers
- [ ] Run automated scan (axe, WAVE, or Lighthouse) as a baseline, not a final check
- [ ] Test keyboard-only navigation manually
