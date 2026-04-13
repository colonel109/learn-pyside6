from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QPushButton
)

import sys
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle('My app')
        
        self.button_is_checked = True
        
        button = QPushButton('Press Me!')
        button.setCheckable(True)
        button.clicked.connect(self.the_button_was_checked)
        button.setChecked(self.button_is_checked)
        
        button.released.connect(
            self.the
        )
        
        self.setCentralWidget(button)
        
    # def the_button_was_clicked(self):
    #     print('Clicked!')
        
    # def the_button_was_checked(self, checked):
    #     self.button_is_checked = checked
    #     print(self.button_is_checked)
    
    def the_button_was_released(self):
        self.button_is_checked = self.button.isChecked()
        
        print(self.button_is_checked)
        
app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()