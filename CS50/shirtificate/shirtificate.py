from fpdf import FPDF

class PDF():
    def __init__(self, name):
        self._pdf = FPDF()
        self._pdf.add_page()
        self._pdf.set_font('helvetica', 'B', 50)
        self._pdf.cell(0, 57, "CS50 Shirtificate", align="C")
        self._pdf.image("shirtificate.png", 10, 70, 190)
        self._pdf.set_font_size(30)
        self._pdf.set_text_color(255, 255, 255)
        self._pdf.cell(-185, 250, f"{name} took CS50", align="C")


    def save(self, name):
        self._pdf.output(name)

def main():
    pdf = PDF(input("Enter a name: "))
    pdf.save("shirtificate.pdf")


if __name__=="__main__":
    main()
