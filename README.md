# 📄 PDF Merger

A simple, dependency-light Python script to merge multiple PDF files into a single combined PDF. Processes an entire folder at once, reports progress file-by-file, and gracefully handles any files that fail — without stopping the whole job.

---

## ✨ Features

- Merges any number of PDFs from a folder into one output file
- Alphabetical sort by filename (optional, configurable)
- Per-file progress output with success/failure indicators
- Skips and reports corrupt or unreadable files without crashing
- Displays final output file size on completion

---

## 🚀 Quick Start

### 1. Clone the repository

```bash
git clone https://github.com/your-username/pdf-merger.git
cd pdf-merger
```

### 2. Install the dependency

```bash
pip install pypdf
```

### 3. Configure the script

Open `merge_pdfs.py` and update the two path variables near the top:

```python
# Folder that contains your PDF files
PDF_FOLDER = r"C:\path\to\your\pdf\folder"   # ← change this

# Where the combined PDF will be saved
OUTPUT_FILE = r"C:\path\to\combined_output.pdf"  # ← change this
```

### 4. Run it

```bash
python merge_pdfs.py
```

---

## 📋 Example Output

```
Found 186 PDF files. Merging...
  [  1/186] ✓ 001_introduction.pdf
  [  2/186] ✓ 002_chapter_one.pdf
  [  3/186] ✗ FAILED: 003_corrupted.pdf — EOF marker not found
  [  4/186] ✓ 004_chapter_two.pdf
  ...

✅ Done! Combined PDF saved to:
   C:\output\combined_output.pdf
   Total pages merged from 185 files | File size: 42.3 MB

⚠️  1 file(s) failed to merge:
   - C:\pdfs\003_corrupted.pdf
```

---

## ⚙️ Configuration Options

| Variable | Default | Description |
|---|---|---|
| `PDF_FOLDER` | *(required)* | Path to the folder containing your PDF files |
| `OUTPUT_FILE` | *(required)* | Full path for the combined output PDF |
| `SORT_FILES` | `True` | Sort files alphabetically before merging. Set to `False` to use filesystem order |

---

## 💡 Tips

**Controlling merge order** — Files are sorted alphabetically by filename. To enforce a custom order, prefix your filenames with numbers:
```
001_intro.pdf
002_background.pdf
003_chapter_one.pdf
...
```

**Reducing output file size** — For large batches, the combined PDF can be sizeable. You can compress it afterward using:
- [Ghostscript](https://www.ghostscript.com/) (free, command-line)
- [Smallpdf](https://smallpdf.com/compress-pdf) (free, browser-based)

**macOS / Linux paths** — Use forward slashes instead of backslashes:
```python
PDF_FOLDER = "/home/user/documents/pdfs"
OUTPUT_FILE = "/home/user/documents/combined_output.pdf"
```

---

## 🛠️ Requirements

- Python 3.7+
- [pypdf](https://pypi.org/project/pypdf/) `pip install pypdf`

---

## 📁 Project Structure

```
pdf-merger/
├── merge_pdfs.py   # Main script
└── README.md       # This file
```

---

