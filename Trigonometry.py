#!/usr/bin/env python3
import math
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

#Question 1
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
        plt.legend(loc = "upper left")
        plt.xlabel("x")
        plt.ylabel(function)
        plt.show()
        return      

#Question 2
def table(function, path):
    x = np.arange(-10,10.05,0.05)
    x = np.round(x, 3)
   # x = np.linspace(-10,10,400)
    df = pd.DataFrame(index = x)
    for i in function:
        if "sin" in function and "sinc" not in function:
            df['sin(x)'] = np.sin(x)
        if "cos" in function:
            df['cos(x)'] = np.cos(x)
        if "sinc" in function and "sin" not in function:
            df['sinc(x)'] = np.sinc(x)
        if "sin" in function and "sinc" in function:
            df['sinc(x)'] = np.sinc(x)
            df['sin(x)'] = np.sin(x)
    string = df.to_string(header=True, index=True)
    f = open (path, 'w')
    f.write(string)
    f.close()
    





filename = input ('--write = ')
path = rf"/Users/skanuga/Desktop/{filename}"
function = input('--function = ')
plot(function)
table = table(function, path)
print(table)

