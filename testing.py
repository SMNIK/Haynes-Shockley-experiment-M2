# -*- coding: utf-8 -*-
"""
Created on Sun Nov 15 17:30:02 2020

@author: masou
"""

import pandas as pd
from fitPlot1 import myList1
from fitPlot2 import myList2
from fitPlot3 import myList3
from fitPlot4 import myList4
from fitPlot5 import myList5
from fitPlot6 import myList6
import xlsxwriter
import matplotlib.pyplot as plt
from scipy import polyfit , polyval
import xlrd
import re

def getExcel():
    global SMN
    xls = xlrd.open_workbook(r'Book1.xlsx', on_demand=True)
    sheetNames = xls.sheet_names()
    for i in sheetNames:
        SMN = pd.read_excel(r'Book1.xlsx', i)
        I = [float(smn) for smn in re.findall(r'-?\d+\.?\d*', i)]
        if I[SMN]==14.4:
            workbook = xlsxwriter.Workbook('D:/analyses.xlsx') #you can choose any name 
            worksheet_analyses=workbook.add_worksheet('analyses') #you can choose any name
            for j in range(8):
                worksheet_analyses.write(1,j,myList1[j])
        elif I[SMN]==20.9:
            for j in range(8):
                worksheet_analyses.write(2,j,myList2[j])
        elif I[SMN]==28.1:
            for j in range(8):
                worksheet_analyses.write(3,j,myList3[j])
        elif I[SMN]==36.4:
            for j in range(8):
                worksheet_analyses.write(4,j,myList4[j])
        elif I[SMN]==44.7:
            for j in range(8):
                worksheet_analyses.write(5,j,myList5[j])
        elif I[SMN]==50:
            for j in range(8):
                worksheet_analyses.write(6,j,myList6[j])
        else:
            pass
        print(I[SMN])
        worksheet_analyses.write('A1','V(v)')
        worksheet_analyses.write('B1','t (\u03BC s)')
        worksheet_analyses.write('C1','delta_t(\u03BC s)')
        worksheet_analyses.write('D1','A(v \u03BC s)')
        worksheet_analyses.write('E1','E_s(v/cm)')
        worksheet_analyses.write('F1','V_d(cm/s)')
        worksheet_analyses.write('G1','mu(cm^2/vs)')
        worksheet_analyses.write('H1','lnA')
        workbook.close()

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