from fpdf import FPDF

pdf = FPDF(orientation='P', unit='mm', format='A4')
pdf.add_page()

pdf.set_font(family="Times",style="B", size=12)
pdf.cell(w=0, h=10, txt="Hello World", border=1, ln=1, align='L')
pdf.cell(w=0, h=10, txt="Hey there", border=1, ln=1, align='L')
pdf.output('output.pdf')