# What's Missing From Your Live Repo

Your live repo (rolandopedralvez-cloud/NTC-LEGAL-REPOSITORY) currently only has 3 of 32
converted documents. This package contains ONLY what's missing — no duplicates.

## What's in this package

```
MISSING-FILES/
├── README-REPLACE-THIS.md          ← REPLACE your repo's README.md with this file
└── examples/
    ├── html/                        ← 29 NEW documents to ADD to examples/html/
    │   └── (29 .html files)
    └── source/                      ← 2 NEW notes to ADD to examples/source/
        ├── ra-3846-needs-ocr.txt
        └── mc-03-03-2005a-needs-ocr.txt
```

## What NOT to touch

These already exist in your live repo and are unchanged — do not re-upload:
- `examples/html/ra-7925.html`
- `examples/html/eo-546.html`
- `examples/html/mc-04-89.html`
- `examples/source/ra-7925-source-note.txt`
- `docs/` folder (design.md, conversion-workflow.md, accessibility.md) — unchanged
- `schema/document-schema.json` — unchanged
- `scripts/validate.py` — unchanged

## What about `ntclivepreview`?

That folder exists in your live repo but wasn't created as part of this project's work.
Leave it alone — this package doesn't touch it.

## How to upload on mobile (GitHub app or browser)

1. Go to your repo → `examples/html/` folder → "Add file" → "Upload files"
2. Upload all 29 `.html` files from this package's `examples/html/` folder
3. Go to `examples/source/` folder → "Add file" → "Upload files"
4. Upload the 2 `.txt` files from this package's `examples/source/` folder
5. Go to the repo root → open `README.md` → tap Edit (pencil icon) → select all,
   delete, paste in the full contents of `README-REPLACE-THIS.md` from this package →
   commit

After this, your repo will have all 32 documents and an accurate README.
