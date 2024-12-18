from PyPDF2 import PdfReader, PdfWriter
from PyPDF2.generic import AnnotationBuilder


def add_text_annotation(input_pdf, output_pdf, comment_text, page_num, x, y):
    """Adds a simple text annotation to a PDF page.

    Args:
        input_pdf: Path to the input PDF.
        output_pdf: Path to the output PDF.
        comment_text: The text to add in the annotation.
        page_num: The page number (0-based).
        x: X coordinate for the annotation box.
        y: Y coordinate for the annotation box.
    """
    reader = PdfReader(input_pdf)
    writer = PdfWriter()

    for i, page in enumerate(reader.pages):
        writer.add_page(page)
        if i == page_num:
            annotation = AnnotationBuilder.text(
                rect=(x, y, x + 200, y + 50),  # x1, y1, x2, y2
                text=comment_text,
                open=False
            )
            
            
            writer.add_annotation(page_number=i, annotation=annotation)



    with open(output_pdf, "wb") as f:
        writer.write(f)

if __name__ == "__main__":
    input_pdf = "input/1-s2.0-S1364815222002444-main.pdf"  # Replace with your PDF path
    output_pdf = "output/annotated_document.pdf"
    comment_text = "This is an example comment added programmatically."
    page_number = 0  # First page
    x_coord = 10 # Example coordinates
    y_coord = 100

    add_text_annotation(input_pdf, output_pdf, comment_text, page_number, x_coord, y_coord)
    print(f"PDF with comment created at: {output_pdf}")
    
    
    