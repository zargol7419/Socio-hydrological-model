# -*- coding: utf-8 -*-
"""
Created on Thu Mar  9 19:21:42 2023

@author: Zahra Soleimanzade
"""
# please run this one Twice if you want it works well!!
import pandas as pd
Qmodflow = pd.read_csv("E:\\zargolooo\\Thesis-04-19\\python-Thesis\\Qmodflow.csv", header=None).values
# printing the array
fin= open("E:\\zargolooo\\Thesis-04-19\\python-Thesis\\4202-Transient-calib8_MODFLOW\\Out_Mf2k\\4202-Transient-calib8.wel","r")
fout = open("E:\\zargolooo\\Thesis-04-19\\python-Thesis\\4202-Transient-calib8_MODFLOW\\Out_Mf2k\\Qmodflow.txt", "w")
for i in range(3040):
    l=fin.readline()
    fout.write(l)
        #save in other file
    i_p=-1
for i in range(45):
    i_p+=1 
    line=fin.readline()
    words=line.split()
    fout.write(line)
    if words[0]=="-1":
        i_p+=1
        line=fin.readline()
        fout.write(line)
    for j in range(3038):
        if j==3037:
            line=fin.readline()
            fout.write(line)
            break
        line=fin.readline()
        low=line.split()
        low[3]=str(Qmodflow[j,i_p%12])
        new=' '.join(low)
        fout.write(new+"\n")
while True:
    line=fin.readline()
    if not line:
        break
    fout.write(line)