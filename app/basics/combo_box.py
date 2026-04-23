from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QComboBox
)

from PySide6.QtCore import Qt

import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle('Combo Box')
        
        combo_box = QComboBox()
        combo_box.addItems(['One', 'Two', 'Three'])    
        combo_box.setEditable(True)
                
        combo_box.currentIndexChanged.connect(self.index_changed)
        combo_box.currentTextChanged.connect(self.text_changed)
        
        self.setCentralWidget(combo_box)
        
    def index_changed(self, i):
        print(i)
                
    def text_changed(self, t):
        print(t)
        
app = QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec()