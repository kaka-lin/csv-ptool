# -*- coding: utf-8 -*-
import csv
import numpy as np

class CSVHandle():
    def __init__(self):
        pass
    
    def read(self, file_name):
        data = []

        with open(file_name, 'r') as csv_file:
            rows = csv.reader(csv_file)
            i = 0
            for row in rows:
                i += 1

                if i >= 12:
                    #row = np.array(row, dtype=float)
                    #row = np.around(row, decimals=1)
                    data.append(row)
        
        data = np.array(data)

        for i in range(len(data)):
            for j in range(len(data[i])):
                data[i][j] = round(float(data[i][j]), 2)

        time = np.array(data[:, 0])
        li_voltage = np.array(data[:, 1])
        print(li_voltage)
        return li_voltage
