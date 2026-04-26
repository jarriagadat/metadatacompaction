import shutil
import re
from pathlib import Path
from datetime import datetime

# =========================
# FOLDERS
# =========================

ROOT = Path(__file__).parent
RENAMED = ROOT / "renamed"
ERRORS = ROOT / "errors"

RENAMED.mkdir(exist_ok=True)
ERRORS.mkdir(exist_ok=True)

LOGFILE = RENAMED / "run_log.txt"

# =========================
# LOGGING
# =========================

def log(msg):
    ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    line = f"[{ts}] {msg}"
    print(line)
    with open(LOGFILE, "a", encoding="utf-8") as f:
        f.write(line + "\n")

# =========================
# HELPERS
# =========================

def infer_year(text):
    m = re.search(r"(19|20)\d{2}", text)
    return m.group() if m else "YYYY"

def clean(text):
    return re.sub(r'[\\/:*?"<>|]', "", text).strip()

def normalize_author(name):
    name = name.replace("_", " ").replace("-", " ")
    name = re.sub(r"\(.*?\)", "", name)
    parts = name.strip().split()
    return parts[-1].capitalize() if parts else "Unknown"

# =========================
# PARSERS
# =========================

def parse_annas_archive(name):
    parts = [p.strip() for p in name.split(" -- ")]
    if len(parts) < 2:
        return None

    title = clean(parts[0])
    authors_raw = parts[1]
    year = infer_year(name)

    authors = []
    for a in authors_raw.split(","):
        auth = normalize_author(a)
        if auth and auth != "Unknown":
            authors.append(auth)

    return title, authors if authors else ["Unknown"], year

def parse_springer(name):
    if " - " not in name:
        return None

    year = infer_year(name)
    first, rest = name.split(" - ", 1)

    author = normalize_author(first)
    title = clean(rest.replace(f"({year})", "").replace("_", " "))

    return title if title else "Untitled", [author], year

def fallback_parse(name):
    parts = re.split(r"--|-|_", name)
    title = clean(parts[0]) if parts else "Untitled"
    year = infer_year(name)
    author = normalize_author(parts[1]) if len(parts) > 1 else "Unknown"

    return title or "Untitled", [author], year

# =========================
# MAIN
# =========================

log("========================================")
log("START RUN — FALLBACK RENAME MODE")

pdfs = sorted(ROOT.glob("*.pdf"), key=lambda p: p.name.lower())
log(f"PDFs found: {len(pdfs)}")

for pdf in pdfs:
    log(f"PROCESSING: {pdf.name}")

    name = pdf.stem
    parsed = parse_annas_archive(name)

    if not parsed:
        parsed = parse_springer(name)

    if not parsed:
        parsed = fallback_parse(name)
        log("USING FALLBACK NAMING")

    title, authors, year = parsed

    if len(authors) == 1:
        new_name = f"{authors[0]} {year} {title}.pdf"
    elif len(authors) == 2:
        new_name = f"{authors[0]} and {authors[1]} {year} {title}.pdf"
    elif len(authors) == 3:
        new_name = f"{authors[0]} {authors[1]} and {authors[2]} {year} {title}.pdf"
    else:
        new_name = f"{authors[0]} et al {year} {title}.pdf"

    new_name = clean(new_name)
    final_path = RENAMED / new_name

    counter = 1
    while final_path.exists():
        final_path = final_path.with_stem(f"{final_path.stem}_{counter}")
        counter += 1

    shutil.move(pdf, final_path)
    log(f"MOVED → renamed/{final_path.name}")

log("========================================")
log("RUN FINISHED — ROOT IS CLEAN")
log("========================================")