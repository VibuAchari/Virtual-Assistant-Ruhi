# core/pdfgen.py

from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font("Arial", "B", 15)
        self.cell(0, 10, "HISTORY", ln=1, align="C")
        self.set_font("Arial", size=12)
        self.cell(0, 10, "Time  |  User  |  Query  |  Date", ln=1, align="C")

    def chapter_body(self, data):
        self.set_font("Arial", size=12)
        for row in data:
            line = "  |  ".join(str(item) for item in row)
            self.cell(0, 10, line, ln=1, align="C")


def create_pdf(data):
    pdf = PDF()
    pdf.add_page()
    pdf.chapter_body(data)
    pdf.output("resources/history.pdf")
