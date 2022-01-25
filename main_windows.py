from tkinter import S
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

import select
import socket
import sys

HOST = "127.0.0.1"
PORT = 1100

# connect to server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))


# Main Window user interface class
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        # create the window, set font, geometry, layout
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 400)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic")
        font.setPointSize(12)
        self.centralwidget.setFont(font)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(60, 110, 281, 231))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        
        # LOGIN push button
        self.loginButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.loginButton.setObjectName("loginButton")
        self.verticalLayout.addWidget(self.loginButton)
        self.loginButton.clicked.connect(self.openLoginWindow) # open Login Window via function

        # REGISTER push button
        self.registerButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.registerButton.setObjectName("registerButton")
        self.verticalLayout.addWidget(self.registerButton)
        self.registerButton.clicked.connect(self.openRegisterWindow) # open Register Window via function

        # EXIT push button
        self.exitButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.exitButton.setObjectName("exitButton")
        self.verticalLayout.addWidget(self.exitButton)
        self.exitButton.clicked.connect(self.showExitPopup) # open Exit Popup via function

        # set parameters for Main Window title - Chat Client
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(60, 40, 281, 51))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic")
        font.setPointSize(24)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter) # Chat Client title in the middle
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)

        # set parameters for menu bar with push buttons
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 400, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        # set parameters for status bar
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        # set titles for each component
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.loginButton.setText(_translate("MainWindow", "Log in"))
        self.registerButton.setText(_translate("MainWindow", "Register"))
        self.exitButton.setText(_translate("MainWindow", "Exit"))
        self.label.setText(_translate("MainWindow", "Chat Client"))
    
    # open Login Window function
    def openLoginWindow(self):
        self.window = QtWidgets.QDialog()
        self.ui = Ui_Login()
        self.ui.setupUi(self.window)
        # MainWindow.hide()
        self.window.show()

    # open Register Window function
    def openRegisterWindow(self):
        self.window = QtWidgets.QDialog()
        self.ui = Ui_Register()
        self.ui.setupUi(self.window)
        # MainWindow.hide()
        self.window.show()

    # open Logout Popup function
    def showLogoutPopup(self):
        msg = QMessageBox()
        msg.setWindowTitle("Log out")
        msg.setText("Are you sure you want to log out?")
        msg.setIcon(QMessageBox.Question)
        msg.setStandardButtons(QMessageBox.Yes|QMessageBox.No)
        msg.exec_()

    # open Exit Popup function
    def showExitPopup(self):
        msg = QMessageBox()
        msg.setWindowTitle("Exit")
        msg.setText("Are you sure you want to exit?")
        msg.setIcon(QMessageBox.Warning)
        msg.setStandardButtons(QMessageBox.Yes|QMessageBox.No)
        ret = msg.exec_()

        # close app if exit confirmed
        if ret == QMessageBox.Yes:
            sys.exit(app.exec_())

    # open Error Popup function
    def showErrorPopup(self):
        msg = QMessageBox()
        msg.setWindowTitle("Error")
        msg.setText("err")
        msg.setIcon(QMessageBox.Critical)
        msg.exec_()


# Login user interface class
class Ui_Login(object):
    def setupUi(self, Login):
        # create the window, set geometry
        Login.setObjectName("Login")
        Login.resize(400, 400)
        self.buttonBox = QtWidgets.QDialogButtonBox(Login)
        self.buttonBox.setGeometry(QtCore.QRect(10, 350, 371, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)

        # set buttons to log in and cancel
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.frame = QtWidgets.QFrame(Login)
        self.frame.setGeometry(QtCore.QRect(20, 100, 361, 231))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")

        # set username line
        self.usernameLine = QtWidgets.QLineEdit(self.frame)
        self.usernameLine.setGeometry(QtCore.QRect(50, 40, 251, 22))
        self.usernameLine.setObjectName("usernameLine")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(50, 10, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")

        # set password line
        self.passwordLine = QtWidgets.QLineEdit(self.frame)
        self.passwordLine.setGeometry(QtCore.QRect(50, 110, 251, 22))
        self.passwordLine.setObjectName("passwordLine")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(50, 80, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        # set parameters for Main Window title - Login
        self.label_3 = QtWidgets.QLabel(Login)
        self.label_3.setGeometry(QtCore.QRect(20, 30, 181, 31))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic")
        font.setPointSize(18)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")

        self.retranslateUi(Login)

        # Accept and reject buttons actions
        self.buttonBox.accepted.connect(self.acceptLogin) # send login data if accepted
        self.buttonBox.accepted.connect(Login.accept)

        self.buttonBox.rejected.connect(Login.reject)

        QtCore.QMetaObject.connectSlotsByName(Login)

    def retranslateUi(self, Login):
        _translate = QtCore.QCoreApplication.translate
        # set titles for each component
        Login.setWindowTitle(_translate("Login", "Login"))
        self.label.setText(_translate("Login", "username"))
        self.label_2.setText(_translate("Login", "password"))
        self.label_3.setText(_translate("Login", "Log in"))

    # send login data to server
    def acceptLogin(self):
        username = self.usernameLine.text()
        password = self.passwordLine.text()
        s.send(bytes("#LOGIN#"+username+"#"+password+"#", "utf-8"))
        # TODO show errors


# Register user interface class
class Ui_Register(object):
    def setupUi(self, Register):
        # create the window, set geometry
        Register.setObjectName("Register")
        Register.resize(400, 400)
        self.buttonBox = QtWidgets.QDialogButtonBox(Register)
        self.buttonBox.setGeometry(QtCore.QRect(10, 350, 371, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)

        # set buttons to register and cancel
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.frame = QtWidgets.QFrame(Register)
        self.frame.setGeometry(QtCore.QRect(20, 100, 361, 231))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")

        # set parameters for Main Window title - Login
        self.label_3 = QtWidgets.QLabel(Register)
        self.label_3.setGeometry(QtCore.QRect(20, 30, 181, 31))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic")
        font.setPointSize(18)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")

        # set username line
        self.usernameLine = QtWidgets.QLineEdit(self.frame)
        self.usernameLine.setGeometry(QtCore.QRect(50, 40, 251, 22))
        self.usernameLine.setObjectName("usernameLine")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(50, 10, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")

        # set password line
        self.passwordLine = QtWidgets.QLineEdit(self.frame)
        self.passwordLine.setGeometry(QtCore.QRect(50, 110, 251, 22))
        self.passwordLine.setObjectName("passwordLine")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(50, 80, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Register)

        # Accept and reject buttons actions
        self.buttonBox.accepted.connect(self.acceptRegister) # send register data if accepted
        self.buttonBox.accepted.connect(Register.accept)

        self.buttonBox.rejected.connect(Register.reject)
        QtCore.QMetaObject.connectSlotsByName(Register)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        # set titles for each component
        Dialog.setWindowTitle(_translate("Register", "Register"))
        self.label_3.setText(_translate("Register", "Register"))
        self.label.setText(_translate("Register", "username"))
        self.label_2.setText(_translate("Register", "password"))

    # send register data to server
    def acceptRegister(self):
        username = self.usernameLine.text()
        password = self.passwordLine.text()
        s.send(bytes("#REGISTER#"+username+"#"+password+"#", "utf-8"))
        # show errors


# List of users user interface class
class Ui_List(object):
    def setupUi(self, List):
        # create the window, set font, geometry
        List.setObjectName("List")
        List.resize(400, 400)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic")
        font.setPointSize(18)

        # set parameters for Main Window title - List of users
        self.label = QtWidgets.QLabel(List)
        self.label.setGeometry(QtCore.QRect(20, 30, 351, 31))
        self.label.setFont(font)
        self.label.setObjectName("label")

        # set parameters for scroll area to enable scrolling through the users list
        self.scrollArea = QtWidgets.QScrollArea(List)
        self.scrollArea.setGeometry(QtCore.QRect(20, 80, 361, 251))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 359, 249))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")

        # set parameters for text browser showing users list
        self.textBrowser = QtWidgets.QTextBrowser(self.scrollAreaWidgetContents)
        self.textBrowser.setGeometry(QtCore.QRect(0, 0, 361, 251))
        self.textBrowser.setObjectName("textBrowser")

        # set up scroll area
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        # LOG OUT push button
        self.logoutPushButton = QtWidgets.QPushButton(List)
        self.logoutPushButton.setGeometry(QtCore.QRect(290, 350, 93, 31))
        self.logoutPushButton.setObjectName("logoutPushButton")

        # REFRESH push button
        self.refreshPushButton = QtWidgets.QPushButton(List)
        self.refreshPushButton.setGeometry(QtCore.QRect(290, 10, 91, 21))
        self.refreshPushButton.setObjectName("refreshPushButton")

        self.retranslateUi(List)
        QtCore.QMetaObject.connectSlotsByName(List)

    def retranslateUi(self, List):
        _translate = QtCore.QCoreApplication.translate
        # set titles for each component
        List.setWindowTitle(_translate("List", "List"))
        self.label.setText(_translate("List", "List of users"))
        self.logoutPushButton.setText(_translate("List", "Log out"))
        self.refreshPushButton.setText(_translate("List", "Refresh"))


# Messenger user interface class
class Ui_Messenger(object):
    def setupUi(self, Messenger):
        # create the window, set font, geometry
        Messenger.setObjectName("Messenger")
        Messenger.resize(400, 400)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic")
        font.setPointSize(18)

        # set parameters for Main Window title - Messenger
        self.label = QtWidgets.QLabel(Messenger)
        self.label.setGeometry(QtCore.QRect(10, 30, 111, 31))
        self.label.setFont(font)
        self.label.setObjectName("label")

        # set parameters for username of user that we are sending texts to and receiving texts from
        self.usernameLabel = QtWidgets.QLabel(Messenger)
        self.usernameLabel.setGeometry(QtCore.QRect(120, 30, 181, 31))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.usernameLabel.setFont(font)
        self.usernameLabel.setObjectName("usernameLabel")

        # set parameters for scroll area to enable scrolling through messages
        self.scrollArea = QtWidgets.QScrollArea(Messenger)
        self.scrollArea.setGeometry(QtCore.QRect(10, 80, 371, 211))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 369, 209))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")

        # set parameters for text browser showing messages
        self.textBrowser = QtWidgets.QTextBrowser(self.scrollAreaWidgetContents)
        self.textBrowser.setGeometry(QtCore.QRect(0, 0, 371, 211))
        self.textBrowser.setObjectName("textBrowser")

        # set up scroll area
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        # window where we can type a message to send
        self.sendTextEdit = QtWidgets.QTextEdit(Messenger)
        self.sendTextEdit.setGeometry(QtCore.QRect(10, 310, 271, 71))
        self.sendTextEdit.setObjectName("sendTextEdit")
        
        # SEND push button
        self.sendPushButton = QtWidgets.QPushButton(Messenger)
        self.sendPushButton.setGeometry(QtCore.QRect(290, 350, 93, 31))
        self.sendPushButton.setObjectName("sendPushButton")

        # BACK push button
        self.backPushButton = QtWidgets.QPushButton(Messenger)
        self.backPushButton.setGeometry(QtCore.QRect(290, 310, 93, 31))
        self.backPushButton.setObjectName("backPushButton")
        
        # REFRESH push button
        self.refreshPushButton = QtWidgets.QPushButton(Messenger)
        self.refreshPushButton.setGeometry(QtCore.QRect(290, 10, 91, 21))
        self.refreshPushButton.setObjectName("refreshPushButton")

        self.retranslateUi(Messenger)
        QtCore.QMetaObject.connectSlotsByName(Messenger)

    def retranslateUi(self, Messenger):
        _translate = QtCore.QCoreApplication.translate
        # set titles for each component
        Messenger.setWindowTitle(_translate("Messenger", "Messenger"))
        self.sendPushButton.setText(_translate("Messenger", "Send"))
        self.backPushButton.setText(_translate("Messenger", "Back"))
        self.label.setText(_translate("Messenger", "Chat with"))
        # self.usernameLabel.setText(_translate("Messenger", "user123"))
        self.usernameLabel.setText(_translate("Messenger", self.usr())) # get user's username via function
        self.refreshPushButton.setText(_translate("Messenger", "Refresh"))
    
    # user that we are texting with name
    def usr(self):
        usr = "ktos"
        return usr




if __name__ == "__main__":
    import sys

    while True:
        # r, w, x = select.select([sys.stdin, s], [], [])
        # if not r:
        #     continue

        app = QtWidgets.QApplication(sys.argv)
        MainWindow = QtWidgets.QMainWindow()
        ui = Ui_MainWindow()
        ui.setupUi(MainWindow)
        MainWindow.show()
        sys.exit(app.exec_())



    # app = QtWidgets.QApplication(sys.argv)
    # List = QtWidgets.QDialog()
    # ui = Ui_List()
    # ui.setupUi(List)
    # List.show()
    # sys.exit(app.exec_())

    # app = QtWidgets.QApplication(sys.argv)
    # Messenger = QtWidgets.QDialog()
    # ui = Ui_Messenger()
    # ui.setupUi(Messenger)
    # Messenger.show()
    # sys.exit(app.exec_())
