import images
import strings
import tkinter
from baseWindow import BaseWindow

class _Images:
    def __init__(self):
        self.SEARCH = tkinter.PhotoImage(file = images.SEARCH)
        self.SAVE = tkinter.PhotoImage(file = images.SAVE)
        self.RESET = tkinter.PhotoImage(file = images.RESET)
        self.ALL_RECORDS = tkinter.PhotoImage(file = images.ALL_RECORDS)
        self.HOME = tkinter.PhotoImage(file = images.HOME)

class AddNewPatient(BaseWindow):
    def __init__(self):
        super().__init__() 
        self.title(strings.TITLE_PRESCRIPTION)
        self._imagesObj = _Images()
        self._buttons = {}
        self.selectedGender = ""
        self._sharedVariable = tkinter.StringVar(value = 1)
        for i in range(3):
            self.rowconfigure(i, weight = 1)
        self._createUI()
        self.mainloop()

    def _createUI(self):
        # This function will create the UI for the add new patient window

        # # Now creating design frames who will be placed in 1st row and 3 row just for the look and feel
        framesProperties = {
            "infoLabelFrame" : {
                "bg" : "#FFFFFF",
                "font" : ("Arial Rounded MT Bold", 15)
            },
            "infoContainers" : {
                "bg" : "#FFFFFF",
                "bd" : 1,
                "highlightthickness" : 2,
                "highlightcolor" : "#b5bdc9"
            }
        }
        frames = {}
    
        # Now creating buttons for the window
        # secondButton : save
        # thirdButton : reset
        buttonProperties = {
            "bg" : "#6C7B95",
            "bd" : 0,
            "compound" : tkinter.LEFT,
            "font" : ("Arial Rounded MT Bold", 15),
            "activebackground" : "#6C7B95",
            "activeforeground" : "#FFFFFF",
            "fg" : "#FFFFFF"
        }

        # creating a frame to contain search and dashboard buttons
        sideFrame = tkinter.Frame(master = self, bg = "#6C7B95")
        sideFrame.grid(row = 0, rowspan = 3, sticky = (tkinter.N, tkinter.S, tkinter.W, tkinter.E))
        sideFrame.grid_columnconfigure(0, weight = 1)
        self._buttons = {
            "save" : tkinter.Button(master = self, text = strings.SAVE, image = self._imagesObj.SAVE, **buttonProperties),
            "reset" : tkinter.Button(master = self, text = strings.RESET, image = self._imagesObj.RESET, **buttonProperties),
            "search" : tkinter.Button(master = sideFrame, text = strings.SEARCH, image = self._imagesObj.SEARCH, **buttonProperties),
            "allRecords" : tkinter.Button(master = sideFrame, text = strings.ALL_RECORDS, image = self._imagesObj.ALL_RECORDS, **buttonProperties),
            "home" : tkinter.Button(master = sideFrame, text = strings.HOME, image = self._imagesObj.HOME, **buttonProperties)
        }
        
        # creating a labelFrame for the basic information entry and label widgets
        basicInfoLabelFrame = tkinter.LabelFrame(master = self, text = strings.ENTER_BASIC_INFORMATION, **framesProperties["infoLabelFrame"])
        basicInfoLabelFrame.grid(row = 0, column = 1, columnspan = 2, pady = 20)

        # creating a labelFrame for the medical information text and label widgets
        medicalInfoLabelFrame = tkinter.LabelFrame(master = self, text = strings.ENTER_MEDICAL_INFORMATION, **framesProperties["infoLabelFrame"])
        medicalInfoLabelFrame.grid(row = 1, column = 1, columnspan = 2, padx = 110)
        for i in range(2):
            basicInfoLabelFrame.columnconfigure(i, weight = 1)
            basicInfoLabelFrame.rowconfigure(i, weight = 1)
            basicInfoLabelFrame.grid_rowconfigure(i, pad = 30)
            basicInfoLabelFrame.grid_columnconfigure(i, pad = 30)
            medicalInfoLabelFrame.columnconfigure(i, weight = 1)
            medicalInfoLabelFrame.rowconfigure(i, weight = 1)
            medicalInfoLabelFrame.grid_rowconfigure(i, pad = 30)
            medicalInfoLabelFrame.grid_columnconfigure(i, pad = 30)
        
        # Now creating the widgets for basic information
        # case no : label, entry
        # name : label, entry
        # age : label, entry
        # gender : radiobuttons
        entryProperties = {
            "width" : 25,
            "bd" : 0,
            "bg" : "#b5bdc9",
            "font" : ("Corbel Regular", 15)
        }
        textProperties = {
            "width" : 50,
            "height" : 7,
            "bd" : 0,
            "bg" : "#b5bdc9",
            "font" : ("Corbel Regular", 15)
        }
        labelProperties = {
            "bg" : "#FFFFFF",
            "fg" : "#000000",
            "font" : ("Arial Rounded MT Bold", 15)
        }
        radioButtonProperties = {
            "bg" : "#FFFFFF",
            "bd" : 0,
            "font" : ("Arial Rounded MT Bold", 10),
            "variable" : self._sharedVariable,
            "command" : self._updateRadioButtonSelected
        }
        frames["basicInfoContainers"] = {
            "caseNo" : tkinter.Frame(master = basicInfoLabelFrame, **framesProperties["infoContainers"]),
            "name" : tkinter.Frame(master = basicInfoLabelFrame, **framesProperties["infoContainers"]),
            "age" : tkinter.Frame(master = basicInfoLabelFrame, **framesProperties["infoContainers"]),
            "gender" : tkinter.Frame(master = basicInfoLabelFrame, **framesProperties["infoContainers"])
        }
        frames["medicalInfoContainers"] = {
            "symptoms" : tkinter.Frame(master = medicalInfoLabelFrame, **framesProperties["infoContainers"]),
            "pathologicalInformation" : tkinter.Frame(master = medicalInfoLabelFrame, **framesProperties["infoContainers"]),
            "disease" : tkinter.Frame(master = medicalInfoLabelFrame, **framesProperties["infoContainers"]),
            "medicine" : tkinter.Frame(master = medicalInfoLabelFrame, **framesProperties["infoContainers"])
        }
        labels = {
            "basicInfo" : {
                "caseNo" : tkinter.Label(master = frames["basicInfoContainers"]["caseNo"], text = strings.CASE_NO, **labelProperties),
                "name" : tkinter.Label(master = frames["basicInfoContainers"]["name"], text = strings.NAME, **labelProperties),
                "age" : tkinter.Label(master = frames["basicInfoContainers"]["age"], text = strings.AGE, **labelProperties),
                "gender" : tkinter.Label(master = frames["basicInfoContainers"]["gender"], text = strings.GENDER, **labelProperties),
            },
            "medicalInfo" : {
                "symptoms" : tkinter.Label(master = frames["medicalInfoContainers"]['symptoms'], text = strings.SYMPTOMS, **labelProperties),
                "pathologicalInformation" : tkinter.Label(master = frames["medicalInfoContainers"]["pathologicalInformation"], text = strings.PATHOLOGICAL_INFORMATION, **labelProperties),
                "disease" : tkinter.Label(master = frames["medicalInfoContainers"]["disease"], text = strings.DISEASE, **labelProperties),
                "medicine" : tkinter.Label(master = frames["medicalInfoContainers"]["medicine"], text = strings.MEDICINE, **labelProperties)
            }
        }
        widgets = {
            "basicInfo" : {
                "caseNo" : tkinter.Entry(master = frames["basicInfoContainers"]["caseNo"], **entryProperties),
                "name" : tkinter.Entry(master = frames["basicInfoContainers"]["name"], **entryProperties),
                "age" : tkinter.Entry(master = frames["basicInfoContainers"]["age"], **entryProperties),
                "gender" : {
                    "maleRadioButton" : tkinter.Radiobutton(master = frames["basicInfoContainers"]["gender"], text = strings.MALE, value = strings.MALE, **radioButtonProperties),
                    "femaleRadioButton" : tkinter.Radiobutton(master = frames["basicInfoContainers"]["gender"], text = strings.FEMALE, value = strings.FEMALE, **radioButtonProperties),
                    "othersRadioButton" : tkinter.Radiobutton(master = frames["basicInfoContainers"]["gender"], text = strings.OTHERS, value = strings.OTHERS, **radioButtonProperties)
                }
            },
            "medicalInfo" : {
                "symptoms" : tkinter.Text(master = frames["medicalInfoContainers"]["symptoms"], **textProperties),
                "pathologicalInformation" : tkinter.Text(master = frames["medicalInfoContainers"]["pathologicalInformation"], **textProperties),
                "disease" : tkinter.Text(master = frames["medicalInfoContainers"]["disease"], **textProperties),
                "medicine" : tkinter.Text(master = frames["medicalInfoContainers"]["medicine"], **textProperties)
            }
        }

        # Now gridding the basic info widgets
        for label in labels["basicInfo"].items():
            label[1].grid(row = 0, sticky = (tkinter.W, tkinter.N, tkinter.S, tkinter.E))
            if(label[0] != "gender"):
                label[1].grid_configure(column = 0)
            else:
                label[1].grid_configure(columnspan = 3)

        for widget in widgets["basicInfo"].items():
            if(widget[0] != "gender"):
                widget[1].grid(row = 1, column = 0, sticky = (tkinter.E, tkinter.N, tkinter.S))
            else:
                for i, radioButton in enumerate(widget[1].values()):
                    radioButton.grid(row = 1, column = i, sticky = (tkinter.N, tkinter.S, tkinter.W, tkinter.E))
        self.gridContainers(list(frames["basicInfoContainers"].items()))

        # Now gridding the medical info widgets
        for label in labels["medicalInfo"].values():
            label.grid(row = 0, column = 0, sticky = (tkinter.N, tkinter.S))
        
        for widget in widgets["medicalInfo"].values():
            widget.grid(row = 1, column = 0)
        self.gridContainers(list(frames["medicalInfoContainers"].items()))
        
        # gridding the save and reset buttons
        row = 0
        for i, button in enumerate(self._buttons.items()):
            if(button[0] == "save" or button[0] == "reset"):
                button[1].grid(row = 2, column = i+1, pady = 20, ipadx = 5)
                if(i == 0):
                    button[1].grid_configure(sticky = (tkinter.E, tkinter.N), padx = 13)
                else:
                    button[1].grid_configure(sticky = (tkinter.W, tkinter.N), padx = 13)
            else:
                button[1].grid(row = row, column = 0, sticky = tkinter.W)
                row += 1
                if(button[0] == "search"):
                    button[1].grid_configure(padx = 5)
                elif(button[0] == "home"):
                    button[1].grid_configure(padx = 1)
    
    def gridContainers(self, containerList):
        for i in range(2):
            for j, container in enumerate(containerList[(i*i)+i : (i+1)*2]):
                container[1].grid(row = i, column = j)
    
    def _updateRadioButtonSelected(self, event = None):
        self.selectedGender = self._sharedVariable.get()
        print(self.selectedGender)
        
AddNewPatient()