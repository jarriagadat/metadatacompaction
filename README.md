```markdown
# MetadataCompaction

**A practical tool for consolidating messy academic metadata under working loads.**

MetadataCompaction is a small Python utility to rename academic PDF files downloaded from mixed sources (Anna’s Archive, Springer, random publishers, personal dumps) into **consistent, usable filenames**.

It is designed to **save time**, not to achieve perfect bibliographic accuracy.

---

## Purpose

Academic PDF libraries usually start in a bad state:

- Long and inconsistent filenames  
- Mixed naming styles  
- Missing authors or years  
- Publisher junk embedded in filenames  

MetadataCompaction automates most of the cleanup so that the library becomes immediately usable.  
The remaining few ambiguous cases can be corrected manually **only when needed**.

---

## What the Script Does

1. You place PDF files in the same folder as the script  
2. You run the script  
3. For each PDF:
   - The filename is read
   - Author, year, and title are inferred from the filename
   - A clean filename is created
   - The file is moved and renamed
4. A log is written describing what happened

After the script finishes:
- No PDFs remain in the root folder
- All PDFs are renamed and organized

---

## Filename Format

All files are renamed into the format:

```

AUTHOR YEAR Title.pdf

```

Examples:

```

Corea 2019 An Introduction to Data.pdf
Ioannidis 2019 Design of Steel Structures to Eurocode.pdf
Unknown YYYY Foundations for Light Garden Walls.pdf

```

If metadata cannot be confidently identified, placeholders are used instead of failing.

---

## Folder Structure After Running

```

project\_folder/
├── rename\_books\_local.py
├── renamed/
│   ├── Clean\_File\_Name.pdf
│   └── run\_log.txt
└── errors/
└── Extremely\_Broken\_File.pdf

```

- Files are **moved**, not copied  
- No PDF remains in the root folder  

---

## How Metadata Is Determined

The script tries several approaches **in order**:

1. **Anna’s Archive style**
   - Filenames using `--` as separators
2. **Publisher / Springer style**
   - Filenames like `Author - Title (Year)`
3. **Fallback**
   - Best possible guess using available words
   - Uses `Unknown` or `YYYY` when necessary

This guarantees that every file is renamed.

---

## Local LLM Support (Ollama)

MetadataCompaction can optionally use **Ollama**, a local large‑language‑model runtime, to assist with difficult filename cases.

- Fully offline
- No API keys
- No cloud services
- No data leaves the machine

LLM output is constrained by deterministic naming rules and fallback logic.

---

## Simple Processing Flow

```

Messy PDF filenames
↓
Read filename text
↓
Infer author, year, title
↓
Create clean filename
↓
Move file to renamed/ or errors/
↓
Write log entry

```

Single pass. No retries. No skipped files.

---

## Logging

Each run creates or appends to:

```

renamed/run\_log.txt

```

The log records:
- Timestamps
- Original filenames
- Classification decisions
- Final filenames

---

## Design Decisions

- PDF contents are not parsed
- No external APIs are required
- Bibliographic perfection is not the goal
- Human judgment is reserved for edge cases

These decisions keep the tool fast, offline, and maintainable.

---

## Engineering Philosophy

MetadataCompaction follows a simple engineering principle:

> Automate most of the work, and design for a usable residual state.

Approximately 90–95% of files are handled automatically.  
The remaining cases are intentionally left for manual refinement.

---

## License

MIT License.

---

## Final Note

This tool exists to reduce cognitive load.

Its purpose is to transform chaotic academic libraries into collections that are immediately searchable, sortable, and usable—without demanding perfection at ingestion time.
```
