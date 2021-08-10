#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  1 09:54:13 2021

@author: joshuaprince
"""


import numpy as np
from scipy.integrate import odeint, solve_ivp
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import subprocess as sp
tmp = sp.call('cls',shell=True) 

def diffeqs1(t, y, kf, kr, Ct):
    [Cn, Cnb] = y
    
    dCn = -kf*Cn*(Ct-Cnb)+kr*Cnb
    dCnb = kf*Cn*(Ct-Cnb)-kr*Cnb
       
    return [dCn, dCnb]

def diffeqs2(t, y, kf, kr, Ct, n):
    [Cn, Cnb] = y
    
    dCn = -kf*Cn**n*(Ct-Cnb/n)+kr*Cnb
    dCnb = kf*Cn**n*(Ct-Cnb/n)-kr*Cnb
       
    return [dCn, dCnb]
 
#Define Ecotoxciological Parameters   
kf= 1 #Forward rate constant of binding 
kr= 0.1 #Reverse rate constant of binding 
n= [0.01,0.02,0.05,0.1,0.2,0.5] #Hill binding constant 
Ct= 200 #Conentration of binding sites

#Define Inital Conditions
Cn0=100 #Initial Concentration of unbound
Cnb0=0 #Initial Concentration of bound

y0 = [Cn0, Cnb0]  # Initial state of the system
 
#Define time-domain to investigate
t_span = (0.0, 50)
t = np.arange(0.0, 1, 0.0001)
    
results=np.zeros((len(t),5,len(n)))

count=0
for ni in n:
    p1 = (kf, kr, Ct)  # Parameters of the system for set 1
    p2 = (kf, kr, Ct, ni)  # Parameters of the system for set 2
    

    result1_solve_ivp = solve_ivp(diffeqs1, t_span, y0, args=p1, method='RK45', t_eval=t)
    result2_solve_ivp = solve_ivp(diffeqs2, t_span, y0, args=p2, method='RK45', t_eval=t)
    
    results[:,0,count]=result1_solve_ivp.t
    results[:,1,count]=result1_solve_ivp.y[0,:]
    results[:,2,count]=result2_solve_ivp.y[0,:]
    results[:,3,count]=result1_solve_ivp.y[1,:]
    results[:,4,count]=result2_solve_ivp.y[1,:]
    
    count=count+1
    
plt.figure(0)
count=0
for ni in n:
    plt.plot(results[:,0,0],results[:,2,count],label=f'n={ni}')
    count=count+1
plt.plot(results[:,0,0],results[:,1,0],label='n=1')
plt.legend()


plt.figure(1)
count=0
for ni in n:
    plt.plot(results[:,0,0],results[:,4,count],label=f'n={ni}')
    count=count+1
plt.plot(results[:,0,0],results[:,3,0],label='n=1')
plt.legend()


