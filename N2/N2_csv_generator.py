#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 20:02:34 2020

@author: joshuaprince
"""
import numpy as np
import pandas as pd
import os

def csv_generator(c_set,parameter_combos_count,parameter_matrix,direct_export_path):
    for pc_i in np.arange(0,parameter_combos_count,1): #Begin for loop to plot the different model paramters using MOL 
        cb=c_set[pc_i][0] #Grab current bound concentration data to plot
        cu=c_set[pc_i][1] #Grab current unbound concentration data to plot
        t=c_set[pc_i][6] #Grab time-vector for this parameter set for plotting
        t_oof=np.floor(np.log10(np.abs(t[1]))).astype(int) #order of magninutde of time-step
        t=np.around(t,-t_oof) #Remove some rounding errors from time data-set
        x=c_set[pc_i][8] #Grab the position-vector for this parameter set for plotting
        x=np.around(x,3) #Remove some rounding errors from position data-set
        cb_data=pd.DataFrame(data=cb, index=x, columns=t) #Create pandas dataframe for bound concentration
        cu_data=pd.DataFrame(data=cu, index=x, columns=t) #Create pandas dataframe for unbound concentration
        cb_data_filename_partial=f'bounddata{pc_i}.csv'
        cb_data_filename_full=os.path.join(direct_export_path,cb_data_filename_partial)
        cu_data_filename_partial=f'unbounddata{pc_i}.csv'
        cu_data_filename_full=os.path.join(direct_export_path,cu_data_filename_partial)
        cb_data.to_csv(cb_data_filename_full) #Export bound dataframe as csv
        cu_data.to_csv(cu_data_filename_full) #Export bound dataframe as csv
    return 0