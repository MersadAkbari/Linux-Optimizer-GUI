import sys
import os
import psutil
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction, QLineEdit, QMessageBox, QMenuBar, QMenu, QRadioButton, QLabel
from PyQt5.QtGui import QIcon, QPalette, QColor, QPixmap,QFont
from PyQt5.QtCore import pyqtSlot, Qt
from PyQt5 import QtCore

app = QApplication(sys.argv)

cmd = 'sudo sh -c "echo 3 > /proc/sys/vm/drop_caches"'
def main():
    app.setStyle("Fusion")
    ex = App()
    sys.exit(app.exec_())
before = psutil.virtual_memory()[2]
class App(QMainWindow):

    def __init__(self):
        super().__init__()

        self.title = 'Linux Optimizer'
        self.left = 10
        self.top = 10
        self.width = 420
        self.height = 380
        self.initUI()
        self.statusBar().showMessage('GitHub.com/MersadAkbari')


    def initUI(self):
        self.label = QLabel(self)
        self.label1 = QLabel(self)


        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
# Create a button in the window
        self.button = QPushButton('Optimize Now !', self)
        self.button.move(150,150)
        self.button.clicked.connect(self.on_click)

        # show all the widgets
        self.update()
        self.show()

    @pyqtSlot()
    def on_click(self):
        os.system(cmd)
        self.label.setText(f"Memory Usage Before Optimization : {before}%")
        self.label.move(50,220)
        self.label.setStyleSheet("border: 1px solid black;")        # loading image
        self.label.setFont(QFont('Arial', 11))
        self.label.resize(320,50)
        self.label.show()

        self.label1.setText(f"Memory Usage Now : {psutil.virtual_memory()[2]}%")
        self.label1.move(50,300)
        self.label1.setStyleSheet("border: 1px solid green;")        # loading image
        self.label1.setFont(QFont('Arial', 15))
        self.label1.resize(320,50)
        self.label1.show()


if __name__ == '__main__':
    main()
