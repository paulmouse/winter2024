from PyQt6.QtWidgets import QApplication, QPushButton, QMainWindow
from PyQt6.QtCore import QSize

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.count = 0
        self.setWindowTitle('Приложение')
        self.button = QPushButton(f'На кнопку нажали: {self.count} раз')
        self.button.clicked.connect(self.the_button_was_clicked)
        self.setFixedSize(QSize(200,200))
        self.setCentralWidget(self.button)

    def the_button_was_clicked(self):
        self.count += 1
        if self.count >=2 and self.count <=4:
            self.button.setText(f'На кнопку нажали: {self.count} разa')
        else: self.button.setText(f'На кнопку нажали: {self.count} раз')

app = QApplication([])
window = MainWindow()
window.show()
app.exec()