import images
import strings
import tkinter
from baseWindow import BaseWindow

class _Images:
    def __init__(self):
        self.ADD_NEW_PATIENT_BUTTON_IMAGE = tkinter.PhotoImage(file = images.ADD_NEW_PATIENT)
        self.SEARCH_MEDICAL_REPORT = tkinter.PhotoImage(file = images.SEARCH_PATIENT_RECORD)
        self.ALL_MEDICAL_RECORDS = tkinter.PhotoImage(file = images.ALL_MEDICAL_RECORDS)

class OptionsWindow(BaseWindow):

    # This is the first window that opens when application first starts
    def __init__(self):
        super().__init__()
        self.rowconfigure(1, weight = 1)
        self._imagesObj = _Images()
        self.buttons = {}
        self.createUI()
        self.mainloop()
    
    def createUI(self):
        # This function will create the UI for options window

        # Now creating design frames who will be placed in 1st row and 3 row just for the look and feel
        designFramesProperties = {
            "width" : self.screenWidth,
            "height" : 36,
            "bg" : "#6C7B95"
        }
        designFrames = {
            "frame1" : tkinter.Frame(master = self, **designFramesProperties),
            "frame2" : tkinter.Frame(master = self, **designFramesProperties)
        }
        # Now putting design frames in root using grid layout manager
        for i in range(2):
            designFrames["frame"+str(i+1)].grid(column = 0, row = (i+1)*i, sticky = (tkinter.W, tkinter.E, tkinter.S, tkinter.N))
        
        # Now creating the buttons required for the window
        # first button will be used to open the window to add a new patient
        # second button will be used to search for the patient
        # third button will be used to see all the records of patients
        buttonsContainer = tkinter.Frame(master = self, bg = "#FFFFFF")
        for i in range(3):
            buttonsContainer.columnconfigure(i, weight = 1)
        buttonsContainer.grid(row = 1, column = 0, sticky = (tkinter.N, tkinter.S, tkinter.E, tkinter.W))
        buttonProperties = {
            "bg" : "#ffffff",
            "bd" : 0,
            "activebackground" : "#f2f2f2",
            "compound" : tkinter.TOP,
            "font" : ("Arial Rounded MT Bold", 15),
            "wraplength" : 400
        }
        self.buttons = {
            "addNewPatient" : tkinter.Button(master = buttonsContainer, text = strings.ADD_NEW_PATIENT, image = self._imagesObj.ADD_NEW_PATIENT_BUTTON_IMAGE, **buttonProperties),
            "searchPatient" : tkinter.Button(master = buttonsContainer, text = strings.SEARCH_PATIENT, image = self._imagesObj.SEARCH_MEDICAL_REPORT, **buttonProperties),
            "displayAllRecords" : tkinter.Button(master = buttonsContainer, text = strings.ALL_MEDICAL_RECORDS, image = self._imagesObj.ALL_MEDICAL_RECORDS, **buttonProperties)
        }
        for i, button in enumerate(self.buttons.values()):
            button.grid(row = 0, column = i, sticky = (tkinter.W, tkinter.E), pady = 260)
            if(i % 2 == 0):
                button.grid_configure(padx = 250)

OptionsWindow()