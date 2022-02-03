from cProfile import label
import tkinter
from DialogBoxes import AlertMessageDialog, ResponseMessageDialog
from baseWindow import BaseWindow
from tkinter import N, W, E, S


class BasicFormStructure(tkinter.Frame):
    def __init__(self, parent: BaseWindow, formName: str):
        super(BasicFormStructure, self).__init__(master=parent,
                                                 width=parent.screenWidth, height=parent.screenHeight/20)
        self._formName = formName
        self._parent = parent
        self.credentialsWidgetsFrame: tkinter.Frame
        self.buttonsContainerFrame: tkinter.Frame
        self._parent.rowconfigure(1, weight=1)
        self._parent.columnconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self._createUI()

    def _createUI(self):
        frameProperties = {
            "border": {
                "master": self._parent,
                "height": self._parent.screenHeight/20,
                "width": self._parent.screenWidth,
                "bg": "#6C7B95",
                "bd": 0
            },
            "middle": {
                "master": self,
                "height": self._parent.screenHeight-200,
                "width": self._parent.screenWidth/4,
                "bg": "#f2f2f2",
                "highlightthickness": 1,
                "highlightbackground": "#97a2b4"
            }
        }
        # Creating top and bottom border frames
        borderFrames = {
            "top": tkinter.Frame(**frameProperties["border"]),
            "bottom": tkinter.Frame(**frameProperties["border"])
        }
        borderFrames["top"].grid(row=0, column=0, sticky=(W, E))
        borderFrames["bottom"].grid(row=2, column=0, sticky=(W, E))
        # Creating base container frame
        credentialsFrame = tkinter.Frame(**frameProperties["middle"])
        credentialsFrame.grid(
            row=0, column=0, sticky=(N, S, W, E), pady=100, padx=450)
        credentialsFrame.columnconfigure(0, weight=1)
        credentialsFrame.rowconfigure(0, weight=1)
        credentialsFrame.rowconfigure(1, weight=2)

        # Creating container frame for header label
        headerLabelContainerFrame = tkinter.Frame(
            master=credentialsFrame, bg="#6C7B95", bd=0)
        headerLabelContainerFrame.grid(row=0, column=0, sticky=(N, S, W, E))
        headerLabelContainerFrame.columnconfigure(0, weight=1)
        headerLabelContainerFrame.rowconfigure(0, weight=1)

        # Creating the header label
        labelProperties = {
            "master": headerLabelContainerFrame,
            "bg": "#6C7B95",
            "fg": "#FFFFFF",
            "bd": 0,
            "text": self._formName,
            "font": ("Poppins-Medium", 30, "bold"),
        }
        headerLabel = tkinter.Label(**labelProperties)
        headerLabel.grid(row=0, column=0, sticky=(N, S))

        # Creating credentials widget container frame
        self.credentialsWidgetsFrame = tkinter.Frame(
            master=credentialsFrame, bg="#f2f2f2", bd=0)
        self.credentialsWidgetsFrame.grid(row=1, column=0, sticky=(N, S, W, E))
        self.credentialsWidgetsFrame.columnconfigure(1, weight=1)

        # Creating button(s) container frame
        self.buttonsContainerFrame = tkinter.Frame(
            master=self.credentialsWidgetsFrame, bg="#f2f2f2", bd=0)
        self.buttonsContainerFrame.grid(row=4, column=0, columnspan=2)
        self.buttonsContainerFrame.columnconfigure(1, weight=1)


class LoginForm(BaseWindow):
    def __init__(self):
        super(LoginForm, self).__init__()
        self.entryBoxes: dict
        self._basicFormStructure = BasicFormStructure(self, "LOGIN")
        self._credentialsWidgetsFrame = self._basicFormStructure.credentialsWidgetsFrame
        self._buttonsContainerFrame = self._basicFormStructure.buttonsContainerFrame
        self._basicFormStructure.grid(row=1, column=0, sticky=(N, S, W, E))
        self._createUI()

    def _createUI(self):
        # Creating label and entry boxes for loginDetailsFrame
        labelProperties = {
            "master": self._credentialsWidgetsFrame,
            "bg": "#F2F2F2",
            "fg": "#6C7B95",
            "bd": 0,
            "font": ("Poppins-Medium", 16, "bold")
        }
        labels = {
            "address": tkinter.Label(**labelProperties, text="Address : "),
            "password": tkinter.Label(**labelProperties, text="Password : "),
            "privateKey": tkinter.Label(**labelProperties, text="Private Key : ")
        }
        entryBoxProperties = {
            "master": self._credentialsWidgetsFrame,
            "bd": 0,
            "bg": "#FFFFFF",
            "font": ("Poppins-Medium", 15),
            "highlightthickness": 2,
            "highlightcolor": "#b5bdc9"
        }
        self.entryBoxes = {
            "address": tkinter.Entry(**entryBoxProperties),
            "password": tkinter.Entry(**entryBoxProperties, show="*"),
            "privateKey": tkinter.Entry(**entryBoxProperties)
        }
        buttonProperties = {
            "master": self._buttonsContainerFrame,
            "width": 22,
            "bg": "#6C7B95",
            "bd": 0,
            "font": ("Poppins-Medium", 16, "bold"),
            "activebackground": "#FFFFFF",
            "activeforeground": "#6C7B95",
            "fg": "#FFFFFF",
        }
        self.buttons = {
            "login": tkinter.Button(**buttonProperties, text="Login"),
            "register": tkinter.Button(**buttonProperties, text="Register"),
            "forgetPassword": tkinter.Button(**buttonProperties, text="Forget password?")
        }

        for i, label in enumerate(labels.values()):
            label.grid(row=i, column=0, sticky=E)

        for i, entryBox in enumerate(self.entryBoxes.values()):
            entryBox.grid(row=i, column=1, sticky=(E, W), padx=20, pady=20)

        for i, button in enumerate(self.buttons.values()):
            if(i == 0 or i == 1):
                button.grid(row=0, column=i, padx=20)
            else:
                button.grid(row=1, column=0, columnspan=2, pady=20)
            if(i == 0):
                button.grid_configure(sticky=E, columnspan=1)
        self.entryBoxes["address"].focus_set()

    def displayErrorMessage(self):
        AlertMessageDialog(self, 350, 150, "Log in Failed")

    def getButtons(self):
        return self.buttons

    def getEntryBoxes(self):
        return self.entryBoxes


class RegisterForm(BaseWindow):
    def __init__(self):
        super(RegisterForm, self).__init__()
        self._entryBoxes: dict
        self._basicFormStructure = BasicFormStructure(self, "REGISTER")
        self._credentialsWidgetsFrame = self._basicFormStructure.credentialsWidgetsFrame
        self._buttonsContainerFrame = self._basicFormStructure.buttonsContainerFrame
        self._basicFormStructure.grid(row=1, column=0, sticky=(N, S, W, E))
        self._createUI()

    def _createUI(self):
        # Creating credentials widgets
        labelProperties = {
            "master": self._credentialsWidgetsFrame,
            "bg": "#F2F2F2",
            "fg": "#6C7B95",
            "bd": 0,
            "font": ("Poppins-Medium", 16, "bold")
        }
        labels = {
            "address": tkinter.Label(**labelProperties, text="Address : "),
            "name": tkinter.Label(**labelProperties, text="Name : "),
            "password": tkinter.Label(**labelProperties, text="Password : "),
            "privateKey": tkinter.Label(**labelProperties, text="Private Key : ")
        }
        entryBoxProperties = {
            "master": self._credentialsWidgetsFrame,
            "bd": 0,
            "bg": "#FFFFFF",
            "font": ("Poppins-Medium", 15),
            "highlightthickness": 2,
            "highlightcolor": "#b5bdc9"
        }
        self._entryBoxes = {
            "address": tkinter.Entry(**entryBoxProperties),
            "name": tkinter.Entry(**entryBoxProperties),
            "password": tkinter.Entry(**entryBoxProperties, show="*"),
            "privateKey": tkinter.Entry(**entryBoxProperties)
        }
        buttonProperties = {
            "master": self._buttonsContainerFrame,
            "text": "Register",
            "width": 22,
            "bg": "#6C7B95",
            "bd": 0,
            "font": ("Poppins-Medium", 16, "bold"),
            "activebackground": "#FFFFFF",
            "activeforeground": "#6C7B95",
            "fg": "#FFFFFF"
        }
        self.buttons = {
            "register": tkinter.Button(**buttonProperties)
        }
        for i, label in enumerate(labels.values()):
            label.grid(row=i, column=0, sticky=(E))

        for i, entryBox in enumerate(self._entryBoxes.values()):
            entryBox.grid(row=i, column=1, sticky=(E, W), padx=20, pady=20)
        self.buttons["register"].grid(row=0, column=0)
        self._entryBoxes["address"].focus_set()

    def displayErrorMessage(self):
        AlertMessageDialog(self, 350, 150, "Registration Failed")

    def displaySuccessMessage(self):
        ResponseMessageDialog(self, 350, 150, "Registered Successfully")

    def getButtons(self):
        return self.buttons

    def getEntryBoxes(self):
        return self._entryBoxes


class ForgetPassword(BaseWindow):
    def __init__(self):
        super(ForgetPassword, self).__init__()
        self._entryBoxes: dict
        self._basicFormStructure = BasicFormStructure(self, "RESET PASSWORD")
        self._credentialsWidgetsFrame = self._basicFormStructure.credentialsWidgetsFrame
        self._buttonsContainerFrame = self._basicFormStructure.buttonsContainerFrame
        self._basicFormStructure.grid(row=1, column=0, sticky=(N, S, W, E))
        self._createUI()

    def _createUI(self):
        # Creating credentials widgets
        labelProperties = {
            "master": self._credentialsWidgetsFrame,
            "bg": "#F2F2F2",
            "fg": "#6C7B95",
            "bd": 0,
            "font": ("Poppins-Medium", 16, "bold")
        }
        labels = {
            "address": tkinter.Label(**labelProperties, text="Address : "),
            "newPassword": tkinter.Label(**labelProperties, text="New Password : "),
            "privateKey": tkinter.Label(**labelProperties, text="Private Key : ")
        }
        entryBoxProperties = {
            "master": self._credentialsWidgetsFrame,
            "bd": 0,
            "bg": "#FFFFFF",
            "font": ("Poppins-Medium", 15),
            "highlightthickness": 2,
            "highlightcolor": "#b5bdc9"
        }
        self._entryBoxes = {
            "address": tkinter.Entry(**entryBoxProperties),
            "newPassword": tkinter.Entry(**entryBoxProperties),
            "privateKey": tkinter.Entry(**entryBoxProperties)
        }
        buttonProperties = {
            "master": self._buttonsContainerFrame,
            "text": "Reset",
            "width": 22,
            "bg": "#6C7B95",
            "bd": 0,
            "font": ("Poppins-Medium", 16, "bold"),
            "activebackground": "#FFFFFF",
            "activeforeground": "#6C7B95",
            "fg": "#FFFFFF"
        }
        self.buttons = {
            "reset": tkinter.Button(**buttonProperties)
        }

        for i, label in enumerate(labels.values()):
            label.grid(row=i, column=0, sticky=E)

        for i, entryBox in enumerate(self._entryBoxes.values()):
            entryBox.grid(row=i, column=1, sticky=(W, E), padx=20, pady=20)

        self.buttons["reset"].grid(row=0, column=0)
        self._entryBoxes["address"].focus_set()

    def displayErrorMessage(self):
        AlertMessageDialog(self, 350, 150, "Reset Password Failed")

    def displaySuccessMessage(self):
        ResponseMessageDialog(self, 350, 150, "Password Reset Successful")

    def getButtons(self):
        return self.buttons

    def getEntryBoxes(self):
        return self._entryBoxes


if __name__ == "__main__":
    ForgetPassword().mainloop()
