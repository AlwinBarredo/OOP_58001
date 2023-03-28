from tkinter import*

window = Tk()
window.geometry("500x400")
window.title("My First GUI")

btn1 = Button(text = "Click Me", bg = 'yellow', fg = 'black')
btn1.place(x = 214, y = 150)
txtfld = Entry(window, border = 10)
txtfld.place(x = 175, y =100)

lbl = Label(window,text = 'My First Demo', font = 'Verdana')
lbl.place(x = 184, y = 50)

window.mainloop()