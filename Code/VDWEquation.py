# -*- coding: utf-8 -*-
"""
Created on Mon Jul 24 15:53:17 2023

@author: jayso
"""
import math
from scipy.integrate import quad
import matplotlib.pyplot as plt
import numpy as np


def VDW(P,T):
    
    def solve_van_der_waals_equation(P):
        n = 1   # Number of moles
        a = 1.59  # Van der Waals constant
        b = 0.0318  # Van der Waals constant
        R = 0.0821  # Ideal gas constant
          # Temperature
        
        # Coefficients for the cubic equation
        A = P
        B = -(P * n * b + n * R * T)
        C = a * n**2
        D = -a * n**3 * b

        # Calculate p and q coefficients
        p = (3 * A * C - B**2) / (3 * A**2)
        q = (2 * B**3 - 9 * A * B * C + 27 * A**2 * D) / (27 * A**3)

        # Calculate discriminant and intermediate values
        discriminant = q**2 / 4 + p**3 / 27
        u = math.pow(-q / 2 + math.sqrt(discriminant), 1/3)
        v = math.pow(-q / 2 - math.sqrt(discriminant), 1/3)

        # Calculate the real root of the cubic equation
        V = u + v - B / (3 * A)

        return V
    
    def int_VDW(P):
        bar_to_atm = P/1.01325
        O2_percentage = 20.947/100
        integral = quad(solve_van_der_waals_equation,O2_percentage,bar_to_atm, complex_func= False)
        L_atm_to_KJ = (integral[0])*101.325/1000 
        return L_atm_to_KJ
    
    return int_VDW(P)

# print(type(VDW(1, 300)))

'''
print(VDW(1, 300))


# Generate pressure values
P_values = np.linspace(0.2, 205, 100)

# Calculate corresponding volume values
V_values = []
for P in P_values:
    V = VDW(P,300)
    V_values.append(V)

# Plotting
plt.plot(P_values, V_values)
plt.xlabel('Pressure (Bar)')
plt.ylabel('Del G (KJ)')
plt.title('van der Waals Equation: Del G vs. Pressure')
plt.grid(True)
plt.show()
'''