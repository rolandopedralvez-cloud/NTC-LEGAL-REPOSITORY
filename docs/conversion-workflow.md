# Conversion Workflow: Source Document → Structured HTML

## Step 1: Triage
Sort each document into one of:
- Clean digital text (Word, clean PDF with selectable text)
- Scanned/image-only PDF or paper
- Already-structured data (spreadsheet, database export)

## Step 2: Extract
- **Word/clean PDF**: extract text directly, preserving heading structure.
- **Scanned**: OCR first (flag for human review — legal text needs accuracy, don't trust OCR blindly).
- **Database**: map existing fields to the schema in `schema/document-schema.json`.

## Step 3: Assign stable IDs
Every citable unit (chapter, section, subsection) gets a permanent ID that never changes, even if the document is renumbered later. Convention:
```
mc-title-{title#}-sec-{section#}
law-{ordinance#}-sec-{section#}
```

## Step 4: Convert cross-references to real links
Find every textual reference like "see Section 3.12" or "as amended by Ordinance 2021-14" and turn it into `<a href="#mc-title-3-sec-12">`. This is the step that makes the "connected MC/laws" query experience possible — it's what lets you click through and see what's related.

## Step 5: Add metadata block
Every document gets the metadata fields defined in the schema: effective date, status, source ordinance, last amended date, tags/topics.

## Step 6: Validate
Run `scripts/validate.py` to catch:
- Missing or duplicate IDs
- Cross-reference links pointing to IDs that don't exist yet
- Missing required metadata fields

## Step 7: Publish
The validated HTML file becomes the canonical source, feeding the public site, search index, and internal tools simultaneously.
