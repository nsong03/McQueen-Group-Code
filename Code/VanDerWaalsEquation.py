# -*- coding: utf-8 -*-
"""
Created on Mon Jul 17 16:32:43 2023

@author: jayso
"""

import math

def solve_van_der_waals_equation(P):
    n = 1   # Number of moles
    a = 1.59  # Van der Waals constant
    b = 0.0318  # Van der Waals constant
    R = 0.0821  # Ideal gas constant
    T = 300  # Temperature
    
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
"""
# Example usage
P = 1  # Pressure (atm)


V = solve_van_der_waals_equation(P)
print("Volume (V):", V)

print(n*R*T/P)
"""