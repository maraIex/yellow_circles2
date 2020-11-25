import sys
import random

from PyQt5 import uic
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QColor, QPainterPath
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QMainWindow


class DisplayWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.do_paint = False
        uic.loadUi('yellow_circles.ui', self)
        self.setWindowTitle('Нажмите кнопку, нажмите. Ну пожалуйста')
        self.btn.clicked.connect(self.b_event)

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_figure(qp)
            qp.end()

    def b_event(self):
        self.paint()

    def paint(self):
        self.do_paint = True
        self.repaint()

    def draw_figure(self, qp):
        color = [255, 255, 0]
        # color = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]
        qp.setBrush(QColor(color[0], color[1], color[2]))
        d = random.randint(0, 500)
        a = random.randint(0, 800)
        b = random.randint(0, 600)
        qp.drawEllipse(a, b, d, d)


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)