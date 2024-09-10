# -*- coding: utf-8 -*-
"""
Created on Fri May 12 17:16:28 2023

@author: Zahra Soleimanzade
"""
import shutil

    # use copyfile()
shutil.copyfile("E:\\zargolooo\\Thesis-04-19\\python-Thesis\\4202-Transient-calib8_MODFLOW\\Out_Mf2k\\Q-2.txt","E:\\zargolooo\\Thesis-04-19\\python-Thesis\\4202-Transient-calib8_MODFLOW\\Out_Mf2k\\4202-Transient-calib8.wel")

import flopy
first = flopy.modflow.Modflow.load("E:\\zargolooo\\Thesis-04-19\\python-Thesis\\4202-Transient-calib8_MODFLOW\\Out_Mf2k\\4202-Transient-calib8.mfn", version='mf2k',exe_name="E:\\zargolooo\\Thesis-04-19\\python-Thesis\\4202-Transient-calib8_MODFLOW\\Out_Mf2k\\mf2k.exe", verbose =True , load_only=None , forgive=False , check =False )
flopy.run_model(exe_name="E:\\zargolooo\\Thesis-04-19\\python-Thesis\\4202-Transient-calib8_MODFLOW\\Out_Mf2k\\mf2k.exe", namefile="E:\\zargolooo\\Thesis-04-19\\python-Thesis\\4202-Transient-calib8_MODFLOW\\Out_Mf2k\\4202-Transient-calib8.mfn")
#getting heads from output files
hdobj = flopy.utils.HeadFile("E:\\zargolooo\\Thesis-04-19\\python-Thesis\\4202-Transient-calib8_MODFLOW\\Out_Mf2k\\4202-Transient-calib8.hed")
Heads = hdobj.get_data(kstpkper=None, mflay=0 , totim=2555)
print(Heads)
time=hdobj.get_times()
print(time)
#import numpy
#a = numpy.asarray(Heads)
#numpy.savetxt("E:\\zargolooo\\Thesis\\python-Thesis\\Head-1.csv", a, delimiter=",")


with open("E:\\zargolooo\\Thesis-04-19\\test code python\\KIJ.txt") as f:
    lines = f.readlines()
    first = list(list(map(int, line.split())) for line in lines)
    for i in first:
        i[0] = i[0] - 1
        i[1] = i[1] - 1
        i[2] = i[2] - 1
print(first)
idx = []
for x in first:
    idx.append(tuple(x))   
print(idx)    
###############
#using extracted IJK in idx as variable
finalHead=[]
for j in idx:
    hdobj = flopy.utils.HeadFile("E:\\zargolooo\\Thesis-04-19\\python-Thesis\\4202-Transient-calib8_MODFLOW\\Out_Mf2k\\4202-Transient-calib8.hed")
    Heads= hdobj.get_ts(idx = j)
    finalHead.append(Heads[84][1])
print(finalHead)
import numpy
a = numpy.asarray(finalHead)
numpy.savetxt("E:\\zargolooo\\Thesis-04-19\\python-Thesis\\Head-2.csv", a, delimiter=",")