# -*- coding: utf-8 -*-
import csv
import numpy as np

class CSVHandle():
    def __init__(self):
        pass
    
    def read(self, file_name):
        data = []
        data_title = []

        with open(file_name, 'r') as csv_file:
            rows = csv.reader(csv_file)
            i = 0
            for row in rows:
                i += 1

                if i >= 12:
                    data.append(row)
                elif i == 11:
                    data_title.append(row)
                    
        data = np.array(data)
        data_title = list(data_title)
            
        return data, data_title

