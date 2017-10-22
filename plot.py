import plotly.plotly as py
import plotly.graph_objs as go
import plotly
import pandas as pd
import math as m
import numpy as np
from read_csv import *

data_sans = CSV_opening('data.csv')
data_volcano = to_data_volcano(data_sans)

names = data_volcano.columns.values.tolist()
trace1 = go.Scatter(
    x = np.array(data_volcano['log(fc)']),
    y = np.array( data_volcano['-log(pvalue)']),
    text = data_volcano['prot_id'],
    mode = 'markers',
    opacity = 0.7,
    marker = {
        'size': 10,
        'line': {'width': 0.5, 'color': 'red'}
    })

data = go.Data([trace1])

layout = go.Layout(
    xaxis={'type': 'log', 'title': 'log(fc)'},
    yaxis={'title': ' - Log(pvalue)'},
    margin={'l': 40, 'b': 40, 't': 10, 'r': 10},
    legend={'x': 0, 'y': 1},
    hovermode='closest')
figure=go.Figure(data=data,layout=layout)
plotly.offline.plot(figure,filename = 'toto.html')
