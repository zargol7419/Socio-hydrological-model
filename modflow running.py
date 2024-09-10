# -*- coding: utf-8 -*-
"""
Created on Fri Mar 10 13:03:07 2023

@author: Zahra Soleimanzade
"""
#Firstly Copying text file into .wel file
# import module
import shutil

# use copyfile()
shutil.copyfile("E:\\zargolooo\\Thesis-04-19\\python-Thesis\\4202-Transient-calib8_MODFLOW\\Out_Mf2k\\Qmodflow.txt","E:\\zargolooo\\Thesis\\python-Thesis\\4202-Transient-calib8_MODFLOW\\Out_Mf2k\\4202-Transient-calib8.wel")
#running modflow
import flopy
import os
import sys
Modmodel = flopy.modflow.Modflow.load("E:\\zargolooo\\Thesis-04-19\\python-Thesis\\4202-Transient-calib8_MODFLOW\Out_Mf2k\\4202-Transient-calib8.mfn", version='mf2k',exe_name="E:\\zargolooo\\Thesis\\python-Thesis\\mf2k.exe", verbose =True , model_ws = "E:\\zargolooo\\Thesis\\python-Thesis\\4202-Transient-calib8_MODFLOW\\Out_Mf2k\\4202-Transient-calib8._ws" , load_only=None , forgive=False , check =False )
import flopy
# running modflow model
flopy.run_model(exe_name="E:\\zargolooo\\Thesis-04-19\\python-Thesis\\4202-Transient-calib8_MODFLOW\\Out_Mf2k\\mf2k.exe", namefile="E:\\zargolooo\\Thesis\\python-Thesis\\4202-Transient-calib8_MODFLOW\Out_Mf2k\\4202-Transient-calib8.mfn")
