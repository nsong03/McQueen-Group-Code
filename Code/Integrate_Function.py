# -*- coding: utf-8 -*-
"""
Created on Mon Jul 24 10:55:26 2023

@author: jayso
"""

from scipy.integrate import quad
import VanDerWaalsEquation as VDW

import math
import matplotlib.pyplot as plt
import numpy as np


def int_VDW(P):
    bar_to_atm = P/1.01325
    O2_percentage = 20.947/100
    integral = quad(VDW.solve_van_der_waals_equation,O2_percentage,bar_to_atm, complex_func= False)
    L_atm_to_KJ = (integral[0])*101.325/1000 
    return L_atm_to_KJ


print(int_VDW(40))
print(int_VDW(205))

'''
# Generate pressure values
P_values = np.linspace(0.2, 205, 100)

# Calculate corresponding volume values
V_values = []
for P in P_values:
    V = int_VDW(P)
    V_values.append(V)

# Plotting
plt.plot(P_values, V_values)
plt.xlabel('Pressure (Bar)')
plt.ylabel('Del G (KJ)')
plt.title('van der Waals Equation: Del G vs. Pressure')
plt.grid(True)
plt.show()
'''
    
    
    
    
    
    
    
    
    
    