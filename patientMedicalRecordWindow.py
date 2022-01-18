import strings
import images
import tkinter
from baseWindow import BaseWindow

class _Images:
    def __init__(self):
        self.BACK = tkinter.PhotoImage(file = images.BACK)
        self.HOME = tkinter.PhotoImage(file = images.HOME)

class MedicalRecord(BaseWindow):
    def __init__(self, patientInformation):
        super().__init__()
        self.title(strings.TITLE_MEDICAL_RECORD)
        self._imagesObj = _Images()
        self.buttons = {}
        self.grid_rowconfigure(0, weight = 1)
        self.grid_rowconfigure(1, weight = 1)
        self.grid_columnconfigure(1, weight = 1)
        self.createUI(patientInformation)
        self.mainloop()
    
    def createUI(self, patientInformation):
        # This function will create the UI for the medical record window

        # Now creating the frames required for the window
        framesProperties = {
            "sideFrame" : {
            "bg" : "#6C7B95",
            "bd" : 0
            },
            "informationContainers" : {
                "bg" : "#FFFFFF",
                "bd" : 1,
                "highlightthickness" : 1,
                "highlightcolor" : "#b5bdc9"
            },
            "infoLabelFrame" : {
                "bg" : "#FFFFFF",
                "font" : ("Arial Rounded MT Bold", 15)
            }
        }
        frames = {
            "sideFrame" : tkinter.Frame(master = self, **framesProperties["sideFrame"]),
            "basicInformation" : tkinter.LabelFrame(master = self, text = "Patient Basic Information", **framesProperties["infoLabelFrame"]),
            "medicalInformation" : tkinter.LabelFrame(master = self, text = "Patient Medical Information", **framesProperties["infoLabelFrame"])
        }
        frames["sideFrame"].grid(row = 0, column = 0, rowspan = 2, sticky = (tkinter.N, tkinter.S, tkinter.W))
        frames["sideFrame"].grid_columnconfigure(0, weight = 1)

        # Now creating the buttons for the sideFrame
        # first button : back
        # second button : home
        buttonProperties = {    
            "bg" : "#6C7B95",
            "bd" : 0,
            "compound" : tkinter.LEFT,
            "font" : ("Arial Rounded MT Bold", 15),
            "activebackground" : "#6C7B95",
            "activeforeground" : "#FFFFFF",
            "fg" : "#FFFFFF"
        }
        self.buttons = {
            "back" : tkinter.Button(master = frames["sideFrame"], text = strings.BACK, image = self._imagesObj.BACK, **buttonProperties),
            "home" : tkinter.Button(master = frames["sideFrame"], text = strings.HOME, image = self._imagesObj.HOME, **buttonProperties)
        }
        
        # Now creating the label that will contain medical record
        labelProperties = {
            "headers" : {
                "bg" : "#FFFFFF",
                "fg" : "#000000",
                "font" : ("Arial Rounded MT Bold", 15)
            },
            "information" : {
                "bg" : "#FFFFFF",
                "fg" : "#000000",
                "font" : ("Corbel Regular", 15)
            }
        }
        frames["basicInfoContainers"] = {
            "caseNo" : tkinter.Frame(master = frames["basicInformation"], **framesProperties["informationContainers"]),
            "name" : tkinter.Frame(master = frames["basicInformation"], **framesProperties["informationContainers"]),
            "age" : tkinter.Frame(master = frames["basicInformation"], **framesProperties["informationContainers"]),
            "gender" : tkinter.Frame(master = frames["basicInformation"], **framesProperties["informationContainers"])
        }
        frames["medicalInfoContainers"] = {
            "symptoms" : tkinter.Frame(master = frames["medicalInformation"], **framesProperties["informationContainers"]),
            "pathologicalInformation" : tkinter.Frame(master = frames["medicalInformation"], **framesProperties["informationContainers"]),
            "disease" : tkinter.Frame(master = frames["medicalInformation"], **framesProperties["informationContainers"]),
            "medicine" : tkinter.Frame(master = frames["medicalInformation"], **framesProperties["informationContainers"])
        }
        labels = {
            "basicInformation" : {
                "caseNo" : [
                    tkinter.Label(master = frames["basicInfoContainers"]["caseNo"], text = strings.CASE_NO, **labelProperties["headers"]),
                    tkinter.Label(master = frames["basicInfoContainers"]["caseNo"], text = patientInformation["caseNo"], **labelProperties["information"])
                ],
                "name" : [
                    tkinter.Label(master = frames["basicInfoContainers"]["name"], text = strings.NAME, **labelProperties["headers"]),
                    tkinter.Label(master = frames["basicInfoContainers"]["name"], text = patientInformation["name"], **labelProperties["information"])
                ],
                "age" : [
                    tkinter.Label(master = frames["basicInfoContainers"]["age"], text = strings.AGE, **labelProperties["headers"]),
                    tkinter.Label(master = frames["basicInfoContainers"]["age"], text = patientInformation["age"], **labelProperties["information"])
                ],
                "gender" : [
                    tkinter.Label(master = frames["basicInfoContainers"]["gender"], text = strings.GENDER, **labelProperties["headers"]),
                    tkinter.Label(master = frames["basicInfoContainers"]["gender"], text = patientInformation["gender"], **labelProperties["information"])
                ]
            },
            "medicalInformation" : {
                "symptoms" : [
                    tkinter.Label(master = frames["medicalInfoContainers"]["symptoms"], text = strings.SYMPTOMS, **labelProperties["headers"]),
                    tkinter.Label(master = frames["medicalInfoContainers"]["symptoms"], text = patientInformation["symptoms"], **labelProperties["information"])
                ],
                "pathologicalInformation" : [
                    tkinter.Label(master = frames["medicalInfoContainers"]["pathologicalInformation"], text = strings.PATHOLOGICAL_INFORMATION, **labelProperties["headers"]),
                    tkinter.Label(master = frames["medicalInfoContainers"]["pathologicalInformation"], text = patientInformation["pathologicalInformation"], **labelProperties["information"])
                ],
                "disease" : [
                    tkinter.Label(master = frames["medicalInfoContainers"]["disease"], text = strings.DISEASE, **labelProperties["headers"]),
                    tkinter.Label(master = frames["medicalInfoContainers"]["disease"], text = patientInformation["disease"], **labelProperties["information"])
                ],
                "medicine" : [
                    tkinter.Label(master = frames["medicalInfoContainers"]["medicine"], text = strings.MEDICINE, **labelProperties["headers"]),
                    tkinter.Label(master = frames["medicalInfoContainers"]["medicine"], text = patientInformation["medicine"], **labelProperties["information"])
                ]
            }
        }

        # Now gridding the buttons of side frame
        for i, button in enumerate(self.buttons.values()):
            button.grid(row = i, column = 0, sticky = (tkinter.W))

        # Now gridding the information labels
        for labelKey in labels.keys():
            for label in labels[labelKey].values():
                label[0].grid(row = 0, column = 0)
                label[1].grid(row = 1, column = 0)
        
        # Now gridding the information label containers
        self._gridInfoContainers(frames["basicInfoContainers"].values())
        self._gridInfoContainers(frames["medicalInfoContainers"].values())

        # Now gridding the label frames
        frames["basicInformation"].grid(row = 0, column = 1)
        frames["medicalInformation"].grid(row = 1, column = 1)
    
    def _gridInfoContainers(self, frames):
        row = -1
        column = 0
        for i, frame in enumerate(frames):
            if(i % 2 == 0):
                row += 1
                column = 0
            else:
                column += 1
        frame.grid(row = row, column = column)

p = {
    "caseNo" : 1,
    "name" : "Harshvardhan Singh Chauhan",
    "age" : 22,
    "gender" : "Male",
    "symptoms" : "Naak beh rahi hai",
    "pathologicalInformation" : "Not Available",
    "disease" : "Common cold",
    "medicine" : "paracetamol"
}

MedicalRecord(p)