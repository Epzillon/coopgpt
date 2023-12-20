class AbstractLayout:
    window = None
    title = ""
    layout = None

    def __init__(self, window, layout=None):
        self.window = window
        self.layout = layout
        self.title = "Co-op GPT"

        self.clearLayout(self.layout)
        self.generateLayout()
        self.registerEvents()

    def clearLayout(self, layout):
        if layout is not None:
            while layout.count():
                item = layout.takeAt(0)
                widget = item.widget()
                if widget is not None:
                    widget.deleteLater()
                else:
                    self.clearLayout(item.layout())

    def generateLayout(self):
        raise NotImplementedError

    def registerEvents(self):
        raise NotImplementedError
