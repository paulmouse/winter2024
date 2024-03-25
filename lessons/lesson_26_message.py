from PyQt6.QtWidgets import QApplication, QMainWindow, QMdiArea, QMdiSubWindow, QTextEdit
from PyQt6.QtGui import QAction
import sys
class MDIWindow(QMainWindow):
    count = 0
    def __init__(self):
        super().    init    ()
        self.mdi = QMdiArea()
        self.setCentralWidget(self.mdi) bar = self.menuBar()
        file = bar.addMenu("File") file.addAction("New") file.addAction("Cascade") file.addAction("Tiled")
        file.triggered[QAction].connect(self.WindowTrig)
        self.setWindowTitle("MDI Application")


editFindAction = QAction(QIcon('t2.png'), 'Find', self)
editFindAction.triggered.connect(self.clickFind)
edit = bar.addMenu("Edit")
edit.addAction(editFindAction) edit.addAction("Copy") edit.addAction("Paste")
exitAction = QAction(QIcon('t1.png'), 'Exit', self)
exitAction.setShortcut('Ctrl+Q') exitAction.setStatusTip('Exit application')
exitAction.triggered.connect(self.close)
fileMenu = bar.addMenu('&Exit')
fileMenu.addAction(exitAction)
file.triggered[QAction].connect(self.WindowTrig)
self.setWindowTitle("MDI Application")

def clickFind(self):
    QMessageBox.about(self, "Title", "Message")
