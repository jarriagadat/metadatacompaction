# MetadataCompaction

A practical tool for consolidating messy academic metadata under working loads.
MetadataCompaction is a small Python script to rename academic PDF files into consistent, usable filenames.
It is designed to handle real‑world messiness and save time, not to achieve perfect bibliographic accuracy.

# What it does

Reads PDF filenames only (no content parsing)
Infers author, year, and title from common filename patterns
Always renames files using the format:

AUTHOR YEAR Title.pdf

Uses safe placeholders (Unknown, YYYY) when metadata is unclear
Moves every file out of the root folder
Writes a detailed log to renamed/run_log.txt

# Why this exists
Academic PDF libraries usually start chaotic: inconsistent names, missing metadata, publisher junk. MetadataCompaction automates most of the cleanup so the library becomes immediately usable, leaving only a small number of edge cases for manual renaming when (and if) you need them.

# How to use

Put PDF files in the same folder as rename_books_local.py
Run:
python rename_books_local.py
The root folder is left clean

Resulting folder structure
project_folder/
rename_books_local.py
renamed/
run_log.txt
errors/
Naming strategy
The script tries, in order:

Anna’s Archive style filenames
Publisher or Springer style filenames
A fallback guess

This guarantees that no file is skipped or lost.
Local LLM support
The script can optionally use a local LLM via Ollama to assist with difficult cases. Ollama runs fully offline, requires no API keys, and never sends data outside the machine.

# Design philosophy
Automate most of the work and design for a usable residual state. MetadataCompaction typically fixes 90–95% of files automatically so you can spend your time on the few cases that actually matter.

# License
MIT
