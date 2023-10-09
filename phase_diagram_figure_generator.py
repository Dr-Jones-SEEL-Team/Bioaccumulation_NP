# -*- coding: utf-8 -*-
"""
Created on Fri May 12 10:28:27 2023

@author: joshu
"""

import pandas as pd
import glob
import os
import numpy as np
import matplotlib.pyplot as plt
import time
from matplotlib.colors import LinearSegmentedColormap
from tqdm import tqdm

# %% Start Timer
t_start=time.time()

#Grab data to process for phase-diagram
directory = r'C:\Users\joshu\Box\Quantum Biofilms\Processed Data\Modeling Paper Figures\Phase diagram Figure'
# directory = r'C:\Users\joshu\Box\Quantum Biofilms\Processed Data\Paper #1 Figures\Figure 2\PS-figure'
for root,dirs,files in os.walk(directory):
    data=[[]]*int((len(files)-1)/2)
    k=0 #start counter
    for file in tqdm(files,desc="processing",ncols=100):
        if 'param' in file and file.endswith(".csv"):
            param_temp=pd.read_csv(file, index_col=None, header=0)
            params_pass=param_temp.to_numpy()
            data_name=file[6:]
            data_intro='totaldata'
            data_temp=f'{data_intro}{data_name}'
            data_pd=pd.read_csv(data_temp, index_col=None, header=0)
            data_pass=data_pd.to_numpy()
            data[k]=[params_pass,data_pass]
            k=k+1
            
#Calculate concentration difference and PS-number
num_data=len(data)
c95=np.zeros(num_data)
PS=np.zeros((num_data,5))
for i in tqdm(np.arange(0,num_data),desc="processing",ncols=100):
    data_calc=data[i][1]
    c_avg=np.average(data_calc[:,1])
    index5=np.where(data_calc[:,0]==0.05)
    index5_int=int(index5[0])
    index95=np.where(data_calc[:,0]==0.95)
    index95_int=int(index95[0])
    subtratum5=np.average(data_calc[:index5_int,1])
    subtratum95=np.average(data_calc[index95_int:,1])
    c95[i]=(subtratum95-subtratum5)/c_avg
    PS[i,4]=c95[i]
    params=data[i][0]
    xi=params[7,1]
    PS[i,0]=xi
    beta=params[8,1]
    PS[i,1]=beta
    a=params[11,1]
    PS[i,2]=a
    b=params[12,1]
    PS[i,3]=b
    # PS[i,4]=-xi*a**(1/2)*beta*b**(1/2)

    
# Sort PS-number data by xi and beta values in ascending/descending order
sorted_indices = np.lexsort((PS[:, 1], PS[:, 0]))
PS = PS[sorted_indices]

x_values = np.unique(PS[:,0]) #Grab xi values for x-axis
y_values = np.unique(PS[:,1]*(np.exp(b)-1))   #Grab phi_max-phi_main values
phase_diag_data=np.zeros((len(y_values),len(x_values))) #initialize plotted data matrix
for xi_i in np.arange(0,len(x_values)):
    for beta_i in np.arange(0,len(y_values)):
        phase_diag_data[beta_i,xi_i]=PS[beta_i+xi_i*len(y_values),4]


# Define the colors for the colormap
colors = ['blue', 'white', 'red']

# Define the corresponding color positions (0 for blue, 0.5 for white, 1 for red)
color_positions = [-1, 0, 1]

# Adjust color positions to start with x=0 and end with x=1
color_positions = [(c - color_positions[0]) / (color_positions[-1] - color_positions[0]) for c in color_positions]

# Create the colormap
cmap_custom = LinearSegmentedColormap.from_list('custom_cmap', list(zip(color_positions, colors)))

plt.figure(figsize=(8,6))
# Plot the heatmap using plt.contourf()
heatmap = plt.contourf(x_values, y_values, phase_diag_data, levels=100, cmap=cmap_custom)
plt.colorbar(pad=0.1)

# Overlay contour lines using plt.contour()
contour = plt.contour(x_values, y_values, phase_diag_data, levels=5, colors='k')
plt.clabel(contour, inline=True, fontsize=8)
plt.xlabel(r'Attachment Site Heterogeneity Constant, $\xi$  ')  # X-axis label
plt.ylabel(r'Adjusted Porosity Heterogeneity Constant, $\beta$*')  # Y-axis label

plt.text(12.5,-0.5,'Interior')
plt.text(11.5,-0.53,'Sequestration')
plt.text(12,0.5,'Periphery')
plt.text(11.5,0.47,'Sequestration')

#Add homogenous biofilm datapoint
plt.scatter(0,0,color='k')
plt.annotate('Homogeneous Biofilm',(0,0),xytext=(10, 10), textcoords='offset points', ha='right', va='bottom')

plt.savefig('Figure_1.tif', format='tif', dpi=300)  # You can specify the dpi (dots per inch) if needed
plt.savefig('Figure_1.eps', format='eps', dpi=300)  # You can specify the dpi (dots per inch) if needed

plt.show()

t_end=time.time()
total_time=t_end-t_start
print('Total time is {} sec'.format(total_time))

