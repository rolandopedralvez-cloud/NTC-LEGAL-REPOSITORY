# Design Document: NTC Legal Repository

## 1. Problem

NTC holds Municipal Codes, laws, resolutions, and related governance documents in mixed formats (Word, PDF, scans, some database entries). There is no unified, accessible, cross-referenced way to:

- Let the public read/search current law.
- Let staff query "what's connected to this," find conflicts, or trace amendment history.
- Guarantee accessibility (WCAG) compliance for public-facing content.

## 2. Core Principle

**Structured HTML is the source of truth — not PDF, not Word.**

Every law, ordinance, or MC section is converted once into a canonical HTML representation with:
- A stable, unique ID per section.
- Real hyperlinks for every cross-reference.
- Machine-readable metadata (dates, status, jurisdiction, tags).

PDFs, if needed, are generated *from* this HTML for printing/download — never the other way around.

## 3. Document Model

Each unit of law (chapter, section, subsection — whatever the smallest citable unit is) becomes one HTML file or one clearly delimited block, with:

| Element | Purpose |
|---|---|
| Stable ID | `mc-title-3-sec-12` — never changes even if renumbered |
| Semantic heading | `<h2>`, `<h3>` matching the real legal hierarchy |
| Cross-reference links | `<a href="#mc-title-3-sec-12">Section 3.12</a>` instead of plain text |
| Metadata block | Effective date, status (active/repealed/amended/superseded), source ordinance number |
| Amendment history | Linked list of prior versions / amending ordinances |

See `schema/document-schema.json` for the exact metadata contract and `examples/html/` for a worked example.

## 4. Pipeline

```
[Mixed source docs]  →  [Triage & OCR if needed]  →  [Structured HTML conversion]
        │                                                      │
        │                                                      ▼
        │                                          [Validation against schema]
        │                                                      │
        ▼                                                      ▼
 [Original archived]                            [Canonical HTML repository]
                                                              │
                              ┌───────────────────────────────┼───────────────────────────┐
                              ▼                                ▼                           ▼
                     [Public website]              [Search index (full-text)]   [Internal query tool]
                     WCAG-compliant                  e.g. Typesense/Elastic       AI/NL layer on top of
                                                                                   the same structured corpus
```

### Step-by-step

1. **Triage**: Sort source docs by format (Word / clean PDF / scanned PDF / database record).
2. **OCR** scanned documents (only where no clean digital source exists) — flag these for human review, OCR is never fully trusted for legal text.
3. **Convert** each document into the HTML model above. This is the highest-effort step and should be piloted on a small batch first.
4. **Validate** — check every doc has: unique ID, valid metadata, no dangling cross-reference links.
5. **Publish** — same HTML source feeds the public site, the search index, and any internal tooling. No duplicate maintenance.

## 5. Platform Options

| Option | Pros | Cons |
|---|---|---|
| Municode / American Legal / General Code | Turnkey, handles conversion + hosting + search | Recurring cost, less control over data model |
| Self-hosted (static site + search index) | Full control, cheaper long-term, data model is yours | You own conversion/maintenance effort |
| Hybrid | Use vendor for public site, mirror structured HTML internally for querying | More moving parts to keep in sync |

## 6. Accessibility

See `docs/accessibility.md`. Non-negotiables for the public site: semantic HTML, keyboard navigation, screen-reader-tested, alt text on all images/maps, accessible PDF as secondary download only.

## 7. Internal Query Layer

Once the corpus is structured HTML with clean metadata and real cross-reference links:
- Full-text search works well out of the box (Typesense, Elasticsearch, even Postgres full-text search for smaller corpora).
- A "referenced by / references" graph can be auto-generated from the `<a href="#...">` links — no manual tagging needed.
- A natural-language query assistant can sit on top of this same corpus, but only performs well if the HTML is clean — garbage in, garbage out.

## 8. Rollout Plan

1. Pilot: convert 3–5 representative documents (one per source format) end-to-end.
2. Validate the schema holds up against real messiness (find edge cases early).
3. Decide platform (vendor vs self-hosted vs hybrid) based on pilot effort.
4. Scale conversion across the full corpus, prioritizing most-referenced/most-viewed laws first.
5. Stand up public site + search index.
6. Layer internal query tooling on top.
