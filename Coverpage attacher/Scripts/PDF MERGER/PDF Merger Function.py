from PyPDF2 import PdfMerger

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
