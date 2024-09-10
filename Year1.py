# -*- coding: utf-8 -*-
"""
Created on Wed May 10 18:38:22 2023

@author: Zahra Soleimanzade
"""
# please run this one Twice if you want it works well!!
import pandas as pd
Q1 = pd.read_csv("E:\\zargolooo\\Thesis-04-19\\python-Thesis\\Q-1.csv", header=None).values
# printing the array
fwel= open("E:\\zargolooo\\Thesis-04-19\\python-Thesis\\4202-Transient-calib8_MODFLOW\\Out_Mf2k\\4202-Transient-calib8.wel","r")
ftxt = open("E:\\zargolooo\\Thesis-04-19\\python-Thesis\\4202-Transient-calib8_MODFLOW\\Out_Mf2k\\Q-1.txt", "w")
for i in range(139810):
    l=fwel.readline()
    ftxt.write(l)
        #save in other file
    i_p=-1
for i in range(9):
    i_p+=1 
    line=fwel.readline()
    words=line.split()
    ftxt.write(line)
    if words[0]=="-1":
        i_p+=1
        line=fwel.readline()
        ftxt.write(line)
    for j in range(3038):
        if j==3037:
            line=fwel.readline()
            ftxt.write(line)
            break
        line=fwel.readline()
        low=line.split()
        low[3]=str(Q1[j,i_p%12])
        new=' '.join(low)
        ftxt.write(new+"\n")
while True:
    line=fwel.readline()
    if not line:
        break
    ftxt.write(line)