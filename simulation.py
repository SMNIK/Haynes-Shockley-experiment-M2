# -*- coding: utf-8 -*-
"""
Created on Sun Nov 15 08:02:55 2020

@author: masou
"""

import pandas as pd
import matplotlib.pyplot as plt

# first = pd.read_excel(<address and name of your file>,<name of the sheet>)
first = pd.read_excel(r'/Book1.xlsx', 'sheet1')
first = first.iloc[500:4000]
plt.plot(first['x'],first['y'])

plt.xlabel('Time (\u03BC s) \n Set of pulses collected at constant d=0.35cm, by varying the sweeping voltage $V_{s}$')
plt.ylabel('Voltage (v)')
plt.title('non-fit')
plt.legend(["14.4v","20.9v","28.1v","36.4v","44.7v"], fontsize=10, loc='upper right')
