# -*- coding: utf-8 -*-
"""
Created on Fri Jun 30 10:53:43 2023

@author: jayso
"""

import EquationBalancer
import csv_extractor as ce


def balance_equations(oxide, filename, show_errors=False):
    # Function to balance chemical equations given an oxide and a CSV file
    
    def get_product_sets(filename):
        # Function to retrieve and return the list of product sets dynamically
        # Modify this function to generate the product sets based on your CSV file
        
        # Use the 'ce.use_csv' function to extract the product names from the CSV file
        names, mpids, eVs = ce.use_csv(filename)
        
        # Create a product set for each name in the 'names' list
        product_sets = [(name,) for name in names]
        
        return product_sets

    def generate_reactant_sets(oxide):
        # Generate the reactant sets based on the given oxide
        reactants_list = []
        
        # Reactant set: Oxide + O2
        reactants_set1 = [oxide, "NiO"]
        reactants_list.append(reactants_set1)
        
        # Reactant set: Oxide + NiO + O2
        reactants_set2 = [oxide, "NiO", "O2"]
        reactants_list.append(reactants_set2)
        
        return reactants_list

    def balance_equation(reactants_list, products_list):
        balanced_equations = []
        
        for products in products_list:
            balanced = False
            
            for reactants in reactants_list:
                try:
                    equation = EquationBalancer.chemical_equation(" + ".join(reactants), " + ".join(products))
                    balanced_equation = EquationBalancer.balance_and_normalize_equation(equation)
                    balanced_equations.append(balanced_equation)
                    balanced = True
                    break  # Exit the loop if the equation is balanced
                except ValueError as e:
                    if show_errors:
                        print("Error balancing equation:", equation)
                        print(str(e))
            
            if not balanced:
                if show_errors:
                    print("No balanced equation found for products:", products)
        
        
        return balanced_equations

    # Generate the reactant sets based on the given oxide
    reactants_list = generate_reactant_sets(oxide)

    # Call the function to get the dynamic list of product sets
    products_list = get_product_sets(filename)

    # Call the balance_equation function
    balanced_equations = balance_equation(reactants_list, products_list)

    # Extract the desired variables from the balanced equations
    normalized_equations = []
    normalized_oxygen_reactant_coeffs = []
    normalized_NiO_reactant_coeffs = []
    first_normalized_product_coeffs = []
    first_normalized_reactant_coeffs = []

    for balanced_equation in balanced_equations:
        normalized_equation, normalized_oxygen_reactant_coeff, normalized_NiO_reactant_coeff, first_normalized_product_coeff, first_normalized_reactant_coeff = balanced_equation
        normalized_equations.append(normalized_equation)
        normalized_oxygen_reactant_coeffs.append(normalized_oxygen_reactant_coeff)
        normalized_NiO_reactant_coeffs.append(normalized_NiO_reactant_coeff)
        first_normalized_product_coeffs.append(first_normalized_product_coeff)
        first_normalized_reactant_coeffs.append(first_normalized_reactant_coeff)

    return normalized_equations, normalized_oxygen_reactant_coeffs, normalized_NiO_reactant_coeffs, first_normalized_product_coeffs, first_normalized_reactant_coeffs


# Main code

# Set the oxide and filename
#print(balance_equations("Nd2O3", "NdNiO_T.csv"))
