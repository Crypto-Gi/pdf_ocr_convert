import os
from pdf2image import convert_from_path
import pytesseract
from PIL import Image
import PyPDF2
from io import BytesIO

def convert_pdf_to_searchable(input_pdf_path, output_pdf_path):
    # Convert PDF to images
    images = convert_from_path(input_pdf_path)
    
    # Create a new PDF writer
    pdf_writer = PyPDF2.PdfWriter()
    
    # Process each page
    for image in images:
        # Perform OCR
        text = pytesseract.image_to_pdf_or_hocr(image, extension='pdf')
        
        # Convert bytes to PDF page
        text_pdf = PyPDF2.PdfReader(BytesIO(text))
        pdf_writer.add_page(text_pdf.pages[0])
    
    # Save the searchable PDF
    with open(output_pdf_path, 'wb') as output_file:
        pdf_writer.write(output_file)

if __name__ == "__main__":
    # Example usage
    input_pdf = "Page1.pdf"
    output_pdf = "searchable_output.pdf"
    
    if os.path.exists(input_pdf):
        convert_pdf_to_searchable(input_pdf, output_pdf)
        print(f"Conversion complete. Searchable PDF saved as: {output_pdf}")
    else:
        print("Input PDF file not found!")