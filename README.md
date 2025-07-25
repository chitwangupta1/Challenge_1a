Here is a complete, single `README.md` file for your **PDF Heading Extractor** project, formatted for GitHub and with all functions and logic described, along with Docker usage instructions:

---

````markdown
# 🧠 PDF Heading Extractor

This project extracts structured headings (`H1`, `H2`, `H3`) from PDF files using font size, boldness, punctuation, layout, and position-based heuristics. It intelligently avoids table content and noisy text using a combination of visual and textual filters.

---

## 🚀 Features

- ✅ Font size–based heading classification
- ✅ Bold and uppercase text emphasis
- ✅ Table-aware filtering using `pdfplumber`
- ✅ Page layout and alignment checks
- ✅ Noise filtering for common patterns
- ✅ Structured JSON output with heading level, page number, and text

---

## 📦 Installation

### 🔧 Local Setup

1. Clone the repo:

   ```bash
   git clone https://github.com/your-username/pdf-heading-extractor.git
   cd pdf-heading-extractor
````

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the script:

   ```bash
   python main.py --pdf_path path/to/file.pdf
   ```

---

### 🐳 Docker Setup

1. **Build Docker image**

   ```bash
   docker build -t pdf-heading-extractor .
   ```

2. **Run PDF extractor inside Docker**

   ```bash
   docker run -it --rm -v "${PWD}:/app" pdf-heading-extractor --pdf_path sample.pdf
   ```


## 📚 Dependencies

* `PyMuPDF (fitz)`
* `pdfplumber`
* `spacy` *(optional for NLP-based scoring)*
* `re`, `collections`, `os`, `json`

---

## 📌 Best Practices

* Prefer PDFs with clear formatting and embedded fonts.
* Exclude scanned PDFs or image-based PDFs (OCR not supported yet).
* Run on multiple PDFs to auto-adjust font size hierarchy per document.

---
