# -*- coding: utf-8 -*-
#FABIEN GENTY
#2017/10
#PROJET LONG VISUALISATEUR DE PROTEINES

#loading librairy

import pandas as pd
import math as m
import numpy as np

def CSV_opening(path):
    """
    Opening the CSV file and cleaning the file with Na
    """
    data_csv = pd.read_csv(path,
                           sep = '\t',
                           names = ['id','pvalue','fold_change'],
                           na_filter = True,
                           na_values =" NaN")

    return data_csv

if __name__ == '__main__':
