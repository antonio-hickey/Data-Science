#---------------------------------------------------------------
# Import Modules
import pandas as pd
import numpy as np
import pathlib
#---------------------------------------------------------------
# Importing Datasets
PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("Data").resolve()
df = pd.read_csv(DATA_PATH.joinpath('next_fight.csv'))
#---------------------------------------------------------------
# Model
def model(xp1,height1,weight1,reach1,stance1,sig_str_lpm1,sig_str_acc1,
          xp2,height2,weight2,reach2,stance2,sig_str_lpm2,sig_str_acc2):
            # Null lists for point system
            points1=[]
            points2=[]

            # Exprience Scaling (record)
            def exp(record1,record2):
                # Dynamically Defining Record
                n_wins1 = record1.find('-')
                if n_wins1 == 1: # if number of wins == 1 then (x-)
                    wins1 = record1[:1]
                    n_loses1 = record1[3:].find('-')
                    if n_loses1 == 0: # if number of loses == 0 then (x-y)
                        loses1 = (record1[2:3])
                        n_draws1 = record1[4:].find('-')
                        if n_draws1 == -1: # if number of draws == -1 then (x-y-z)
                            draws1 = record1[-1:]
                        elif n_draws1 == -2: # if number of draws == -2 then (x-y-zz)
                            draws1 = record1[-2:]
                    elif n_loses1 == 1: # if number of loses == 1 then (x-yy)
                        loses1 = (record1[3:4])
                        if n_draws1 == -1: # if number of draws == -1 then (x-yy-z)
                            draws1 = record1[-1:]
                        elif n_draws1 == -2: # if number of draws == -2 then (x-yy-zz)
                            draws1 = record1[-2:]
                elif n_wins1 == 2:  # if number of wins == 2 then (xx-)
                    wins1 = record1[:2] 
                    n_loses1 = record1[3:].find('-')
                    if n_loses1 == 0: # if number of loses == 0 then (xx-y)
                        loses1 = (record1[2:3])
                        n_draws1 = record1[4:].find('-')
                        if n_draws1 == -1: # if number of draws == -1 then (xx-y-z)
                            draws1 = record1[-1:]
                        elif n_draws1 == -2: # else if number of draws == -2 (xx-y-zz)
                            draws1 = record1[-2:]
                    elif n_loses1 == 1: # else if number of loses == 0 then (xx-yy)
                        loses1 = (record1[3:4])
                        n_draws1 = record1[4:].find('-')
                        if n_draws1 == -1: # if number of draws == -1 then (xx-yy-z)
                            draws1 = record1[-1:]
                        elif n_draws1 == -2: # else if number of draws == -2 then (xx-yy-zz)
                            draws1 = record1[-2:]
                
                n_wins2 = record2.find('-')
                if n_wins2 == 1: 
                    wins2 = record2[:1]
                    n_loses2 = record2[3:].find('-')
                    if n_loses2 == 0: 
                        loses2 = (record2[2:3])
                        n_draws2 = record2[4:].find('-')
                        if n_draws2 == -1: 
                            draws2 = record2[-1:]
                        elif n_draws2 == -2: 
                            draws2 = record2[-2:]
                    elif n_loses2 == 1: 
                        loses2 = (record2[3:4])
                        if n_draws2 == -1: 
                            draws2 = record2[-1:]
                        elif n_draws2 == -2: 
                            draws2 = record2[-2:]
                elif n_wins2 == 2:  
                    wins2 = record2[:2] 
                    n_loses2 = record2[3:].find('-')
                    if n_loses2 == 0: 
                        loses2 = (record2[2:3])
                        n_draws2 = record2[4:].find('-')
                        if n_draws2 == -1: 
                            draws2 = record2[-1:]
                        elif n_draws2 == -2: 
                            draws2 = record2[-2:]
                    elif n_loses2 == 1: 
                        loses2 = (record2[3:4])
                        n_draws2 = record2[4:].find('-')
                        if n_draws2 == -1: 
                            draws2 = record2[-1:]
                        elif n_draws2 == -2: 
                            draws2 = record2[-2:]
                #---------------------------------------------------------------
                # Point System
                n_fights1 = int(wins1) + int(loses1)  # Num of fights
                n_fights2 = int(wins2) + int(loses2)
                exp_diff = n_fights1 - n_fights2 # Exprience Difference (total fights - total fights)
                if exp_diff > 0:
                    points1.append(1)
                if exp_diff < 0:
                    points2.append(1)
                
                win_rate1 = int(wins1) / n_fights1 * 100 #  Win Rate
                win_rate2 = int(wins2) / n_fights2 * 100
                if win_rate1 > win_rate2:
                    points1.append(1)
                if win_rate1 < win_rate2:
                    points2.append(1)
                
                #---------------------------------------------------------------
                # Printing
                print('fighter 1 has {} wins / {} loses ({}%) | points: {}'.format(wins1,loses1,win_rate1,sum(points1)))
                print('fighter 2 has {} wins / {} loses ({}%)| points: {} \n'.format(wins2,loses2,win_rate2,sum(points2)))
                #---------------------------------------------------------------
            #---------------------------------------------------------------
            exp(record1,record2)
#---------------------------------------------------------------
model(fighter1['Record'],fighter1['Age'],fighter1['Height'],fighter1['Weight'],fighter1['Reach'],
      fighter2['Record'],fighter2['Age'],fighter2['Height'],fighter2['Weight'],fighter2['Reach'])
#---------------------------------------------------------------
