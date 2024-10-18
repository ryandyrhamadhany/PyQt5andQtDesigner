from PyQt5.QtWidgets import QApplication, QPushButton, QLabel, QMainWindow, QWidget, QVBoxLayout

class Mywindow(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        btn1 = QPushButton("btn 1")
        btn2 = QPushButton("btn 2")
        btn3 = QPushButton("btn 3")
        btn4 = QPushButton("btn 4")
        layout.addWidget(btn1)
        layout.addWidget(btn2)
        layout.addWidget(btn3)
        layout.addWidget(btn4)
        self.setLayout(layout)

app = QApplication([])
window = Mywindow()
window.show()
app.exec_()