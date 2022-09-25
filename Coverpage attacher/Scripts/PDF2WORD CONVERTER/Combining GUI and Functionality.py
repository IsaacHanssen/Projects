from tkinter import *
from tkinter import messagebox
import glob
import win32com.client
import os

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
            wb.SaveAs2(out_file, FileFormat=16) # file format for docx
            success = True
            wb.Close()
            return out_file
        word.Quit
        if success == False:
            return messagebox.showerror("Error", "There was something wrong with the name of the file, make sure it is in the correct directory")

    except:
        return messagebox.showerror("Error", "Something happened in the code, try again.")

root = Tk()

root.title("PDF to Word Converter")
root.geometry("500x200")
root.resizable(width=False, height=False)
# ICON
root.iconbitmap("PDFtoWord.ico")


# BACKGROUND AESTHETIC
canva = Canvas(root,bg="#2A8F70")
canva.place(x=-1,y=-1,width=500,height=50)
canva.config(highlightthickness=0)
# BACKGROUND COLOUR
root.configure(bg='#2FA17E')
Font_tuple = ("", 15, "bold")
Label1 = Label(root, text="PDF to Word Converter",bg="#2A8F70",font=Font_tuple)
Label1.pack(pady=12)

ent = Entry(root,width=50, bg="#CFFDEA")
ent.pack(pady=15)

def myClick():
    ConvertPDFtoWORD(ent.get())

myButton = Button(root, text = "Enter the filename here:", command = myClick, bg="#08C776")
myButton.pack(pady=0.125) 

root.mainloop()


