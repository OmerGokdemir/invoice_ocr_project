import os
import pytesseract
from pdf2image import convert_from_path
import pandas as pd
import re
from PIL import Image

# Tesseract path (example for Windows)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

INPUT_DIR = "invoices"
OUTPUT_CSV = "extracted_invoices.csv"
OUTPUT_XLSX = "extracted_invoices.xlsx"

def extract_data_from_text(text):
    invoice_number = re.search(r'Invoice\s*No[:\-]?\s*([\w\-]+)', text, re.IGNORECASE)
    date = re.search(r'Date[:\-]?\s*([\d/.-]+)', text, re.IGNORECASE)
    total = re.search(r'(Total\s*(Amount)?\s*(Due)?[:\-]?\s*\$?\s*)([\d.,]+)', text, re.IGNORECASE)
    company = re.search(r'Company[:\-]?\s*(.+)', text, re.IGNORECASE)

    return {
        "Invoice Number": invoice_number.group(1) if invoice_number else "",
        "Date": date.group(1) if date else "",
        "Total Amount": total.group(4) if total else "",
        "Company Name": company.group(1) if company else ""
    }

def process_pdf(pdf_path):
    images = convert_from_path(pdf_path)
    text = ""
    for img in images:
        text += pytesseract.image_to_string(img)
    return extract_data_from_text(text)

def main():
    data = []
    for file in os.listdir(INPUT_DIR):
        if file.endswith(".pdf"):
            pdf_path = os.path.join(INPUT_DIR, file)
            info = process_pdf(pdf_path)
            info["File Name"] = file
            data.append(info)

    df = pd.DataFrame(data)
    df.to_csv(OUTPUT_CSV, index=False)
    df.to_excel(OUTPUT_XLSX, index=False, engine='openpyxl')
    print(f"✅ Extraction completed! Results saved to {OUTPUT_CSV} and {OUTPUT_XLSX}")

if __name__ == "__main__":
    main()
