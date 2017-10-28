# -*- coding: utf-8 -*-
#FABIEN GENTY
#2017/10
#PROJET LONG VISUALISATEUR DE PROTEINES

# importing librairy
from bokeh.plotting import figure, output_file, show,ColumnDataSource
from bokeh.models import HoverTool
import pandas as pd
import math as m
import numpy as np


# ouveture du CVS  avec traitements de données
def CSV_opening(path):
    """
    Opening the CSV file and cleaning the file with Na and
    preparing the data for the volcano plot
    """
    data_csv = pd.read_csv( path,
                           sep = '\t',
                           names = ['acession','pvalue','fc'],
                           na_filter = True,
                           na_values =" NaN",
                           header = 0 )
    DF = pd.DataFrame()
    for row in data_csv.itertuples():
        dt = row[1]
        logp =  - m.log2(row[2])
        fc =   m.log10(row[3])
        tmp = pd.Series([dt,logp,fc])
        DF = DF.append(tmp,ignore_index=True)
    DF.columns = ['accession','-log(pvalue)','log(fc)']
    return DF

# calling the csv file
data_sans = CSV_opening('/home/fabien/Documents/volcano-f/data.csv')

# seting the data
index = np.array(data_sans['accession'])
x = np.array(data_sans['log(fc)'])
y = np.array(data_sans['-log(pvalue)'])

# dicrtionnay for the hoover tool
source = ColumnDataSource(
    data=dict(
        x= x,
        y=y,
        accession =index))

hover = HoverTool(tooltips=[
    ("accession", "@accession"),
    ("x","@x"),
    ("y","@y")
    ])

# setting the tools
TOOLS="crosshair,pan,wheel_zoom,box_zoom,reset,box_select,lasso_select"
# create a new plot with a title and axis labels
p = figure(
    title = " Volcano plot",
    x_axis_label = 'log(fc)',
    y_axis_label = '-log(pvalue)',
    tools = TOOLS,
    plot_width = 800,
    plot_height = 800)

p.add_tools(hover)

# output to static HTML file
output_file("vocano_pot.html",
    title="volcano plot")

# add a circle renderer with vectorized colors and sizes
p.circle('x','y',source = source)

# show the results
show(p)
