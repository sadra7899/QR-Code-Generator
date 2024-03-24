from tkinter import *
import qrcode
import sys
from termcolor import colored, cprint




root = Tk()
root.title("QR creator")
root.geometry("700x700")
root.config(bg="gray")
root.resizable(False, False)



def generate():
    text = entry.get()
    qr = qrcode.make(text)
    qr.save("Qrcode/" + str() + ".png")
    global Image
    Image = PhotoImage(file="Qrcode/" + str() + ".png")
    Image_view.config(image=Image)
    
Image_view = Label(root, bg="gray")
Image_view.place(x=210, y=200)
title = Label(root, text="QR CODE GENERATOR", font="arial 20 bold")
title.place(x=200, y=10)
entry = Entry(root, width=28, font="Italic 15")
entry.place(x=200, y=80)
Button(
    root, text="Generate", width=20, height=2, bg="light gray", fg="black", cursor="hand2", command=generate
).place(x=275, y=125)
root.mainloop()
