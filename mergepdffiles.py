"""Importing the Library
[pip install PyPDF2]"""

from PyPDF2 import PdfMerger

merge = PdfMerger()

files =['file1.pdf','file2.pdf','file3.pdf','file4.pdf']

for file in files:
    merge.append(file)
    
merge.write("Merged.pdf")

merge.close()
print("PDFs merged successfully!")