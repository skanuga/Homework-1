#!/usr/bin/env python3
import math
import matplotlib.pyplot as plt
import numpy as np


def plot(function):
    x = np.linspace(-10, 10, 40)
    for i in function:
        if "sin" in function and "sinc" not in function:
            plt.plot (x, np.sin(x), "blue", label = "sin(x)")
        if "cos" in function:
            plt.plot (x, np.cos(x), "magenta", label = "cos(x)")    
        if "sinc" in function and "sin" not in function:
            plt.plot (x, np.sinc(x), "teal", label = "sinc(x)")
        if "sin" in function and "sinc" in function:
            plt.plot (x, np.sin(x), "blue", label = "sin(x)")
            plt.plot (x, np.sinc(x), "teal", label = "sinc(x)")
        plt.title ("Trigonometry Plot")
        plt.legend()
        plt.xlaber("x")
        plt.ylabel(function)
        plt.show()
        
   
function = input('--function = ')
plot(function)

