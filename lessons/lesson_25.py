from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow
from PyQt6.QtCore import QSize, Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.count = 0
        self.setWindowTitle('Приложение')
        self.button = QPushButton("Press Me!")
        self.button.clicked.connect(self.the_button_was_clicked)
        self.setFixedSize(QSize(400,400))
        self.setCentralWidget(self.button)

    def the_button_was_clicked(self):
        print('Clicked!')
        self.button.setText('Already clicked!')
        self.button.setEnabled(False)
        self.count += 1
        self.setWindowTitle(f'Cliced: {self.count}')


app = QApplication([]) # приложение
# window = QWidget() # класс, от которого унаследованы все виджеты
# window = QPushButton('Push me!')
# window = QMainWindow()
window = MainWindow()
window.show() ##окно по умолчанию скрыто.
app.exec() # запускаем цикл событий, которые обрабатывает приложение