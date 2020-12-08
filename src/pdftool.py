#!/usr/bin/env python3

import sys
from PyPDF2 import PdfFileReader, PdfFileWriter

def rotate_pages(pdf_path):
    pdf_writer = PdfFileWriter()
    pdf_reader = PdfFileReader(pdf_path)
    # Rotate page 90 degrees to the right
    page_0 = pdf_reader.getPage(0).rotateClockwise(90)
    pdf_writer.addPage(page_0)

    with open('rotate_pages.pdf', 'wb') as fh:
        pdf_writer.write(fh)

def merge_pdfs(paths):
    pdf_writer = PdfFileWriter()

    for path in paths:
        pdf_reader = PdfFileReader(path)
        for page in range(pdf_reader.getNumPages()):
            # Add each page to the writer object
            pdf_writer.addPage(pdf_reader.getPage(page))

    # Write out the merged PDF
    with open("merged.pdf", 'wb') as out:
        pdf_writer.write(out)

def split(path, name_of_split):
    pdf = PdfFileReader(path)
    for page in range(pdf.getNumPages()):
        pdf_writer = PdfFileWriter()
        pdf_writer.addPage(pdf.getPage(page))

        output = f'{name_of_split}{page}.pdf'
        with open(output, 'wb') as output_pdf:
            pdf_writer.write(output_pdf)

def add_encryption(input_pdf, output_pdf, password):
    pdf_writer = PdfFileWriter()
    pdf_reader = PdfFileReader(input_pdf)

    for page in range(pdf_reader.getNumPages()):
        pdf_writer.addPage(pdf_reader.getPage(page))

    pdf_writer.encrypt(user_pwd=password, owner_pwd=None,
                       use_128bit=True)

    with open(output_pdf, 'wb') as fh:
        pdf_writer.write(fh)

def rm_encryption(input_pdf, output_pdf, password):
    pdf_writer = PdfFileWriter()
    pdf_reader = PdfFileReader(input_pdf)

    if pdf_reader.isEncrypted:
        pdf_reader.decrypt(password)

        for page in range(pdf_reader.getNumPages()):
            pdf_writer.addPage(pdf_reader.getPage(page))

        with open(output_pdf, 'wb') as fh:
            pdf_writer.write(fh)

def main():
    pdf_paths = sys.argv
    #merge_pdfs(pdf_paths[1:])
    rm_encryption(pdf_paths[1], "no_password.pdf", "password")

if __name__ == '__main__':
    main()
