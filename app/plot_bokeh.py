# -*- coding: utf-8 -*-
#FABIEN GENTY
#2017/10
#PROJET LONG VISUALISATEUR DE PROTEINES

# importing librairy

import opening_csv as cs
import plot

# calling the csv file
data_sans = cs.CSV_opening('/home/fabien/Documents/volcano-f/data.csv')
plot.volcano_plot(data_sans)
