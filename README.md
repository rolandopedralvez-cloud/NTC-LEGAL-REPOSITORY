# NTC Legal Repository — NTC Region VII (Central Visayas)

A structured, accessible, searchable repository of National Telecommunications Commission (NTC)
laws, Memorandum Circulars, and related issuances, sourced from
[region7.ntc.gov.ph/laws-rules-and-regulations](https://region7.ntc.gov.ph/laws-rules-and-regulations/).

**Status: 32 of 50 target documents converted.**

## Repo structure

```
NTC-LEGAL-REPOSITORY/
├── README.md                  # this file
├── docs/
│   ├── design.md               # architecture & design doc
│   ├── conversion-workflow.md  # source document → structured HTML pipeline
│   └── accessibility.md        # WCAG checklist
├── schema/
│   └── document-schema.json    # metadata contract every document follows
├── scripts/
│   └── validate.py             # checks examples/html/ for missing IDs, broken cross-refs
├── examples/
│   ├── html/                   # the 32 converted documents (source of truth)
│   └── source/                 # notes on documents that still need OCR or sourcing
└── ui/
    ├── index.html               # Tabler-based browsing dashboard
    ├── README.md                 # UI-specific documentation
    └── data/documents.js         # UI's data layer, mirrors examples/html/ content
```

## What's converted (32 documents)

- **Foundational laws**: act-3846 (Act 3846), eo-546 (Executive Order 546), ra-7925 (Republic Act 7925)
- **Memorandum Circulars (29)**: mc-02-01-97, mc-02-02-2005, mc-02-03-87, mc-04-89,
  mc-05-06-2007, mc-05-08-2018, mc-05-09-2001, mc-06-04-99, mc-07-08-2016, mc-07-08-85,
  mc-08-08-2004, mc-09-07-2007, mc-09-4-94, mc-1-04-88, mc-10-07-2007, mc-10-10-2003,
  mc-10-12-95, mc-11-11-2007, mc-11-12-2001, mc-11-21-88, mc-12-08-92, mc-13-09-2004,
  mc-14-09-92, mc-14-89, mc-16-11-2004, mc-17-2-2002, mc-19-12-2000, mc-7-6-98, mc-87-174

Each document lives as one canonical HTML file in `examples/html/`, with a JSON metadata
comment block matching `schema/document-schema.json` (id, title, type, status, effective
date, amendment history, cross-references, tags, jurisdiction).

**Verbatim full text** (the original wording as issued, not a paraphrase) has been
backfilled for 3 of the 32 documents so far: MC 04-89, MC 06-04-99, MC 10-07-2007. The
remaining 29 have structured summary sections only; the "Full Original Text" toggle in the
UI falls back to the summary with a clear notice when verbatim text isn't available yet.

Two source documents are flagged as scanned/non-machine-readable and are not yet
convertible without OCR review — see `examples/source/*-needs-ocr.txt`.

## How the pieces fit together

`examples/html/` is the canonical source of truth — one structured HTML file per document,
validated against `schema/document-schema.json`. The `ui/` folder is a separate, working
dashboard (Tabler-based) that reads from `ui/data/documents.js`, a plain-JS mirror of the
same documents, kept in sync by hand for now (see `ui/README.md` for the sync note and the
full UI feature list — search, category sidebar, Case Binder, Print/PDF view, Summary/Full
Text toggle).

## Adding a new document

1. Find the real document on region7.ntc.gov.ph and fetch the actual source PDF — never
   fabricate content. If it's scanned/non-machine-readable, flag it in
   `examples/source/[id]-needs-ocr.txt` and skip conversion.
2. Follow `docs/conversion-workflow.md` to convert it into the same HTML structure used by
   existing files in `examples/html/` (match an existing file's metadata block pattern).
3. Run `python3 scripts/validate.py` — must show 0 errors.
4. Add a matching entry to `ui/data/documents.js` with the same `id`.
5. Update this README's document list and counts, and confirm the doc IDs listed here match
   the actual files in `examples/html/` exactly.

## Next steps

1. Continue converting documents toward the 50-document target (18 remaining).
2. Continue backfilling verbatim `fullText` for already-converted documents.
3. Automate the sync between `examples/html/*.html` and `ui/data/documents.js` (currently
   hand-maintained) so the two never drift.
4. Run the WCAG checklist in `docs/accessibility.md` before treating the UI as public-facing.
