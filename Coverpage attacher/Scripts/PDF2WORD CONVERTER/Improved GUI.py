from tkinter import *
import glob
import win32com.client
import os

root = Tk()

root.title("PDF to Word Converter")
root.geometry("500x200")

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

pdfs_path = ""

def myClick():
    global pdfs_path
    pdfs_path = ent.get()
    root.quit()

myButton = Button(root, text = "Enter the filename here:", command = myClick, bg="#08C776")
myButton.pack(pady=0.125) 

root.mainloop()
