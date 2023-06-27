import os
from fpdf import FPDF

pdf = FPDF()
pdf.set_auto_page_break(0)


path = r"D:\picture"
imagelist = [i for i in os.listdir(path)]

print(imagelist)

for image in sorted(imagelist):
    pdf.add_page()
    pdf.image(os.path.join(path, image))

pdf.output(os.path.join(path, "tdsql.pdf"))
