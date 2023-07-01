# -*- coding: utf-8 -*-
"""
Created on Thu Jun 29 14:00:55 2023

@author: jayso
"""

# This is the plotter specifically for PrNiO. Since it is using the class for PrNiO.

import matplotlib.pyplot as plt
import numpy as np
import Combind_Datapt2




def plot_seperate(filename, oxide, maximum_temp,P, seperate: bool):
    
    # Coordinates (X, Y) 
    x = np.linspace(-1000,maximum_temp)
    y = x
    
    data_class = Combind_Datapt2.class_input(filename, oxide)
    
    
    #Graph Domain and Range
    plt.xlim(0, maximum_temp)
    plt.ylim(-500, 500)
    
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
            plt.plot(y,chemical.slope(x,P) + chemical.y_int(oxide), label= chemical.name)
            #print(chemical.O2,chemical.del_S)
            #print(chemical.y_int(oxide))
        
            #Show Grid
            plt.legend(loc = 'lower right')
            
            
        plt.grid()
        plt.show()
        
maximum_temp = 8000
filename = "PrNiO_T.csv"
oxide = "Pr6O11" 

plot_seperate(filename, oxide ,maximum_temp, 1000, False)
    

