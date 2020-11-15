# -*- coding: utf-8 -*-
"""
Created on Sun Nov 15 15:30:42 2020

@author: masou
"""

import numpy as np
from plot import x , y , mean , alpha
from scipy.optimize import curve_fit
import matplotlib.pylab as plt

def gauss(x,a,b,alpha):
    return (a*np.exp(-0.5*((x-b)/alpha)**2))
popt,pcov = curve_fit(gauss,x,y,p0=[0,mean,alpha])
plt.figure(1)
plt.plot(x,y,label='20.9v')
plt.plot(x,gauss(x,*popt),color='black',linewidth=2)
plt.legend()