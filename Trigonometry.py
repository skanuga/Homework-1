import math
import matplotlib.pyplot as plt
import numpy as np


def plot(function):
    x = np.linspace(-10, 10, 40)
    for i in func:
        if "sin" in function:
            plt.plot (x, np.sin(x), "blue", label = "sin(x)")
        if "cos" in function:
            plt.plot (x, np.cos(x), "magenta", label = "cos(x)")    
        if "sinc" in function:
            plt.plot (x, np.sinc(x), "teal", label = "sinc(x)")
        plt.plot()
        plt.show()
        
        
        
    
    
function = input('--function = ')
plot(function)
