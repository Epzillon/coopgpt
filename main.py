import sys
from PyQt6.QtWidgets import QApplication, QWidget
from Layout.MainLayout import MainLayout

app = QApplication([])

window = QWidget()
window.setWindowTitle("Co-op GPT")
window.setGeometry(100, 200, 400, 200)

ml = MainLayout(window)

window.setLayout(ml.layout)
window.show()

sys.exit(app.exec())