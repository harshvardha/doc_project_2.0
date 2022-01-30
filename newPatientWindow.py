import images
import strings
import tkinter
from tkinter import N, S, W, E
from baseWindow import BaseWindow
from DialogBoxes import ResponseMessageDialog, AlertMessageDialog, SearchDialog


class _Images:
    def __init__(self):
        self.SEARCH = tkinter.PhotoImage(file=images.SEARCH)
        self.SAVE = tkinter.PhotoImage(file=images.SAVE)
        self.RESET = tkinter.PhotoImage(file=images.RESET)
        self.ALL_RECORDS = tkinter.PhotoImage(file=images.ALL_RECORDS)
        self.HOME = tkinter.PhotoImage(file=images.HOME)


class AddNewPatient(BaseWindow):
    def __init__(self):
        super().__init__()
        self.title(strings.TITLE_PRESCRIPTION)
        self._imagesObj = _Images()
        self._buttons = {}
        self.widgets = {}
        self.selectedGender = ""
        self._sharedVariable = tkinter.StringVar(value=1)
        for i in range(3):
            self.rowconfigure(i, weight=1)
        self._createUI()
        self.mainloop()

    def _createUI(self):
        # This function will create the UI for the add new patient window

        # # Now creating design frames who will be placed in 1st row and 3 row just for the look and feel
        framesProperties = {
            "infoLabelFrame": {
                "bg": "#FFFFFF",
                "font": ("Poppins-Medium", 16, "bold")
            },
            "infoContainers": {
                "bg": "#FFFFFF",
                "bd": 1,
                "highlightthickness": 2,
                "highlightcolor": "#b5bdc9"
            }
        }
        frames = {}

        # Now creating buttons for the window
        # secondButton : save
        # thirdButton : reset
        buttonProperties = {
            "bg": "#6C7B95",
            "bd": 0,
            "compound": tkinter.LEFT,
            "font": ("Poppins-Medium", 16, "bold"),
            "activebackground": "#6C7B95",
            "activeforeground": "#FFFFFF",
            "fg": "#FFFFFF"
        }

        # creating a frame to contain search and dashboard buttons
        sideFrame = tkinter.Frame(master=self, bg="#6C7B95")
        sideFrame.grid(row=0, rowspan=3, sticky=(
            tkinter.N, tkinter.S, tkinter.W, tkinter.E))
        sideFrame.grid_columnconfigure(0, weight=1)
        self._buttons = {
            "save": tkinter.Button(master=self, text=strings.SAVE, image=self._imagesObj.SAVE, **buttonProperties),
            "reset": tkinter.Button(master=self, text=strings.RESET, image=self._imagesObj.RESET, command=self._reset, **buttonProperties),
            "search": tkinter.Button(master=sideFrame, text=strings.SEARCH, image=self._imagesObj.SEARCH, **buttonProperties),
            "allRecords": tkinter.Button(master=sideFrame, text=strings.ALL_RECORDS, image=self._imagesObj.ALL_RECORDS, **buttonProperties)
        }

        # creating a labelFrame for the basic information entry and label widgets
        basicInfoLabelFrame = tkinter.LabelFrame(
            master=self, text=strings.ENTER_BASIC_INFORMATION, **framesProperties["infoLabelFrame"])
        basicInfoLabelFrame.grid(row=0, column=1, columnspan=2, pady=20)

        # creating a labelFrame for the medical information text and label widgets
        medicalInfoLabelFrame = tkinter.LabelFrame(
            master=self, text=strings.ENTER_MEDICAL_INFORMATION, **framesProperties["infoLabelFrame"])
        medicalInfoLabelFrame.grid(row=1, column=1, columnspan=2, padx=110)
        for i in range(2):
            basicInfoLabelFrame.columnconfigure(i, weight=1)
            basicInfoLabelFrame.rowconfigure(i, weight=1)
            basicInfoLabelFrame.grid_rowconfigure(i, pad=30)
            basicInfoLabelFrame.grid_columnconfigure(i, pad=30)
            medicalInfoLabelFrame.columnconfigure(i, weight=1)
            medicalInfoLabelFrame.rowconfigure(i, weight=1)
            medicalInfoLabelFrame.grid_rowconfigure(i, pad=30)
            medicalInfoLabelFrame.grid_columnconfigure(i, pad=30)

        # Now creating the widgets for basic information
        # case no : label, entry
        # name : label, entry
        # age : label, entry
        # gender : radiobuttons
        entryProperties = {
            "width": 25,
            "bd": 0,
            "bg": "#b5bdc9",
            "font": ("Poppins-Medium", 15)
        }
        textProperties = {
            "width": 50,
            "height": 7,
            "bd": 0,
            "bg": "#b5bdc9",
            "font": ("Poppins-Medium", 15)
        }
        labelProperties = {
            "bg": "#FFFFFF",
            "fg": "#000000",
            "font": ("Poppins-Medium", 16, "bold")
        }
        radioButtonProperties = {
            "bg": "#FFFFFF",
            "bd": 0,
            "font": ("Poppins-Medium", 10),
            "variable": self._sharedVariable,
            "command": self._updateRadioButtonSelected
        }
        frames["basicInfoContainers"] = {
            "address": tkinter.Frame(master=basicInfoLabelFrame, **framesProperties["infoContainers"]),
            "name": tkinter.Frame(master=basicInfoLabelFrame, **framesProperties["infoContainers"]),
            "age": tkinter.Frame(master=basicInfoLabelFrame, **framesProperties["infoContainers"]),
            "gender": tkinter.Frame(master=basicInfoLabelFrame, **framesProperties["infoContainers"])
        }
        frames["medicalInfoContainers"] = {
            "symptoms": tkinter.Frame(master=medicalInfoLabelFrame, **framesProperties["infoContainers"]),
            "pathologicalInformation": tkinter.Frame(master=medicalInfoLabelFrame, **framesProperties["infoContainers"]),
            "disease": tkinter.Frame(master=medicalInfoLabelFrame, **framesProperties["infoContainers"]),
            "medicine": tkinter.Frame(master=medicalInfoLabelFrame, **framesProperties["infoContainers"])
        }
        labels = {
            "basicInfo": {
                "address": tkinter.Label(master=frames["basicInfoContainers"]["address"], text=strings.ADDRESS, **labelProperties),
                "name": tkinter.Label(master=frames["basicInfoContainers"]["name"], text=strings.NAME, **labelProperties),
                "age": tkinter.Label(master=frames["basicInfoContainers"]["age"], text=strings.AGE, **labelProperties),
                "gender": tkinter.Label(master=frames["basicInfoContainers"]["gender"], text=strings.GENDER, **labelProperties),
            },
            "medicalInfo": {
                "symptoms": tkinter.Label(master=frames["medicalInfoContainers"]['symptoms'], text=strings.SYMPTOMS, **labelProperties),
                "pathologicalInformation": tkinter.Label(master=frames["medicalInfoContainers"]["pathologicalInformation"], text=strings.PATHOLOGICAL_INFORMATION, **labelProperties),
                "disease": tkinter.Label(master=frames["medicalInfoContainers"]["disease"], text=strings.DISEASE, **labelProperties),
                "medicine": tkinter.Label(master=frames["medicalInfoContainers"]["medicine"], text=strings.MEDICINE, **labelProperties)
            }
        }
        self.widgets = {
            "basicInfo": {
                "address": tkinter.Entry(master=frames["basicInfoContainers"]["address"], **entryProperties),
                "name": tkinter.Entry(master=frames["basicInfoContainers"]["name"], **entryProperties),
                "age": tkinter.Entry(master=frames["basicInfoContainers"]["age"], **entryProperties),
                "gender": {
                    "male": tkinter.Radiobutton(master=frames["basicInfoContainers"]["gender"], text=strings.MALE, value=strings.MALE, **radioButtonProperties),
                    "female": tkinter.Radiobutton(master=frames["basicInfoContainers"]["gender"], text=strings.FEMALE, value=strings.FEMALE, **radioButtonProperties),
                    "others": tkinter.Radiobutton(master=frames["basicInfoContainers"]["gender"], text=strings.OTHERS, value=strings.OTHERS, **radioButtonProperties)
                }
            },
            "medicalInfo": {
                "symptoms": tkinter.Text(master=frames["medicalInfoContainers"]["symptoms"], **textProperties),
                "pathologicalInformation": tkinter.Text(master=frames["medicalInfoContainers"]["pathologicalInformation"], **textProperties),
                "disease": tkinter.Text(master=frames["medicalInfoContainers"]["disease"], **textProperties),
                "medicine": tkinter.Text(master=frames["medicalInfoContainers"]["medicine"], **textProperties)
            }
        }

        # Now gridding the basic info widgets
        for label in labels["basicInfo"].items():
            label[1].grid(row=0, sticky=(W, N, S, E))
            if(label[0] != "gender"):
                label[1].grid_configure(column=0)
            else:
                label[1].grid_configure(columnspan=3)

        for widget in self.widgets["basicInfo"].items():
            if(widget[0] != "gender"):
                widget[1].grid(row=1, column=0, sticky=(E, N, S))
            else:
                for i, radioButton in enumerate(widget[1].values()):
                    radioButton.grid(row=1, column=i, sticky=(N, S, W, E))
        self.gridContainers(list(frames["basicInfoContainers"].items()))

        # Now gridding the medical info widgets
        for label in labels["medicalInfo"].values():
            label.grid(row=0, column=0, sticky=(N, S))

        for widget in self.widgets["medicalInfo"].values():
            widget.grid(row=1, column=0)
        self.gridContainers(list(frames["medicalInfoContainers"].items()))

        # gridding the save and reset buttons
        row = 0
        for i, button in enumerate(self._buttons.items()):
            if(button[0] == "save" or button[0] == "reset"):
                button[1].grid(row=2, column=i+1, pady=20, ipadx=5)
                if(i == 0):
                    button[1].grid_configure(
                        sticky=(E, N), padx=13)
                else:
                    button[1].grid_configure(
                        sticky=(W, N), padx=13)
            else:
                button[1].grid(row=row, column=0, sticky=tkinter.W)
                row += 1
                if(button[0] == "search"):
                    button[1].grid_configure(padx=5)
                elif(button[0] == "home"):
                    button[1].grid_configure(padx=1)

    def gridContainers(self, containerList):
        for i in range(2):
            for j, container in enumerate(containerList[(i*i)+i: (i+1)*2]):
                container[1].grid(row=i, column=j)

    def _updateRadioButtonSelected(self, event=None):
        self.selectedGender = self._sharedVariable.get()

    def _reset(self):
        basic = self.widgets["basicInfo"]
        for i, box in enumerate(basic.values()):
            if(i != 3):
                box.delete(0, tkinter.END)
        medical = self.widgets["medicalInfo"]
        for box in medical.values():
            box.delete("1.0", tkinter.END)

    def displaySuccessMessage(self):
        ResponseMessageDialog(self, 350, 150, "Saved Successfully")

    def displayErrorMessage(self):
        AlertMessageDialog(self, 350, 150, "Error Saving Data")

    def displaySearchDialog(self) -> str:
        searchDialog = SearchDialog(self, 350, 150, "Search Patient")
        return searchDialog.getAddress()

    def getButtons(self):
        return self._buttons

    def getInformationWidgets(self):
        return self.widgets


# AddNewPatient()
