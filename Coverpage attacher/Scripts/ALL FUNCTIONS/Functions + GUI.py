from PyPDF2 import PdfMerger
import glob
import win32com.client
import os
from docx2pdf import convert
from tkinter import messagebox
from tkinter import *


def PDFMerger(pdfs_path1, pdfs_path2):
    try:
        pdfs = [pdfs_path1 + ".pdf", pdfs_path2 + ".pdf"]
        merger = PdfMerger()
        for pdf in pdfs:
            merger.append(pdf)
        out_file = merger.write("result.pdf")
        merger.close()
        return out_file
    except:
        return messagebox.showerror("Error", "There was something wrong with the name of the file, make sure it is in the correct directory")

def ConvertPDFtoWORD(pdfs_path):
    word = win32com.client.Dispatch("Word.Application")
    word.visible = 0
    success = False
    try:
        for i, doc in enumerate(glob.iglob(pdfs_path + ".pdf")):
            filename = doc.split('\\')[-1]
            in_file = os.path.abspath(doc)
            wb = word.Documents.Open(in_file)
            out_file = os.path.abspath(pdfs_path + ".docx".format(i))
            wb.SaveAs2(out_file, FileFormat=16)
            success = True
            wb.Close()
            return out_file
        word.Quit
        if success == False:
            return messagebox.showerror("Error", "There was something wrong with the name of the file, make sure it is in the correct directory")

    except:
        return messagebox.showerror("Error", "Something happened in the code, try again.")


def Word2PDF(filename):
    try:
        filename = filename + ".docx"
        return convert(filename)
    except:
        return messagebox.showerror("Error", "There was something wrong with the name of the file, make sure it is in the correct directory")

class converter(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("300x300")
        self.resizable(False, False)
        self.title("Coversheet Combiner")

    def Label(self):
        self.canvas=Canvas(self,width=400,height=50,bg="light grey")
        self.canvas.place(x=0,y=0)
        self.canvas=Canvas(self,width=400,height=5,bg="black")
        self.canvas.place(x=0,y=0)

        self.title=Label(self,text="Coversheet Combiner", font = ("", 15, "bold"), bg = "light grey")
        self.title.place(x = 10, y=20)
        self.title=Label(self,text="PDF2WORD ", font = ("", 10, "bold"))
        self.title.place(x = 10, y=60)
        self.title=Label(self,text="WORD2PDF", font = ("", 10, "bold"))
        self.title.place(x = 10, y=130)
        self.title=Label(self,text="PDF COMBINER", font = ("", 10, "bold"))
        self.title.place(x = 10, y=200)

    

    def Entry(self):
        self.pdf2word=Entry(self,borderwidth=0,highlightthickness=1)
        self.pdf2word.place(x=10,y=80,width=250,height=20)
        self.word2pdf=Entry(self,borderwidth=0,highlightthickness=1)
        self.word2pdf.place(x=10,y=150,width=250,height=20)

        self.Combiner1=Entry(self,borderwidth=0,highlightthickness=1)
        self.Combiner1.place(x=10,y=220,width=250,height=20)
        self.Comniner2=Entry(self,borderwidth=0,highlightthickness=1)
        self.Comniner2.place(x=10,y=243,width=250,height=20)

    def Button(self):
        def MyClickP2W():
            ConvertPDFtoWORD(self.pdf2word.get())
        def MyClickW2P():
            Word2PDF(self.word2pdf.get())
        def MyClickPDFCombiner():
            PDFMerger(self.Combiner1.get(), self.Comniner2.get())
    
        self.pdf2wordbutton=Button(self, text="Enter Filename", font="bold 8", command = MyClickP2W)
        self.pdf2wordbutton.place(x=10,y=103,width=90,height=20)
        self.word2pdfbutton=Button(self, text="Enter Filename", font="bold 8", command = MyClickW2P)
        self.word2pdfbutton.place(x=10,y=173,width=90,height=20)
        self.word2pdfbutton=Button(self, text="Enter Filename", font="bold 8", command = MyClickPDFCombiner)
        self.word2pdfbutton.place(x=10,y=266,width=90,height=20)

if __name__ == "__main__":
    converter = converter()
    converter.Label()
    converter.Entry()
    converter.Button()
    converter.mainloop()