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


def experimental_data_extractor(experimental_data_file):
    data = pd.read_csv(experimental_data_file, header=None) #Import data into pandas dataframe
    data=data.to_numpy() #Immediately convert to a numpy array
    
    # %%Converting Data into Dimensionless Fomr
    #First, convert distance into dimensionless form
    max_x=np.max(data[:,1]) #Calculate max distance
    data[:,1]=data[:,1]/max_x #Divide each distance by max-distance
    data[:,1]=1-data[:,1]#since in the model the biofilm-water interface is x=1, will need to convert distances to reflect that
     
    #No need to convert absorbance values. that will be handled later. 
    
    #Similar fitting will be done for dimensionless time 
        
    return data

# %%
"""
Created on 11/2/2022

@author: joshuaprince

Purpose; Script to extract data from Tseng fits. Hmm, once I did the edited on excel this is actually a pretty simple code. Oh well. 
Version 1.0

    
"""