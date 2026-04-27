import sys

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QSlider

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle('Slider')
        
        widget = QSlider()
        
        widget.setMinimum(-10)
        widget.setMaximum(100)
        widget.setSingleStep(5)
        
        widget.setOrientation(Qt.Horizontal)
        
        widget.valueChanged.connect(self.current_value)
        widget.sliderMoved.connect(self.slider_moved)
        widget.sliderReleased.connect(self.slider_released)
        widget.sliderPressed.connect(self.slider_pressed)
        self.setCentralWidget(widget)
        
        
    def current_value(self, i):
        print(f'Value: {i}')
        
    def slider_moved(self, e):
        print(f'Moved: {e}')
        
    def slider_released(self):
        print('slider released')

    def slider_pressed(self):
        print('slider pressed')
                   
app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()  