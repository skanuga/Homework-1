#!/usr/bin/env python3
import math
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def plot(function):
    """
    

    Parameters
    ----------
    function : function, or list of functions to be graphed 

    Returns plot of all functions graphed with legend and axes titled
    -------
    None.

    """
    x = np.linspace(-10, 10, 400) #create a list of x values
    for i in function: #plot functions as thy appear in the input list of functions
        if "sin" in function and "sinc" not in function:
            plt.plot (x, np.sin(x), "blue", label = "sin(x)")
        if "cos" in function:
            plt.plot (x, np.cos(x), "magenta", label = "cos(x)")    
        if "sinc" in function and "sin" not in function:
            plt.plot (x, np.sinc(x), "teal", label = "sinc(x)")
        if "sin" in function and "sinc" in function:
            plt.plot (x, np.sin(x), "blue", label = "sin(x)")
            plt.plot (x, np.sinc(x), "teal", label = "sinc(x)")
            #plot title, legend, axis titles
        plt.title ("Trigonometry Plot") 
        plt.legend(loc = "upper left")
        plt.xlabel("x")
        plt.ylabel(function)
        plt.show()
        return      
   

def table(function, path):
    """
    

    Parameters
    ----------
    function : list of functions to be calculated
    path : path of file generated

    Returns txt file with a table of function values
    -------
    None.

    """
    x = np.arange(-10,10.05,0.05)  #create a list of x values - becomes left most column of txt file
    x = np.round(x, 3) #round x values to 2 decimal places
  
    df = pd.DataFrame(index = x) #use data frame to generate a table
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
            # enter data points for each of the requested functions into the data frame
    string = df.to_string(header=True, index=True)
    f = open(path, 'w') #open and write into the txt file
    f.write(string)
    f.close()
    
# def readfromfile(readfile):
#     ##stopped here
    
#     return



def print(img, filename):
    
    if 'jpeg' in img:
        plt.savefig(path, format='jpg')
    if 'eps' in img:
        plt.savefig(path, format='eps')
    if 'pdf' in img:
        plt.savefig(path, format='pdf')
    ##UNTESTED
    
    

#readfile = input('--read from file = ')
filename = input ('--write = ')
path = rf"/Users/skanuga/Desktop/{filename}"
function = input('--function = ')
plot = plot(function)
img = input('--print = ')
plot(function)
table = table(function, path)
print(table)
