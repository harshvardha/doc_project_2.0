from Schemas import PatientData
import strings
import images
import tkinter
from baseWindow import BaseWindow
from tkinter import N, S, W, E


class _Images:
    def __init__(self):
        self.BACK = tkinter.PhotoImage(file=images.BACK)


class MedicalRecord(BaseWindow):
    def __init__(self, patientInformation):
        super().__init__()
        self.title(strings.TITLE_MEDICAL_RECORD)
        self._imagesObj = _Images()
        self.buttons = {}
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.columnconfigure(1, weight=1)
        self.createUI(patientInformation)
        self.mainloop()

    def createUI(self, patientInformation):
        # Now creating the frames required for the window
        framesProperties = {
            "sideFrame": {
                "master": self,
                "bg": "#6C7B95",
                "bd": 0
            },
            "informationContainers": {
                "bg": "#FFFFFF",
                "bd": 1,
                "highlightthickness": 1,
                "highlightcolor": "#b5bdc9"
            },
            "infoLabelFrame": {
                "bg": "#FFFFFF",
                "font": ("Poppins-Medium", 16, "bold")
            }
        }
        frames = {
            "sideFrame": tkinter.Frame(**framesProperties["sideFrame"]),
            "basicInformation": tkinter.LabelFrame(master=self, **framesProperties["infoLabelFrame"], text="Patient Basic Information"),
            "medicalInformation": tkinter.LabelFrame(master=self, **framesProperties["infoLabelFrame"], text="Patient Medical Information")
        }
        frames["sideFrame"].grid(row=0, column=0, rowspan=2, sticky=(N, S))
        frames["sideFrame"].grid_columnconfigure(0, weight=1)
        for i in range(2):
            frames["basicInformation"].columnconfigure(i, weight=1)
            frames["basicInformation"].rowconfigure(i, weight=1)
            frames["medicalInformation"].columnconfigure(i, weight=1)
            frames["medicalInformation"].rowconfigure(i, weight=1)

        # Now creating the buttons for the sideFrame
        # first button : back
        # second button : home
        buttonProperties = {
            "bg": "#6C7B95",
            "bd": 0,
            "compound": tkinter.LEFT,
            "font": ("Poppins-Medium", 16, "bold"),
            "activebackground": "#6C7B95",
            "activeforeground": "#FFFFFF",
            "fg": "#FFFFFF"
        }
        self.buttons = {
            "back": tkinter.Button(master=frames["sideFrame"], text=strings.BACK, image=self._imagesObj.BACK, **buttonProperties),
        }

        # Now creating the label that will contain medical record
        labelProperties = {
            "headers": {
                "bg": "#6C7B95",
                "fg": "#000000",
                "font": ("Poppins-Medium", 16, "bold")
            },
            "information": {
                "bg": "#FFFFFF",
                "fg": "#000000",
                "font": ("Poppins-Medium", 16, "bold"),
                "wraplength": 530
            }
        }
        frames["basicInfoContainers"] = {
            "address": tkinter.Frame(master=frames["basicInformation"], **framesProperties["informationContainers"]),
            "name": tkinter.Frame(master=frames["basicInformation"], **framesProperties["informationContainers"]),
            "age": tkinter.Frame(master=frames["basicInformation"], **framesProperties["informationContainers"]),
            "gender": tkinter.Frame(master=frames["basicInformation"], **framesProperties["informationContainers"])
        }
        frames["medicalInfoContainers"] = {
            "symptoms": tkinter.Frame(master=frames["medicalInformation"], **framesProperties["informationContainers"]),
            "pathologicalInformation": tkinter.Frame(master=frames["medicalInformation"], **framesProperties["informationContainers"]),
            "disease": tkinter.Frame(master=frames["medicalInformation"], **framesProperties["informationContainers"]),
            "medicine": tkinter.Frame(master=frames["medicalInformation"], **framesProperties["informationContainers"])
        }
        labels = {
            "basicInformation": {
                "address": [
                    tkinter.Label(master=frames["basicInfoContainers"]["address"],
                                  text=strings.ADDRESS, **labelProperties["headers"]),
                    tkinter.Label(master=frames["basicInfoContainers"]["address"],
                                  text=patientInformation.address, **labelProperties["information"])
                ],
                "name": [
                    tkinter.Label(master=frames["basicInfoContainers"]["name"],
                                  text=strings.NAME, **labelProperties["headers"]),
                    tkinter.Label(master=frames["basicInfoContainers"]["name"],
                                  text=patientInformation.name, **labelProperties["information"])
                ],
                "age": [
                    tkinter.Label(master=frames["basicInfoContainers"]["age"],
                                  text=strings.AGE, **labelProperties["headers"]),
                    tkinter.Label(master=frames["basicInfoContainers"]["age"],
                                  text=patientInformation.age, **labelProperties["information"])
                ],
                "gender": [
                    tkinter.Label(master=frames["basicInfoContainers"]["gender"],
                                  text=strings.GENDER, **labelProperties["headers"]),
                    tkinter.Label(master=frames["basicInfoContainers"]["gender"],
                                  text=patientInformation.gender, **labelProperties["information"])
                ]
            },
            "medicalInformation": {
                "symptoms": [
                    tkinter.Label(master=frames["medicalInfoContainers"]["symptoms"],
                                  text=strings.SYMPTOMS, **labelProperties["headers"]),
                    tkinter.Label(master=frames["medicalInfoContainers"]["symptoms"],
                                  text=patientInformation.symptoms, **labelProperties["information"])
                ],
                "pathologicalInformation": [
                    tkinter.Label(master=frames["medicalInfoContainers"]["pathologicalInformation"],
                                  text=strings.PATHOLOGICAL_INFORMATION, **labelProperties["headers"]),
                    tkinter.Label(master=frames["medicalInfoContainers"]["pathologicalInformation"],
                                  text=patientInformation.pathologicalInformation, **labelProperties["information"])
                ],
                "disease": [
                    tkinter.Label(master=frames["medicalInfoContainers"]["disease"],
                                  text=strings.DISEASE, **labelProperties["headers"]),
                    tkinter.Label(master=frames["medicalInfoContainers"]["disease"],
                                  text=patientInformation.disease, **labelProperties["information"])
                ],
                "medicine": [
                    tkinter.Label(master=frames["medicalInfoContainers"]["medicine"],
                                  text=strings.MEDICINE, **labelProperties["headers"]),
                    tkinter.Label(master=frames["medicalInfoContainers"]["medicine"],
                                  text=patientInformation.medicine, **labelProperties["information"])
                ]
            }
        }

        # Now gridding the buttons of side frame
        for i, button in enumerate(self.buttons.values()):
            button.grid(row=i, column=0)

        # Now gridding the label frames
        frames["basicInformation"].grid(
            row=0, column=1, sticky=(W, E, N, S), padx=20, pady=20)
        frames["basicInformation"].columnconfigure(0, weight=1)
        frames["basicInformation"].columnconfigure(1, weight=1)
        frames["medicalInformation"].grid(
            row=1, column=1, sticky=(W, E, N, S), padx=20, pady=20)
        frames["medicalInformation"].columnconfigure(0, weight=1)
        frames["medicalInformation"].columnconfigure(1, weight=1)

        # Now gridding the information label containers
        self._gridInfoContainers(frames["basicInfoContainers"].values())
        self._gridInfoContainers(frames["medicalInfoContainers"].values())

        for frame in frames["basicInfoContainers"].values():
            frame.columnconfigure(0, weight=1)

        for frame in frames["medicalInfoContainers"].values():
            frame.columnconfigure(0, weight=1)

        # Now gridding the information labels
        for labelKey in labels.keys():
            for i, label in enumerate(labels[labelKey].values()):
                label[0].grid(row=0, column=0, sticky=(N, S, W, E))
                label[1].grid(row=1, column=0, sticky=(N, S, W, E))

    def _gridInfoContainers(self, frames):
        row = -1
        column = 0
        for i, frame in enumerate(frames):
            if(i % 2 == 0):
                row += 1
                column = 0
            else:
                column += 1
            frame.grid(row=row, column=column, sticky=(W, E))

    def getButtons(self):
        return self.buttons


# p = PatientData(
#     address="0xc3b19E1ee86d0387A7C0e82b6e3955629Db76D04",
#     name="Harshvardhan Singh Chauhan",
#     age=22,
#     gender="Male",
#     symptoms="high body temperature",
#     pathologicalInformation="Not Available",
#     disease="Fever",
#     medicine="paracetamol"
# )

# MedicalRecord(p)
