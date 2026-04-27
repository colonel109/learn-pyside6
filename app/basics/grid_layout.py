import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QApplication,
    QGridLayout,
    QLabel,
    QMainWindow,
    QWidget,
)
from layout_colorwidget import Color

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My grid layout")

        layout = QGridLayout()

        layout.addWidget(Color("red"), 0, 0)
        layout.addWidget(Color("blue"), 1, 1)
        layout.addWidget(Color("green"), 4, 1)
        layout.addWidget(Color("purple"), 3, 2)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)
app = QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec()




