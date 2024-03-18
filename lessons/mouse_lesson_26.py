import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow, QLabel, QVBoxLayout,QLineEdit,QHBoxLayout, QTextEdit, QGridLayout

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('MainWindow')
        self.label = QLabel('Click')
        self.setCentralWidget(self.label)
    def mouseMoveEvent(self, a):
        self.label.setText('mouseMoveEvent')
    def mousePressEvent(self, a):
        self.label.setText('mousePressEvent')

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()

