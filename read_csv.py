# -*- coding: utf-8 -*-
#FABIEN GENTY
#2017/10
#PROJET LONG VISUALISATEUR DE PROTEINES

#loading librairy

import pandas as pd
import math as m
import numpy as np
import datetime


data_csv = pd.read_csv('data.csv',
                       sep = '\t',
                       names = ['id','pvalue','A','B'],
                       na_filter = True,
                       na_values =" NaN")


#data_sans = data_csv.dropna(subset = ['id', 'pvalue', 'A', 'B' ])

#columns = ['id','logpvalue','logfc']
#df = pd.DataFrame( columns = columns)
#df = df.fillna(0) # with 0s rather than NaNs
#print(data_sans)


DF = pd.DataFrame()

for row in data_sans.itertuples():
    
    dt = row[1]
    logp = round(m.log(row[2],2),4)
    fc =  - round(m.log10(row[3]/row[4]),4)
    tmp = pd.Series([dt,logp,fc])
    DF = DF.append(tmp,ignore_index=True)


print(DF)