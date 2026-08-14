from PyPDF2 import PdfWriter

merger = PdfWriter() # Means here the merger will work under the pdf writer
pdfs=[]
n=int(input("How many pdfs you want to merge? == "))

for i in range(0,n):
    name=input(f"Enter the name of pdf{i+1}: ")
    pdfs.append(name)

for pdf in pdfs:
    merger.append(pdf)
merger.write("merged-pdf.pdf")
merger.close()

















# from PyPDF2 import pdfwriter
# merger=pdfwriter()
# pdfs=[]

# n=int(input("Enter the number of files you want to merge: "))
# for i in range(0,n):
#     name=input(f"Enter the name of file{i+1}: ")
#     pdfs.append(name)

# for pdf in pdfs:
#     merger.append(pdf)
#merger.write("merged_pdf_writer")
#merger.close()


