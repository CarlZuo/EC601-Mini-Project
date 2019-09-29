import sys
import Google_Api
import time
import GetTwitterFunction
from Google_Api import sample_analyze_sentiment
from GetTwitterFunction import getTwitterFeeds

from PyQt5.QtWidgets import QPushButton, QApplication, QWidget, QLineEdit, QLabel, QLCDNumber


class WinForm(QWidget):
    def __init__(self, parent=None):
        super(WinForm, self).__init__(parent)
        self.setGeometry(300, 300, 350, 350)
        self.setWindowTitle('Sentiment Analysis')
        self.Run = QPushButton('Run', self)
        self.Run.setGeometry(250, 100, 80, 40)
        self.Run.setStyleSheet("background-color: green")
        self.Run.clicked.connect(self.run)

        self.Inf = QLabel(self)
        self.Inf.move(40, 40)
        self.Inf.resize(200, 40)
        self.Inf.setText('Please type in something')


        self.Inline = QLineEdit(self)
        self.Inline.move(40,100)
        self.Inline.resize(200,40)

        self.Outline = QLCDNumber(self)
        self.Outline.move(90,170)
        self.Outline.resize(150,80)
        self.Outline.setDigitCount(2)
        self.Outline.display(00)

        self.Run.setDisabled(True)
        self.Inline.textChanged.connect(self.disableRun)

    def disableRun(self):

        self.Run.setDisabled(True)

        for ele in self.Inline.text():
            if ele != ' ':
                self.Run.setDisabled(False)



    def run(self):
      

        self.Inf.setText('Please waiting........')
        time.sleep(0.5)
        score = analyze(self.Inline.text())
        self.Outline.display(score)
        self.Inf.setText('Please type in something')


def analyze(txtin):
    
    eles = getTwitterFeeds(txtin, "en", 100, "recent")
    sum = 0
    if len(eles) == 0:
      return 50


    for ele in eles :
        sum = sum + sample_analyze_sentiment(ele)
    score = int(sum / len(eles) * 100 + 50)
    if score > 100:
      score = 100
    if score < 0:
      score = 0
    return score




if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = WinForm()
    win.show()
    sys.exit(app.exec_())