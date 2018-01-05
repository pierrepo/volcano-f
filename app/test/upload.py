# -*- coding: utf-8 -*-
import os
from flask import Flask, render_template
from flask_uploads import UploadSet, configure_uploads, IMAGES, patch_request_class
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import SubmitField

app = Flask(__name__)
app.config['SECRET_KEY'] = 'I have a dream'
app.config['UPLOADED_PHOTOS_DEST'] = os.getcwd() +'/upload_data'

upload_csv = UploadSet('photos', extensions = ('csv'))
configure_uploads(app, upload_csv)
patch_request_class(app)  # set maximum file size, default is 16MB

class UploadForm(FlaskForm):
    upload_csv = FileField(validators=[FileAllowed(upload_csv, u'Please use a csv file'), FileRequired(u'The file is empty')])
    submit = SubmitField(u'Upload')


@app.route('/', methods=['GET', 'POST'])
def upload_file():
    form = UploadForm()
    if form.validate_on_submit():
        filename = upload_csv.save(form.upload_csv.data)
        file_url = upload_csv.url(filename)
    else:
        file_url = None
    return render_template('index.html', form=form, file_url=file_url)


if __name__ == '__main__':
    app.run()
