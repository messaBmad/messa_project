# Installer reportlab si nécessaire :
# pip install reportlab

from reportlab.pdfgen import canvas

def txt_to_pdf(txt_file, pdf_file):
    c = canvas.Canvas(pdf_file)
    with open(txt_file, "r") as file:
        lines = file.readlines()

    y = 800
    for line in lines:
        c.drawString(100, y, line.strip())
        y -= 20

    c.save()

# Utilisation de la fonction
txt_to_pdf("txt_essai.txt", "pdf_essai.pdf")

print()
input("Appuyez sur une touche pour afficher votre fichier PDF converti ...")
print("__________________________________")

# Lecture du même fichier PDF
from pypdf import PdfReader

reader = PdfReader("pdf_essai.pdf")
page = reader.pages[0]
print(page.extract_text())

print()
input("Appuyez sur une touche pour quitter")


