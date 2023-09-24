# -*- coding: utf-8 -*-
"""
Spyder Editor

Proof that we aren't losing wish stones by divinate implementation'

"""


import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from statistics import mean

pool_list = ["Legendary Esper", "Legendary Divinate", "Epic Esper", "Epic Divinate", "Rare Esper", "Rare Divinate"]

def pull_weighted():
    rand_num = random.uniform(0, 1)
    if rand_num <= 0.01:
        return "Legendary Esper"
    elif rand_num <= 0.02:
        return "Legendary Divinate"
    elif rand_num <= 0.11:
        return "Epic Esper"
    elif rand_num <= 0.20:
        return "Epic Divinate"
    elif rand_num <= 0.60:
        return "Rare Esper"
    else:
        return "Rare Divinate"
    
def legacy_pull_weighted():
    rand_num = random.uniform(0, 1)
    if rand_num <= 0.01:
        return "Legendary Esper"
    elif rand_num <= 0.10:
        return "Epic Esper"
    else:
        return "Rare Esper"
    
def wishstone_calc(record):
    if record == "Legendary Esper":
        return 20
    elif record == "Epic Esper":
        return 1
    else :
        return 0

random_pull = random.choices(pool_list, weights=(1,1,9,9,40,40))
pulls = []
average_leg_per_pull = []
pity = 0
wishstones = 0

legacy_pulls = []
legacy_average_leg_per_pull = []
legacy_pity = 0
legacy_wishstones = 0

for i in range(20000):
    if pity == 99:
        pulls.append("Legendary Esper")
        legacy_pulls.append("Legendary Esper")
        pity = 0
        legacy_pity = 0
        wishstones += 20
        legacy_wishstones += 20
    else :
        pull = pull_weighted()
        legacy_pull = legacy_pull_weighted()
        pulls.append(pull)
        wishstones += wishstone_calc(pull)
        legacy_pulls.append(legacy_pull)
        legacy_wishstones += wishstone_calc(legacy_pull)
        if pull == "Legendary Esper" :
            pity = 0
            legacy_pity = 0
        else :
            pity += 1
            legacy_pity += 1
    num_leg_esp = pulls.count("Legendary Esper")
    avg_leg = num_leg_esp / (i+1)
    average_leg_per_pull.append(avg_leg)
    
    legacy_num_leg_esp = legacy_pulls.count("Legendary Esper")
    legacy_avg_leg = legacy_num_leg_esp / (i+1)
    legacy_average_leg_per_pull.append(legacy_avg_leg)
    
print(average_leg_per_pull[19999])
print(wishstones)
print(legacy_average_leg_per_pull[19999])
print(legacy_wishstones)


print(f'Average Probability of Pulling Legendary Esper: {pd.average_leg_per_pull.mean()}')

plt.plot(average_leg_per_pull, label="New Version")
plt.plot(legacy_average_leg_per_pull, label="Legacy Version")
plt.ylabel("Average Probability of Obtaining Legendary Esper")
plt.xlabel("Spin")
plt.legend()
plt.show




