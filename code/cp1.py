import math
import scipy as sp
import numpy as np
import matplotlib.pyplot as plt

parentInit = 100
aHalf = 1.1
aLambda = np.log(2)/ahalf
def parentdecay(time) :
    return parentInit * np.exp(-(aLambda*time))
x= np.arange(0, 3000, 1)
y = parentdecay(x)