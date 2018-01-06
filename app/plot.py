# -*- coding: utf-8 -*-
#FABIEN GENTY
#2017/10
#PROJET LONG VISUALISATEUR DE PROTEINES

# importing librairy
from bokeh.plotting import figure, output_file, show,ColumnDataSource
from bokeh.models import HoverTool,Span,Slider, CustomJS,CategoricalColorMapper
from bokeh.layouts import row, widgetbox
from bokeh.models.widgets import *
import opening_csv as cs
import pandas as pd
import numpy as np

def volcano_plot(data_sans):

    index = data_sans['accession']
    x = data_sans['log(fc)']
    y = data_sans['-log(pvalue)']

    # dicrtionnay for the hoover tool
    source = ColumnDataSource(
        data=dict(
            x = x,
            y = y,
            accession = index))

    hover = HoverTool(tooltips=[
        ("accession", "@accession"),
        ("x","@x"),
        ("y","@y")
        ])

    yrange=[min(y)-0.1,max(y)+0.1]
    xrange = [min(x)-1,max(x)+0.1]

    # setting the tools
    TOOLS=",pan,wheel_zoom,box_zoom,reset,box_select,lasso_select"

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
    #p.title.text = "volcano plot"
    #p.title.align = "center"
    #p.title.text_color = "blue"
    #p.title.text_font_size = "25px"
    #p.title.background_fill_color = "#aaaaee"
    p.add_tools(hover)


    #setting the widgets slider
    h_slider = Slider(start=yrange[0],end=yrange[1], value=1, step=.1, title="variation of log(pvalue)")
    v_slider_right = Slider(start = 0, end = xrange[1], value=1, step=.01,title="right fold change")
    v_slider_left = Slider(start =xrange[0], end=0, value=1, step=.01,title="left log fold change")


    #setting the widgets slider
    h_slider = Slider(start=yrange[0],end=yrange[1], value=1, step=.1, title="variation of log(pvalue)")
    v_slider_right = Slider(start = 0, end = xrange[1], value=0.5, step=.01,title="right fold change")
    v_slider_left = Slider(start =xrange[0], end=0, value=-0.5, step=.01,title="left log fold change")
    p.renderers.extend([vline1,vline2, hline])

    # add a circle points
    p.circle('x','y',source = source)

    # callback of the sliders
    h_slider.callback = CustomJS(args=dict(span=hline, slider=h_slider),code="""span.location = slider.value""")
    v_slider_right.callback = CustomJS(args=dict(span=vline1, slider=v_slider_right),code="""span.location = slider.value""")
    v_slider_left.callback = CustomJS(args=dict(span=vline2, slider=v_slider_left),code="""span.location = slider.value""")

    columns = [TableColumn(field="accession", title="numero d'accession"),
               TableColumn(field="x", title="log(fc)"),
               TableColumn(field="y", title="-log(pvalue)")
               ]
    data_table = DataTable(source=source, columns=columns, width=400, height=280)


    def update_data_frame(attrname, old, new):

        #prendre les valeurs des slider
        low =  v_slider_left.value
        up = v_slider_right.value
        back_value = h_slider.value

        # creation des nouveaux dataframe ciblés up_regulated et

        df_low = pd.DataFrame()
        df_up = pd.DataFrame()

        for fc,pv,name in zip(data_sans['log(fc)'],data_sans['-log(pvalue)'],data_sans['accession']) :
            if (data_sans[data_sans['log(fc)'] > up and :
                buff = [name,fc,pv]
                df_low.append(buff)


    # show the results
    layout = row(p, widgetbox(v_slider_left,v_slider_right,h_slider,data_table ))
    return layout


if __name__ == "__main__":
        main()
