import sys
from PyQt6.QtWidgets import QLabel, QWidget, QPushButton, QVBoxLayout, QHBoxLayout
from Layout.AbstractLayout import AbstractLayout
from Layout.GameLayout import GameLayout
# from Layout.SettingsLayout import SettingsLayout

class MainLayout(AbstractLayout):
    def generateLayout(self):
        # Create Layout
        layout = QVBoxLayout()
        buttonLayout = QHBoxLayout(objectName="main_menu_buttons")

        # Generate Widgets
        helloMsg = QLabel("<h1>Hello, World!</h1>")
        startBtn = QPushButton("Start", objectName="start_button", parent=self.window)
        settingsBtn = QPushButton("Settings", objectName="settings_button", parent=self.window)
        quitBtn = QPushButton("Quit", objectName="quit_button", parent=self.window)


        # Add Widgets to Layout
        layout.addWidget(helloMsg)
        buttonLayout.addWidget(startBtn)
        buttonLayout.addWidget(settingsBtn)
        buttonLayout.addWidget(quitBtn)
        layout.addLayout(buttonLayout)

        self.layout = layout

    def registerEvents(self):
        startBtn = self.window.findChild(QPushButton, "start_button")
        settingsBtn = self.window.findChild(QPushButton, "settings_button")
        quitBtn = self.window.findChild(QPushButton, "quit_button")

        startBtn.clicked.connect(self.startBtnClick)
        settingsBtn.clicked.connect(self.settingsBtnClick)
        quitBtn.clicked.connect(self.quitBtnClick)
    
    def startBtnClick(self):
        gl = GameLayout(self.window, self.layout)
        self.window.layout().addLayout(gl.layout)

    def settingsBtnClick(self):
        print("settings")

    def quitBtnClick(self):
        sys.exit()