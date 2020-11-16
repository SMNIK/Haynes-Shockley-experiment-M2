# -*- coding: utf-8 -*-
"""
Created on Sun Nov 15 15:30:42 2020

@author: masou
"""

import numpy as np
from plotting import x , y , mean , alpha 
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

def gauss(x,a,b,alpha):
    return (a*np.exp(-0.5*((x-b)/alpha)**2))
popt,pcov = curve_fit(gauss,x,y,p0=[0,mean,alpha])
plt.figure(1)
plt.plot(x,y,label='20.9v')
plt.plot(x,gauss(x,*popt),color='black',linewidth=2)
plt.legend()

t = popt[1]
delta_t = np.sqrt(np.log(4))*2*popt[2]
d = 3
Area = popt[0]*2*popt[2]*np.sqrt(np.pi/2)
E_s = 20.9/d
D = 0.35
V_d = D*1e6/t
mu = V_d/E_s
lnA = np.log(Area)
myList = [20.9,t,delta_t,Area,E_s,V_d,mu,lnA]
print(myList)