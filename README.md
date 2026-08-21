# NTC Legal Repository — Design & Data Model

A structured, accessible, searchable repository for NTC's Municipal Codes (MC), laws, ordinances, and related governance documents.

## Goal

Convert mixed-format legal documents (Word, PDF, scanned, database exports) into a **single normalized HTML data model** so that:

1. The public can browse/search laws on an accessible website (WCAG-compliant).
2. Internal staff can query, cross-reference, and govern using the same structured source of truth.
3. Cross-references between sections ("see Sec. 3.12") become real, clickable, machine-readable links.
4. The corpus is clean enough to power search indexing and AI-assisted query tools later.

## Repo Structure

```
ntc-legal-repo/
├── README.md                  # This file
├── docs/
│   ├── design.md               # Full architecture & design doc
│   ├── conversion-workflow.md  # How to convert source docs → HTML model
│   └── accessibility.md        # WCAG checklist for public site
├── schema/
│   └── document-schema.json    # Metadata schema for each law/MC section
├── examples/
│   ├── source/                 # Sample raw inputs (what you start with)
│   └── html/                   # Sample converted structured HTML
└── scripts/
    └── validate.py             # Checks HTML files against schema conventions
```

## Quick Start

1. Read `docs/design.md` for the full architecture.
2. Look at `examples/source/` vs `examples/html/` to see a before/after conversion.
3. Use `schema/document-schema.json` as the metadata contract every document must follow.
4. Run `scripts/validate.py` against your converted files to catch missing IDs, broken cross-refs, etc.

## Status

This is a design-stage repository. It now includes a **real pilot batch of 3 converted documents** from
NTC Region VII (region7.ntc.gov.ph), pulled from their public Laws, Rules and Regulations page:

- `examples/html/ra-7925.html` — Republic Act 7925, Public Telecommunications Policy Act
- `examples/html/eo-546.html` — Executive Order 546, creating the NTC
- `examples/html/mc-04-89.html` — Memorandum Circular 04-89, Sanctions for Violations

All three pass `scripts/validate.py` with 0 errors. This proves the conversion pipeline on real,
messy source PDFs (including one with heavy OCR artifacts in other MCs on the same site).

Next steps: pull more documents from the same index page (region7.ntc.gov.ph/information/laws-rules-and-regulations/),
convert at scale, and stand up the search/query layer described in `docs/design.md`.
