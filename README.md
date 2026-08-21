# NTC Project — Combined Package

This zip contains BOTH pieces of the NTC project, bundled for easy upload from mobile:

```
NTC-COMBINED/
├── NTC-LEGAL-REPOSITORY/   ← push to your existing rolandopedralvez-cloud/NTC-LEGAL-REPOSITORY repo
└── NTC-UI/                 ← push to a NEW repo (e.g. NTC-UI) for the dashboard
```

## How to upload from GitHub's mobile/web interface

1. Extract this zip on your device (any file manager or "zip extractor" app).
2. Use GitHub's "Add file → Upload files" to upload `NTC-LEGAL-REPOSITORY/` contents into your
   existing repo, and `NTC-UI/` contents into a new repo you create.

### When you're back on a PC
```bash
unzip NTC-COMBINED.zip
cd NTC-COMBINED/NTC-LEGAL-REPOSITORY
git remote add origin https://github.com/rolandopedralvez-cloud/NTC-LEGAL-REPOSITORY.git
git push origin main

cd ../NTC-UI
git remote add origin https://github.com/rolandopedralvez-cloud/NTC-UI.git
git branch -M main
git push -u origin main
```

## What's new in this batch

1 more real document added:
- MC 19-12-2000 — Master Administrative Fee Schedule (General Services) — the comprehensive fee
  schedule referenced by many other Circulars already in this repository

**Note:** Two documents were briefly generated with plausible-but-unverified fee figures and have
been removed — they were never actually fetched from a real source, only guessed at based on
similar documents. Only content pulled from a real, verified fetch is included here.

**Total: 22 documents** (2 laws + 20 Memorandum Circulars across 12 categories), all validated with 0 errors.
**Progress toward the 50-document target: 22/50.**

Two source PDFs were found to be scanned images with no extractable text and are flagged for the
OCR backlog: Republic Act 3846 (the Radio Control Law) and MC 03-03-2005A. See
`NTC-LEGAL-REPOSITORY/examples/source/*-needs-ocr.txt`.
