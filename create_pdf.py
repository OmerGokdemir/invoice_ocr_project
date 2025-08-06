from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
import os

def create_invoice_pdf(filename, company, invoice_no, date, total):
    c = canvas.Canvas(filename, pagesize=A4)
    width, height = A4

    c.setFont("Helvetica-Bold", 16)
    c.drawString(50, height - 50, "INVOICE")

    c.setFont("Helvetica", 12)
    c.drawString(50, height - 100, f"Company: {company}")
    c.drawString(50, height - 130, f"Invoice No: {invoice_no}")
    c.drawString(50, height - 160, f"Date: {date}")
    c.drawString(50, height - 190, f"Total: ${total}")

    c.save()
    print(f"{filename} created.")

# Örnek kullanım:
os.makedirs("invoices", exist_ok=True)

create_invoice_pdf("invoices/invoice1.pdf", "Example Inc.", "2023-456", "15.07.2023", "4350,00")
create_invoice_pdf("invoices/invoice2.pdf", "Trial LLC.", "2023-789", "21.07.2023", "2175,50")
