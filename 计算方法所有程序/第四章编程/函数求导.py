import numpy as np
from scipy.misc import *

def f(x): 
    return x**5
for x in range(1, 4):
    print （scipy.derivative(f, x, dx=1e-6, n = 2)）
