#!/usr/bin/env python3
"""Front-matter checker for content/publication entries.

New entries are usually made by copying a sibling publication folder and editing
the fields. When a field is missed, the site silently shows the wrong paper. This
catches that class of error: a title that disagrees with cite.bib, a DOI reused
from the folder it was copied from, an author slug that matches no folder in
content/authors/, an image the theme will not pick up, and categories or projects
outside the allowed vocabulary.

Runs with no dependencies. If pyyaml is importable it is used for the front-matter
parse, which is worth having: the fallback parser below is deliberate about the two
places it used to get YAML wrong (a `booktitle` field is not a `title`, and a quoted
scalar may span several lines), but a real parser is what Hugo will apply.

Two things this reports are conventions, not defects:
  * "date year does not match folder name year" — this repo dates entries by the
    ISSUE year, which is what the folder name encodes. Crossref instead reports the
    earliest of online/print, so an online-first paper legitimately differs
    (oliveira-2011: online 2009, issue 2011, folder and date both 2011).
  * "no doi" on street-2011-a — a conference paper (publication_types: ['1']) with
    no DOI assigned.

Usage: python3 scripts/check_publications.py [repo_root]
Exit code 1 if any ERROR is reported.
"""
import os
import re
import sys
from collections import defaultdict

try:
    import yaml
except ImportError:
    yaml = None

CATEGORIES = {
    "Modelling decision-making and uncertainty",
    "Efficient formulation and solution methods",
    "Energy systems",
    "Production and operations planning",
    "Supply chain management",
    "Humanitarian and healthcare logistics",
}

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ROOT = os.path.abspath(sys.argv[1]) if len(sys.argv) > 1 else REPO
PUBS = os.path.join(ROOT, "content", "publication")
AUTHORS = os.path.join(ROOT, "content", "authors")
PROJECTS = os.path.join(ROOT, "content", "project")

problems = []


def report(level, folder, msg):
    problems.append((level, folder, msg))


def closed(val):
    """True if a scalar opening with a quote closes it (YAML doubles quotes to escape)."""
    q = val[0]
    body = val[1:]
    if q == "'":
        body = body.replace("''", "")
    return body.endswith(q)


def front_matter(text):
    """Fallback parser: {key: raw_value} for top-level scalars, 'authors' as a list."""
    lines = text.split("\n")
    if lines and lines[0].strip() == "---":
        lines = lines[1:]
    fm, authors, i = {}, [], 0
    while i < len(lines):
        line = lines[i]
        if line.strip() == "---":
            break
        m = re.match(r"^([A-Za-z_][A-Za-z0-9_]*):\s*(.*)$", line)
        if not m:
            i += 1
            continue
        key, val = m.group(1), m.group(2)
        if key == "authors" and not val.strip():
            i += 1
            while i < len(lines) and re.match(r"^\s*-\s", lines[i]):
                authors.append(re.sub(r"^\s*-\s*", "", lines[i]))
                i += 1
            fm["authors"] = authors
            continue
        # unterminated flow sequence: keep consuming lines until brackets balance
        while val.count("[") > val.count("]") and i + 1 < len(lines):
            i += 1
            val += " " + lines[i].strip()
        # a quoted scalar may span lines; consume until the quote closes
        if val[:1] in ("'", '"') and not closed(val):
            while i + 1 < len(lines):
                i += 1
                val += " " + lines[i].strip()
                if closed(val):
                    break
        fm[key] = val.strip()
        i += 1
    fm.setdefault("authors", authors)
    return fm


def flow_list(raw):
    """Parse `[a, b]`. Returns (items, ok); ok is False if raw is not a flow list."""
    raw = raw.strip()
    if raw in ("", "[]"):
        return [], True
    if not (raw.startswith("[") and raw.endswith("]")):
        return [raw], False
    inner = raw[1:-1].strip()
    if not inner:
        return [], True
    return [p.strip().strip("'\"") for p in inner.split(",") if p.strip()], True


def unquote(s):
    s = s.strip()
    if len(s) > 1 and s[0] in "'\"" and s[-1] == s[0]:
        s = s[1:-1]
    return s.replace("''", "'")


def words(s):
    return set(re.findall(r"[a-z0-9]+", s.lower()))


def overlap(a, b):
    """Jaccard similarity of two word sets, for fuzzy title/journal comparison."""
    return len(a & b) / max(len(a | b), 1)


author_folders = {
    name.lower(): name
    for name in os.listdir(AUTHORS)
    if os.path.isdir(os.path.join(AUTHORS, name))
}
project_folders = {
    n for n in os.listdir(PROJECTS) if os.path.isdir(os.path.join(PROJECTS, n))
}

doi_map = defaultdict(list)
entries = sorted(
    d for d in os.listdir(PUBS) if os.path.isfile(os.path.join(PUBS, d, "index.md"))
)

for folder in entries:
    path = os.path.join(PUBS, folder)
    with open(os.path.join(path, "index.md")) as fh:
        text = fh.read()
    raw = front_matter(text)

    # --- prefer a real YAML parse; the fallback keeps the checker dependency-free
    fm, parsed = raw, False
    if yaml is not None and text.startswith("---"):
        try:
            loaded = yaml.safe_load(text.split("---", 2)[1]) or {}
            fm, parsed = loaded, True
        except yaml.YAMLError as exc:
            report("ERROR", folder, f"front matter does not parse: {str(exc)[:120]}")
            continue

    def value(key, default=""):
        v = fm.get(key, default)
        return v if parsed else unquote(v)

    authors = fm.get("authors") or []
    if isinstance(authors, str):
        authors = [authors]

    if not parsed:
        # without a real parser, catch the one defect it would have caught: an
        # unquoted scalar containing ": " is not valid YAML
        for key, val in raw.items():
            if key == "authors" or not isinstance(val, str) or not val:
                continue
            if val[0] in "'\"":
                if len(val) < 2 or not closed(val):
                    report("ERROR", folder, f"{key}: quote is not closed")
            elif ": " in val:
                report(
                    "ERROR",
                    folder,
                    f"{key} is an unquoted scalar containing ': ' — YAML will not parse it",
                )

    # --- authors resolve to a real folder, with no stray whitespace
    for entry in raw["authors"]:  # raw, so trailing whitespace is still visible
        ref = entry.strip()
        if entry != entry.rstrip():
            report("WARN", folder, f"author ref has trailing whitespace: {ref!r}")
        if not re.match(r"^[gp]_", ref):
            continue  # external co-author, written out in full
        if ref.lower() not in author_folders:
            report("ERROR", folder, f"author {ref!r} has no folder in content/authors/")
        elif author_folders[ref.lower()] != ref:
            report(
                "WARN",
                folder,
                f"author {ref!r} differs in case from folder {author_folders[ref.lower()]!r}",
            )

    # --- DOI present and unique
    doi = str(value("doi") or "").strip()
    if not doi:
        report("WARN", folder, "no doi")
    else:
        doi_map[doi.lower().rstrip("/ ")].append(folder)

    # --- date well-formed, and its year matches the folder-name year
    date = str(value("date") or "")
    if not re.match(r"^\d{4}-\d{2}-\d{2}$", date):
        report("ERROR", folder, f"date {date!r} is not YYYY-MM-DD")
    else:
        m = re.search(r"(19|20)\d{2}", folder)
        if m and m.group(0) != date[:4]:
            report(
                "WARN",
                folder,
                f"date year {date[:4]} does not match folder name year {m.group(0)}",
            )

    # --- index.md title and journal vs cite.bib
    bib_path = os.path.join(path, "cite.bib")
    if not os.path.isfile(bib_path):
        report("ERROR", folder, "no cite.bib")
    else:
        bib = open(bib_path).read()
        title = str(value("title") or "")
        # the leading boundary keeps this from matching `booktitle = {...}`
        bt = re.search(r"(?:^|[,{\s])title\s*=\s*[{\"](.+?)[}\"]\s*,", bib, re.S)
        if bt and title and overlap(words(title), words(re.sub(r"[{}]", "", bt.group(1)))) < 0.6:
            report(
                "ERROR",
                folder,
                "index.md title disagrees with cite.bib title\n"
                f"        index: {title[:90]}\n"
                f"        bib  : {bt.group(1)[:90]}",
            )
        types = str(fm.get("publication_types", ""))
        field = "booktitle" if "1" in types else "journal"
        bj = re.search(field + r"\s*=\s*[{\"](.+?)[}\"]\s*,", bib, re.S)
        pub = str(value("publication") or "").strip("*")
        if bj and pub:
            a = words(pub.replace(" and ", " & "))
            b = words(re.sub(r"[{}\\]", "", bj.group(1)))
            if overlap(a, b) < 0.6:
                report(
                    "ERROR",
                    folder,
                    f"publication {pub!r} disagrees with cite.bib {field} {bj.group(1)!r}",
                )

    # --- the theme only renders an image named featured.*
    images = [f for f in os.listdir(path) if re.search(r"\.(jpe?g|png|gif|webp)$", f, re.I)]
    stray = [f for f in images if not f.lower().startswith("featured.")]
    if stray:
        report(
            "ERROR",
            folder,
            f"image(s) not named featured.*, so the theme ignores them: {', '.join(stray)}",
        )

    # --- categories / projects vocabularies
    for key, allowed in (("categories", CATEGORIES), ("projects", project_folders)):
        val = fm.get(key, [])
        if parsed:
            if val is None:
                val = []
            if not isinstance(val, list):
                report("ERROR", folder, f"{key} is not a list: {val!r}")
                val = []
        else:
            val, ok = flow_list(val)
            if not ok:
                report("ERROR", folder, f"{key} is not a list: {fm.get(key)!r}")
                val = []
        for item in val:
            if item not in allowed:
                report("ERROR", folder, f"unknown {key[:-1]} {item!r}")

for doi, folders in sorted(doi_map.items()):
    if len(folders) > 1:
        report("ERROR", folders[0], f"doi {doi} is shared with: {', '.join(folders[1:])}")

errors = [p for p in problems if p[0] == "ERROR"]
for level, folder, msg in sorted(problems, key=lambda p: (p[1], p[0])):
    print(f"{level:5} {folder}: {msg}")
print(
    f"\n{len(entries)} entries checked with "
    f"{'pyyaml' if yaml else 'the built-in parser'}: "
    f"{len(errors)} errors, {len(problems) - len(errors)} warnings"
)
sys.exit(1 if errors else 0)
