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

---

## 🧩 Core Logic and Function Descriptions

### `extract_headings_from_pdf(pdf_path)`

* **Purpose:** Main function that orchestrates extraction using both `fitz` and `pdfplumber`.
* **Steps:**

  * Loads each page using `fitz` to get text spans and font sizes.
  * Cross-references table boundaries from `pdfplumber`.
  * Applies multiple heading filters and classification heuristics.

---

### `is_heading_like(text: str)`

* **Purpose:** Heuristic filter for identifying likely heading texts.
* **Checks:**

  * Length (> 3 and < 120)
  * Does not start with "Figure", "Table", "Fig."
  * No more than one period (.)
  * Avoids numerical-only lines or codes
  * Excludes typical footers or boilerplate (e.g., "Copyright")

---

### `get_dominant_font_sizes(doc)`

* **Purpose:** Returns most common font sizes across pages to define H1, H2, H3 hierarchy.
* **Logic:**

  * Counts frequency of each font size
  * Picks top 3 largest sizes as `H1`, `H2`, `H3` based on order

---

### `overlaps_table(x0, y0, x1, y1, tables)`

* **Purpose:** Checks if a text block is inside any table using its bounding box.
* **Input:** Span coordinates `(x0, y0, x1, y1)`
* **Logic:** Compares span with every table's bbox to detect overlap

---

### `classify_heading(font_size, font_map)`

* **Purpose:** Maps font size to heading level
* **Returns:** `"H1"`, `"H2"`, `"H3"` or `None`

---

### `normalize_text(text)`

* **Purpose:** Strips whitespace and replaces multiple spaces
* **Usage:** Cleans raw span text before evaluation

---

### `extract_font_size_map(counter)`

* **Purpose:** Builds a font size → heading level mapping (H1 > H2 > H3)
* **Example:**

  ```python
  {
    20.0: "H1",
    17.0: "H2",
    14.0: "H3"
  }
  ```

---

### `filter_and_score_heading(span)`

* **Future Work (Optional):** Assigns score to each span using more advanced logic (NLP, casing, punctuation balance)

---

## 🧪 Example Output

```json
[
  {
    "level": "H1",
    "page": 1,
    "text": "1. Introduction to the Foundation Level Extensions"
  },
  {
    "level": "H2",
    "page": 2,
    "text": "1.1 Background and Purpose"
  }
]
```

---

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

## 💡 Future Improvements

* [ ] Add markdown output with heading levels
* [ ] Add visual overlay for headings in extracted PDF
* [ ] Integrate OCR for scanned documents
* [ ] Train transformer-based classifier for better heading detection

---

## 👤 Author

**Chitwan Gupta**
📧 \[[email@example.com](mailto:email@example.com)]
🌐 [github.com/your-username](https://github.com/your-username)

---

## 📝 License

MIT License. See `LICENSE` file for details.

```

---

Let me know if you'd like the `main.py`, `Dockerfile`, or `requirements.txt` file to go with this.
```
