# -*- coding: utf-8 -*-
"""
Created on Fri May 12 17:15:40 2023

@author: Zahra Soleimanzade
"""
# please run this one Twice if you want it works well!!
import pandas as pd
Q2 = pd.read_csv("E:\\zargolooo\\Thesis-04-19\\python-Thesis\\Q-2.csv", header=None).values
# printing the array
fwel2= open("E:\\zargolooo\\Thesis-04-19\\python-Thesis\\4202-Transient-calib8_MODFLOW\\Out_Mf2k\\4202-Transient-calib8.wel","r")
ftxt2 = open("E:\\zargolooo\\Thesis-04-19\\python-Thesis\\4202-Transient-calib8_MODFLOW\\Out_Mf2k\\Q-2.txt", "w")
for i in range(167164):
    l=fwel2.readline()
    ftxt2.write(l)
        #save in other file
    i_p=-1
for i in range(9):
    i_p+=1 
    line=fwel2.readline()
    words=line.split()
    ftxt2.write(line)
    if words[0]=="-1":
        i_p+=1
        line=fwel2.readline()
        ftxt2.write(line)
    for j in range(3038):
        if j==3037:
            line=fwel2.readline()
            ftxt2.write(line)
            break
        line=fwel2.readline()
        low=line.split()
        low[3]=str(Q2[j,i_p%12])
        new=' '.join(low)
        ftxt2.write(new+"\n")
while True:
    line=fwel2.readline()
    if not line:
        break
    ftxt2.write(line)