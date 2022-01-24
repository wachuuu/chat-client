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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(500, 500)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic")
        font.setPointSize(12)
        self.centralwidget.setFont(font)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 100, 451, 311))
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

        self.listButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.listButton.setObjectName("listButton")
        self.verticalLayout.addWidget(self.listButton)

        self.messageButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.messageButton.setObjectName("messageButton")
        self.verticalLayout.addWidget(self.messageButton)

        self.logoutButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.logoutButton.setObjectName("logoutButton")
        self.verticalLayout.addWidget(self.logoutButton)
        self.logoutButton.clicked.connect(self.showLogoutPopup)

        self.exitButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.exitButton.setObjectName("exitButton")
        self.verticalLayout.addWidget(self.exitButton)
        self.exitButton.clicked.connect(self.showExitPopup)

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 30, 181, 31))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic")
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 500, 21))
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
        self.listButton.setText(_translate("MainWindow", "List"))
        self.messageButton.setText(_translate("MainWindow", "Message"))
        self.logoutButton.setText(_translate("MainWindow", "Log out"))
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
        msg.exec_()

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
        self.buttonBox.setGeometry(QtCore.QRect(40, 350, 341, 32))
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
        # TODO
        # send username and password to server
        # show errors


class Ui_Register(object):
    def setupUi(self, Register):
        Register.setObjectName("Register")
        Register.resize(400, 400)
        self.buttonBox = QtWidgets.QDialogButtonBox(Register)
        self.buttonBox.setGeometry(QtCore.QRect(40, 350, 341, 32))
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
        # print(username, " + ", password)
        # TODO
        # send username and password to server
        # show errors



if __name__ == "__main__":
    import sys

    # with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    #     s.connect((HOST, PORT))

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())