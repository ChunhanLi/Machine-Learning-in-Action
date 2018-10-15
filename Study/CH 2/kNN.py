# coding: utf-8
import numpy as np
def createDataSet():
    group = np.array([[1, 1.1], [1, 1], [0,0], [0,0.1]])
    labels = ['A', 'A', 'B', 'B']
    return group , labels
