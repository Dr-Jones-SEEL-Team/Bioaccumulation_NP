#!/usr/bin/env python3
# -*- coding: utf-8 -*-

vn_experimental_data_extractor=1.0

import os
import numpy as np
import matplotlib.pyplot as plt
import docx
from docx.shared import Pt
from datetime import datetime
import matplotlib.animation as anim
from matplotlib.animation import FuncAnimation
import pandas as pd


def exp_data_fitter(c_set,exp_data,parameter_combos_count):
    
    for pc_i in np.arange(0,parameter_combos_count,1): #Begin for loop to plot the different model paramters tested
    
        # %% Grab relevant data from model     
        ct=c_set[pc_i][14] #Grab total dimensionless concentration plot
        x=c_set[pc_i][9] #Grab the position-vector for this parameter set for plotting
        t=c_set[pc_i][7] #Grab time-vector for this parameter set for plotting
        
        #Get model results into array similar to experimental results
        
        
        # %% Remove baseline from experimental AU values
        baseline=8.20 #This is apprently the baseline AU value, when the experimental results should really be zero (eye-balled it)
        exp_data[:,2]=exp_data[:,2]-baseline
        
        # %% Initialize collated results array
        exp_data_shape=np.shape(exp_data) #Shape of experimental data
        collated_results=np.append(exp_data,np.zeros((exp_data_shape[0],1)),axis=1) #Initialize vector which ahs expeirmental and model results. First three columns ar eexperimental data, last column is model fit
        
        # %% Convert dimensionless mdoel results inot dimenional model results
        to= 3 #guess at dimensionless time [min]
        kconv=200 #guess at absorbance units-NP concentration conversion factor
        t_d=t*to #convert dimensionless time into dimensional time [min]
        ct_d=kconv*ct #convert dimensionless total concentration to absorbance units
        
        # %% Calculate model values to put in collated vector

         #Need to interpolate between model values to get the neccesary experimental predictions
        # ti_old=-1
        # for i in np.arange(0,len(collated_results)): #loop over all expeirmental values
        #     ti_new=collated_results[i,0] #grab time-point to use
        #     if ti_old==ti_new:
        #         pass
        #     else: #when we have a new time to extract
        #         ti_old=ti_new
        #         t_subset=collated_results[collated_results[:, 0] == ti_old, :] #grab only experimental values at that time-point
                
                
                
        #     x_i=collated_results[i,2]
        #     for j in np.arange(0,len(x)):
        #         if x>i
        
    return 0

# %%
"""
Created on 11/2/2022

@author: joshuaprince

Purpose; Script to extract data from Tseng fits. Hmm, once I did the edited on excel this is actually a pretty simple code. Oh well. 
Version 1.0

    
"""