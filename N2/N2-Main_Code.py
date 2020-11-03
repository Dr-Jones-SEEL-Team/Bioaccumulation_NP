#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 16:13:07 2020

@author: joshuaprince
"""


#Inputs Code Block
"""
This cell take in the inputs to this code. This does so by:
1a) takes in the user-specified dimensional values for the code, or 
1b) takes in user-specified dimensionless numbers then
2) defines the relevant inputs and outputs which go to the heart of the code 

This is the primary code one should be modifying when testing different physical systems for the model
"""

from IPython import get_ipython
get_ipython().magic('reset -sf')

# %% Imports
import time
import os
import numpy as np
from N2_RJ import *
from N2_method_of_lines import *
from N2_parameter_tester import *
from N2_parameter_matrix import *
from N2_report_generator import *

# %% Start Timer
t_start=time.time()

# %%Inputs Code Block
h=np.array([0.00001]) #Define timesteps to test
tol=np.array([10**(-8)])  #Define the tolerance the code will run with when running Newton-Rhapson
t1=np.array([0]) #Define initialtime vector of values to test
t2=np.array([2]) #Final Time
nx=np.array([100]) #Mesh size
gam=np.array([0.1]) #Define dimenionless ratio of diffusivities to test
beta=np.array([0]) #Define the dimensionless ratio of potentials to test
F=np.array([100]) #Define the dimensionless forward reaction rate constant to test
Re=np.array([0]) #Define the dimensionless reverse reaction rate constant to test
n=np.array([0.8]) #Define the hill coeffecient to test
ci=10**(-8) #Define the inital concentration in the biofilm (Can't be zero, if one wants to be zero, set it to a very small number instead)


# %% Generate Parameter Matrix for Testing
[parameter_matrix,parameter_combos_count]=parameter_matrix_generator(h,tol,t1,t2,nx,gam,beta,F,Re,n)
                    
# %% Run parameters through numerical model (Heart of the Code)               
c_set = parameter_checker(parameter_matrix,ci) #output the set of concentration over time and space results for each set of parameters tested

# %% Report Generator: Exports Plots as Word Document to Seperate Directory (see file N2_report_generator.py)
direct_export_path='/Users/joshuaprince/Northeastern University/Jones SEEL Team - Bioremediation of Nanoparticles/Modelling Work/Model Results/N2/Direct Exports' #Direct Export path for Files, used for actual script outputs
report=plot_generator(c_set,parameter_combos_count,parameter_matrix,direct_export_path)

# %% Stop Timer
#End timer
t_end=time.time()
total_time=t_end-t_start
print('Total time is {} sec'.format(total_time))

#%% To export report, turn on this code block
#Finish Report
para5=report.add_paragraph(f'Time to Run (sec): {total_time}     ')
report_filename_partial=f'N2_report.docx'
report_filename_full=os.path.join(direct_export_path,report_filename_partial)
report.save(report_filename_full)



