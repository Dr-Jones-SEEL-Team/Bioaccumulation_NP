#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""CURRENTLY UNDER CONSTRUCTION TO PRODUCE DIMENSIONALIZED RESULTS"""

# %% Code Version Numbers
vn_N2=1.7 #See meta-data at bottom for details
vn_Main_Code=1.4 #See meta-data fro details

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
from N2_csv_generator import *
from N2_linear_fitting import *
from N2_dim_analysis import *

# %% Start Timer
t_start=time.time()

# %% Determine what run number this is then update run number
author_initials='JP'
counter_file = open("counter_file.txt",'r+')
old_count_number=int(counter_file.readline(1))
new_count_number=str(old_count_number+1)
counter_file = open("counter_file.txt",'w')
counter_file.writelines([new_count_number, author_initials])
counter_file.close()

# %%Inputs Code Block
h=np.array([5e-5]) #Define timesteps to test
tol=np.array([10**(-8)])  #Define the tolerance the code will run with when running Newton-Rhapson
t1=np.array([0]) #Define initialtime vector of values to test
t2=np.array([2]) #Final Time
nx=np.array([100]) #Mesh size
ci=10**(-10) #Define the inital concentration in the biofilm (Can't be zero, if one wants to be zero, set it to a very small number instead)
Do= 10**-10 #Diffisivity of NP in the supernatant [m^2/s]
Dmin=10**-11 #Diffusivity of NP in biofilm [m^2/s]
zeta=-0.025 #Zeta potential [Volts, -25 mV] 
H= 100*10**-6 #Biofilm thickness [m, 100 microns]
kf= 1 #forward rate constant for binding kinetics [(m^3/s)*(m^3/kg)^(n-1)/(sites)]
ct= 1 #total concentration of binding sites [sites/m^3]
Kp= 10 #parition coeffeicent for NP across supernatant-biofilm interface [dimensionless]
co= 0.0001 #Concentration of nanoparticle in the supernatant [kg/m^3, 100 ug/L]
kr= 1 #Reverse bidning rate constant [1/s]
phim= 1 #maximum potential in the biofilm [V]
n= 0.85 #Hill coeffecient [Dimensionless]
dim_param=[Do, Dmin, zeta, h, kf, ct, Kp, co, kr, phim]



# %% Physical constants
eta=0.001  #dyanmic viscosity of water [kg/m/s] (https://www.engineeringtoolbox.com/water-dynamic-kinematic-viscosity-d_596.html)
eps0=8.85*10**-12 #Permeativity of free space [F/m] https://en.wikipedia.org/wiki/Vacuum_permittivity
epsr=78.3 #Relative permittivity of water at 25 C [unitless] https://en.wikipedia.org/wiki/Vacuum_permittivity
phio=(Do-Dmin)*eta/eps0/epsr/zeta #Characteristic potential  for transport [V]


# %% Calculate Dimensionless Parameters
"""gam=np.array([Dmin/(Do-Dmin)]) #Define dimenionless ratio of diffusivities to test""" #hard-coding out proper line for debugging
gam=np.array([1]) #Define dimenionless ratio of diffusivities to test
"""beta=np.array([phim/phio]) #Define the dimensionless ratio of potentials to test""" #hard-coding out proper line for debugging
beta=np.array([1]) #Define the dimensionless ratio of potentials to test
"""F=np.array([kf*ct*(Kp*co)**(n-1)*H**2/(Do-Dmin)]) #Define the dimensionless forward reaction rate constant to test""" #hard-coding out proper line for debugging
F=np.array([1]) #Define the dimensionless forward reaction rate constant to test
"""Re=np.array([kr*ct*H**2/(Do-Dmin)/Kp/co]) #Define the dimensionless reverse reaction rate constant to test""" #hard-coding out proper line for debugging
Re=np.array([1]) #Define the dimensionless reverse reaction rate constant to test
n=np.array([n]) #Define hill coeffecient for binding


# %% Generate Parameter Matrix for Testing
[parameter_matrix,parameter_combos_count,vn_parameter_matrix_generator]=parameter_matrix_generator(h,tol,t1,t2,nx,gam,beta,F,Re,n)
                    
# %% Run parameters through numerical model (Heart of the Code)               
[c_set,vn_parameter_checker,vn_method_of_lines,vn_RJ] = parameter_checker(parameter_matrix,ci) #output the set of concentration over time and space results for each set of parameters tested

# %% Export results to csv files
direct_export_path='/Users/joshuaprince/Northeastern University/Jones SEEL Team - Bioremediation of Nanoparticles/Modelling Work/Model Results/N2/Direct Exports' #Direct Export path for Files, used for actual script outputs
vn_csv_generator = csv_generator(c_set,parameter_combos_count,parameter_matrix,direct_export_path,new_count_number)

# %% Fit model to first order approximation, plot approximation, and determine fit of approximation
[perc_acc_matrix,vn_linear_fitting]=linear_fit(c_set,parameter_combos_count,parameter_matrix)

""" Dimensionless Report Generator commented Out whne running dimensional version"
# %% Report Generator: Exports Plots as Word Document to Seperate Directory (see file N2_report_generator.py)
report=plot_generator(c_set,parameter_combos_count,parameter_matrix,new_count_number,vn_N2,vn_Main_Code,vn_parameter_matrix_generator,vn_parameter_checker,vn_csv_generator,vn_method_of_lines,vn_RJ,perc_acc_matrix,vn_linear_fitting)
"""

# %% Dimensional Report Generator: converts data to dimensional form, generates pltos and generates report
report=dim_analysis(c_set,parameter_combos_count,parameter_matrix,dim_param,new_count_number,vn_N2,vn_Main_Code,vn_parameter_matrix_generator,vn_parameter_checker,vn_csv_generator,vn_method_of_lines,vn_RJ,perc_acc_matrix,vn_linear_fitting)

# %% Stop Timer
#End timer
t_end=time.time()
total_time=t_end-t_start
print('Total time is {} sec'.format(total_time))

#%% To export report, turn on this code block
#Finish Report
para5=report.add_paragraph(f'Time to Run (sec): {total_time}     ')
report_filename_partial=f'N2_report{new_count_number}.docx'
report_filename_full=os.path.join(direct_export_path,report_filename_partial)
report.save(report_filename_full)

"""

Created on Tue Jun 16 16:13:07 2020

@author: joshuaprince

Overall N2.1 Computer Model Meta-data
Version 1.7

Changes from version 1.6 to 1.7 (11/11/2020 9;00 pm):
    Added linear fits functions, along with neccesary report plotting

Changes from version 1.5 to 1.6 (11/3/2020 4:35 pm):
    Added version number tracker for all scripts

Changes from  version 1.4 and 1.5 (11/3/2020 8:15 am):
    In report_generator, added plot close functionalities for all plots (python was complaining about holding so many plots in memory)

Changes from version 1.4 to 1.3: (11/3/2020 8:00 am)
    Main_code and report_generator were changed so that the unbound animation isn't a direct export, but an internal export, since it is now included in the report.
    
Changes from version 1.3 to 1.2: (11/3/2020 7:50 am)
    Main_Code.py and csv_generator were changed so that when csv files with data were exported, they are labelled with run number so data isn't overridden everytime model is run



Main_Code File Meta-data
Version 1.5

Changes from Version 1.4 to 1.5 (11/11/2020 9:00 pm):
    Added linear fit function

Changes from Version 1.3 to 1.4 (11/3/2020 9:00 am):
    Added Version number tracker for all scripts
    Line 5, 6: Added new manual entry variable which tracks version number for overall N2 model and Main_Code
    

Changes from Version 1.2 to Version 1.3 (11/3/2020 8:00 am):
    Changed animated gif from direct exporting to internal exporting
    Line 90: direct_export_path variable removed from function call

Changes from version 1.2 to version 1.1 (11/3/2020 7:45 am):
    Added run number labeling for csv-data exports so data isn't so easily lost
    Line 88: variable "new_count_number" was added to function pass
"""



