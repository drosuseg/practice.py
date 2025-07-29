#PyQt5 introduction
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QIcon
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap

class MainWindow(QMainWindow):
    def __init__(self):
     super().__init__()
     self.setWindowTitle("My cool first GUI")
     self.setGeometry(0,0,800,600)
     self.setWindowIcon(QIcon("pic.png"))

     label = QLabel(self)
     label.setGeometry(0,0,550,550)

     pixmap = QPixmap("pic.png")
     label.setPixmap(pixmap)

     label.setScaledContents(True)

     label.setGeometry(0,0, label.width(), label.height())

  #   label = QLabel("Hello", self)
  #   label.setFont(QFont("Arial", 40))
  #   label.setGeometry(0,0,300,100)
  #   label.setStyleSheet("color:black;"
  #                       "background-color: #eab676;"
  #                       "font-weight: bold;"
   #                      "font-style: italic;"
   #                      "text-decoration: overline;")
   #  label.setAlignment(Qt.AlignHCenter)


def main():
   app = QApplication(sys.argv)
   window = MainWindow()
   window.show()
   sys.exit(app.exec_())

if __name__ == "__main__":
   main()
    

