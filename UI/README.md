# NTC Legal Repository — UI (Tabler)

A working dashboard UI for browsing NTC Region VII laws, MCs, and orders — built on
[Tabler](https://github.com/tabler/tabler) (via CDN, no build step needed).

## What's here

- `index.html` — the whole app: sidebar navigation by category, search with highlighting,
  document list, detail view with clickable cross-references, a **Case Binder** for pinning
  documents to a matter, and a **Print / Save PDF** view with formal citation formatting.
- `data/documents.js` — 28 converted documents from NTC Region VII, structured as plain JS
  objects mirroring the schema in the legal repo (`schema/document-schema.json`).

## Features

**Category navigation** — the sidebar mirrors the actual structure of
region7.ntc.gov.ph/laws-rules-and-regulations/: top-level Republic Acts, Presidential
Decrees, Department Orders, and Executive Orders, plus a collapsible Memorandum Circulars
group with the same lettered A–O sub-categories used on the real site (Aeronautical,
Amateur, Broadcast, Cellular Mobile, CPE, Civic Group, Fixed and Land Mobile, Low Power
Equipment, Maritime, Radio Communication Dealers, ROC, Radio Training Center, Telecom,
Value Added, Wireless Data Network). Each entry shows a document count; categories with no
converted documents yet appear greyed out rather than being hidden, so the full scope of
the source site stays visible even before every category has content.

**Search** — filters titles, tags, and section text as you type; matching terms are
highlighted inline in both the list and detail views.

**Full document view** — every section, cross-references rendered as live links, a
"Referenced By" reverse-lookup, and status badges (Active/Amended/Repealed). A
**Summary / Full Original Text toggle** lets you switch between the paraphrased section
view and the verbatim original wording as issued by NTC — the print button prints whichever
view is active. Documents without verbatim text yet fall back to the summary with a clear
notice, rather than silently showing paraphrased content as if it were the original.

**Print / PDF view** — the "Print / Save PDF" button on any document strips all navigation
chrome via a dedicated print stylesheet and appends a formal citation line (title, date,
retrieval date) at the bottom — use your browser's "Save as PDF" print destination to export.
When "Full Original Text" mode is active, this prints the verbatim text, matching what a case
file would need.

**Case Binder** — click the folder icon on any document card (or the "Add to Binder" button
in detail view) to pin it to a working case file. The binder persists in the browser
(`localStorage`) across sessions. Open the binder from the sidebar to see all pinned
documents in one place, each with its section text and citation, ready to print as a single
combined packet for a case or matter.

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
`effective_date`, `tags`, `cross_references`, `sections` (each with a `heading` and
`body`, plus an optional `refs` array if that section should auto-link to another
document's short title), and optionally `fullText` — the verbatim original text of the
document as issued, used by the "Full Original Text" toggle. As of now, `fullText` is
populated for 2 of 30 documents (MC 04-89, MC 06-04-99) as a proof of concept; the rest
still fall back to the summary view. Since these are official Philippine government
issuances, they are public domain under Philippine IP law, so reproducing them in full is
not a copyright concern — the remaining gap is purely a matter of backfilling the fetches.

## Next steps for scaling this up

1. **Automate the sync**: write a small script that reads the metadata JSON comment block
   out of each `examples/html/*.html` file in the legal repo and regenerates
   `data/documents.js` automatically, so you're not hand-editing both.
2. **Move to real search**: once you have 50+ documents, swap the in-browser `.filter()`
   search for a proper index (Typesense, Elasticsearch, or even a lightweight client-side
   library like Lunr.js) — the current search is fine for a handful of docs but won't
   scale past a few hundred.
3. **Case Binder upgrades**: name/save multiple binders (one per matter), add private notes
   per document, export the whole binder as a single merged PDF rather than relying on
   browser print, and — if this becomes a shared team tool — move binder storage from
   `localStorage` (per-browser only) to the `window.storage` API so binders sync across
   devices and users.
4. **Publish**: this static site can be hosted for free on GitHub Pages directly from this
   repo, or deployed anywhere that serves static files.
5. **Accessibility pass**: run this through the WCAG checklist in the legal repo's
   `docs/accessibility.md` before treating it as public-facing.

