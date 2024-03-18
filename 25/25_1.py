import sys
from PyQt6.QtWidgets import QApplication, QPushButton, QMainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Clicks change')
        self.count = 0

        self.button = QPushButton('click')
        self.setCentralWidget(self.button)
        self.button.setCheckable(True)
        self.button.clicked.connect(self.button_clicked)

    def button_clicked(self):
        self.count += 1
        self.button.setText('clicked ' + str(self.count) + ' times')
        print(self.count)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
