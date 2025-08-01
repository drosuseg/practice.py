import sys 
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel,
                            QPushButton, QVBoxLayout, QHBoxLayout)
from PyQt5.QtCore import QTimer, QTime, Qt
from PyQt5.QtGui import QFont, QFontDatabase

class Stopwatch(QWidget):
    def __init__ (self):
         super().__init__()
         self.time = QTime(0 , 0 , 0 ,0 )
         self.time_label = QLabel("00:00:00:00", self)
         self.start_button = QPushButton("Start",self)
         self.stop_button = QPushButton("Stop",self)
         self.reset_button = QPushButton("Reset",self)
         self.timer = QTimer(self)
         self.initUI()
    
    def initUI(self):
         self.setWindowTitle("Stopwatch")

         vbox = QVBoxLayout()
         vbox.addWidget(self.time_label)

         self.setLayout(vbox)

         self.time_label.setAlignment(Qt.AlignCenter)

         hbox = QHBoxLayout()
         hbox.addWidget(self.start_button)
         hbox.addWidget(self.stop_button)
         hbox.addWidget(self.reset_button)

         vbox.addLayout(hbox)

         self.setStyleSheet("""
            QPushButton, QLabel{
              padding:20px;
              font-weight:bold;          
                            }
             QPushButton{
               font-size: 50px;
                            }  
            QLabel{
               font-size: 120px;
               background-color: black;
               border-radius: 20px;
               color: #1cff55;
                            }                                    
                            """)         
         font_id = QFontDatabase.addApplicationFont("DS-DIGIT.TTF")
         font_family = QFontDatabase.applicationFontFamilies(font_id)[0]
         my_font = QFont(font_family, 150)
         self.time_label.setFont(my_font)

         self.start_button.clicked.connect(self.start)
         self.stop_button.clicked.connect(self.stop)
         self.reset_button.clicked.connect(self.reset)
         self.timer.timeout.connect(self.update_display)

    def start(self):
         self.timer.start(10)

    def stop(self):
         self.timer.stop()

    def reset(self):
         self.timer.stop()
         self.time = QTime(0,0,0,0)
         self.time_label.setText(self.format_time(self.time))
    
    def format_time(self, time):
         hours = time.hour()
         minutes = time.minute()
         seconds = time.second()
         milliseconds = time.msec()//10
         return f"{hours:02}:{minutes:02}:{seconds:02}.{milliseconds:02}"
    
    def update_display(self):
         self.time= self.time.addMSecs(10)
         self.time_label.setText(self.format_time(self.time))

if __name__ == "__main__":
     app = QApplication(sys.argv)
     stopwatch = Stopwatch()
     stopwatch.show()
     sys.exit(app.exec())