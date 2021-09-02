import tkinter
from tkinter import *
from PIL import Image, ImageTk

# Creating a basic window
root = Tk()

# Defining the size of the window screen
root.geometry("1000x800")

# Creating a photoimgage object of the image in the path
img = Image.open("C:/Users/ASUS/PycharmProjects/GUI Projects/.png")
loading_img = ImageTk.PhotoImage(img)

# image is ready to show
ready_to_show = Label(root, image=loading_img)

# placing image by giving its coordinates x and y
ready_to_show.place(x=100, y=100)

mainloop()

