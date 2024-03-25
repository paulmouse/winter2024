from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow, QLabel, QVBoxLayout,QLineEdit,QHBoxLayout, QTextEdit, QGridLayout, QMessageBox
from PyQt6.QtCore import QSize, Qt

class Calculator(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Calculator')
        w,h = 200,25

        self.line1 = QLineEdit()
        self.line1.setFixedSize(QSize(w,h))

        self.line2 = QLineEdit()
        self.line2.setFixedSize(QSize(w,h))

        self.button_add = QPushButton("+")
        self.button_add.setFixedSize(QSize(w,h))
        self.button_add.clicked.connect(self.the_button_add)

        self.button_sub = QPushButton("-")
        self.button_sub.setFixedSize(QSize(w,h))
        self.button_sub.clicked.connect(self.the_button_sub)

        self.button_mul = QPushButton("*")
        self.button_mul.setFixedSize(QSize(w,h))
        self.button_mul.clicked.connect(self.the_button_mul)

        self.button_div = QPushButton("/")
        self.button_div.setFixedSize(QSize(w,h))
        self.button_div.clicked.connect(self.the_button_div)

        self.button_fine_div = QPushButton("//")
        self.button_fine_div.setFixedSize(QSize(w,h))
        self.button_fine_div.clicked.connect(self.the_button_fine_div)

        self.button_rem = QPushButton("%")
        self.button_rem.setFixedSize(QSize(w,h))
        self.button_rem.clicked.connect(self.the_button_rem)

        self.text = QTextEdit()
        self.text.setFixedSize(QSize(w, w))

        self.label = QLabel('=')
        self.label.setFixedSize(QSize(w, h))
        font = self.label.font()
        font.setPointSize(10)
        self.label.setFont(font)

        # layout = QVBoxLayout()
        # widgets = [self.line1, self.line2, self.label, self.text, self.button_add, self.button_sub, self.button_mul, self.button_div, self.button_fine_div, self.button_rem]
        # for w in widgets:
        #     layout.addWidget((w))
        layout = QGridLayout()
        layout.addWidget(self.line1, 0, 0)
        layout.addWidget(self.line2, 0, 1)
        layout.addWidget(self.label, 0, 2)
        # layout.addWidget(self.text, 0, 3)
        # ---
        layout.addWidget(self.button_add, 1, 0)
        layout.addWidget(self.button_sub, 1, 1)

        layout.addWidget(self.button_mul, 2, 0)
        layout.addWidget(self.button_div, 2, 1)
        # ---
        layout.addWidget(self.button_fine_div, 3, 0)
        layout.addWidget(self.button_rem, 3, 1)



        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def the_button_add(self):
        QMessageBox.about(self,'Title', 'Нажали +')
        try:
            res = '='+str(eval(self.line1.text()+'+'+self.line2.text()))
        except:
            res = 'Error'
        self.label.setText(res)
        self.text.append(res)

    def the_button_sub(self):
        try:
            res = '=' + str(eval(self.line1.text() + '-' + self.line2.text()))
        except:
            res = 'Error'
        self.label.setText(res)
        self.text.append(res)

    def the_button_mul(self):
        try:
            res = '=' + str(eval(self.line1.text() + '*' + self.line2.text()))
        except:
            res = 'Error'
        self.label.setText(res)
        self.text.append(res)

    def the_button_div(self):
        try:
            res = '=' + str(eval(self.line1.text() + '/' + self.line2.text()))
        except:
            res = 'Error'
        self.label.setText(res)
        self.text.append(res)

    def the_button_fine_div(self):
        try:
            res = '=' + str(eval(self.line1.text() + '//' + self.line2.text()))
        except:
            res = 'Error'
        self.label.setText(res)
        self.text.append(res)

    def the_button_rem(self):
        try:
            res = '=' + str(eval(self.line1.text() + '%' + self.line2.text()))
        except:
            res = 'Error'
        self.label.setText(res)
        self.text.append(res)


app = QApplication([]) # приложение
# window = QWidget() # класс, от которого унаследованы все виджеты
# window = QPushButton('Push me!')
# window = QMainWindow()
window = Calculator()
window.show() ##окно по умолчанию скрыто.
app.exec() # запускаем цикл событий, которые обрабатывает приложение