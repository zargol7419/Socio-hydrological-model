# -*- coding: utf-8 -*-
"""
Created on Fri May 12 17:17:01 2023

@author: Zahra Soleimanzade
"""
# please run this one Twice if you want it works well!!
import pandas as pd
Q3 = pd.read_csv("E:\\zargolooo\\Thesis-04-19\\python-Thesis\\Q-3.csv", header=None).values
# printing the array
fwel3= open("E:\\zargolooo\\Thesis-04-19\\python-Thesis\\4202-Transient-calib8_MODFLOW\\Out_Mf2k\\4202-Transient-calib8.wel","r")
ftxt3 = open("E:\\zargolooo\\Thesis-04-19\\python-Thesis\\4202-Transient-calib8_MODFLOW\\Out_Mf2k\\Q-3.txt", "w")
for i in range(194518):
    l=fwel3.readline()
    ftxt3.write(l)
        #save in other file
    i_p=-1
for i in range(9):
    i_p+=1 
    line=fwel3.readline()
    words=line.split()
    ftxt3.write(line)
    if words[0]=="-1":
        i_p+=1
        line=fwel3.readline()
        ftxt3.write(line)
    for j in range(3038):
        if j==3037:
            line=fwel3.readline()
            ftxt3.write(line)
            break
        line=fwel3.readline()
        low=line.split()
        low[3]=str(Q3[j,i_p%12])
        new=' '.join(low)
        ftxt3.write(new+"\n")
while True:
    line=fwel3.readline()
    if not line:
        break
    ftxt3.write(line)