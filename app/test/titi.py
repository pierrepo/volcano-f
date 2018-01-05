#set the library
import os
from flask import *
from werkzeug.utils import secure_filename


@app.route('/template', methods=['GET', 'POST'])
def template():
    if request.method == 'POST':
        return "Hello"
    return render_template('index.html')


if __name__ == '__main__':
  app.run(debug=True)
