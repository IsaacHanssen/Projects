from tkinter import *
import glob
import win32com.client
import os

root = Tk()

root.title("PDF to Word Converter")
root.geometry("500x200")

Label1 = Label(root, text="PDF to Word Converter",font=10)
Label1.pack(pady=5)

ent = Entry(root,width=50)
ent.pack(pady=20)

pdfs_path = ""

def myClick():
    global pdfs_path
    pdfs_path = ent.get()
    root.quit()

myButton = Button(root, text = "Enter the file location", command = myClick)
myButton.pack() 

root.mainloop()

word = win32com.client.Dispatch("Word.Application")
word.visible = 0

for i, doc in enumerate(glob.iglob(pdfs_path)):
    print(doc)
    filename = doc.split('\\')[-1]
    in_file = os.path.abspath(doc)
    print(in_file)
    wb = word.Documents.Open(in_file)
    out_file = os.path.abspath(pdfs_path +filename[0:-4]+ ".docx".format(i))
    print("outfile\n",out_file)
    wb.SaveAs2(out_file, FileFormat=16) # file format for docx
    print("success...")
    wb.Close()

word.Quit()