from PyQt5.QtWidgets import QMainWindow, QGraphicsScene, QGraphicsView
from PyQt5.QtGui import QBrush, QPen, QColor
from PyQt5.QtCore import Qt
from window import Ui_MainWindow
import numpy as np
from BatAlgorithm import BatAlgorithm


class MainWindow(QMainWindow):
    pointsize = 10
    black_pen = QPen(QColor.fromRgb(0, 0, 0))
    bat_color = QBrush(QColor.fromRgb(196, 108, 0))

    def __init__(self, alg: BatAlgorithm):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.scene = QGraphicsScene()
        self.alg = alg
        self.ui.oneIteration.clicked.connect(self.draw_bats)
        self.ui.initialize.clicked.connect(self.set_initial_distribution)

    def draw_bats(self, x):
        for elem in x:
            self.scene.addEllipse(int(elem[0]) - self.pointsize / 2, int(elem[1]) - self.pointsize / 2,
                                  self.pointsize, self.pointsize,
                                  self.black_pen, self.bat_color)

    def set_initial_distribution(self):
        self.alg.proses_init()
        a = self.alg.x.copy()
        a = (a + 10) * 10
        self.draw_bats(a)




