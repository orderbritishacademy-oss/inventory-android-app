from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
import os

def create_bill(invoice, party, total):
    os.makedirs("bills", exist_ok=True)
    path = f"bills/{invoice}.pdf"
    c = canvas.Canvas(path, pagesize=A4)
    c.drawString(50, 800, "Kidzibooks Publications")
    c.drawString(50, 770, f"Invoice: {invoice}")
    c.drawString(50, 740, f"Party: {party}")
    c.drawString(50, 710, f"Total: ₹{total}")
    c.save()
    return path
