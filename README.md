📚 MetadataCompaction

A practical tool for consolidating messy academic metadata under working loads.

MetadataCompaction is a pragmatic Python utility to rename and normalize academic PDF files downloaded from heterogeneous sources (e.g. Anna’s Archive, Springer, Elsevier), using filename heuristics with graceful fallback rules and optional local LLM assistance via Ollama.
The goal is usability, not perfect bibliographic reconstruction.

🧠 Motivation
Large academic libraries often begin in a highly disturbed state:

inconsistent filenames
missing or partial metadata
publisher‑specific naming conventions
mixed standards and document types

Pursuing perfect metadata at ingestion time is expensive and unnecessary.
MetadataCompaction applies a controlled “load” to chaotic filenames, compacting them into a usable residual state.
The remaining uncertainty is intentionally deferred to human judgment, where it belongs.

✨ Core Features

✅ Handles real‑world messy filenames
✅ Supports:

Anna’s Archive–style filenames
Springer / publisher book filenames


✅ Optional local LLM support via Ollama (offline, no APIs)
✅ Always renames files (never ignores or drops them)
✅ Graceful fallback when metadata is incomplete
✅ Deterministic, repeatable behavior
✅ Produces filenames optimized for fast search tools (e.g. Everything)


🤖 Local LLM Support (Ollama)
MetadataCompaction is designed to optionally leverage Ollama to assist with difficult filename cases without relying on cloud APIs.
Why Ollama?

✅ Runs fully local and offline
✅ No API keys
✅ No data leakage
✅ Ideal for large private academic libraries

The LLM is not trusted blindly — it is used only as an assistive tool, and all outputs are constrained by deterministic naming rules and fallbacks.

In other words: LLMs help under uncertainty, but rules remain in control.


📁 Expected Folder Structure
Place the script and PDFs in the same folder:
project_folder/
├── rename_books_local.py
├── book1.pdf
├── book2.pdf
├── renamed/
│   └── run_log.txt
└── errors/


▶ Usage

Place PDF files in the same directory as rename_books_local.py
Run:
``
python rename_books_local.py
``
📦 Output Behavior
After execution:

✅ All PDFs are moved out of the root folder
✅ The root folder is left clean
✅ Files are placed into:

renamed/
errors/


✅ A detailed execution log is written to:

renamed/run_log.txt


🏷️ Naming Strategy
All files are normalized into a consistent, search‑friendly format:
AUTHOR YEAR Title.pdf

Examples
Corea 2019 An Introduction to Data.pdf
Ioannidis 2019 Design of Steel Structures to Eurocode.pdf
Unknown YYYY Foundations for Light Garden Walls.pdf


Parsing Priority

Known filename conventions (e.g. Anna’s Archive)
Publisher‑specific patterns (e.g. Springer)
Fallback renaming when metadata is unclear

This guarantees that no file is ever skipped or lost.

🚧 Design Decisions (Intentional)
MetadataCompaction intentionally:

❌ Does not parse PDF content by default
❌ Does not attempt perfect bibliographic accuracy
❌ Does not depend on cloud services or APIs

These constraints keep the tool:

fast
offline‑friendly
robust
easy to maintain

Reference managers can be applied after filenames are stabilized.

🧪 Engineering Philosophy
This tool follows a practical approach
MetadataCompaction automates approximately 90–95% of library cleanup, allowing the remaining edge cases to be resolved manually only when they are actually encountered again.

📜 License
MIT License — see the LICENSE file.

🧑‍🔧 Final Note
MetadataCompaction exists to save cognitive bandwidth.
It is a preprocessing tool — not a citation manager, not a catalog, and not a replacement for human judgment.
Its purpose is simple: Make large academic libraries immediately usable.

┌──────────────────────────────┐
│     Root Folder (PDFs)       │
│      Messy Filenames         │
└───────────────┬──────────────┘
                │
                ▼
┌──────────────────────────────┐
│     Filename Parser Layer    │
│                              │
│  1. Anna’s Archive pattern   │
│  2. Publisher pattern        │
│  3. Fallback heuristic       │
│                              │
└───────────────┬──────────────┘
                │
                ▼
┌──────────────────────────────┐
│   Normalization & Rules      │
│                              │
│  • Author extraction         │
│  • Year inference            │
│  • Title cleanup             │
│                              │
└───────────────┬──────────────┘
                │
                ▼
┌──────────────────────────────┐
│   Deterministic Renaming     │
│                              │
│   AUTHOR YEAR Title.pdf      │
│                              │
└───────────────┬──────────────┘
                │
        ┌───────┴────────┐
        ▼                ▼
┌──────────────┐  ┌──────────────┐
│   renamed/   │  │    errors/   │
│ (usable PDFs)│  │ (edge cases) │
└──────────────┘  └──────────────┘


🧠 Architectural Principles

Single pass processing
No file is skipped
Fallback always available
Human‑in‑the‑loop by design
Offline, deterministic execution
