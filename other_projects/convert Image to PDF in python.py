#a simple code to convert any image into pdf using python
#first pip install fpdf

from fpdf import FPDF
pdf=FPDF()
#image list is the list with all image filenames
for image in imagelist:
  pdf.add_page()
  pdf.image(image,x,y,w,h)
pdf.output("yourfile.pdf", "F")
