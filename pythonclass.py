from PyQt5.QtWidgets import QApplication, QPushButton, QLabel, QMainWindow, QWidget

class Mywindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.label = QLabel(self)
        self.label.setText("Label 1")
        self.label.move(200,0)
        self.button = QPushButton(self)
        self.button.setText("Button 1")
        
        
app = QApplication([])
window = Mywindow()
window.show()
app.exec_()