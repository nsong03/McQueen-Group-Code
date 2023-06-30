# -*- coding: utf-8 -*-
"""
Created on Wed Jun 28 22:04:21 2023

@author: jayso
"""

import csv
    
def use_csv(filename):
    names = []
    mpids = []
    eVs = []
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            name = row[0]
            mpid = row[1]
            eV = float(row[2])
            names.append(name)
            mpids.append(mpid)
            eVs.append(eV)
        
        return names, mpids, eVs