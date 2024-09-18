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
    
        if "sin" in function and "sinc" not in function and len(function) <= 5: #sin alone
            plt.plot (x, np.sin(x), "blue", label = "sin(x)")
            # print('sin')
        if "cos" in function and len(function) <= 5: #cos alone
            plt.plot (x, np.cos(x), "magenta", label = "cos(x)")  
           # print('cos')
        if "sinc" in function and len(function)==4: #sinc alone
            plt.plot (x, np.sinc(x), "teal", label = "sinc(x)")
            #print('sinc')
        if "cos" in function and "sinc" in function and len(function) >= 8: #cos,sinc
             plt.plot (x, np.cos(x), "magenta", label = "cos(x)")  
             plt.plot (x, np.sinc(x), "teal", label = "sinc(x)")
             #print('cos,sin')
        if "sin" in function and "sinc" in function and "cos" not in function and len(function) >= 8: #sin,sinc
             plt.plot (x, np.sin(x), "blue", label = "sin(x)")
             plt.plot (x, np.sinc(x), "teal", label = "sinc(x)")
             #print('sin,sinc')
        if "cos" in function and "sin" in function and len(function) <= 7: #cos,sinc
             plt.plot (x, np.cos(x), "magenta", label = "cos(x)")  
             plt.plot (x, np.sin(x), "blue", label = "sin(x)")
             #print('cos,sin')        
        if len(function) > 10: #sin,sinc,cos
            plt.plot (x, np.sin(x), "blue", label = "sin(x)")
           # print('all')
            
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
        if "sin" in function and "sinc" not in function and len(function) <= 5: #sin alone
            df['sin(x)'] = np.sin(x)
        if "cos" in function and len(function) <= 5: #cos alone
            df['cos(x)'] = np.cos(x)
        if "sinc" in function and len(function)==4: #sinc alone
            df['sinc(x)'] = np.sinc(x)
        if "cos" in function and "sinc" in function and len(function) >= 8: #cos,sinc
            df['cos(x)'] = np.cos(x)
            df['sinc(x)'] = np.sinc(x)
        if "sin" in function and "sinc" in function and "cos" not in function and len(function) >= 8: #sin,sinc
            df['sinc(x)'] = np.sinc(x)
            df['sin(x)'] = np.sin(x)
        if "cos" in function and "sin" in function and len(function) <= 7: #cos,sin
            df['cos(x)'] = np.cos(x)
            df['sin(x)'] = np.sin(x)
        if len(function) > 10: #sin,sinc,cos
            df['sinc(x)'] = np.sinc(x)
            df['sin(x)'] = np.sin(x)
            df['cos(x)'] = np.cos(x)
            # enter data points for each of the requested functions into the data frame
        return df    
    
def textfile(df, txtfile):
    string = df.to_string(header=True, index=True)
    f = open(path, 'w') #open and write into the txt file
    f.write(string)
    f.close()
    #print('Writing table into TXT')
    
fig = plt.figure()
def readfromfile(function,path):
    headerlist = df.columns.astype(str)
    headers = ' '.join(headerlist)
    x = df.index.tolist()
    for i in headers:
        if "sin" in headers and "sinc" not in headers: #sin alone
            y_sin = df["sin(x)"].tolist()
            plt.plot(x, y_sin, "royalblue", label = "sin(x)")   
        if "cos" in headers: #cos alone
            y_cos = df["cos(x)"].tolist()
            plt.plot(x, y_cos, "cyan", label = "cos(x)")
        if "sinc" in headers and len(headerlist)==1: #sinc alone
            y_sinc = df["sinc(x)"].tolist()
            plt.plot(x, y_sinc, "coral", label = "sinc(x)")    
        if "sinc" in headers and "cos" in headers and len(headerlist) == 2: #cos,sinc
            y_sinc = df["sinc(x)"].tolist()
            plt.plot(x, y_sinc, "coral", label = "sinc(x)")  
        if "sinc" in headers and "cos" not in headers and len(headerlist) == 2: #sin,sinc
            y_sinc = df["sinc(x)"].tolist()
            y_sin = df["sin(x)"].tolist()
            plt.plot(x, y_sin, "royalblue", label = "sin(x)") 
            plt.plot(x, y_sinc, "coral", label = "sinc(x)")  
        if len(headerlist) == 3: #sin,sinc,cos
            y_sin = df["sin(x)"].tolist()
            y_sinc = df["sinc(x)"].tolist()
            plt.plot(x, y_sinc, "coral", label = "sinc(x)")                          
            plt.plot(x, y_sin, "royalblue", label = "sin(x)") 
            
        plt.xlabel('x')
        plt.ylabel(f"{function}")
        plt.title('Tigonometry Graph From TXT File')
        plt.legend(loc = "upper left")
        plt.show()
        return
    
             
def prnt(img):
    
    if 'jpeg' in img:
        path = rf"/Users/skanuga/Desktop/{filename}.jpeg"
        fig.savefig(path, format='jpeg')
    if 'eps' in img:
        path = rf"/Users/skanuga/Desktop/{filename}.jpeg"
        fig.savefig(path, format='eps')
    if 'pdf' in img:
        path = rf"/Users/skanuga/Desktop/{filename}.jpeg"
        fig.savefig(path, format='pdf')
    print('exporting...')
        
    ##UNTESTED
    
    

function = input('--function = ')
plot(function)

plot = plot(function)

filename = input ('--write = ')
path = rf"/Users/skanuga/Desktop/{filename}"
table(function, path)
df=table(function, path)
textfile(df,path)
readfile = input('--read from file = ')
readfromfile(function, path)
df = table(function,path)
img = input('--print = ')
prnt(img)

