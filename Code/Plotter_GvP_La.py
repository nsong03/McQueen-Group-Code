# -*- coding: utf-8 -*-
"""
Created on Thu Jun 29 14:00:55 2023

@author: jayso
"""

# The is the plotter for G v P. Only switched the x variable

import matplotlib.pyplot as plt
import numpy as np
import Combind_Datapt2


def plot_seperate(filename, oxide, maximum_P,T, seperate: bool):
    
    # Coordinates (X, Y) 
    x = np.linspace(0.000001,8000,100000)
    y = x
    
    data_class = Combind_Datapt2.class_input(filename, oxide)
    
    
    #Graph Domain and Range
    plt.xlim(1, maximum_P)
    plt.ylim(10, 30)
    
    #Add X and Y Lable
    plt.xlabel("Pressure Bar")
    plt.ylabel('del G (KJ)')

    if seperate:
        for chemical in data_class:
            #Add a title
            plt.title(chemical.name + " Temperature = " + str(T) + " K")
            #Plot
            plt.plot(y,chemical.slope_P(x,T) + chemical.y_int(oxide))
        
            #Show Grid
            plt.grid()
            plt.show()
    else:
        for chemical in data_class:
            plt.title(file + " Temperature = " + str(T) + " K")
            #Plot
            plt.plot(y,chemical.slope_P(x,T) + chemical.y_int(oxide), label= chemical.name)
            #print(chemical.O2,chemical.del_S,chemical.O2)
            #print(chemical.y_int(oxide))
        
            #Show Grid
            plt.legend(loc = 'lower right')
            
            
        plt.grid()
        plt.show()
        
maximum_P = 1000
filepath = r"C:\Users\jayso\OneDrive - Howard University\Howard\Summer 2023\PARADIM\McQueen Group\Code\Data\\"
file = 'LaNiO'
fileend = r"_T1.csv"
oxide = "La2O3" 
T = 1000


plot_seperate(filepath + file + fileend, oxide,maximum_P, T, False)
    

