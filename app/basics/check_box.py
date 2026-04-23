from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QVBoxLayout,
    QCheckBox,
    QWidget
)

from PySide6.QtCore import Qt

import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle('My app')
        
        cb = QCheckBox('This is a checkbox')
        # cb.setCheckState(Qt.PartiallyChecked)
        
        cb.stateChanged.connect(self.show_state)
        
        
        
        # container = QWidget()
        
        # layout = QVBoxLayout()
        # layout.addWidget(cb)
        
        # container.setLayout(layout)
        
        self.setCentralWidget(cb)
    
    
    def show_state(self, s):
        print(s == Qt.Checked)
        print(s)
                                    
app = QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec()