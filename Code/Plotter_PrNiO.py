# -*- coding: utf-8 -*-
"""
Created on Thu Jun 29 14:00:55 2023

@author: jayso
"""

# This is the plotter specifically for PrNiO. Since it is using the class for PrNiO.

import matplotlib.pyplot as plt
import numpy as np
import Combind_Data



def plot_seperate(filename, reactants, maximum_temp,P, seperate: bool):
    
    # Coordinates (X, Y) 
    x = np.linspace(-1000,maximum_temp)
    y = x
    
    data_class = Combind_Data.class_input(filename, reactants)
    
    #Graph Domain and Range
    plt.xlim(0, maximum_temp)
    plt.ylim(-500, 0)
    
    #Add X and Y Lable
    plt.xlabel("Temperature K")
    plt.ylabel('del G')

    if seperate:
        for chemical in data_class:
            #Add a title
            plt.title(chemical.name + " P = " + str(P) + " Bar")
            #Plot
            plt.plot(y,chemical.slope(x,P) + chemical.del_H)
        
            #Show Grid
            plt.grid()
            plt.show()
    else:
        for chemical in data_class:
            plt.title("PrNiO " + " P = " + str(P) + " Bar")
            #Plot
            plt.plot(y,chemical.slope(x,P) + chemical.del_H, label= chemical.name)
        
            #Show Grid
            plt.legend(loc = 'lower right')
            
            
        plt.grid()
        plt.show()
        

    

