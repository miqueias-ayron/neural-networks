import numpy as np
from typing import List

def step(x:float)->float:
    if x >= 1:
        return 1
    return 0
 
def sigmoid(x:float)->float:
    return 1/(1+np.exp(-x))

def tanh(x:float)->float:
    return (np.exp(x)-np.exp(-x))/((np.exp(x)+np.exp(-x)))

def ReLU(x:float)->float:
    return max(0,x)

def softmax(x:List[float])->List[float]:
    '''we return a list of probabilities, where each element is
    the probability of the respective class'''
    ex = np.exp(x)
    return ex/ex.sum()

def linear(x):
    return x
