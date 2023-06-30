# -*- coding: utf-8 -*-
"""
Created on Wed Jun 28 22:06:49 2023

@author: jayso
"""

# This file takes the data from the csv file and balanced equation and put them in a class

import EquationBalancer as Eb
import csv_extractor as ce
import Chemical_Data_Class

# This function takes a file and prints out multiple tuples for each variable
def combind_data(filename, reactants):
    #reactants = "Pr6O11 + NiO + O2"
    names, mpids, eVs = ce.use_csv(filename)
    
    normalized_equations = []
    normalized_oxygen_reactant_coeffs = []
    normalized_NiO_reactant_coeffs = []
    normalized_product_coeff = []
    
    for name in names:
        # Running the Equations that give us the data
        chemical_equation = Eb.chemical_equation(reactants, name)
        normalized_equation, normalized_oxygen_reactant_coeff, normalized_NiO_reactant_coeff, first_normalized_product_coeff = Eb.balance_and_normalize_equation(chemical_equation)
        
        # Taking the data and putting it all in tuples that line up with the names
        normalized_equations.append(normalized_equation)
        normalized_oxygen_reactant_coeffs.append(normalized_oxygen_reactant_coeff)
        normalized_NiO_reactant_coeffs.append(normalized_NiO_reactant_coeff)
        normalized_product_coeff.append(first_normalized_product_coeff)
        
        
    return names, mpids, eVs, normalized_equations, normalized_oxygen_reactant_coeffs, normalized_NiO_reactant_coeffs, normalized_product_coeff
        

# print(data_PrNiO_list)
    
# This function takes the variables and put them into a class, but in list
def class_input(filename, reactants):
    names, mpids, eVs, normalized_equations, normalized_oxygen_reactant_coeffs, normalized_NiO_reactant_coeffs, normalized_product_coeff = combind_data(filename, reactants)

    objects = []

    for i in range(len(names)):
        obj = Chemical_Data_Class.ChemicalData(names[i], mpids[i], eVs[i], normalized_equations[i], normalized_oxygen_reactant_coeffs[i], normalized_NiO_reactant_coeffs[i],normalized_product_coeff[i])
        objects.append(obj)
    
    return objects





    
