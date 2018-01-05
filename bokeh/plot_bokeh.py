# -*- coding: utf-8 -*-
#FABIEN GENTY
#2017/10
#PROJET LONG VISUALISATEUR DE PROTEINES

# importing librairy
from bokeh.plotting import figure, output_file, show,ColumnDataSource
from bokeh.models import HoverTool,Span,Slider, CustomJS
from bokeh.layouts import row, widgetbox
from bokeh.models.widgets import *
import pandas as pd
import math as m
import numpy as np

# opening CVS file, cleaning data and computing the data for the volcano plot
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

yrange=[min(y)-0.1,max(y)+0.1]
xrange = [min(x)-1,max(x)+0.1]
# setting the tools
TOOLS="crosshair,pan,wheel_zoom,box_zoom,reset,box_select,lasso_select"
# create a new plot with a title and axis labels
p = figure(
    y_range=yrange,
    x_range = xrange,
    x_axis_label = 'log(fc)',
    y_axis_label = '-log(pvalue)',
    tools = TOOLS,
    plot_width = 800,
    plot_height = 800)

# title modification
p.title.text = "volcano plot"
p.title.align = "center"
p.title.text_color = "blue"
p.title.text_font_size = "25px"
#p.title.background_fill_color = "#aaaaee"


#setting the widgets slider
h_slider = Slider(start=yrange[0],end=yrange[1], value=1, step=.1, title="variation of log(pvalue)")
v_slider_right = Slider(start = 0, end = xrange[1], value=1, step=.01,title="right fold change")
v_slider_left = Slider(start =xrange[0], end=0, value=1, step=.01,title="left log fold change")


# Horizontal line
hline = Span(location=h_slider.value, dimension='width', line_color='green', line_width=2)
# Vertical line
vline1 = Span(location =v_slider_right.value , dimension='height', line_color='blue', line_width=2)
vline2 = Span(location=v_slider_left.value, dimension='height', line_color='black', line_width=2)

p.renderers.extend([vline1,vline2, hline])
p.add_tools(hover)

# output to static HTML file
output_file("vocano_pot.html",title="volcano plot")

# add a circle points
p.circle('x','y',source = source)

# callback of the sliders
h_slider.callback = CustomJS(args=dict(span=hline, slider=h_slider),code="""span.location = slider.value""")
v_slider_right.callback = CustomJS(args=dict(span=vline1, slider=v_slider_right),code="""span.location = slider.value""")
v_slider_left.callback = CustomJS(args=dict(span=vline2, slider=v_slider_left),code="""span.location = slider.value""")

'''
def update_data_frame(attrname, old, new):

    #prendre les valeurs des slider
    low =  v_slider_left.value
    up = v_slider_right.value
    back_value = h_slider.value

    low = -0.20
    up = 0.26
    back_value = 4,20

    # creation des nouveaux dataframe ciblés up_regulated et

    df_low = pd.DataFrame()
    df_up = pd.DataFrame()

    for fc,pv,name in zip(data_sans['log(fc)'],data_sans['-log(pvalue)'],data_sans['accession']) :
        if (data_sans[data_sans['log(fc)'] > up and :
            buff = [name,fc,pv]
            df_low.append(buff)
        

'''

# show the results

show(row(p, widgetbox(v_slider_left,v_slider_right,h_slider )))
