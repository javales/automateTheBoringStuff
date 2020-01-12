# /usr/bin/env python3

##############################################################################
# https://www.udemy.com/course/automate/learn/lecture/3465848?start=0#overview
## Section 14: Excel, Word, and PDF Documents (Lesson 42-45) - only Lesson 44 - Reading and Editing PDFs

# Install third-party module PyPDF2 with pip install PyPDF2 to read and modify PDF files

import PyPDF2
import os

print('')
print('##############################################################################')
print('Section 14: Excel, Word, and PDF Documents (Lesson 42-45) - only Lesson 44 - Reading and Editing PDFs')
print('##############################################################################')
print('')

# Change Current Working Directory
os.chdir('/Proj/study/udemy/automateTheBoringStuff')

pdfFile = open('finishing-our-application-slides.pdf', 'rb') #open in Read Binary mode instead of default Read Only

#pass file to PyPDF2 and store in Reader object
readerFile = PyPDF2.PdfFileReader(pdfFile)

#Reader objects have a number variable for number of pages
pagesCount = readerFile.numPages
print('Number of pages in finishing-our-application-slides.pdf file:')
print(pagesCount)
print('')

#Store page object using getPage() method
page = readerFile.getPage(0)
pageTextOut = page.extractText()
print('Printing page 0 text from document:')
print(pageTextOut)
print('')

print('Printing all text from all pages:')
for pageNum in range(readerFile.numPages):
    print(readerFile.getPage(pageNum).extractText())

print('')

#Page Level editing, combining pages from one PDF file with another PDF file
pdfFile2 = open('finishing-our-application-slides2.pdf', 'rb') #open in Read Binary mode instead of default Read Only

#pass file to PyPDF2 and store in second Reader object
readerFile2 = PyPDF2.PdfFileReader(pdfFile2)

#Use Writer object to create a file that is a combination of the two above
writerFile = PyPDF2.PdfFileWriter() #at this point only exists computer memory

#Write objects have a writePage() method to allow adding pages to end of document
#Loop through both Read objects and write their pages to the Write object
for pageNum in range(readerFile.numPages):
    page = readerFile.getPage(pageNum)
    writerFile.addPage(page)

for pageNum in range(readerFile2.numPages):
    page = readerFile2.getPage(pageNum)
    writerFile.addPage(page)

#Now save WriteFile object to hard drive
outputFile = open('finishing-our-application-slidesCOMBINED.pdf', 'wb') #Write Binary Mode
writerFile.write(outputFile)

#Close them all
outputFile.close()
pdfFile.close()
pdfFile2.close()