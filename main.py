import random
import numpy as np
import window
import functions as func
import visualisation
import sys
from BatAlgorithm import *
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWidgets import QMainWindow, QGraphicsScene, QGraphicsView

if __name__ == '__main__':
    dimension = 2
    n_bat = 100
    n_generation = 100000
    r0 = 0.81
    alpha = 0.95
    gamma = 0.95
    f_min = 0
    f_max = 1
    b_down = -10
    b_up = 10
    maxCount = 700

    ba_array = []

    app = QApplication([])
    application = visualisation.MainWindow(
        BatAlgorithm(dimension, n_bat, n_generation, r0, alpha, gamma, f_min, f_max, b_down, b_up, func.easom,
                     maxCount))
    application.show()

    sys.exit(app.exec())
