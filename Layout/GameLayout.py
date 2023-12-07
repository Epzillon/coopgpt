import PySimpleGUI as sg
import Layout.AbstractLayout as al

class GameLayout(al.AbstractLayout):
    players = []

    def __init__(self, players, exitCallback):
        super().__init__()
        self.players = players
        self.exitCallback = exitCallback

    def generateLayout(self):
        player_column = [
            [
                sg.Text("Players")
            ],
            [
                sg.Listbox(
                    values=self.players, enable_events=True, size=(40, 20), key="-PLAYERLIST-"
                )
            ],
        ]
        story_column = [
            [sg.Text("Story here...")],
            [sg.In(), sg.Button("Send")]
        ]

        return [
            [
                sg.Column(player_column),
                sg.VSeperator(),
                sg.Column(story_column),
            ]
        ]
    
    def handleEvents(self, window):
        while True:
            event, values = window.read()
            if event == sg.WIN_CLOSED:
                break

        if event == "-PLAYERLIST-":
            pass # do things here

        window.close()

        return self.exitCallback()
