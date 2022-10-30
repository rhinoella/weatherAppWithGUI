# the controller connects the model (backend) to the frontend UI

class WeatherController:
    def __init__(self, model, view):
        print("created cityweather")
        self._model = model
        self._view = view

        # connecting the button/lineedit to the submit function
        self._view.inputWidget.lineEdit.returnPressed.connect(self.submit)  # when 'enter' is pressed
        self._view.inputWidget.submitButton.clicked.connect(self.submit)  # when the button is clicked

    def submit(self):
        print("button has been pressed")
        cityInput = self._view.inputWidget.gettext  # gets the user input
        validInput = self._model.inputcheck(cityInput)  # checks the input
        if not validInput:
            # input is invalid
            print("not a valid input")
            self._view.inputWidget.inputfailed()  # notifies user their input failed
            self._view.inputWidget.lineEdit.clear()  # clears the input box
        else:
            print("valid input")
            # getting the data
            self._model.getgeocode()
            self._model.getweather()

            # gets the icons
            imageProfile = self._model.getIcon()
            # sends the icons to the UI to edit the widget
            self._view.editresults(imageProfile, self._model)
