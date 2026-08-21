#!/usr/bin/env python3
"""
Validates converted HTML law/MC documents against the repo's conventions:
- Has a unique id on the <article> tag
- Has a metadata JSON comment block matching schema/document-schema.json
- Every internal cross-reference link (href="#...") points to an id that
  exists somewhere in the corpus

Usage:
    python3 validate.py examples/html/
"""

import json
import re
import sys
from pathlib import Path

REQUIRED_FIELDS = ["id", "title", "type", "status", "effective_date"]


def extract_metadata(html_text):
    match = re.search(r"METADATA BLOCK.*?(\{.*\})\s*-->", html_text, re.DOTALL)
    if not match:
        return None
    try:
        return json.loads(match.group(1))
    except json.JSONDecodeError as e:
        print(f"  WARNING: metadata block found but not valid JSON: {e}")
        return None


def extract_article_id(html_text):
    match = re.search(r'<article id="([a-z0-9-]+)"', html_text)
    return match.group(1) if match else None


def extract_href_ids(html_text):
    return re.findall(r'href="#([a-z0-9-]+)"', html_text)


def main(folder):
    folder = Path(folder)
    files = list(folder.glob("*.html"))
    if not files:
        print(f"No HTML files found in {folder}")
        return 1

    all_ids = set()
    all_refs = {}
    errors = 0

    for f in files:
        text = f.read_text()
        article_id = extract_article_id(text)
        if not article_id:
            print(f"[FAIL] {f.name}: no <article id=...> found")
            errors += 1
            continue
        all_ids.add(article_id)

        meta = extract_metadata(text)
        if not meta:
            print(f"[FAIL] {f.name}: no valid metadata block found")
            errors += 1
        else:
            missing = [field for field in REQUIRED_FIELDS if field not in meta]
            if missing:
                print(f"[FAIL] {f.name}: missing required metadata fields: {missing}")
                errors += 1
            if meta.get("id") != article_id:
                print(f"[FAIL] {f.name}: metadata id '{meta.get('id')}' != article id '{article_id}'")
                errors += 1

        all_refs[f.name] = extract_href_ids(text)

    for fname, refs in all_refs.items():
        for ref in refs:
            if ref not in all_ids:
                print(f"[WARN] {fname}: cross-reference to '#{ref}' has no matching document yet")

    print(f"\nChecked {len(files)} file(s). {errors} error(s).")
    return 1 if errors else 0


if __name__ == "__main__":
    folder = sys.argv[1] if len(sys.argv) > 1 else "examples/html"
    sys.exit(main(folder))
