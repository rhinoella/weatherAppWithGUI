from PyQt5 import QtCore, QtGui, QtWidgets

class MainWindow(object):
    def __init__(self, Dialog):
        super().__init__()
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 400)
        Dialog.setMinimumSize(QtCore.QSize(251, 200))
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(170, 70, 121, 40))
        self.lineEdit.setObjectName("lineEdit")

        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(90, 70, 50, 40))
        self.label.setObjectName("label")

        self.labelTitle = QtWidgets.QLabel(Dialog)
        self.labelTitle.setGeometry(QtCore.QRect(80, 20, 250, 16))
        self.labelTitle.setObjectName("label_2")

        self.failedNotice = QtWidgets.QLabel(Dialog)
        self.failedNotice.setGeometry(QtCore.QRect(120, 270, 250, 40))
        self.failedNotice.setObjectName("failedNotice")

        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(150, 150, 80, 40))
        self.pushButton.setObjectName("Submit")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "City :"))
        self.labelTitle.setText(_translate("Dialog", "Get your latest weather forecast!"))
        self.failedNotice.setText(_translate("Dialog", " "))
        self.pushButton.setText(_translate("Dialog", "Submit"))

    def inputfailed(self):
        self.failedNotice.setText("Invalid city, try again")
        self.lineEdit.setText(" ")

    def gettext(self):
        print("got text")
        return self.lineEdit.text()


