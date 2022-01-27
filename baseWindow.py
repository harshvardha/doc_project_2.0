import tkinter


class BaseWindow(tkinter.Tk):
    def __init__(self):
        super().__init__()
        self.screenWidth = self.winfo_screenwidth()
        self.screenHeight = self.winfo_screenheight()
        self.geometry("%dx%d" % (self.screenWidth, self.screenHeight))
        self.configure(bg="#FFFFFF")
