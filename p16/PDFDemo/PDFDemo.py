
from fpdf import FPDF
 
pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=12)
pdf.cell(w=100,h=20,txt="Test3",ln=1)
pdf.cell(w=100,h=20,txt="Test4",ln=2)
pdf.output("test.pdf")