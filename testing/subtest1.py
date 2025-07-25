import pdfplumber

def detect_table_like_structures(pdf_path):
    tables_found = []

    with pdfplumber.open(pdf_path) as pdf:
        for page_num, page in enumerate(pdf.pages, start=1):
            # Use built-in table extractor
            tables = page.extract_tables()

            if tables:
                tables_found.append("True")
                print(f"\n✅ Tables found on Page {page_num}:")
                for table in tables:
                    for row in table:
                        print(row)
            else:
                tables_found.append("False")
                print(f"❌ No table found on Page {page_num}")
    
    if not tables_found:
        print("\nNo tables detected in the PDF.")
        
detect_table_like_structures(r"sample_pdfs/pdfs/file01.pdf")