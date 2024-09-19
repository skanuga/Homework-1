#!/usr/bin/env python3
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 16:06:57 2024

@author: skanuga
"""
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
            plt.plot (x, np.sin(x), "deepskyblue", label = "sin(x)")   
            
        if "sinc" in function and len(function)==4: #sinc alone
            plt.plot (x, np.sinc(x), "springgreen", label = "sinc(x)")
            
        if "cos" in function and len(function) <= 5: #cos alone
            plt.plot (x, np.cos(x), "magenta", label = "cos(x)") 
             
        if "cos" in function and "sinc" in function and len(function) >= 8: #cos,sinc
             plt.plot (x, np.cos(x), "magenta", label = "cos(x)")  
             plt.plot (x, np.sinc(x), "springgreen", label = "sinc(x)")
            
        if "sin" in function and "sinc" in function and "cos" not in function and len(function) >= 8: #sin,sinc
             plt.plot (x, np.sin(x), "deepskyblue", label = "sin(x)")
             plt.plot (x, np.sinc(x), "springgreen", label = "sinc(x)")
             
        if "cos" in function and "sin" in function and len(function) <= 7: #cos,sinc
             plt.plot (x, np.cos(x), "magenta", label = "cos(x)")  
             plt.plot (x, np.sin(x), "deepskyblue", label = "sin(x)")
             
        if len(function) > 10: #sin,sinc,cos
            plt.plot (x, np.sin(x), "deepskyblue", label = "sin(x)")
            
            
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

    Returns df, a DataFrame of values and their corresponding function values
    -------


    """
    x = np.arange(-10,10.05,0.05)  #create a list of x values - becomes left most column of txt file
    x = np.round(x, 3) #round x values to 2 decimal places
  
    df = pd.DataFrame(index = x) #use data frame to generate a table
    for i in function:
        if "sin" in function and "sinc" not in function and len(function) <= 5: #sin alone
            df['sin(x)'] = np.sin(x)
            
        if "sinc" in function and len(function)==4: #sinc alone
            df['sinc(x)'] = np.sinc(x)
            
        if "cos" in function and len(function) <= 5: #cos alone
            df['cos(x)'] = np.cos(x)
            
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
    
def textfile(df, path):
    """
    

    Parameters
    ----------
    df : Data Frame of table data
    path : string of path of file to be created, written into, and saved

    Returns
    -------
    None.

    """
    string = df.to_string(header=True, index=True) #create headings
    f = open(path, 'w') #open the txt file
    f.write(string) #write into txt file
    f.close() #close file
    


def readfromfile(function,path):
    """
    

    Parameters
    ----------
    function : list of functions to be calcluated from input
    path : string of the path of the file to be read

    Returns
    -------
    None.

    """
    headerlist = df.columns.astype(str) #create a list of headers from the table
    headers = ' '.join(headerlist)
    x = df.index.tolist() # x values are taken from the left most column of the text file
    for i in headers: #for each header, create a list of y values from the table and then plot the list against the x values
        if "sin" in headers and "sinc" not in headers: #sin alone
            y_sin = df["sin(x)"].tolist()
            plt.plot(x, y_sin, "royalblue", label = "sin(x)")   
            
        if "sinc" in headers and len(headerlist)==1: #sinc alone
            y_sinc = df["sinc(x)"].tolist()
            plt.plot(x, y_sinc, "coral", label = "sinc(x)")  
            
        if "cos" in headers: #cos alone
            y_cos = df["cos(x)"].tolist()
            plt.plot(x, y_cos, "cyan", label = "cos(x)")  
            
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
         
        #add plot title, axis titles, and legend
        plt.xlabel('x')
        plt.ylabel(f"{function}")
        plt.title('Tigonometry Graph From TXT File')
        plt.legend(loc = "upper left")
        plt.show()
        return
    
    
fig = plt.figure() #create a figure to save   
         
def prnt(img):
    """
    

    Parameters
    ----------
    img : input string of the file type to be created

    Returns
    -------
    None.

    """
    #save image in the format corresponding to the input
    if 'jpeg' in img:
        path = rf"/Users/skanuga/Desktop/{file}.jpeg"
        fig.savefig(path, format='jpeg')
    if 'eps' in img:
        path = rf"/Users/skanuga/Desktop/{file}.eps"
        fig.savefig(path, format='eps')
    if 'pdf' in img:
        path = rf"/Users/skanuga/Desktop/{file}.pdf"
        fig.savefig(path, format='pdf')

 
    
    

function = input('--function = ')
plot(function)
file = input ('--write = ')
path = rf"/Users/skanuga/Desktop/{file}"
table(function, path)
df=table(function, path)
textfile(df,path)
readfromfile(function, path)
df = table(function,path)
img = input('--print = ')
prnt(img)

