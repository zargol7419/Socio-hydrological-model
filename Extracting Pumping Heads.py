# -*- coding: utf-8 -*-
"""
Created on Thu Apr  6 23:14:49 2023

@author: Zahra Soleimanzade
"""
# Extracting Heads from computed matrix for pumping wells
import flopy
#first of all we should extract rows columns from well file
fin= open("E:\\zargolooo\\Thesis\\test code python\\4202-Transient-calib8.wel","r")
fout = open("E:\\zargolooo\\Thesis\\test code python\\KIJ.txt", "w")
for i in range(3041):
    l=fin.readline()
for j in range(3037):
    line=fin.readline()
    low=line.split()
    k=low[0]
    row=low[1]
    col=low[2]
    fout.write(k+" "+row+" "+col+" "+"\n")
with open("E:\\zargolooo\\Thesis\\test code python\\KIJ.txt") as f:
    lines = f.readlines()
    first = list(list(map(int, line.split())) for line in lines)
    for i in first:
        i[0] = i[0] - 1
        i[1] = i[1] - 1
        i[2] = i[2] - 1
idx = []
for x in first:
    idx.append(tuple(x))   
print(idx)
#using extracted IJK in idx as variable
finalHead=[]
for j in idx:
    hdobj = flopy.utils.HeadFile("E:\\zargolooo\\Thesis\\python-Thesis\\4202-Transient-calib8_MODFLOW\\Out_Mf2k\\4202-Transient-calib8.hed")
    Heads= hdobj.get_ts(idx = j)
    finalHead.append(Heads[60][1])
print(finalHead)
import numpy
a = numpy.asarray(finalHead)
numpy.savetxt("E:\\zargolooo\\Thesis\\python-Thesis\\PumpingHeads-Historical.csv", a, delimiter=",")