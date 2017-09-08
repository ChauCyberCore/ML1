import TrainFile
import numpy as np
import matplotlib.pyplot as plt

def Test(X_test):

    TrainValue = TrainFile.train()

    y_test = TrainValue[0]*X_test+TrainValue[1]

    return y_test