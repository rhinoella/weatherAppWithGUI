from PyQt5 import QtCore, QtGui, QtWidgets


class InputWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        # parent layout- vertical box layout
        self.vBoxLayout = QtWidgets.QVBoxLayout(self)
        self.vBoxLayout.setObjectName("vBoxLayout")

        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(13)
        self.labelTitle = QtWidgets.QLabel(self)
        self.labelTitle.setFont(font)
        self.vBoxLayout.addWidget(self.labelTitle, 0, QtCore.Qt.AlignmentFlag.AlignCenter)
        self.labelTitle.setObjectName("label_2")
        self.labelTitle.setText("Get your latest weather forecast!")

        # nesting a horisontal box layout within the vertical box layout so two widgets sit side by side
        self.hBoxLayout = QtWidgets.QHBoxLayout(self)
        self.hBoxLayout.addSpacing(QtWidgets.QSizePolicy.Maximum)  # spacing on the left

        self.citylabel = QtWidgets.QLabel(self)
        self.citylabel.setFont(font)
        self.citylabel.setObjectName("label")
        self.citylabel.resize(self.citylabel.sizeHint())  # gets the size of the label
        self.citylabel.setSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed) # fixing the size
        self.citylabel.setText("City : ")
        self.hBoxLayout.addWidget(self.citylabel)

        font = QtGui.QFont()
        font.setFamily("Segoe UI Semilight")
        font.setPointSize(12)
        self.lineEdit = QtWidgets.QLineEdit(self)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)  # fixing the size
        self.hBoxLayout.addWidget(self.lineEdit)
        self.hBoxLayout.addSpacing(QtWidgets.QSizePolicy.Maximum) # spacing on the right

        self.vBoxLayout.setObjectName("hBoxLayout")
        self.vBoxLayout.addLayout(self.hBoxLayout)

        self.failedNotice = QtWidgets.QLabel(self)
        self.failedNotice.setFont(font)
        self.failedNotice.setObjectName("failedNotice")
        self.vBoxLayout.addWidget(self.failedNotice, 0, QtCore.Qt.AlignmentFlag.AlignCenter)

        # nesting another hboxlayout in the parent one, so that we can minimize the size of the button
        self.hBoxLayout2 = QtWidgets.QHBoxLayout(self)
        self.hBoxLayout2.addSpacing(QtWidgets.QSizePolicy.Maximum)  # adding spacing on the left

        self.submitButton = QtWidgets.QPushButton(self)
        self.submitButton.setFont(font)
        self.submitButton.setObjectName("Submit")
        self.submitButton.setText("Submit")
        self.submitButton.setSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)  # fixing the size
        self.hBoxLayout2.addWidget(self.submitButton)

        self.hBoxLayout2.addSpacing(QtWidgets.QSizePolicy.Maximum)  # adding spacing on the right
        self.vBoxLayout.addLayout(self.hBoxLayout2)


    def inputfailed(self):
        # notifies the user their input failed
        self.failedNotice.setText("Invalid city, try again")
        self.lineEdit.setText(" ")

    @property
    def gettext(self):
        # returns the text that the user typed
        print("got text")
        return self.lineEdit.text()



