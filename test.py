from tkinter import *


class MainWindow(Frame):
    def __init__(self):
        super().__init__()
        self.pack(expand=Y, fill=BOTH)

        outercanvas = Canvas(self, width=200, height=100, bg='#00ffff')
        outercanvas.pack(expand=Y, fill=BOTH)
        innerframe = Frame(self)
        innerframe.pack()
        innercanvas = Canvas(innerframe, width=100, height=50)

        outercanvas.create_window(50, 25, anchor=NW, window=innerframe)

        innercanvas.create_text(10, 10, anchor=NW, text="Hello")


root = MainWindow()
root.mainloop()
