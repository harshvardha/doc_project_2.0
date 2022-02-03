import tkinter
from tkinter import Toplevel
from baseWindow import BaseWindow
from strings import ALERT, RESPONSE, WM_DELETE_WINDOW


class SearchDialog(Toplevel):
    def __init__(self, parent: BaseWindow, width: int, height: int, dialogName: str):
        super(SearchDialog, self).__init__(parent)
        self.parent = parent
        self.width = width
        self.height = height
        self.address = ""
        self.addressEntryBox: tkinter.Entry
        self.searchButton: tkinter.Button
        self.geometry("%dx%d+%d+%d" % (width, height,
                      self.winfo_rootx()+parent.screenWidth/2.6, self.winfo_rooty()+parent.screenWidth/5))
        self.title(dialogName)
        self.transient(parent)
        self.configure(bg="#FFFFFF")
        self._createUI()
        self.focus_set()
        self.grab_set()
        self.addressEntryBox.focus_set()
        self.bind("<Escape>", self._cancel)
        self.bind("<Return>", self._search)
        self.protocol(WM_DELETE_WINDOW, self._cancel)
        self.rowconfigure(1, weight=1)
        self.columnconfigure(0, weight=1)

    def _createUI(self):
        # Creating container frames
        frameProperties = {
            "height": self.height/5,
            "width": self.width,
            "bd": 0
        }
        frames = {
            "top": tkinter.Frame(master=self, bg="#6C7B95", **frameProperties),
            "middle": tkinter.Frame(master=self, bg="#FFFFFF", **frameProperties),
            "bottom": tkinter.Frame(master=self, bg="#6C7B95", **frameProperties)
        }
        for i, frame in enumerate(frames.values()):
            if(i == 1):
                frame.columnconfigure(1, weight=1)
            frame.grid(row=i, column=0, sticky=(
                tkinter.W, tkinter.E, tkinter.N))

        # Creating address label, entry widget and search button for middle frame
        textProperties = {
            "bg": "#FFFFFF",
            "fg": "#000000",
            "bd": 0,
            "font": ("Arial Rounded MT Bold", 15)
        }
        entryBoxProperties = {
            "width": 15,
            "bd": 0,
            "bg": "#FFFFFF",
            "font": ("Corbel Regular", 15),
            "highlightthickness": 2,
            "highlightcolor": "#b5bdc9"
        }
        searchButtonProperties = {
            "master": frames["middle"],
            "text": "Search",
            "bg": "#6C7B95",
            "bd": 0,
            "font": textProperties["font"],
            "activebackground": "#6C7B95",
            "activeforeground": "#FFFFFF",
            "fg": "#FFFFFF"
        }
        addressLabel = tkinter.Label(
            master=frames["middle"], text="Address : ", **textProperties)
        addressLabel.grid(row=0, column=0, sticky=tkinter.W)
        self.addressEntryBox = tkinter.Entry(
            master=frames["middle"], **entryBoxProperties)
        self.addressEntryBox.grid(row=0, column=1, sticky=(
            tkinter.W, tkinter.E, tkinter.N, tkinter.S), padx=10, pady=10)
        self.searchButton = tkinter.Button(**searchButtonProperties)
        self.searchButton.grid(row=1, column=0, columnspan=2,
                               sticky=(tkinter.S, tkinter.N))

    def _cancel(self, event=None):
        self.parent.focus_set()
        self.destroy()

    def _search(self):
        self.address = self.addressEntryBox.get()
        self.withdraw()
        self.update_idletasks()

    def getAddress(self):
        return self.address


class MessageDialog(Toplevel):
    def __init__(self, parent: BaseWindow, width: int, height: int, message: str):
        super(MessageDialog, self).__init__(parent)
        self.parent = parent
        self.width = width
        self.height = height
        self.message = message
        self.transient(parent)
        self.configure(bg="#FFFFFF")
        self.focus_set()
        self.grab_set()
        self.bind("<Escape>", self._cancel)
        self.bind("<Return>", self._ok)
        self.protocol(WM_DELETE_WINDOW, self._cancel)
        self.geometry("%dx%d+%d+%d" % (width, height, self.winfo_rootx() +
                      parent.screenWidth/2.6, self.winfo_rooty()+parent.screenHeight/5))
        self.rowconfigure(1, weight=1)
        self.columnconfigure(0, weight=1)
        self._createUI()

    def _createUI(self):
        # Creating continer frames
        frameProperties = {
            "height": self.height/7,
            "width": self.width,
            "bd": 0
        }
        frames = {
            "top": tkinter.Frame(master=self, bg="#6C7B95", **frameProperties),
            "middle": tkinter.Frame(master=self, bg="#FFFFFF", **frameProperties),
            "bottom": tkinter.Frame(master=self, bg="#6C7B95", **frameProperties)
        }
        for i, frame in enumerate(frames.values()):
            if(i == 1):
                frame.columnconfigure(0, weight=1)
                frame.rowconfigure(0, weight=1)
                frame.rowconfigure(1, weight=1)
            frame.grid(row=i, column=0, sticky=(
                tkinter.W, tkinter.E, tkinter.N))

        # Creating labels, text box and update button
        labelProperties = {
            "master": frames["middle"],
            "bg": "#FFFFFF",
            "fg": "#000000",
            "bd": 0,
            "wraplength": 350,
            "text": self.message,
            "font": ("Arial Rounded MT Bold", 15)
        }
        buttonProperties = {
            "master": frames["middle"],
            "width": 10,
            "text": "Ok",
            "bg": "#6C7B95",
            "bd": 0,
            "font": ("Arial Rounded MT Bold", 15),
            "activebackground": "#6C7B95",
            "activeforeground": "#FFFFFF",
            "fg": "#FFFFFF",
            "command": self._ok
        }
        messageLabel = tkinter.Label(**labelProperties)
        messageLabel.grid(row=0, column=0, sticky=(
            tkinter.W, tkinter.E, tkinter.N, tkinter.S), pady=12)
        okButton = tkinter.Button(**buttonProperties)
        okButton.grid(row=1, column=0, sticky=(
            tkinter.N, tkinter.S))

    def _cancel(self, event=None):
        self.parent.focus_set()
        self.destroy()

    def _ok(self, event=None):
        self.withdraw()
        self.update_idletasks()
        self._cancel()


class ResponseMessageDialog(MessageDialog):
    def __init__(self, parent: BaseWindow, width: int, height: int, message: str):
        super(ResponseMessageDialog, self).__init__(
            parent, width, height, message)
        self.title(RESPONSE)


class AlertMessageDialog(MessageDialog):
    def __init__(self, parent: BaseWindow, width: int, height: int, message: str):
        super(AlertMessageDialog, self).__init__(
            parent, width, height, message)
        self.title(ALERT)


if __name__ == "__main__":
    base = BaseWindow()
    #ResponseMessageDialog(base, 350, 150, "Saved Successfully")
    AlertMessageDialog(
        base, 350, 150, "No patient with this address exist")
    base.mainloop()
