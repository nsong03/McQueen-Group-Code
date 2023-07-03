# -*- coding: utf-8 -*-
"""
Created on Thu Jun 29 11:45:13 2023

@author: jayso
"""

# This is the class for the materials I am using. It is currently set to PrNiO

import numpy as np
import chemparse as cp


def get_total_atoms(chemical_name):
    formula = cp.parse_formula(chemical_name)
    total_atoms = sum(formula.values())
    return total_atoms

def get_atoms_in_second_element(chemical_formula):
    formula = cp.parse_formula(chemical_formula)
    if formula:
        second_element = list(formula.keys())[1]
        atom_count = formula[second_element]
        return atom_count
    else:
        return 0


    
class ChemicalData:
    cf = 96.491
    SSO2 = 205/1000 #standard state O2
    Enthalpy_NiO = -1.216*2*cf
    Enthalpy_Pr6O11 = -2.403*17*cf
    Enthalpy_La2O3 = -3.738*5*cf
    Enthalpy_Nd2O3 = -3.670*5*cf
    R = 8.314/1000
    
    def __init__(self, name, mpid, eV, normalized_equation, normalized_oxygen_reactant_coeff, normalized_NiO_reactant_coeff, normalized_product_coeff, first_normalized_reactant_coeff):
        self.name = name
        self.mpid = mpid
        self.eV = eV
        self.total_num_atoms = get_total_atoms(self.name)
        self.balanced_equation = normalized_equation
        # This is really important that you decided to make this negative. Explain why its easier, and why it works
        self.O2 = -normalized_oxygen_reactant_coeff
        self.NiO = normalized_NiO_reactant_coeff
        self.oxide_coeff = first_normalized_reactant_coeff
        self.product_coeff = normalized_product_coeff
        self.del_S = self.SSO2*self.O2
        # self.y_intercept = self.y_int(self.name)
        
    def __str__(self):
        return f"Name: {self.name}, MPID: {self.mpid}, Energy: {self.eV} eV, O2 Coeff: {self.O2}, NiO coeff: {self.NiO},Oxide coeff: {self.oxide_coeff}, del_S: {self.del_S}"
    
    def info(self):
        return f"Name: {self.name}"
    
    def show_list(self):
        print( self.name, self.mpid, self.eV, self.normalized_equation, self.O2, self.NiO)
    
    def slope_T(self,x,P):
        slope = -x*((self.del_S - self.O2*self.R*np.log(P)))
        #print(slope)
        return slope
    
    def slope_P(self,x,T):
        slope = -T*((self.del_S - self.O2*self.R*np.log(x)))
        #print(slope)
        return slope
    
    def del_G(self,del_H, T, P):
        R = 8.413/1000
        del_S = 205/1000
        O2 = self.O2
        del_G = del_H + -T*(del_S*O2 - O2*R*np.log(P))
        return del_G
        
    
    def y_int(self,oxide):
        cf = 96.491
        Enthalpy_Pr6O11 = -2.403*17*cf/6
        Enthalpy_La2O3 = -3.738*5*cf/2
        Enthalpy_Nd2O3 = -3.670*5*cf/2
        
        def get_enthalpy(oxide):
            if oxide == "La2O3":
                
                return Enthalpy_La2O3
            elif oxide == "Pr6O11":
                
                return Enthalpy_Pr6O11
            elif oxide == "Nd2O3":
                
                return Enthalpy_Nd2O3
            else:
                return None  # Return None or handle other cases as needed
            
        def get_enthalpy12345(oxide):
            if oxide == "La2O3":
                name = "LaNiO"
                return Enthalpy_La2O3, name
            elif oxide == "Pr6O11":
                name = 'PrNiO'
                return Enthalpy_Pr6O11, name
            elif oxide == "Nd2O3":
                name = "NdNiO"
                return Enthalpy_Nd2O3, name
            else:
                return None  # Return None or handle other cases as needed
            
        y_intercept = (self.eV*self.product_coeff*self.cf*self.total_num_atoms) - ((self.Enthalpy_NiO*self.NiO) + ((get_enthalpy(oxide))))
        #print(self.eV*self.product_coeff*self.cf*self.total_num_atoms)
        #print((self.Enthalpy_NiO*self.NiO) )
        #print(((get_enthalpy(oxide))))
        #print(self.oxide_coeff)
        #print(y_intercept)
        #print(Enthalpy_La2O3)
        return y_intercept

