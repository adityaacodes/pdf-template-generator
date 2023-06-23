import pandas
from fpdf import FPDF

df = pandas.read_csv("topics.csv", sep=',')

pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=0)

for index, row in df.iterrows():
    pdf.add_page()

    pdf.set_font(family="Times", style="B", size=34)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=0, h=24, txt=row['Topic'], align="L", ln=1)
    pdf.line(x1=10, y1=30, x2=200, y2=30)

    # Set the footer
    pdf.ln(255)
    pdf.set_font(family="Times", style="B", size=8)
    pdf.set_text_color(180, 180, 180)
    pdf.cell(w=0, h=8, txt=row['Topic'], align="R", ln=1)

    for i in range(row['Pages'] - 1):
        pdf.add_page()

        # Set the footer
        pdf.ln(278)
        pdf.set_font(family="Times", style="B", size=8)
        pdf.set_text_color(180, 180, 180)
        pdf.cell(w=0, h=8, txt=row['Topic'], align="R", ln=1)

pdf.output("Output.pdf")
