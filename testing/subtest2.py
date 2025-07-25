import fitz  # PyMuPDF

def classify_blocks(pdf_path, max_pages=5):
    doc = fitz.open(pdf_path)

    for page_num in range(min(len(doc), max_pages)):
        if page_num >= 6:
            break
        page = doc[page_num]
        blocks = page.get_text("dict")["blocks"]
        print(f"\n=== Page {page_num + 1} ===\n")

        for i, block in enumerate(blocks):
            block_type = block["type"]
            bbox = block["bbox"]

            if block_type == 0:
                # TEXT BLOCK
                text_lines = []
                for line in block.get("lines", []):
                    line_text = "".join([span["text"] for span in line["spans"]]).strip()
                    if line_text:
                        text_lines.append(line_text)

                block_text = "\n".join(text_lines)
                print(f"[Block #{i+1}] TYPE: TEXT (bbox={bbox})")
                print(block_text)
                print("-" * 80)

            elif block_type == 1:
                # IMAGE BLOCK
                print(f"[Block #{i+1}] TYPE: IMAGE (bbox={bbox})")
                print("<< Embedded image >>")
                print("-" * 80)

            elif block_type == 2:
                # DRAWING BLOCK
                print(f"[Block #{i+1}] TYPE: DRAWING (bbox={bbox})")
                print("<< Vector drawing — could be shapes, lines, or table borders >>")
                print("-" * 80)

            else:
                print(f"[Block #{i+1}] TYPE: UNKNOWN (type={block_type}, bbox={bbox})")
                print("-" * 80)

def main():
    pdf_path = r"sample_pdfs/pdfs/file03.pdf"
    classify_blocks(pdf_path, max_pages=10)  # For the first 10 pages

if __name__ == "__main__":
    main()
