# -*- coding: utf-8 -*-
"""
Created on Wed Jun 28 22:06:49 2023

@author: jayso
"""

# This file takes the data from the csv file and balanced equation and put them in a class

import EquationBalancerpt2 as Eb2
import csv_extractor as ce
import Chemical_Data_Class

# This function takes a file and prints out multiple tuples for each variable
def combind_data(filename, oxide):
    #reactants = "Pr6O11 + NiO + O2"
    names, mpids, eVs = ce.use_csv(filename)
    
    normalized_equations, normalized_oxygen_reactant_coeffs, normalized_NiO_reactant_coeffs, normalized_product_coeffs, first_normalized_reactant_coeffs = Eb2.balance_equations(oxide, filename)

    #print(len(names))
    #print(len(mpids))
    #print(len(eVs))
    #print(len(normalized_equations))
    #print(len(normalized_oxygen_reactant_coeffs))
    #print(len(normalized_NiO_reactant_coeffs))
    #print(len(normalized_product_coeffs))
    #print(len(first_normalized_reactant_coeffs))

        
        
    return names, mpids, eVs, normalized_equations, normalized_oxygen_reactant_coeffs, normalized_NiO_reactant_coeffs, normalized_product_coeffs, first_normalized_reactant_coeffs
        

# print(data_PrNiO_list)
    
# This function takes the variables and put them into a class
def class_input(filename, oxide):
    names, mpids, eVs, normalized_equations, normalized_oxygen_reactant_coeffs, normalized_NiO_reactant_coeffs, normalized_product_coeffs, first_normalized_reactant_coeffs = combind_data(filename, oxide)

    objects = []

    for i in range(len(names)):
        obj = Chemical_Data_Class.ChemicalData(names[i], mpids[i], eVs[i], normalized_equations[i], normalized_oxygen_reactant_coeffs[i], normalized_NiO_reactant_coeffs[i], normalized_product_coeffs[i], first_normalized_reactant_coeffs[i])
        objects.append(obj)
    
    return objects


#combind_data("LaNiO_T.csv", "La2O3")




    
