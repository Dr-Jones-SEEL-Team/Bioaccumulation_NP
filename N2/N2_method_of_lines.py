#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 31 17:25:29 2020

@author: joshuaprince
"""

import numpy as np
import scipy as sp
from scipy import sparse
from scipy.sparse import linalg

from N2_RJ import *

def method_of_lines(t,x,y,h,p,tol):
    yw=y[:,0] #Initalize the working concentration vector
    index=np.arange(0,len(t)) #Creater index vector
    whoops=0 #initialize error function
    for i in index: #Begin for loop which iterates over all the entries in the time vector, assigning them the value td
        if i==0: continue
        else:
            yold=yw #update the old y-value
            yw[0]=1 #hardcode in boundary condition
            out=RJ(x,yw,p); #Calculate Residual and Jacobian from new y value
            R=out[0] #Grab the Residual
            J=out[1] #Grab the Jacobian
            #print('This is the residual')
            #print(R)
            R=yw-yold-h*R
            k=0
            while np.linalg.norm(R)>tol :
                k=k+1
                J=np.eye(len(yw))-h*J; #Calculate new Jacobian from new y
                #print('This is the Jacobian and the determinant')
                #print(J)
                #print(np.linalg.det(J))
                J=sp.sparse.csc_matrix(J)
                dif=-sp.sparse.linalg.spsolve(J,R) #Apply built in sparse Linear solver to find delta from J and R
                #dif=-np.linalg.solve(J,R)  #Regular Solver. Just keeping it in there in case the sparse solver isn't working for some reason
                #print('This is delta')
                #print(dif)
                #This section is to determine if the differecne will make the working y outside the domain, and apply a different change
                #ywc=yw+dif
                
                #This is the working area
                yw=yw+dif ; #Update y
                #print('This is the new y')
                #print(yw)
                out=RJ(x,yw,p); #Calculate Residual and Jacobian from new y value
                R=out[0] #Grab the Residual
                #print('This is the residual')
                #print(R)
                J=out[1] #Grab the Jacobian
                R=yw-yold-h*R ; #Update Residual
                if k>100:
                    print('Whoops')
                    whoops=whoops+1
                    break
            y[:,i]=yw
    return (y,whoops)