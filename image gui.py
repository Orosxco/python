from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title("tkinter image experiment")
root.geometry("300x300")

upload = Image.open("zonda walpaper.jpg")
image = ImageTk.PhotoImage(upload)

label = Label(root,image = image,height = 200,width = 250)
label.place(x = 50,y = 0)

root.mainloop()