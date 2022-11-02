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


def experimental_data_extractor():
    data = pd.read_csv('filename.csv')
    data.head() # to display the first 5 lines of loaded data


        
        # %%
    return 

# %%
"""
Created on 11/2/2022

@author: joshuaprince

Purpose; Script to extract data from Tseng fits
Version 1.0

Changes from Version 0.1 to 1.0 (2/20/2022 1:30 am)
    Got initial ocde to run. Had to comment out most functionalities
    
"""