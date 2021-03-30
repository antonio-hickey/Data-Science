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
# Define Fighters 1 & 2
for x in range(len(df)):
    f1 = df.loc[x][:15]
    f2 = df.loc[x][15:]
    #---------------------------------------------------------------
    # Model
    def model(xp1,height1,weight1,reach1,stance1,age1,sig_str_lpm1,sig_str_acc1,sig_str_abs1,sig_str_def1,td_avg1,td_acc1,td_def1,sub_avg1,
              xp2,height2,weight2,reach2,stance2,age2,sig_str_lpm2,sig_str_acc2,sig_str_abs2,sig_str_def2,td_avg2,td_acc2,td_def2,sub_avg2):
                # Null lists for point system
                f1_points=[]
                f2_points=[]

                # Exprience Scaling (record)
                def exp(record1,record2):
                    global loses1
                    global loses2
                    global wins1
                    global wins2
                    #---------------------------------------------------------------
                    # Dynamically Defining Record
                    #---------------------------------------------------------------

                    # Fighter 1
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

                    # Fighter 2
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
                    #-----------------------------------------
                    return wins1,wins2,loses1,loses2
                    #---------------------------------------------------------------
                #---------------------------------------------------------------
                # Height
                #---------------------------------------------------------------
                def height(height1,height2):
                    height1 = height1.replace(" ",'')
                    height1 = height1.replace('"','')
                    height1 = height1.replace("'",".")
                    height2 = height2.replace(" ",'')
                    height2 = height2.replace('"','')
                    height2 = height2.replace("'",".")
                    diff = float(height1) - float(height2) 
                    return diff
                #---------------------------------------------------------------
                # Weight
                #---------------------------------------------------------------
                def weight(weight1,weight2):
                    diff = weight1 - weight2
                    return diff
                #---------------------------------------------------------------
                # Reach
                #---------------------------------------------------------------
                def reach(reach1,reach2):
                    diff = reach1 - reach2
                    return diff
                #---------------------------------------------------------------
                # Age
                #---------------------------------------------------------------
                def age(age1,age2):
                    diff = age1 - age2
                    return diff
                #---------------------------------------------------------------
                # significant stikes landed per minute
                #---------------------------------------------------------------
                def sig_str_lpm(s1,s2):
                    diff = s1 - s2
                    return diff
                #---------------------------------------------------------------
                # significant stikes accuracy
                #---------------------------------------------------------------
                def sig_str_acc(s1,s2):
                    s1 = int(s1.replace("%",''))
                    s2 = int(s2.replace("%",''))
                    diff = s1 - s2
                    return diff
                #---------------------------------------------------------------
                # Significant strikes absorbed
                #---------------------------------------------------------------
                def sig_str_abs(s1,s2):
                    diff = s1 - s2
                    return diff
                #---------------------------------------------------------------
                # SIgnificant stirkes defeended
                #---------------------------------------------------------------
                def sig_str_def(f1,f2):
                    f1 = int(f1.replace("%",''))
                    f2 = int(f2.replace("%",''))
                    diff = f1 - f2
                    return diff
                #---------------------------------------------------------------
                # Takedown Average
                #---------------------------------------------------------------
                def td_avg(f1,f2):
                    diff = f1 - f2
                    return diff
                #---------------------------------------------------------------
                # Takedown Accuracy
                #---------------------------------------------------------------
                def td_acc(f1,f2):
                    f1 = int(f1.replace("%",''))
                    f2 = int(f2.replace("%",''))
                    diff = f1 - f2
                    return diff
                #---------------------------------------------------------------
                # Takedown Defence
                #---------------------------------------------------------------
                def td_def(f1,f2):
                    f1 = int(f1.replace("%",''))
                    f2 = int(f2.replace("%",''))
                    diff = f1 - f2
                    return diff
                #---------------------------------------------------------------
                # Submission Average
                #---------------------------------------------------------------
                def sub_avg(f1,f2):
                    diff = f1 - f2
                    return diff
            
                #---------------------------------------------------------------
                # Point System
                #---------------------------------------------------------------

                # Xp
                n_fights1 = int((exp(f1[1],f2[1]))[0]) + int((exp(f1[1],f2[1]))[2])  # Num of fights
                n_fights2 = int((exp(f1[1],f2[1]))[1]) + int((exp(f1[1],f2[1]))[3])
                exp_diff = n_fights1 - n_fights2 # Exprience Difference (total fights - total fights)
                if exp_diff > 0:
                    f1_points.append(1)
                if exp_diff < 0:
                    f2_points.append(1)
                win_rate1 = int((exp(f1[1],f2[1]))[0]) / n_fights1 * 100 #  Win Rate
                win_rate2 = int((exp(f1[1],f2[1]))[1]) / n_fights2 * 100
                if win_rate1 > win_rate2:
                    f1_points.append(1)
                if win_rate1 < win_rate2:
                    f2_points.append(1)

                # Height
                if height(height1,height2) > 0:
                    f1_points.append(1)
                if height(height1,height2) < 0:
                    f2_points.append(1)   

                # Weight
                if weight(weight1,weight2) >= 15:
                    f1_points.append(1)
                if weight(weight1,weight2) <= -15:
                    f2_points.append(1)

                # Reach
                if reach(reach1,reach2) > 0:
                    f1_points.append(1)
                if reach(reach1,reach2) < 0:
                    f2_points.append(1)
                
                # Age 
                if age(age1,age2) > 3:
                    f2_points.append(1)
                if age(age1,age2) < -3:
                    f1_points.append(1)
                
                # significant strikes landed per min
                if  sig_str_lpm(sig_str_lpm1,sig_str_lpm2) > 0:
                    f1_points.append(1)
                if sig_str_lpm(sig_str_lpm1,sig_str_lpm2) < 0:
                    f2_points.append(1)

                # significant strikes accuracy
                if sig_str_acc(sig_str_acc1,sig_str_acc2) > 0:
                    f1_points.append(1)
                if sig_str_acc(sig_str_acc1,sig_str_acc2) < 0:
                    f2_points.append(1)

                # significant stikes absorbed
                if sig_str_abs(sig_str_abs1,sig_str_abs2) > 0:
                    f1_points.append(1)
                if sig_str_abs(sig_str_abs1,sig_str_abs2) < 0:
                    f2_points.append(1)
                
                # significant stikes defended
                if sig_str_def(sig_str_def1,sig_str_def2) > 0:
                    f1_points.append(1)
                if sig_str_def(sig_str_def1,sig_str_def2) < 0:
                    f2_points.append(1)
                
                # Takedown Average
                if td_avg(td_avg1,td_avg2) > 0:
                    f1_points.append(1)
                if td_avg(td_avg1,td_avg2) < 0:
                    f2_points.append(1)

                # Takedown Accouracy
                if td_acc(td_acc1,td_acc2) > 0:
                    f1_points.append(1)
                if td_acc(td_acc1,td_acc2) < 0:
                    f2_points.append(1)
                
                # Takedown Defence
                if td_def(td_def1,td_def2) > 0:
                    f1_points.append(1)
                if td_def(td_def1,td_def2) < 0:
                    f2_points.append(1)

                # Sumbission Average
                if sub_avg(sub_avg1,sub_avg2) > 0:
                    f1_points.append(1)
                if sub_avg(sub_avg1,sub_avg2) < 0:
                    f2_points.append(1)
                
                #---------------------------------------------------------------
                # Printing
                #print('fighter 1 has {} points'.format(sum(f1_points)))
                #print('fighter 2 has {} points \n'.format(sum(f2_points)))
                if sum(f1_points) > sum(f2_points):
                    print('Projected winner is {}'.format(f1[0]))
                if sum(f1_points) < sum(f2_points):
                    print('Projected winner is {}'.format(f2[0]))
#---------------------------------------------------------------
    #---------------------------------------------------------------
    model(f1[1],f1[2],f1[3],f1[4],f1[5],f1[6],f1[7],f1[8],f1[9],f1[10],f1[11],f1[12],f1[13],f1[14],
          f2[1],f2[2],f2[3],f2[4],f2[5],f2[6],f2[7],f2[8],f2[9],f2[10],f2[11],f2[12],f2[13],f2[14])
    #---------------------------------------------------------------
