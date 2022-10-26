from fpdf import FPDF
from fpdf.enums import Align

name = input("Name: ")

shirt = FPDF(orientation="P", unit="mm", format="A4")
shirt.add_page()
shirt.set_font('helvetica', size=36)
shirt.cell(w=0, txt="CS50 Shirtificate", align=Align.C)
shirt.set_y(50)
shirt.image("shirtificate.png", w=shirt.epw)
shirt.set_y(120)
shirt.set_font(style="B", size=18)
shirt.set_text_color(255, 255, 255)
shirt.cell(w=0, txt=f"{name} took CS50", align=Align.C)
shirt.output("shirtificate.pdf")