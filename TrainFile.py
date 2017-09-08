import numpy as np
from scipy.stats.stats import pearsonr
import matplotlib.pyplot as plt

def train():

    csv = np.genfromtxt('train.csv', delimiter=",", skip_header=215)

    X = csv[:,0]
    y = csv[:,1]


    average_X = np.average(X)
    average_y = np.average(y)

    sd_X = np.std(X)
    sd_y = np.std(y)

    r = pearsonr(X,y)

    B= r[0]*(sd_y/sd_X)

    A= average_y - B*average_X

    Total = 0
    for i in range(len(X)):
        y_predict = B*X[i]+A
        Total = Total + ((y_predict - y[i])**2)
    Error = np.sqrt(Total/len(X))

    plt.plot(X,y,'ro')
    plt.plot(X,B*X+A)
    #plt.show()

    value = [B,A,Error]
    return value




