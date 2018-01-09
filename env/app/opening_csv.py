# -*- coding: utf-8 -*-
#FABIEN GENTY
#2017/10
#PROJET LONG VISUALISATEUR DE PROTEINES

#loading librairy

import pandas as pd
import math as m
import numpy as np

# opening CVS file, cleaning data and computing the data for the volcano plot
def CSV_opening(path):
    """
    Opening the CSV file and cleaning the file with Na and
    preparing the data for the volcano plot
    """
    #getting csv data into pandas DataFrame
    path = "data.csv"
    data_csv = pd.read_csv( path,
                           sep = '\t',
                           names = ['acession','pvalue','fc'],
                           na_filter = True,
                           na_values =" NaN",
                           header = 0 )
    DF = pd.DataFrame()
    #add a column with three names
    for row in data_csv.itertuples():
        dt = row[1]
        logp =  - m.log10(row[2])
        fc =   m.log2(row[3])
        tmp = pd.Series([dt,logp,fc])
        DF = DF.append(tmp,ignore_index=True)
        DF['position'] = "normal"
        
    DF.columns = ['access','pvalue','logfc','pos']
    DF.loc[((DF.logfc < -0.5) & (DF.pvalue > 1)) ,['pos']] = "down"
    DF.loc[((DF.logfc > 0.5) & (DF.pvalue > 1)) ,['pos']] = "up"
    return DF

if __name__ == "__main__":
    main()
