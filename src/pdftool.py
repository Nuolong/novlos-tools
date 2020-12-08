#!/usr/bin/env python3

# imports
import sys
from PyPDF2 import PdfFileReader, PdfFileWriter

# adds encryption to all PDFs in paths with passcode password
def add_encryption(paths, password, new_name):
    pdf_writer = PdfFileWriter()

    for i, path in enumerate(paths):
        if path == 0: # empty
            continue
        pdf_reader = PdfFileReader(path)

        for page in range(pdf_reader.getNumPages()):
            pdf_writer.addPage(pdf_reader.getPage(page))

        pdf_writer.encrypt(user_pwd=password, owner_pwd=None,
                           use_128bit=True)

        with open(new_name + "_" + str(i) + ".pdf", 'wb') as fh:
            pdf_writer.write(fh)

def rm_encryption(paths, password, new_name):
    pdf_writer = PdfFileWriter()
    pdf_reader = PdfFileReader(input_pdf)

    if pdf_reader.isEncrypted:
        pdf_reader.decrypt(password)

        for page in range(pdf_reader.getNumPages()):
            pdf_writer.addPage(pdf_reader.getPage(page))

        with open(output_pdf, 'wb') as fh:
            pdf_writer.write(fh)

def merge_pdfs(paths, new_name):
    pdf_writer = PdfFileWriter()

    for path in paths:
        pdf_reader = PdfFileReader(path)
        for page in range(pdf_reader.getNumPages()):
            # Add each page to the writer object
            pdf_writer.addPage(pdf_reader.getPage(page))

    # Write out the merged PDF
    with open("merged.pdf", 'wb') as out:
        pdf_writer.write(out)

def slice(paths, start, end, new_name):
    pdf = PdfFileReader(path)
    for page in range(pdf.getNumPages()):
        pdf_writer = PdfFileWriter()
        pdf_writer.addPage(pdf.getPage(page))

        output = f'{name_of_split}{page}.pdf'
        with open(output, 'wb') as output_pdf:
            pdf_writer.write(output_pdf)
