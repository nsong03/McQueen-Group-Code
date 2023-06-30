# -*- coding: utf-8 -*-
"""
Created on Thu Jun 29 15:42:23 2023

@author: jayso
"""

# This is my plotter function where I am attempting to get past the superflous species error

import Plotter_PrNiO

'''
reactants = "Pr6O11 + NiO + O2"
Plotter_PrNiO.plot_seperate('PrNiO_T.csv', reactants, 8000,1, False)
'''
'''
reactants_list = [
    "Pr6O11 + NiO + O2",
    "Pr6O11 + NiO"
    # Add more reactant combinations as needed
]

def try_different_variables(variables_list):
    for variable in variables_list:
        try:
            # Call your function with the current variable
            result = Plotter_PrNiO.plot_seperate('LaNiO_T.csv', variable, 8000,1, False)
            return result  # Stop trying different variables once successful
        except Exception as e:
            print(f"Error with {variable}: {str(e)}")
            continue

    # If all variables failed
    print("Unable to process any variable in the list")

# Example list of variables to try
variables_list = [
    "La2O3 + NiO + O2",
    "La2O3 + NiO"
    # Add more reactant combinations as needed
]

# Call the try_different_variables function
try_different_variables(variables_list)

'''
import itertools

def try_different_variables(variables_list):
    cycle_iterator = itertools.cycle(variables_list)

    while True:
        variable = next(cycle_iterator)
        try:
            # Call your function with the current variable
            result = Plotter_PrNiO.plot_seperate('LaNiO_T.csv', variable, 8000,1, False)
            return result  # Stop trying different variables once successful
        except Exception as e:
            print(f"Error with {variable}: {str(e)}")
            continue

    print("Unable to process any variable in the list")

# Example list of variables to try
variables_list = [
    "La2O3 + NiO + O2",
    "La2O3 + NiO"
    # Add more reactant combinations as needed
]

# Call the try_different_variables function
try_different_variables(variables_list)