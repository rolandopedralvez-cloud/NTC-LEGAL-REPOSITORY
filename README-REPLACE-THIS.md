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

This is a design-stage repository. It now includes a **real pilot batch of 32 converted documents** from
NTC Region VII (region7.ntc.gov.ph). This list is generated directly from the files present in
`examples/html/` to avoid drift between this README and the actual repository contents:

- `ra-7925.html` — Republic Act 7925, Public Telecommunications Policy Act
- `eo-546.html` — Executive Order 546, creating the NTC
- `act-3846.html` — Act No. 3846, Radio Control Law (originally flagged as unreadable scan; later
  resolved using a verified fetch of a compiled reference document — see note below)
- `mc-04-89.html` — Sanctions for Violations (General Services)
- `mc-87-174.html` — Revised Amateur Radio Regulations (Amateur Services)
- `mc-02-03-87.html` — Revised Amateur Regulations Implementation (Amateur Services)
- `mc-09-4-94.html` — Amateur License Renewal Guidelines (Amateur Services)
- `mc-14-09-92.html` — TVRO Station Registration and Licensing (Broadcast Services)
- `mc-11-11-2007.html` — Digital FM Radio Broadcast Guidelines (Broadcast Services)
- `mc-05-06-2007.html` — Consumer Protection Guidelines (Telecom Services)
- `mc-09-07-2007.html` — LEC Interconnection Rules (Telecom Services)
- `mc-06-04-99.html` — GMDSS Radio Personnel Qualifications (Maritime Services)
- `mc-10-12-95.html` — RLM Seminar Guidelines (Fixed and Land Mobile Services)
- `mc-1-04-88.html` — CPE Rules and Regulations (CPE Services)
- `mc-13-09-2004.html` — Modified Admin Fee for VAS (Value Added Services)
- `mc-17-2-2002.html` — Radio Training Center GMDSS Course Rules (Radio Training Center)
- `mc-16-11-2004.html` — Communications Technician Course RTS Rules (Radio Training Center)
- `mc-05-09-2001.html` — Certificate of Competency and Endorsement (Radio Operator's Certificate)
- `mc-07-08-85.html` — RLM Certificate Without Examination (Radio Operator's Certificate)
- `mc-14-89.html` — Government Radio Operator Certificate (Radio Operator's Certificate)
- `mc-11-21-88.html` — Personal Radio Service Rules (Civic Group Services)
- `mc-12-08-92.html` — Civic Action Radio Network Rules (Civic Group Services)
- `mc-02-01-97.html` — Short Range Radio Service Licensing (Low Power Equipment)
- `mc-08-08-2004.html` — Mobile Phone Dealer Rules (Cellular Mobile Services)
- `mc-11-12-2001.html` — CMTS/Spread Spectrum Fee Amendments (Cellular Mobile Services)
- `mc-02-02-2005.html` — Fixed Wireless Access Frequency Allocation (Wireless Data Network Services)
- `mc-07-08-2016.html` — Fixed Wireless Systems 71–86 GHz Allocation (Wireless Data Network Services)
- `mc-10-10-2003.html` — CATV/DBS Competition Rules (Broadcast Services)
- `mc-05-08-2018.html` — UWB Short Range Device Amendment (Low Power Equipment)
- `mc-10-07-2007.html` — Reference Access Offers (RAO) for Interconnection (Telecom Services)
- `mc-7-6-98.html` — SRRS Amendments & Dealer Licensing Guidelines (Radio Communication Dealers Services)
- `mc-19-12-2000.html` — Master Administrative Fee Schedule (General Services)

All thirty-two pass `scripts/validate.py` with 0 errors, spanning 16 different MC categories plus
3 core laws.

**Act 3846 resolution:** originally flagged as an unreadable scanned PDF (the standalone source URL
still is). Its full genuine text was later found and verified inside a compiled reference document
also hosted on the NTC Region VII site (`Basis_for_NTC_practices.pdf`), which contains Act 3846 in
full, machine-readable form as its first entry. That fetch is the actual source for `act-3846.html`.
See `examples/source/ra-3846-needs-ocr.txt` for the full history of this resolution.

**Remaining known gap:** `examples/source/mc-03-03-2005a-needs-ocr.txt` flags MC 03-03-2005A as a
scanned PDF still needing OCR.

**Progress toward 50-document target:** 32 of 50. Continuing in batches — each document requires an
individual verified fetch, so this proceeds a handful at a time rather than all at once.

**Integrity note:** earlier in this repository's history, files with plausible-but-unverified content
appeared in the working directory multiple times without a corresponding real fetch, and one such
file was briefly committed before being caught and removed in a later commit. Every document
currently present in `examples/html/` has been cross-checked against its actual source fetch as of
the most recent commit. If auditing this repo, verify against the actual file listing above (which
is kept in sync with `examples/html/`) rather than trusting any single past commit message in isolation.
