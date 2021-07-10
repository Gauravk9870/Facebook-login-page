from tkinter import *

window = Tk()
window.config(bg="#E8E8E8")
width = window.winfo_screenwidth()
height = window.winfo_screenheight()

window.geometry("%dx%d" % (width, height))

facebook = Label(window, text="facebook",bg="#E8E8E8", font=("Klavika", 50, 'bold'), fg="#427bff")
facebook.place(x=150, y=210)

tagline1 = Label(window, text="Facebook helps you connect and share",bg="#E8E8E8", font="Leelawadee 20 ", fg="black")
tagline1.place(x=150, y=290)

tagline2 = Label(window, text="with the people in your life.", bg="#E8E8E8" , font="Leelawadee 20 ", fg="black")
tagline2.place(x=150, y=323)

canvas = Canvas(window, width=415, height=320, bg="#fffcfc")
canvas.place(x=750, y=175)

username = Entry(window, width=28, font=("Verdana", 15), bg="#E8E8E8", fg="#999999")
username.insert(10, 'Mobile number or email address')
username.place(x=775, y=207, height=50)

password = Entry(window, width=28, font=("Verdana", 15),  bg="#E8E8E8", fg="#999999")
password.insert(10, 'Password')
password.place(x=775, y=267, height=50)

login = Button(window, text="                  Login                ", bg="#008ad3", font=("Klavika", 20, 'bold'), fg="white", height=0, border=0)
login.place(x=775, y=327, height=50)

forget = Button(window, text="Forgotten Password?", bg="white", font=("Klavika", 10), fg="#008ad3", height=1, border=0)
forget.place(x=900, y=377, height=20)

forget = Button(window, text="Create New Account", bg="#93c572", font=("Klavika", 20, 'bold'), fg="white", height=1, border=0)
forget.place(x=820, y=420, height=50)

forget = Button(window, text="Create a Page", bg="#E8E8E8" ,font=("Klavika", 10, "bold"), fg="black", height=1, border=0)
forget.place(x=810, y=500, height=20)

label = Label(window, text="for a celebrity, band or business", bg="#E8E8E8" ,font=("Klavika", 10), fg="black")
label.place(x=910, y=500)




mainloop()
