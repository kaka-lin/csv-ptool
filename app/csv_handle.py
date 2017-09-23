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

                if i >= 11:
                    data.append(row)

        data = np.array(data)
            
        return data
