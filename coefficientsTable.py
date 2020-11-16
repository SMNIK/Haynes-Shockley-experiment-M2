# -*- coding: utf-8 -*-
"""
Created on Sun Nov 15 16:49:07 2020

@author: masou
"""
import pandas as pd
from fitPlot import myList
import xlsxwriter
import matplotlib.pyplot as plt
from scipy import polyfit , polyval

workbook = xlsxwriter.Workbook('D:/analyses.xlsx') 
worksheet_analyses=workbook.add_worksheet('analyses')
for j in range(8):
    worksheet_analyses.write(1,j,myList[j])
worksheet_analyses.write('A1','V(v)')
worksheet_analyses.write('B1','t (\u03BC s)')
worksheet_analyses.write('C1','delta_t(\u03BC s)')
worksheet_analyses.write('D1','A(v \u03BC s)')
worksheet_analyses.write('E1','E_s(v/cm)')
worksheet_analyses.write('F1','V_d(cm/s)')
worksheet_analyses.write('G1','mu(cm^2/vs)')
worksheet_analyses.write('H1','lnA')
workbook.close()
plt.show()

analyses = pd.read_excel(r'D:/analyses.xlsx','analyses') #you can choose any name
time = analyses['t (\u03BC s)']
lnA = analyses['lnA']
plt.figure(2)
plt.scatter(time,lnA,color='g',marker='*',alpha=0.6,s=100)
plt.xlabel('Time (\u03BC s)')
plt.ylabel('lnA')
plt.grid()
sMn = polyfit(time,lnA,1)
plt.plot(time,polyval(sMn,time))
plt.show()