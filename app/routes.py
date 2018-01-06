#set the library
import os,shutil
from flask import *
from werkzeug.utils import secure_filename
import opening_csv as cs
from bokeh.models import HoverTool,Span,Slider, CustomJS
from bokeh.layouts import row, widgetbox
from bokeh.models.widgets import *
import pandas as pd
import numpy as np
from bokeh.embed import components
from bokeh import *
from bokeh.plotting import figure,ColumnDataSource
import plot as d

#set the download prefereces
UPLOAD_FOLDER = 'upload_data'
ALLOWED_EXTENSIONS = set(['txt','csv'])

def allowed_file(filename):
    return '.' in filename and \
    filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def delete_file():
    path = os.path.dirname(os.path.abspath('routes.py'))
    path = path.replace('/templates','')
    path = path +'/upload_data'
    for the_file in os.listdir(path):
        file_path = os.path.join(path, the_file)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
        except Exception as e:
            print(e)
def path_to_csv():
    path = os.path.dirname(os.path.abspath('routes.py'))
    path = path.replace('/templates','')
    path = path +'/upload_data'
    filename = os.listdir(path)
    path2 = path +'/' +filename[0]
    return path2

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
app.secret_key = 'super secret key'


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            delete_file()
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('plot',filename=filename))
    return render_template('home.html')

@app.route('/plot')
def plot():
    data_sans = cs.CSV_opening(path_to_csv())
    # Create the plot
    graph = d.volcano_plot(data_sans)

    # Embed plot into HTML via Flask Render
    script, div = components(graph)
    return render_template("plot.html", script=script, div=div)

@app.route('/board')
def board():
  return render_template('board.html')

@app.route('/about')
def about():
  return render_template('about.html')

if __name__ == '__main__':
  app.run(debug=True)
