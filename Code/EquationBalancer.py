# -*- coding: utf-8 -*-
"""
Created on Wed Jun 28 16:42:31 2023

@author: jayso
"""

# This balances the equation and returns the variables listed below.
# The inputs are the reactants and products

from chempy import balance_stoichiometry
import chemparse as cp

def get_oxygen_coefficient(reactants):
    for reactant in reactants:
        elements = reactant.split()
        if elements[1] == "O2":
            return float(elements[0])

    raise ValueError("No O2 found in the reactants")
    
def get_NiO_coefficient(reactants):
    for reactant in reactants:
        elements = reactant.split()
        if elements[1] == "NiO":
            return float(elements[0])

    raise ValueError("No NiO found in the reactants")
    

def balance_and_normalize_equation(equation):    
    
    reactants, products = equation.split("->")

    # Split the reactants and products into individual compounds
    reactant_compounds = [compound.strip() for compound in reactants.split("+")]
    product_compounds = [compound.strip() for compound in products.split("+")]
    
    # Get all the compounds in on list
    all_compounds = reactant_compounds + product_compounds

    # Balance the equation using chempy
    balanced_reactants, balanced_products = balance_stoichiometry(reactant_compounds, product_compounds)

    # Build the balanced equation
    balanced_equation = " + ".join(f"{coeff} {compound}" for compound, coeff in balanced_reactants.items())
    balanced_equation += " -> "
    balanced_equation += " + ".join(f"{coeff} {compound}" for compound, coeff in balanced_products.items())


    compounds = balanced_equation.split(" -> ")
    reactants = compounds[0].split(" + ")
    products = compounds[1].split(" + ")

    #Code to get number of atoms in first reactant element (La2O3, Pr6O11)
    formula = cp.parse_formula(reactant_compounds[0])

    first_element = list(formula.keys())[0]
    atom_count_first_reactant_first_element = formula[first_element]

    #the 2 is added so we can start with 1/2 instead of 1. This is because we want the 1-1-3
    first_reactant_coeff = (int(reactants[0].split()[0]))
    normalizer_coeff = first_reactant_coeff*atom_count_first_reactant_first_element

    normalized_reactants = [f"{int(coeff)/normalizer_coeff} {compound}" for coeff, compound in (item.split() for item in reactants)]
    normalized_products = [f"{int(coeff)/normalizer_coeff} {compound}" for coeff, compound in (item.split() for item in products)]

    #Get the O2 coeff
    normalized_oxygen_reactant_coeff = get_oxygen_coefficient(normalized_reactants)
    normalized_NiO_reactant_coeff = get_NiO_coefficient(normalized_reactants)

    # Get the normalized coefficients for the products
    normalized_product_coeffs = [int(coeff)/normalizer_coeff for coeff, _ in (item.split() for item in products)]
    
    # Get the first normalized product coeff
    first_normalized_product_coeff = normalized_product_coeffs[0]
    
    normalized_equation = " + ".join(normalized_reactants) + " -> " + " + ".join(normalized_products)
    '''
    print("This is the atom count for the first element in the ractants ",atom_count_first_reactant_first_element)
    print(all_compounds)
    print("-----------------------")
    print("this is the normalized oxygen reactant coeff", normalized_oxygen_reactant_coeff)
    '''
    return normalized_equation, normalized_oxygen_reactant_coeff, normalized_NiO_reactant_coeff, first_normalized_product_coeff


def chemical_equation(reactants, products):
    equation = (reactants + " -> " + products)
    return equation






