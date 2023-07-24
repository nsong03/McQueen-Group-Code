# -*- coding: utf-8 -*-
"""
Created on Mon Jul 17 16:55:23 2023

@author: jayso
"""

import math
import matplotlib.pyplot as plt
import numpy as np

import VanDerWaalsEquation as VDW

# Generate pressure values
P_values = np.linspace(0.2, 5, 100)

# atm to bar
#1 atm = 1.01325 bar

# Example usage
P = 10  # Pressure (atm)



# Calculate corresponding volume values
V_values = []
for P in P_values:
    V = VDW.solve_van_der_waals_equation(P)
    V_values.append(V)

# Plotting
plt.plot(P_values, V_values)
plt.xlabel('Pressure (atm)')
plt.ylabel('Volume (V)')
plt.title('van der Waals Equation: Volume vs. Pressure')
plt.grid(True)
plt.show()
