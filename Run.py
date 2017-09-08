import TestFile
import numpy as np
import pandas as pd

X = np.genfromtxt('test.csv', delimiter=",")

#Y = csv[:, 1]

y=TestFile.Test(X)
#X1 = X[:,0:1]
#Y1 = Y[:,0:1]
#y1 = y[:,0:1]

#output=[X1,Y1,y1]
output=[X,y]
#columns = ["X","Y","Y Predict"]


myoutput = pd.DataFrame(output)

myoutput.T.to_csv('output.csv', index= False, header = False)




