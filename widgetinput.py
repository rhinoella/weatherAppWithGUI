from PyQt5 import QtCore, QtGui, QtWidgets


class InputWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.gridLayout = QtWidgets.QGridLayout(self)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)

        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(13)
        self.labelTitle = QtWidgets.QLabel(self)
        self.labelTitle.setFont(font)
        self.labelTitle.setObjectName("label_2")
        self.labelTitle.setText("Get your latest weather forecast!")
        self.gridLayout.addWidget(self.labelTitle, 0, 1, 1, 1, QtCore.Qt.AlignmentFlag.AlignCenter)

        # nesting a horisontal box layout within the vertical box layout so two widgets sit side by side
        self.hBox = QtWidgets.QHBoxLayout(self)

        self.citylabel = QtWidgets.QLabel(self)
        self.citylabel.setFont(font)
        self.citylabel.setObjectName("label")
        self.citylabel.resize(self.citylabel.sizeHint())  # gets the size of the label
        self.citylabel.setText("City : ")
        self.hBox.addWidget(self.citylabel)

        font = QtGui.QFont()
        font.setFamily("Segoe UI Semilight")
        font.setPointSize(12)
        self.lineEdit = QtWidgets.QLineEdit(self)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setMaximumWidth(260)
        self.lineEdit.setSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.hBox.addWidget(self.lineEdit)

        self.gridLayout.addLayout(self.hBox, 1, 1, 1, 1, QtCore.Qt.AlignmentFlag.AlignCenter)

        # spacing on the right

        self.failedNotice = QtWidgets.QLabel(self)
        self.failedNotice.setFont(font)
        self.failedNotice.setObjectName("failedNotice")
        self.gridLayout.addWidget(self.failedNotice, 2, 1, 1, 1)

        self.submitButton = QtWidgets.QPushButton(self)
        self.submitButton.setFont(font)
        self.submitButton.setObjectName("Submit")
        self.submitButton.setText("Submit")
        self.submitButton.setMaximumWidth(self.submitButton.width())  # sets the width to the width of the text
        # prevents the button from resizing as window is resized
        self.submitButton.setSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addWidget(self.submitButton, 3, 1, 1, 1, QtCore.Qt.AlignmentFlag.AlignCenter)


    def inputfailed(self):
        # notifies the user their input failed
        self.failedNotice.setText("Invalid city, try again")
        self.lineEdit.setText(" ")

    @property
    def gettext(self):
        # returns the text that the user typed
        print("got text")
        return self.lineEdit.text()
