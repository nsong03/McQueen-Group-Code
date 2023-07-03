# -*- coding: utf-8 -*-
"""
Created on Wed Jun 21 22:40:20 2023

@author: jayson johnson
"""

import csv
import matplotlib.pyplot as plt
import numpy as np
import chemparse as cp

'''
import sys
sys.path.append('/path/to/other/folder')

import module_name  # Import the file from the other folder

'''

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
    
    def __init__(self, name, mpid, eV):
        self.name = name
        self.mpid = mpid
        self.total_num_atoms = get_total_atoms(self.name)
        self.num_atoms_second_element = get_atoms_in_second_element(self.name)
        self.eV = eV
        self.O2 = -(self.num_atoms_second_element)/2
        self.del_H = self.total_num_atoms*self.eV*self.cf*(1/self.O2)
        self.del_S = -self.SSO2
        self.R = 8.314/1000
        
        

    def __str__(self):
        return f"Name: {self.name}, MPID: {self.mpid}, Energy: {self.eV} eV, num_atoms: {self.total_num_atoms}"
    
    def slope(self,x,P):
        return -x*((self.del_S) - -1*self.R*np.log(P))
    
    # n = -1 since only one mole is getting turned to a solid

#you broke it trying to make it a function so it it all easier. This is understandable. Now you need to think it though.

# Read data from the CSV file and create instances of ChemicalData



def plot_seperate(filename, maximum_temp,P, seperate: bool):
    
    chemicals = []
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            name = row[0]
            mpid = row[1]
            eV = float(row[2])
            chemical = ChemicalData(name, mpid, eV)
            chemicals.append(chemical)
    
    # Coordinates (X, Y) 
    x = np.linspace(0,maximum_temp)
    y = x
    
    #Graph Domain and Range
    plt.xlim(0, maximum_temp)
    plt.ylim(-1500, 1000)
    
    #Add X and Y Lable
    plt.xlabel("Temperature K")
    plt.ylabel('del G')

    if seperate:
        for chemical in chemicals:
            #Add a title
            plt.title(chemical.name + " P = " + str(P) + " Bar")
            #Plot
            plt.plot(y,chemical.slope(x,P) + chemical.del_H)
        
            #Show Grid
            plt.grid()
            plt.show()
    else:
        for chemical in chemicals:
            plt.title("oxides " + " P = " + str(P) + " Bar")
            #Plot
            plt.plot(y,chemical.slope(x,P) + chemical.del_H, label= chemical.name)
        
            #Show Grid
            #plt.legend(loc = 'lower right')
            
            
        plt.grid()
        plt.show()
        
        
plot_seperate('oxides_T.csv', 3000,1, False)




