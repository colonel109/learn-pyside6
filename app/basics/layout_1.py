import sys

from PySide6 import QtWidgets
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QHBoxLayout,
    QVBoxLayout,
    QWidget
)

from layout_colorwidget import Color

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My App")

        master_layout = QHBoxLayout()

        layout_1 = QVBoxLayout()
        layout_2 = QVBoxLayout()
        layout_3 = QVBoxLayout()

        layout_1.addWidget(Color("blue"))

        layout_2.addWidget(Color("red"))
        layout_2.addWidget(Color("blue"))
        layout_2.addWidget(Color("green"))

        layout_3.addWidget(Color("purple"))
        layout_3.addWidget(Color("red"))

        master_layout.addLayout(layout_1)
        master_layout.addLayout(layout_2)
        master_layout.addLayout(layout_3)

        master_layout.setSpacing(10)
        container = QWidget()

        container.setLayout(master_layout)

        self.setCentralWidget(container)
app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
