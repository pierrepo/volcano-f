# -*- coding: utf-8 -*-
#FABIEN GENTY
#2017/10
#PROJET LONG VISUALISATEUR DE PROTEINES

#loading librairy

import pandas as pd
import math as m
import numpy as np

def set_CSV(path):
    """
    Opening the CSV file and cleaning the file with Na
    """
    data_csv = pd.read_csv(path,
                           sep = '\t',
                           header=0,
                           na_filter = True,
                            index_col=False,
                           na_values =" NaN")
    del data_csv["Unnamed: 0"]
    return data_csv

if __name__ == '__main__':
    main()
    #donne = set_CSV("data_table/data_down.csv")
    #print(donne)
