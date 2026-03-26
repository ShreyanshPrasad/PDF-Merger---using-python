
import os
import glob
from pypdf import PdfWriter, PdfReader


PDF_FOLDER = r"C:\Users\RAKSHIT\Downloads\Papers\PDF"   # ← change this

OUTPUT_FILE = r"C:\Users\RAKSHIT\Downloads\Papers\combined\combined_output.pdf"  # ← change this

# Sort files alphabetically (change to False to use filesystem order)
SORT_FILES = True


def merge_pdfs(folder: str, output: str, sort: bool = True) -> None:
    # Collect all PDF files
    pdf_files = glob.glob(os.path.join(folder, "*.pdf"))

    if not pdf_files:
        print(f"[ERROR] No PDF files found in: {folder}")
        return

    if sort:
        pdf_files.sort()

    print(f"Found {len(pdf_files)} PDF files. Merging...")

    writer = PdfWriter()
    failed = []

    for i, pdf_path in enumerate(pdf_files, start=1):
        try:
            reader = PdfReader(pdf_path)
            for page in reader.pages:
                writer.add_page(page)
            print(f"  [{i:>3}/{len(pdf_files)}] ✓ {os.path.basename(pdf_path)}")
        except Exception as e:
            print(f"  [{i:>3}/{len(pdf_files)}] ✗ FAILED: {os.path.basename(pdf_path)} — {e}")
            failed.append(pdf_path)

    # Write the combined PDF
    with open(output, "wb") as out_file:
        writer.write(out_file)

    size_mb = os.path.getsize(output) / (1024 * 1024)
    print(f"\n✅ Done! Combined PDF saved to:\n   {output}")
    print(f"   Total pages merged from {len(pdf_files) - len(failed)} files | File size: {size_mb:.1f} MB")

    if failed:
        print(f"\n⚠️  {len(failed)} file(s) failed to merge:")
        for f in failed:
            print(f"   - {f}")


if __name__ == "__main__":
    merge_pdfs(PDF_FOLDER, OUTPUT_FILE, SORT_FILES)
