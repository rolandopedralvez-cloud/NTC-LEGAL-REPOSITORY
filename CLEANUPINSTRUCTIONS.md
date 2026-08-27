# Cleanup instructions — upload via GitHub web/mobile

## 1. Replace README.md

Upload the attached `README.md` to the repo root using **Add file → Upload files**, same as
before. GitHub will detect it already exists and ask to overwrite/commit — confirm. This
replaces the stale "28 documents" README with an accurate 32-document README whose document
list is now verified to exactly match `examples/html/`.

## 2. Delete these files (use the file's "..." / trash-can icon → Delete file, on GitHub mobile web or app)

**Root-level duplicates/instructions — delete these 4 files at the repo root:**
- `index.html` (byte-identical duplicate of `ui/index.html`)
- `data/documents.js` (byte-identical duplicate of `ui/data/documents.js` — after deleting
  this, the now-empty `data/` folder disappears automatically)
- `README-REPLACE-THIS.md` (one-time upload instructions, no longer needed)
- `UPLOAD-INSTRUCTIONS.md` (one-time upload instructions, no longer needed)

**Nested duplicate folder — delete all 30 files below (the whole `NTC-LEGAL-REPOSITORY/`
folder disappears automatically once every file inside it is deleted; every one of these is
confirmed to also exist, unchanged, in the real `examples/html/`, `docs/`, `schema/`, and
`scripts/` folders, so nothing unique is lost):**

- NTC-LEGAL-REPOSITORY/README.md
- NTC-LEGAL-REPOSITORY/docs/accessibility.md
- NTC-LEGAL-REPOSITORY/docs/conversion-workflow.md
- NTC-LEGAL-REPOSITORY/docs/design.md
- NTC-LEGAL-REPOSITORY/examples/html/eo-546.html
- NTC-LEGAL-REPOSITORY/examples/html/mc-02-01-97.html
- NTC-LEGAL-REPOSITORY/examples/html/mc-02-02-2005.html
- NTC-LEGAL-REPOSITORY/examples/html/mc-04-89.html
- NTC-LEGAL-REPOSITORY/examples/html/mc-05-06-2007.html
- NTC-LEGAL-REPOSITORY/examples/html/mc-06-04-99.html
- NTC-LEGAL-REPOSITORY/examples/html/mc-07-08-85.html
- NTC-LEGAL-REPOSITORY/examples/html/mc-08-08-2004.html
- NTC-LEGAL-REPOSITORY/examples/html/mc-09-07-2007.html
- NTC-LEGAL-REPOSITORY/examples/html/mc-09-4-94.html
- NTC-LEGAL-REPOSITORY/examples/html/mc-1-04-88.html
- NTC-LEGAL-REPOSITORY/examples/html/mc-10-12-95.html
- NTC-LEGAL-REPOSITORY/examples/html/mc-11-21-88.html
- NTC-LEGAL-REPOSITORY/examples/html/mc-12-08-92.html
- NTC-LEGAL-REPOSITORY/examples/html/mc-13-09-2004.html
- NTC-LEGAL-REPOSITORY/examples/html/mc-14-09-92.html
- NTC-LEGAL-REPOSITORY/examples/html/mc-14-89.html
- NTC-LEGAL-REPOSITORY/examples/html/mc-16-11-2004.html
- NTC-LEGAL-REPOSITORY/examples/html/mc-17-2-2002.html
- NTC-LEGAL-REPOSITORY/examples/html/mc-19-12-2000.html
- NTC-LEGAL-REPOSITORY/examples/html/mc-87-174.html
- NTC-LEGAL-REPOSITORY/examples/html/ra-7925.html
- NTC-LEGAL-REPOSITORY/examples/source/mc-03-03-2005a-needs-ocr.txt
- NTC-LEGAL-REPOSITORY/examples/source/ra-3846-needs-ocr.txt
- NTC-LEGAL-REPOSITORY/examples/source/ra-7925-source-note.txt
- NTC-LEGAL-REPOSITORY/schema/document-schema.json
- NTC-LEGAL-REPOSITORY/scripts/validate.py

## 3. Leave untouched

- `ntclivepreview/` — not part of this work, purpose unclear, leave as-is per your prior
  instruction.
- `ui/` folder, `examples/html/`, `examples/source/`, `docs/`, `schema/`, `scripts/` at the
  repo root — these are the real, current files and are unaffected by this cleanup.

## Verified before sending this

- `examples/html/` baseline: 32 files, matches your list exactly, nothing missing or
  duplicated.
- Root `index.html` vs `ui/index.html`: byte-identical (0-line diff).
- Root `data/documents.js` vs `ui/data/documents.js`: byte-identical (0-line diff).
- Nested `NTC-LEGAL-REPOSITORY/examples/html/` (22 files): every file also exists,
  content-identical in ID, in the real `examples/html/` (32 files) — nothing unique in the
  nested copy.
- New `README.md`: document ID list cross-checked against `examples/html/*.html` filenames —
  empty diff (exact match, 32 IDs).
- `scripts/validate.py` run against `examples/html/`: **0 errors** (only expected
  breadcrumb-anchor warnings, same as before).
