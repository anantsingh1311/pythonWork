import pdfreader
from pdfreader import PDFDocument, SimplePDFViewer

# creating a pdf document instance frpm a binary file:
fd = open("first.pdf","rb")
# doc = PDFDocument(fd)

# all_pages = [p for p in doc.pages()]

# print(len(all_pages))

# from io import BytesIO

# with open()

viewr = SimplePDFViewer(fd)

for canvas in viewr:
    print(canvas.text_content)

