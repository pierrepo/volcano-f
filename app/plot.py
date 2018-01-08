# -*- coding: utf-8 -*-
#FABIEN GENTY
#2017/10
#PROJET LONG VISUALISATEUR DE PROTEINES

# importing librairy
from bokeh.plotting import figure, output_file, show,ColumnDataSource
from bokeh import *
from bokeh.models import HoverTool,Span,Slider, CustomJS,CategoricalColorMapper,Button, DataTable, TableColumn
from bokeh.layouts import row, widgetbox
from bokeh.models.widgets import *
from bokeh.embed import components,autoload_static
import opening_csv as cs
import pandas as pd
import numpy as np
from os.path import dirname, join


def volcano_plot(data_sans):
    index = data_sans['access']
    x = data_sans['logfc']
    y = data_sans['pvalue']
    pos = data_sans['pos']


    source = ColumnDataSource(
        data=dict(
            x = x,
            y = y,
            accession = index,
            position = pos
            ))

    color_mapper = CategoricalColorMapper(factors=["up","normal","down"],
                                            palette=['yellow', 'green','blue'])
    # dictionnary for the hoover tool
    hover = HoverTool(tooltips=[
        ("accession", "@accession"),
        ("x","@x"),
        ("y","@y")
        ])

    yrange=[min(y)-0.1,max(y)+0.1]
    xrange = [min(x)-1,max(x)+0.1]

    # setting the tools
    TOOLS=",pan,wheel_zoom,box_zoom,reset,box_select,lasso_select,previewsave"

    # create a new plot with a title and axis labels
    p = figure(
        y_range=yrange,
        x_range = xrange,
        x_axis_label = 'log(fc)',
        y_axis_label = '-log(pvalue)',
        tools = TOOLS,
        plot_width = 800,
        plot_height = 800)

    p.add_tools(hover)

    # title modification
    p.title.text = "pvalue versus fold-change"
    p.title.align = "center"
    p.title.text_color = "blue"
    p.title.text_font_size = "25px"
    #p.title.background_fill_color = "#aaaaee"


    #setting the widgets slider
    h_slider = Slider(start=yrange[0],end=yrange[1], value=1, step=.1, title="variation of log(pvalue)")
    v_slider_right = Slider(start = 0, end = xrange[1], value=0.5, step=.01,title="right fold change")
    v_slider_left = Slider(start =xrange[0], end=0, value=-0.5, step=.01,title="left log fold change")

    # Horizontal line
    hline = Span(location=h_slider.value, dimension='width', line_color='green', line_width=2)
    # Vertical line
    vline1 = Span(location =v_slider_right.value , dimension='height', line_color='blue', line_width=2)
    vline2 = Span(location=v_slider_left.value, dimension='height', line_color='black', line_width=2)


    #setting the widgets slider
    h_slider = Slider(start=yrange[0],end=yrange[1], value=1, step=.1, title="variation of log(pvalue)")
    v_slider_right = Slider(start = 0, end = xrange[1], value=0.5, step=.01,title="right fold change")
    v_slider_left = Slider(start =xrange[0], end=0, value=-0.5, step=.01,title="left log fold change")
    p.renderers.extend([vline1,vline2, hline])

    # add a circle points
    p.circle('x','y',source = source,
    color=dict(field='position', transform=color_mapper),
    legend='position'
    )
    #setting the code to obain a real time ajustement of value and color
    #on th plot
    code="""
    var data = source.data;
    var low =  v_slider_left.value;
    var up = v_slider_right.value
    var back_value = h_slider.value;

    x = data['x']
    y = data['y']
    pos = data['position']

    span.location = slider.value

    for (i = 0; i < x.length; i++) {
        if( (x[i] < low) && (y[i] > back_value)) {
            pos[i] = 'down'
        } else if ((x[i] > up) && (y[i] > back_value)){
            pos[i] = 'up'
        } else {
            pos[i] = 'normal'
        }
    }
    console.log(source.data)
    source.change.emit()
    """
    # callback of the sliders
    h_slider.callback       = CustomJS(args=dict(source=source, span=hline,  slider=h_slider,       v_slider_left=v_slider_left,h_slider=h_slider,v_slider_right=v_slider_right), code=code)
    v_slider_right.callback = CustomJS(args=dict(source=source, span=vline1, slider=v_slider_right, v_slider_left=v_slider_left,h_slider=h_slider,v_slider_right=v_slider_right), code=code)
    v_slider_left.callback  = CustomJS(args=dict(source=source, span=vline2, slider=v_slider_left,  v_slider_left=v_slider_left,h_slider=h_slider,v_slider_right=v_slider_right), code=code)

    # creating du tableau des résulats de la selection datacolumn
    columns = [TableColumn(field="accession", title="numero d'accession"),
               TableColumn(field="x", title="log(fc)"),
               TableColumn(field="y", title="-log(pvalue)"),
               TableColumn(field="position", title="position"),
               ]

    data_table = DataTable(source=source, columns=columns, width=400, height=280)
    # creating of the download button
    button = Button(label="Download", button_type="success")
    button.callback = CustomJS(args=dict(source=source),code=open(join(dirname(__file__),"static/js/download.js")).read())
    layout = row(p, widgetbox(v_slider_left,v_slider_right,h_slider,data_table,button))
    return layout

if __name__ == "__main__":
       main()
