from tkinter import S
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
# from register import Ui_Register
# from login import Ui_Login


import select
import socket
import sys

HOST = "127.0.0.1"
PORT = 1100

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
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
        
        self.loginButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.loginButton.setObjectName("loginButton")
        self.verticalLayout.addWidget(self.loginButton)
        self.loginButton.clicked.connect(self.openLoginWindow)

        self.registerButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.registerButton.setObjectName("registerButton")
        self.verticalLayout.addWidget(self.registerButton)
        self.registerButton.clicked.connect(self.openRegisterWindow)

        self.exitButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.exitButton.setObjectName("exitButton")
        self.verticalLayout.addWidget(self.exitButton)
        self.exitButton.clicked.connect(self.showExitPopup)

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
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 400, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.loginButton.setText(_translate("MainWindow", "Log in"))
        self.registerButton.setText(_translate("MainWindow", "Register"))
        self.exitButton.setText(_translate("MainWindow", "Exit"))
        self.label.setText(_translate("MainWindow", "Chat Client"))
    
    def openLoginWindow(self):
        self.window = QtWidgets.QDialog()
        self.ui = Ui_Login()
        self.ui.setupUi(self.window)
        # MainWindow.hide()
        self.window.show()

    def openRegisterWindow(self):
        self.window = QtWidgets.QDialog()
        self.ui = Ui_Register()
        self.ui.setupUi(self.window)
        # MainWindow.hide()
        self.window.show()

    def showLogoutPopup(self):
        msg = QMessageBox()
        msg.setWindowTitle("Log out")
        msg.setText("Are you sure you want to log out?")
        msg.setIcon(QMessageBox.Question)
        msg.setStandardButtons(QMessageBox.Yes|QMessageBox.No)
        msg.exec_()

    def showExitPopup(self):
        msg = QMessageBox()
        msg.setWindowTitle("Exit")
        msg.setText("Are you sure you want to exit?")
        msg.setIcon(QMessageBox.Warning)
        msg.setStandardButtons(QMessageBox.Yes|QMessageBox.No)
        ret = msg.exec_()
        if ret == QMessageBox.Yes:
            sys.exit(app.exec_())


    def showErrorPopup(self):
        msg = QMessageBox()
        msg.setWindowTitle("Error")
        msg.setText("err")
        msg.setIcon(QMessageBox.Critical)
        msg.exec_()


class Ui_Login(object):
    def setupUi(self, Login):
        Login.setObjectName("Login")
        Login.resize(400, 400)
        self.buttonBox = QtWidgets.QDialogButtonBox(Login)
        self.buttonBox.setGeometry(QtCore.QRect(10, 350, 371, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.frame = QtWidgets.QFrame(Login)
        self.frame.setGeometry(QtCore.QRect(20, 100, 361, 231))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
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
        self.label_3 = QtWidgets.QLabel(Login)
        self.label_3.setGeometry(QtCore.QRect(20, 30, 181, 31))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic")
        font.setPointSize(18)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")

        self.retranslateUi(Login)

        self.buttonBox.accepted.connect(self.acceptLogin)
        self.buttonBox.accepted.connect(Login.accept)

        self.buttonBox.rejected.connect(Login.reject)

        QtCore.QMetaObject.connectSlotsByName(Login)

    def retranslateUi(self, Login):
        _translate = QtCore.QCoreApplication.translate
        Login.setWindowTitle(_translate("Login", "Login"))
        self.label.setText(_translate("Login", "username"))
        self.label_2.setText(_translate("Login", "password"))
        self.label_3.setText(_translate("Login", "Log in"))

    def acceptLogin(self):
        username = self.usernameLine.text()
        password = self.passwordLine.text()
        print(username, " + ", password)
        s.send(bytes("#LOGIN#"+username+"#"+password+"#", "utf-8"))
        # show errors


class Ui_Register(object):
    def setupUi(self, Register):
        Register.setObjectName("Register")
        Register.resize(400, 400)
        self.buttonBox = QtWidgets.QDialogButtonBox(Register)
        self.buttonBox.setGeometry(QtCore.QRect(10, 350, 371, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label_3 = QtWidgets.QLabel(Register)
        self.label_3.setGeometry(QtCore.QRect(20, 30, 181, 31))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic")
        font.setPointSize(18)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.frame = QtWidgets.QFrame(Register)
        self.frame.setGeometry(QtCore.QRect(20, 100, 361, 231))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
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

        self.buttonBox.accepted.connect(self.acceptRegister)
        self.buttonBox.accepted.connect(Register.accept)

        self.buttonBox.rejected.connect(Register.reject)
        QtCore.QMetaObject.connectSlotsByName(Register)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Register", "Register"))
        self.label_3.setText(_translate("Register", "Register"))
        self.label.setText(_translate("Register", "username"))
        self.label_2.setText(_translate("Register", "password"))

    def acceptRegister(self):
        username = self.usernameLine.text()
        password = self.passwordLine.text()
        s.send(bytes("#REGISTER#"+username+"#"+password+"#", "utf-8"))
        # show errors


class Ui_List(object):
    def setupUi(self, List):
        List.setObjectName("List")
        List.resize(400, 400)
        self.label = QtWidgets.QLabel(List)
        self.label.setGeometry(QtCore.QRect(20, 30, 351, 31))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic")
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.scrollArea = QtWidgets.QScrollArea(List)
        self.scrollArea.setGeometry(QtCore.QRect(20, 80, 361, 251))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 359, 249))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.textBrowser = QtWidgets.QTextBrowser(self.scrollAreaWidgetContents)
        self.textBrowser.setGeometry(QtCore.QRect(0, 0, 361, 251))
        self.textBrowser.setObjectName("textBrowser")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.backPushButton = QtWidgets.QPushButton(List)
        self.backPushButton.setGeometry(QtCore.QRect(290, 350, 93, 31))
        self.backPushButton.setObjectName("backPushButton")
        self.refreshPushButton = QtWidgets.QPushButton(List)
        self.refreshPushButton.setGeometry(QtCore.QRect(290, 10, 91, 21))
        self.refreshPushButton.setObjectName("refreshPushButton")

        self.retranslateUi(List)
        QtCore.QMetaObject.connectSlotsByName(List)

    def retranslateUi(self, List):
        _translate = QtCore.QCoreApplication.translate
        List.setWindowTitle(_translate("List", "List"))
        self.label.setText(_translate("List", "List of users"))
        self.backPushButton.setText(_translate("List", "Back"))
        self.refreshPushButton.setText(_translate("List", "Refresh"))


class Ui_Messenger(object):
    def setupUi(self, Messenger):
        Messenger.setObjectName("Messenger")
        Messenger.resize(400, 400)
        self.sendTextEdit = QtWidgets.QTextEdit(Messenger)
        self.sendTextEdit.setGeometry(QtCore.QRect(10, 310, 271, 71))
        self.sendTextEdit.setObjectName("sendTextEdit")
        self.scrollArea = QtWidgets.QScrollArea(Messenger)
        self.scrollArea.setGeometry(QtCore.QRect(10, 80, 371, 211))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 369, 209))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.textBrowser = QtWidgets.QTextBrowser(self.scrollAreaWidgetContents)
        self.textBrowser.setGeometry(QtCore.QRect(0, 0, 371, 211))
        self.textBrowser.setObjectName("textBrowser")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.sendPushButton = QtWidgets.QPushButton(Messenger)
        self.sendPushButton.setGeometry(QtCore.QRect(290, 350, 93, 31))
        self.sendPushButton.setObjectName("sendPushButton")
        self.backPushButton = QtWidgets.QPushButton(Messenger)
        self.backPushButton.setGeometry(QtCore.QRect(290, 310, 93, 31))
        self.backPushButton.setObjectName("backPushButton")
        self.label = QtWidgets.QLabel(Messenger)
        self.label.setGeometry(QtCore.QRect(10, 30, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic")
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.usernameLabel = QtWidgets.QLabel(Messenger)
        self.usernameLabel.setGeometry(QtCore.QRect(120, 30, 181, 31))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.usernameLabel.setFont(font)
        self.usernameLabel.setObjectName("usernameLabel")
        self.refreshPushButton = QtWidgets.QPushButton(Messenger)
        self.refreshPushButton.setGeometry(QtCore.QRect(290, 10, 91, 21))
        self.refreshPushButton.setObjectName("refreshPushButton")

        self.retranslateUi(Messenger)
        QtCore.QMetaObject.connectSlotsByName(Messenger)

    def retranslateUi(self, Messenger):
        _translate = QtCore.QCoreApplication.translate
        Messenger.setWindowTitle(_translate("Messenger", "Messenger"))
        self.sendPushButton.setText(_translate("Messenger", "Send"))
        self.backPushButton.setText(_translate("Messenger", "Back"))
        self.label.setText(_translate("Messenger", "Chat with"))
        # self.usernameLabel.setText(_translate("Messenger", "user123"))
        self.usernameLabel.setText(_translate("Messenger", self.usr()))
        self.refreshPushButton.setText(_translate("Messenger", "Refresh"))
    
    def usr(self):
        usr = "ktos"
        return usr




if __name__ == "__main__":
    import sys
    # app = QtWidgets.QApplication(sys.argv)
    # MainWindow = QtWidgets.QMainWindow()
    # ui = Ui_MainWindow()
    # with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    #     s.connect((HOST, PORT))

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
