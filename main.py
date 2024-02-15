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
    dimensi= 4
    n_bat=100
    n_generasi=100000
    r0=0.81
    alpha=0.95
    gamma=0.95
    fmin=0
    fmax=1
    b_down =-10
    b_up =10
    maxCount = 700

    ba_array = []


    app = QApplication([])
    application = visualisation.MainWindow()
    application.show()

    #for i in range(0, 10):
        #ba_array.append(BatAlgorithm(
                #dimensi, n_bat, n_generasi, r0, alpha, gamma-i/10.0, fmin, fmax, b_down, b_up, func.easom, maxCount))


    sys.exit(app.exec())





