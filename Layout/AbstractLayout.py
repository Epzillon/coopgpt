import PySimpleGUI as sg

class AbstractLayout:
    def __init__(self):
        self.title = "Co-op GPT"

    def generateLayout(self):
        pass

    def render(self):
        window = sg.Window(self.title, self.generateLayout())

        return self.handleEvents(window)

    def handleEvents(self, window):
        pass