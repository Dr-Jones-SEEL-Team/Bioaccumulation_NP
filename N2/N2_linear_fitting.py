#!/usr/bin/env python3
# -*- coding: utf-8 -*-

vn_linear_fitting=1.1

import numpy as np
import matplotlib.pyplot as plt
import os

def linear_fit(c_set,parameter_combos_count,parameter_matrix):
    
    # %% Calculate linear best fit, slope and intercept for each parameter set
    lin_fit=np.zeros((parameter_combos_count,2))#initialize matrix to store linear best fit parameters
    perc_acc_matrix= [[0 for i in range(1)] for j in range(parameter_combos_count)]
    for pc_i in np.arange(0,parameter_combos_count,1): #Begin for loop over different model paramter sets 
        F= parameter_matrix[pc_i,7] #Grab the Dimensionless forward rate constant for parameter set
        Re= parameter_matrix[pc_i,8] #Grab the Dimensionless reverse rate constant for parameter set
        Eq=F/(F+Re)+1 #Calculate Equilibrium total concentration value (assumes theta equilibrates to one, which it is defined to)
        taverage_conc_overtime=c_set[pc_i][4] #Grab current change in concentration data to plot (total NP)
        norm_tavg_conc=Eq-taverage_conc_overtime #Normalize average concentration by equilibrium concentration
        tchange_in_conc=c_set[pc_i][5] #Grab current change in concentration data to plot (total NP)
        [m,b]=np.polyfit(norm_tavg_conc,tchange_in_conc,1) #Find linear fit for plot
        lin_fit[pc_i,0]=m
        lin_fit[pc_i,1]=b #Store fit into matrix
        
    # %% Use paramteres to generate best-fit data
        t=c_set[pc_i][6] #Grab time-vector for this parameter set
        fit_conc=np.zeros(len(t))#Initialize concentration vector
        count=0 #Begin counter
        for t_i in t:
            fit_conc[count]=Eq-Eq*np.exp(-m*t_i)
            count=count+1
        
    # %% Generate Plot and save    
        plt.figure(100+pc_i)
        plt.plot(t,taverage_conc_overtime,label='Results')
        plt.plot(t,fit_conc,label='Model')
        upper_1 = np.amax(taverage_conc_overtime)*1.1 #Upper Bound on Average total Concentration
        upper_2 = np.amax(fit_conc)*1.1 #Upper bound on fit average total concentration overtime
        if upper_1>upper_2:
            uplimit=upper_1
        else: uplimit=upper_2
        plt.xlim(left=parameter_matrix[pc_i,2],right=parameter_matrix[pc_i,3]) 
        plt.ylim(bottom=0,top=uplimit)
        plt.xlabel('Time',fontsize=14)
        plt.ylabel('Average Dimensionless Concentration',fontsize=14)
        plt.title('Model vs First-order Mass Transfer',fontsize=16)
        plt.xticks(fontsize=12)
        plt.yticks(fontsize=12)
        plt.legend(loc=(0.7,0.05))
        plt.text(0.4,0.5,f'm={m}, b={b}')
        linear_filename_partial=f'Linearplot{pc_i}.png'
        internal_export_path='/Users/joshuaprince/Northeastern University/Jones SEEL Team - Bioremediation of Nanoparticles/Modelling Work/Model Results/N2/Internal Exports' #Indirect Export path for Files, used for outputs which only get using internally
        linear_filename_full=os.path.join(internal_export_path,linear_filename_partial)
        plt.savefig(linear_filename_full)
        
    # %% Determine fit of first-order approximation
        percents=[0.4,0.5,0.7,0.8,0.9,0.95,0.97,0.99] #The percent bioaccumulated that will be checked 
        perc_acc_model=taverage_conc_overtime/Eq #convert concentration vectors to percent accumulated vectors
        perc_acc_approx=fit_conc/Eq 
        perc_acc_table=np.zeros((len(percents),4))
        k=0 #counter for percents for loop
        for p_i in percents:
            j=0 #reset counter for time-search loop
            for t_i in t:
                if perc_acc_model[j]>p_i:
                    mod_time=t_i #Time neccesary for model to reach evaluated percent accumulated
                    break
                j=j+1 #Update counter in time search loop
            j=0 #reset counter for time-search loop
            for t_i in t:
                if perc_acc_approx[j]>p_i:
                    approx_time=t_i #time neccesary for first-order approximation to reach evaluated percent accumulated
                    break
                j=j+1 #Update counter in time search loop
            perc_acc_table[k,0]=p_i
            perc_acc_table[k,1]=mod_time
            perc_acc_table[k,2]=approx_time
            perc_acc_table[k,3]=(mod_time-approx_time)/mod_time
            k=k+1 #Update counter in percent loop  
        perc_acc_matrix[pc_i][0]=perc_acc_table
    return [perc_acc_matrix,vn_linear_fitting]



"""
Purpose: Script to fit concentration data to first-order mass-transfer relation, plot this compared to the model results, and create a percent accumulated table to compare the two

Version 1.1

Created on Wed Nov 11 10:19:35 2020

@author: joshuaprince (prince.j@northeastern.edu)
"""


