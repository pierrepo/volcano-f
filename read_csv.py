# -*- coding: utf-8 -*-
#FABIEN GENTY
#2017/10
#PROJET LONG VISUALISATEUR DE PROTEINES

#loading librairy

import pandas as pd
import math as m
import numpy as np
import datetime

def CSV_opening(path):
    """
    Opening the CSV file and cleaning the file with Na
    """
    data_csv = pd.read_csv(path,
                           sep = '\t',
                           names = ['id','pvalue','A','B'],
                           na_filter = True,
                           na_values =" NaN")


    data_sans = data_csv.dropna(subset = ['id', 'pvalue', 'A', 'B' ])
    return data_sans


def to_data_volcano(data_frame):
    """
    preparing the data for the volcano plot
    """
    DF = pd.DataFrame()
    for row in data_frame.itertuples():
        dt = row[1]
        logp = round(m.log(row[2],2),4)
        fc =  - round(m.log10(row[3]/row[4]),4)
        tmp = pd.Series([dt,logp,fc])
        DF = DF.append(tmp,ignore_index=True)
    return DF

if __name__ == '__main__':
    Data = CSV_opening('/home/fabien/Documents/volcano-f/data.csv')
    data_volcano = to_data_volcano(Data)
    data_volcano.columns = ['prot_id',' -log(pvalue)','log(fc)']
    print(data_volcano)
