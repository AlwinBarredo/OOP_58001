from tkinter import *
window = Tk()
window.geometry("400x200+10+10")
window.title("Grid Manager")

txt1 = Entry(window,bd=2)
txt1.grid(row=0, column=0)
txt1.insert(0, " " "row 0" " " "column 0")

txt2 = Entry(window,bd=2)
txt2.grid(row=0, column=1)
txt2.insert(0, " " "row 0" " " "column 1")

txt3 = Entry(window,bd=2)
txt3.grid(row=0, column=2)
txt3.insert(0, " " "row 0" " " "column 2")


txt4 = Entry(window,bd=2)
txt4.grid(row=1, column=0)
txt4.insert(0, " " "row 1" " " "column 0")

txt5 = Entry(window,bd=2)
txt5.grid(row=1, column=1)
txt5.insert(0, " " "row 1" " " "column 1")

txt6 = Entry(window,bd=2)
txt6.grid(row=1, column=2)
txt6.insert(0, " " "row 1" " " "column 2")


txt7 = Entry(window,bd=2)
txt7.grid(row=2, column=0)
txt7.insert(0, " " "row 2" " " "column 0")

txt8 = Entry(window,bd=2)
txt8.grid(row=2, column=1)
txt8.insert(0, " " "row 2" " " "column 1")

txt9 = Entry(window,bd=2)
txt9.grid(row=2, column=2)
txt9.insert(0, " " "row 2" " " "column 2")

txt10 = Entry(window,bd=2)
txt10.grid(row=3, column=0)
txt10.insert(0, " " "row 3" " " "column 0")

txt11 = Entry(window,bd=2)
txt11.grid(row=3, column=1)
txt11.insert(0, " " "row 3" " " "column 1")

txt12 = Entry(window,bd=2)
txt12.grid(row=3, column=2)
txt12.insert(0, " " "row 3" " " "column 2")

window.mainloop()