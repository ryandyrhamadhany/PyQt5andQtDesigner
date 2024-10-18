from PyQt5.QtWidgets import QApplication, QPushButton, QLabel, QMainWindow

app = QApplication([])
window = QMainWindow()

label = QLabel(window)

label.setText("Label 1")
label.move(200, 0)

button = QPushButton(window)
button.setText("button 1")

window.show()
app.exec_()
