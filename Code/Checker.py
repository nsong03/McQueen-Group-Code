# -*- coding: utf-8 -*-
"""
Created on Mon Jul  3 15:55:12 2023

@author: jayso
"""

import Combind_Datapt2

    
def check(T,P,filename, oxide):
    data_class = Combind_Datapt2.class_input(filename, oxide)
    for chemical in data_class:
        y_int = chemical.y_int(oxide)
        del_G = chemical.del_G(y_int,T,P)
        print(del_G)
        
    
filepath = r"C:\Users\jayso\OneDrive - Howard University\Howard\Summer 2023\PARADIM\McQueen Group\Code\Data\\"
file = 'LaNiO'
fileend = r"_T.csv"
oxide = "La2O3" 

check(1000, 150, filepath + file + fileend, oxide)

# Id say next steps are to make a new file with only the things we care about. Read from that.


