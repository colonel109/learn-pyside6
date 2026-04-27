import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QSpinBox, QDoubleSpinBox

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle('Spin Box')
        
        widget = QSpinBox()
        
        widget.setMinimum(-10)
        widget.setMaximum(3)
        widget.setSingleStep(3)
        
        widget.setPrefix('$')
        widget.setSuffix('c')
        
        widget.valueChanged.connect(self.value_changed)
        widget.textChanged.connect(self.text_changed)
        
        self.setCentralWidget(widget)
    
    def value_changed(self, i):
        print(f'Changed value {i}')
        
    def text_changed(self, j):
        print(f'Changed text {j}')

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()