import tkinter

class BaseWindow(tkinter.Tk):
    def __init__(self):
        super().__init__()
        self.screenWidth = self.winfo_screenwidth()
        screenHeight = self.winfo_screenheight()
        self.geometry("%dx%d" % (self.screenWidth, screenHeight))
        self.configure(bg = "#FFFFFF")