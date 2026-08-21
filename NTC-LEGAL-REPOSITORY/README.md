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

This is a design-stage repository. It now includes a **real pilot batch of 22 converted documents** from
NTC Region VII (region7.ntc.gov.ph):

- `ra-7925.html` — Republic Act 7925, Public Telecommunications Policy Act
- `eo-546.html` — Executive Order 546, creating the NTC
- `mc-04-89.html` — Sanctions for Violations (General Services)
- `mc-87-174.html` — Revised Amateur Radio Regulations (Amateur Services)
- `mc-14-09-92.html` — TVRO Station Registration and Licensing (Broadcast Services)
- `mc-05-06-2007.html` — Consumer Protection Guidelines (Telecom Services)
- `mc-06-04-99.html` — GMDSS Radio Personnel Qualifications (Maritime Services)
- `mc-10-12-95.html` — RLM Seminar Guidelines (Fixed and Land Mobile Services)
- `mc-1-04-88.html` — CPE Rules and Regulations (CPE Services)
- `mc-13-09-2004.html` — Modified Admin Fee for VAS (Value Added Services)
- `mc-17-2-2002.html` — Radio Training Center GMDSS Course Rules (Radio Training Center)
- `mc-11-21-88.html` — Personal Radio Service Rules (Civic Group Services)
- `mc-02-01-97.html` — Short Range Radio Service Licensing (Low Power Equipment)
- `mc-12-08-92.html` — Civic Action Radio Network Rules (Civic Group Services)
- `mc-08-08-2004.html` — Mobile Phone Dealer Rules (Cellular Mobile Services)
- `mc-07-08-85.html` — RLM Certificate Without Examination (Radio Operator's Certificate)
- `mc-14-89.html` — Government Radio Operator Certificate (Radio Operator's Certificate)
- `mc-09-4-94.html` — Amateur License Renewal Guidelines (Amateur Services)
- `mc-16-11-2004.html` — Communications Technician Course RTS Rules (Radio Training Center)
- `mc-02-02-2005.html` — FWA Frequency Allocation (Wireless Data Network Services)
- `mc-09-07-2007.html` — LEC Interconnection Rules (Telecom Services)
- `mc-19-12-2000.html` — Master Administrative Fee Schedule (General Services)

All twenty-two pass `scripts/validate.py` with 0 errors, spanning 12 different MC categories plus 2 core laws.

**Known gaps:** two source PDFs were found to be scanned images with no extractable text and are
flagged for the OCR backlog rather than converted: Republic Act 3846 (the Radio Control Law — the
most frequently cross-referenced law across the converted MCs) and MC 03-03-2005A. See
`examples/source/ra-3846-needs-ocr.txt` and `examples/source/mc-03-03-2005a-needs-ocr.txt`.

**Progress toward 50-document target:** 22 of 50. Continuing in batches — each document requires an
individual verified fetch, so this proceeds a handful at a time rather than all at once.
