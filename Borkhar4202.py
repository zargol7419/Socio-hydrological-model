# -*- coding: utf-8 -*-
"""
Created on Sun Mar  5 19:01:52 2023

@author:  Zahra-Soelimanzade / Thesis Project - 4202
"""
# Running Netlogo file / historical memory
## ***Attention*** Run this part using "Run Selection" for each part and then go for the rest ***Attention*** ##
import subprocess
import pyNetLogo
#import numpy as np
#import pandas as pd
netlogo = pyNetLogo.NetLogoLink(gui=True)
netlogo.load_model("E:\\zargolooo\\Thesis-04-19\\python-Thesis\\farmers behavior model3.nlogo")
netlogo.command('go-historical-Memory-1')
##  Go for runnig modflow for historical memory  ##
subprocess.run(["python","transter to modflow.py"])
subprocess.run(["python","transter to modflow.py"])
subprocess.run(["python", "E:\\zargolooo\\Thesis-04-19\\python-Thesis\\4202-Transient-calib8_MODFLOW\\Out_Mf2k\\modflow running.py"])
subprocess.run(["python", "historical heads at pumping cells.py"])
##Part 2 After Runnig Modflow for Historical memory
netlogo.command('go-historical-Memory-2')
netlogo.command('simulate-social-behavior')

## Part3 For running First Year Of decision Making
netlogo.command('Go-decision-making-year1-1')

## At  this step Go for Python file Year1 and Then Modflow-Q1 ##
subprocess.run(["python", "Year1.py"])
subprocess.run(["python", "Year1.py"])
subprocess.run(["python", "E:\\zargolooo\\Thesis-04-19\\python-Thesis\\4202-Transient-calib8_MODFLOW\\Out_Mf2k\\Modflow-Q1.py"])
netlogo.command('Go-decision-making-year1-2')
## if you wnat to count the number of offenders right here Do it##
netlogo.command('simulate-social-behavior')

##Part4 runnig second year of decision making
netlogo.command('Go-decision-making-year2-1')
## At  this step Go for Python file Year2 and Then Modflow-Q2 ##
subprocess.run(["python", "Year2.py"])
subprocess.run(["python", "Year2.py"])
subprocess.run(["python", "E:\\zargolooo\\Thesis-04-19\\python-Thesis\\4202-Transient-calib8_MODFLOW\\Out_Mf2k\\Modflow-Q2.py"])
netlogo.command('Go-decision-making-year2-2')
## if you wnat to count the number of offenders right here Do it##
netlogo.command('simulate-social-behavior')

##Part5 runnig third year of decision making
netlogo.command('Go-decision-making-year3-1')
## At  this step Go for Python file Year3 and Then Modflow-Q3 ##
subprocess.run(["python", "Year3.py"])
subprocess.run(["python", "Year3.py"])
subprocess.run(["python", "E:\\zargolooo\\Thesis-04-19\\python-Thesis\\4202-Transient-calib8_MODFLOW\\Out_Mf2k\\Modflow-Q3.py"])
netlogo.command('Go-decision-making-year3-2')
## if you wnat to count the number of offenders right here Do it##
netlogo.command('simulate-social-behavior')

##Part6 runnig forth year of decision making
netlogo.command('Go-decision-making-year4-1')
## At  this step Go for Python file Year4 and Then Modflow-Q4 ##
subprocess.run(["python", "Year4.py"])
subprocess.run(["python", "Year4.py"])
subprocess.run(["python", "E:\\zargolooo\\Thesis-04-19\\python-Thesis\\4202-Transient-calib8_MODFLOW\\Out_Mf2k\\Modflow-Q4.py"])
netlogo.command('Go-decision-making-year4-2')
## if you wnat to count the number of offenders right here Do it##
netlogo.command('simulate-social-behavior')