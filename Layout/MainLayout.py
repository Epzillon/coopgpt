import PySimpleGUI as sg
import Layout.AbstractLayout as al
import Layout.GameLayout as gl
import Layout.SettingsLayout as sl

class MainLayout(al.AbstractLayout):
    def generateLayout(self):
        return [[sg.Text("Co-op GPT")], [sg.Button("Start"), sg.Button("Settings"), sg.Button("Quit")]]

    def handleEvents(self, window):
        # Create an event loop
        while True:
            event, values = window.read()

            if event == "Start":
                gli = gl.GameLayout(["gabbe", "gabbe2"], self.render) # Players hard-coded for now
                window.close()
                gli.render()
            elif event == "Settings":
                sli = sl.SettingsLayout(["gabbe", "gabbe2"], self.render) # Players hard-coded for now
                window.close()
                sli.render()
            elif event == "Quit" or event == sg.WIN_CLOSED:
                break

        window.close()