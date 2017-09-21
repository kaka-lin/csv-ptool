# -*- coding: utf-8 -*-
import csv
import matplotlib.pyplot as plt
import numpy as np

file = []

with open('data.csv', 'r') as f:
    r = csv.reader(f)
    i = 0
    for row in r:
        i += 1

        if i >= 12:
            #row = np.array(row, dtype=float)
            #row = np.around(row, decimals=1)
            file.append(row)
        
file = np.array(file)

for i in range(len(file)):
    for j in range(len(file[i])):
        file[i][j] = round(float(file[i][j]), 2)

time = np.array(file[:, 0])
li_voltage = np.array(file[:, 1])
print(li_voltage)

plt.plot(li_voltage)
plt.ylim(0, 40)
plt.show()