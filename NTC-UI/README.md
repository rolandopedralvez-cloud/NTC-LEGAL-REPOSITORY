# NTC Legal Repository — UI (Tabler)

A working dashboard UI for browsing NTC Region VII laws, MCs, and orders — built on
[Tabler](https://github.com/tabler/tabler) (via CDN, no build step needed).

## What's here

- `index.html` — the whole app: sidebar navigation by category, search, document list,
  and detail view with clickable cross-references (e.g. click "EO 546" inside RA 7925's
  text and it jumps straight to that document).
- `data/documents.js` — the 3 pilot documents (RA 7925, EO 546, MC 04-89), structured as
  plain JS objects mirroring the schema in the legal repo (`schema/document-schema.json`).

## Run it locally

No build step — just serve the folder:

```bash
cd ntc-ui
python3 -m http.server 8000
```

Then open `http://localhost:8000` in a browser.

(Opening `index.html` directly by double-clicking also works in most browsers, but a local
server avoids any file:// path quirks.)

## How it connects to the legal repo

This UI reads from `data/documents.js`, not directly from the `.html` files in the legal
repo's `examples/html/` folder. That's intentional for now — it keeps the UI simple and
fast while the legal repo stays the canonical source of truth for the actual legal text
and metadata.

**As you convert more documents in the legal repo**, add a matching entry to
`data/documents.js` following the same shape: `id`, `title`, `category`, `status`,
`effective_date`, `tags`, `cross_references`, and `sections` (each with a `heading` and
`body`, plus an optional `refs` array if that section should auto-link to another
document's short title).

## Next steps for scaling this up

1. **Automate the sync**: write a small script that reads the metadata JSON comment block
   out of each `examples/html/*.html` file in the legal repo and regenerates
   `data/documents.js` automatically, so you're not hand-editing both.
2. **Move to real search**: once you have 50+ documents, swap the in-browser `.filter()`
   search for a proper index (Typesense, Elasticsearch, or even a lightweight client-side
   library like Lunr.js) — the current search is fine for a handful of docs but won't
   scale past a few hundred.
3. **Publish**: this static site can be hosted for free on GitHub Pages directly from this
   repo, or deployed anywhere that serves static files.
4. **Accessibility pass**: run this through the WCAG checklist in the legal repo's
   `docs/accessibility.md` before treating it as public-facing.
