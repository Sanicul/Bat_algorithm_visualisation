from PyQt5.QtWidgets import QMainWindow, QGraphicsScene, QGraphicsView
from PyQt5.QtGui import QBrush, QPen, QColor
from PyQt5.QtCore import Qt
from window import Ui_MainWindow
from BatAlgorithm import BatAlgorithm


class MainWindow(QMainWindow):
    pointsize = 10
    black_pen = QPen(QColor.fromRgb(0, 0, 0))
    bat_color = QBrush(QColor.fromRgb(196, 108, 0))
    algorithm =

    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.scene = QGraphicsScene()

    def draw_bats(self, x):
        for elem in x:
            self.scene.addEllipse(elem[0] - self.pointsize / 2, elem[1] - self.pointsize / 2, self.pointsize,
                                  self.pointsize, self.black_pen, self.bat_color)
