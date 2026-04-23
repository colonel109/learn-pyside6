from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QVBoxLayout,
    QWidget,
    QCheckBox,
    QLabel
)

from PySide6.QtGui import QPixmap

import sys, os

base_dir = os.path.dirname(__file__)
print('Current working folder:', os.getcwd())
print('Path are relative to:', base_dir)

class MainWindows(QMainWindow):
    def __init__(self):
        super().__init__()
        
        image = QLabel('Hello')
        # font = image.font()
        # font.setPointSize(30)
        # image.setFont(font)
        image.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
        image.setPixmap(QPixmap(os.path.join(base_dir, 'otje.jpg')))
        image.setScaledContents(True)
    
        
        checkbox = QCheckBox('Movie')
        checkbox.setText('2')
        
        layout = QVBoxLayout()
        # layout.addWidget(checkbox)
        layout.addWidget(image)
        
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

app = QApplication(sys.argv)
     
window = MainWindows()
window.show()
        
app.exec()