from PyQt6.QtWidgets import (QApplication, QPushButton, QWidget,
                             QMainWindow, QLabel, QLineEdit, QTextEdit)
from PyQt6.QtGui import QIcon, QAction
import sys


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        textEdit = QTextEdit()
        self.setCentralWidget(textEdit)

        exitAction = QAction(QIcon('exit.png'), 'Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(self.close)

        self.statusBar()

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(exitAction)

        # пункт меню описание
        fileMenu = menubar.addMenu('&Description')
        fileMenu.addAction(QAction("This app was made just for fun", self))

        # пункт меню инструкция
        fileMenu = menubar.addMenu('&Instruction')
        cntI = ['&How to...', '&Docs', 'Instruction']
        for i in cntI:
            fileMenu.addAction(QAction(i, self))

        # пункт меню help
        fileMenu = menubar.addMenu('&Help')
        cntH = ['&Help Content', '&Helper', 'Smth else']
        for i in cntH:
            fileMenu.addAction(QAction(i, self))


        toolbar = self.addToolBar('Exit')
        toolbar.addAction(exitAction)

        self.setGeometry(300,300,350,250)
        self.setWindowTitle('MAin W')
        self.show()
    def createActions(self):
        self.helpContentAction = QAction(QIcon('help'), self)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec())