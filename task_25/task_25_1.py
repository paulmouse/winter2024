from PyQt6.QtWidgets import QApplication, QPushButton, QMainWindow
from PyQt6.QtCore import QSize

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.count = 0
        self.setWindowTitle('Приложение')
        self.button = QPushButton(f'{self.count}')
        self.button.clicked.connect(self.the_button_was_clicked)
        self.setFixedSize(QSize(200,200))
        self.setCentralWidget(self.button)

    def the_button_was_clicked(self):
        self.count += 1
        self.button.setText(f'{self.count}')





app = QApplication([]) # приложение
# window = QWidget() # класс, от которого унаследованы все виджеты
# window = QPushButton('Push me!')
# window = QMainWindow()
window = MainWindow()
window.show() ##окно по умолчанию скрыто.
app.exec() # запускаем цикл событий, которые обрабатывает приложение