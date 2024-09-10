# -*- coding: utf-8 -*-
"""
Created on Sun May 21 19:00:06 2023

@author: Amirhosein & Zargol
"""
def fitness_func( ga_instance , solution , solution_idx):
    ## initializing variables 
    import flopy
    import numpy
    import csv
    import pandas as pd
    import math
    import sklearn.metrics
    import subprocess
    with open("E:\\zargolooo\\Thesis-04-19\\python-Thesis\\ABC.csv", 'w') as f:
       write = csv.writer(f)
       write.writerow(solution)
    df = pd.read_excel("E:\\zargolooo\\Thesis-04-19\\python-Thesis\\OBS.xlsx", sheet_name=0)
    OBS = df.to_numpy()
    netlogo.command("start-from-the-scratch")
    netlogo.command('go-historical-Memory-1')
    ##  Go for runnig modflow for historical memory  ##
    subprocess.run(["python", "E:\\zargolooo\\Thesis-04-19\python-Thesis\\transter to modflow.py"])
    subprocess.run(["python", "E:\\zargolooo\\Thesis-04-19\\python-Thesis\\modflow running.py"])
    subprocess.run(["python", "E:\\zargolooo\\Thesis-04-19\\python-Thesis\\historical heads at pumping cells.py"])
       ##Part 2 After Runnig Modflow for Historical memory
    netlogo.command('go-historical-Memory-2')
    netlogo.command('simulate-social-behavior')
    ## Part3 For running First Year Of decision Making
    netlogo.command('Go-decision-making-year1-1')
    subprocess.run(["python", "E:\\zargolooo\\Thesis-04-19\\python-Thesis\\Year1.py"])
    subprocess.run(["python", "Modflow-Q1.py"])
    ## At  this step Go for Python file Year1 and Then Modflow-Q1 ##
    netlogo.command('Go-decision-making-year1-2')
    ## if you wnat to count the number of offenders right here Do it##
    netlogo.command('simulate-social-behavior')
    ##Part4 runnig second year of decision making
    netlogo.command('Go-decision-making-year2-1')
    subprocess.run(["python", "E:\\zargolooo\\Thesis-04-19\\python-Thesis\\Year2.py"])
    subprocess.run(["python", "Modflow-Q2.py"])
    ## At  this step Go for Python file Year2 and Then Modflow-Q2 ##
    netlogo.command('Go-decision-making-year2-2')
    ## if you wnat to count the number of offenders right here Do it##
    netlogo.command('simulate-social-behavior')

    ##Part5 runnig third year of decision making
    netlogo.command('Go-decision-making-year3-1')
    subprocess.run(["python", "E:\\zargolooo\\Thesis-04-19\\python-Thesis\\Year3.py"])
    subprocess.run(["python", "Modflow-Q3.py"])
    ## At  this step Go for Python file Year3 and Then Modflow-Q3 ##
    netlogo.command('Go-decision-making-year3-2')
    ## if you wnat to count the number of offenders right here Do it##
    netlogo.command('simulate-social-behavior')

    ##Part6 runnig forth year of decision making
    netlogo.command('Go-decision-making-year4-1')
    subprocess.run(["python", "E:\\zargolooo\\Thesis-04-19\\python-Thesis\\Year4.py"])
    subprocess.run(["python", "Modflow-Q4.py"])
    ## At  this step Go for Python file Year4 and Then Modflow-Q4 ##
    netlogo.command('Go-decision-making-year4-2')
    ## RMSE calculation
    hdobj = flopy.utils.HeadFile("E:\\zargolooo\\Thesis-04-19\\python-Thesis\\4202-Transient-calib8_MODFLOW\\Out_Mf2k\\4202-Transient-calib8.hed")
    idx = [(0,57,51),(0,79,46), (0,33,51), (0,61,74), (0,53,87), (0,63,113), (0,94,75), (0,82,63), (0,27,93), (0,66,62), (0,40,26), (0,98,88), (0,90,34), (0,61,100),(0,86,92), (0,72,71), (0,55,64), (0,43,69), (0,27,27), (0,63,39), (0,69,53), (0,42,58), (0,33,12),(0,36,19), (0,87,67)]
    calculated_OBS = []
    for j in idx:
        Hed = hdobj.get_ts(idx = j)
        calculated_OBS.append(Hed[:,1])
    calculated_OBS =numpy.asarray(calculated_OBS)
    
    ##RMSE calculation##
    RMSE1 = []
    for i in range(25) :
        mse = sklearn.metrics.mean_squared_error(calculated_OBS[i], OBS[i])
        rmse = math.sqrt(mse)
        RMSE1.append(rmse)
    RMSE = 1 / (sum(RMSE1 ) / len(RMSE1 ) )
    return RMSE
def on_gen(ga_instance):
    print("Generation : ", ga_instance.generations_completed)
    print("Fitness of the best solution :", ga_instance.best_solution()[1])
 # initializing GA parameters
import pyNetLogo
netlogo = pyNetLogo.NetLogoLink(gui=True)
netlogo.load_model("E:\\zargolooo\\Thesis-04-19\\python-Thesis\\farmers behavior model3.nlogo")

num_generations = 10
sol_per_pop = 10
num_genes = 3
gene_type = float
init_range_low = 0
init_range_high = 1
parent_selection_type = "rank"
keep_parents = 4
crossover_type = "single_point"
crossover_probability = 0.7
mutation_type = "adaptive"
mutation_probability = [0.08, 0.01]
num_parents_mating = 2* round(crossover_probability*sol_per_pop/2)
import pygad
ga_instance = pygad.GA(num_generations = num_generations , num_parents_mating = num_parents_mating, fitness_func = fitness_func , sol_per_pop = sol_per_pop , num_genes = num_genes , init_range_low = init_range_low , init_range_high = init_range_high , gene_type = gene_type , parent_selection_type = parent_selection_type , keep_parents= keep_parents , crossover_type = crossover_type , crossover_probability= crossover_probability , mutation_type = mutation_type , mutation_probability=mutation_probability , on_generation = on_gen)
ga_instance.run()
ga_instance.plot_fitness(title = "Generation vs. Fitness" , xlabel = "Generation" , ylabel="Fitness")
best_solution, best_solution_fitness, best_match_idx = ga_instance.best_solution()
print(best_solution)
print(best_solution_fitness)
filename = "Social Coefficient Calibaration"
ga_instance.save(filename = filename)
#solution = [[ 0.7,0.15,0.15],[0.4,0.2,0.4],[0.1,0.3,0.6],[0.3,0.15,0.55]]
#test1=[]
#for k in solution:
#   test = fitness_func(k)
#   test1.append(test)
#print(test1)