import fitz  # PyMuPDF
import re
import json
from collections import Counter

# Rules: reject these
EXCLUDE_PHRASES = {
    "page", "version", "may", "istqb", "foundation",
    "international software testing qualifications board",
    "©", "trademark", "registered"
}

# Check if text is valid heading
def is_valid_heading(text, size, font, color, common_size, common_font, common_color):
    text = text.strip()
    if not text or len(text.split()) < 2:
        return False

    text_lower = text.lower()

    if any(excl in text_lower for excl in EXCLUDE_PHRASES):
        return False
    if re.match(r'^page \d+ of \d+', text_lower):
        return False
    if text_lower in {"table of contents", "revision history"}:
        return True

    return size != common_size or font != common_font or color != common_color

# Classify H1 vs H2
def classify_level(text, font_size, size_to_level):
    # Try pattern match first
    if re.match(r'^\d+\.\s', text) or re.match(r'^\d+\.\d+', text):
        return "H2"
    if re.match(r'^\d+\s', text):
        return "H1"
    # Fallback: use font size group
    level = size_to_level.get(round(font_size, 1))
    return level if level else "H1"

# Build mapping of font size -> H1/H2 level
def get_size_to_level(font_stats, common_size):
    heading_sizes = [round(size, 1) for _, size, _ in font_stats if size > common_size]
    size_counts = Counter(heading_sizes)
    unique_sizes = sorted(size_counts, reverse=True)
    size_to_level = {}
    if unique_sizes:
        size_to_level[unique_sizes[0]] = "H1"
        if len(unique_sizes) > 1:
            size_to_level[unique_sizes[1]] = "H2"
    return size_to_level

# Main extraction logic
def extract_headings(pdf_path):
    doc = fitz.open(pdf_path)
    headings = []
    font_stats = []

    # Pass 1: collect font stats
    for page in doc:
        for block in page.get_text("dict")["blocks"]:
            for line in block.get("lines", []):
                for span in line["spans"]:
                    font_stats.append((span["font"], span["size"], span["color"]))

    # Get common font (body text)
    font_counter = Counter(font_stats)
    common_font, common_size, common_color = font_counter.most_common(1)[0][0]
    size_to_level = get_size_to_level(font_stats, common_size)

    # Pass 2: extract headings
    for page_num, page in enumerate(doc, start=1):
        lines_seen = set()
        for block in page.get_text("dict")["blocks"]:
            for line in block.get("lines", []):
                full_text = " ".join(span["text"].strip() for span in line["spans"])
                if not full_text or full_text in lines_seen:
                    continue
                lines_seen.add(full_text)

                # Use the first span to check style
                span = line["spans"][0]
                size, font, color = span["size"], span["font"], span["color"]

                if is_valid_heading(full_text, size, font, color, common_size, common_font, common_color):
                    level = classify_level(full_text, size, size_to_level)
                    headings.append({
                        "level": level,
                        "text": full_text,
                        "page": page_num
                    })

    # Deduplicate
    unique_headings = []
    seen_text = set()
    for h in headings:
        key = h["text"].lower()
        if key not in seen_text:
            seen_text.add(key)
            unique_headings.append(h)

    # Title is first good H1
    title = next((h["text"] for h in unique_headings if h["level"] == "H1"), "Untitled Document")

    return {
        "title": title,
        "outline": unique_headings
    }

# Example usage
if __name__ == "__main__":
    result = extract_headings(r"sample_pdfs/pdfs/file03.pdf")  # your uploaded file
    print(json.dumps(result, indent=4, ensure_ascii=False))


# r"sample_pdfs/pdfs/file02.pdf"