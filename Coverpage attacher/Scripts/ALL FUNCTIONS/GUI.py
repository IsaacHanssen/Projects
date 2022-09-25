from tkinter import *

class converter(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("300x300")
        self.resizable(False, False)
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
        self.pdf2wordbutton=Button(self, text="Enter Filename", font="bold 8")
        self.pdf2wordbutton.place(x=10,y=103,width=90,height=20)
        self.word2pdfbutton=Button(self, text="Enter Filename", font="bold 8")
        self.word2pdfbutton.place(x=10,y=173,width=90,height=20)
        self.word2pdfbutton=Button(self, text="Enter Filename", font="bold 8")
        self.word2pdfbutton.place(x=10,y=266,width=90,height=20)



if __name__ == "__main__":
    converter = converter()
    converter.Label()
    converter.Entry()
    converter.Button()
    converter.mainloop()