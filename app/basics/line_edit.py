from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QLineEdit,
    QVBoxLayout,
    QWidget
)

from PySide6.QtCore import Qt

import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle('Combo Box')
        
        line_edit_2 = QLineEdit('default text')
        
        line_edit_2.setPlaceholderText('Enter your text here')
        line_edit_2.returnPressed.connect(self.return_pressed)
        line_edit_2.textChanged.connect(self.text_changed)
        line_edit_2.selectionChanged.connect(self.selection_changed)
        line_edit_2.textEdited.connect(self.text_edited)    
        
        self.setCentralWidget(line_edit_2)
        
    def return_pressed(self):
        print('return pressed')
        self.centralWidget().setText('Boom')
        
    def selection_changed(self):
        print('selection changed')
        # print(s)
        
    def text_changed(self, p):
        print('text_changed')
        print(p)
    
    def text_edited(self, x):
        print('text edited')
        print(x)             
           
        
app = QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec()