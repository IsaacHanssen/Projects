from PyPDF2 import PdfMerger
import glob
import win32com.client
import os
from docx2pdf import convert

def PDFMerger(pdfs_path1, pdfs_path2):
    try:
        pdfs = [pdfs_path1, pdfs_path2]
        merger = PdfMerger()
        for pdf in pdfs:
            merger.append(pdf)
        out_file = merger.write("result.pdf")
        merger.close()
        return out_file
    except:
        return print("Something happened in the code, try again!")

def ConvertPDFtoWORD(pdfs_path):
    word = win32com.client.Dispatch("Word.Application")
    word.visible = 0
    success = False
    try:
        for i, doc in enumerate(glob.iglob(pdfs_path + ".pdf")):
            print(doc)
            filename = doc.split('\\')[-1]
            in_file = os.path.abspath(doc)
            print(in_file)
            wb = word.Documents.Open(in_file)
            out_file = os.path.abspath(pdfs_path + ".docx".format(i))
            print("outfile\n",out_file)
            wb.SaveAs2(out_file, FileFormat=16) # file format for docx
            success = True
            print("success...")
            wb.Close()
            return out_file
        word.Quit
        if success == False:
            return print("There was something wrong with the name of the file, make sure it is in the correct directory")

    except:
        return print("Something happened in the code, try again.")

def Word2PDF(filename):
    filename = filename + ".docx"
    return convert(filename)