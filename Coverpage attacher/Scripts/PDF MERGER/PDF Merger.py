from PyPDF2 import PdfMerger
from tkinter import *

root = Tk()

root.title("PDF Merger")
root.geometry("500x200")

Label1 = Label(root, text="PDF Merger",font='Times')
Label1.pack(pady=0)
Label2 = Label(root, text="First PDF",font=('Times', 10))
Label2.pack(pady=4)
ent = Entry(root,width=50)
ent.pack(pady=4)
Label3 = Label(root, text="Second PDF",font=('Times', 10))
Label3.pack(pady=4)
ent2 = Entry(root,width=50)
ent2.pack(pady=4)

pdfs_path1 = ""
pdfs_path2 = ""

def myClick():
    global pdfs_path1
    global pdfs_path2
    pdfs_path1 = ent.get()
    pdfs_path2 = ent2.get()
    root.quit()

myButton = Button(root, text = "Enter the file location", command = myClick)
myButton.pack() 

root.mainloop()

pdfs = [pdfs_path1, pdfs_path2]

merger = PdfMerger()

for pdf in pdfs:
    merger.append(pdf)

merger.write("result.pdf")
merger.close()