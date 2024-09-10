# -*- coding: utf-8 -*-
"""
Created on Fri May 12 17:18:23 2023

@author: Zahra Soleimanzade
"""
# please run this one Twice if you want it works well!!
import pandas as pd
Q4 = pd.read_csv("E:\\zargolooo\\Thesis-04-19\\python-Thesis\\Q-4.csv", header=None).values
# printing the array
fwel4= open("E:\\zargolooo\\Thesis-04-19\\python-Thesis\\4202-Transient-calib8_MODFLOW\\Out_Mf2k\\4202-Transient-calib8.wel","r")
ftxt4 = open("E:\\zargolooo\\Thesis-04-19\\python-Thesis\\4202-Transient-calib8_MODFLOW\\Out_Mf2k\\Q-4.txt", "w")
for i in range(221872):
    l=fwel4.readline()
    ftxt4.write(l)
        #save in other file
    i_p=-1
for i in range(9):
    i_p+=1 
    line=fwel4.readline()
    words=line.split()
    ftxt4.write(line)
    if words[0]=="-1":
        i_p+=1
        line=fwel4.readline()
        ftxt4.write(line)
    for j in range(3038):
        if j==3037:
            line=fwel4.readline()
            ftxt4.write(line)
            break
        line=fwel4.readline()
        low=line.split()
        low[3]=str(Q4[j,i_p%12])
        new=' '.join(low)
        ftxt4.write(new+"\n")
while True:
    line=fwel4.readline()
    if not line:
        break
    ftxt4.write(line)