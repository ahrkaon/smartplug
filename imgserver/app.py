from flask import Flask, render_template, request, redirect
from werkzeug.utils import secure_filename
import os
import logging

img_folder = os.path.join('static', 'test1.jpg')

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = img_folder
@app.after_request
def set_response_headers(response):
    response.headers['Cache-Control']='no-cache, no-store, must-revalidate'
    response.headers['Pragma']='no-cache'
    response.headers['Expires'] = '0'
    return response
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload')
def render_file():
    return render_template('upload.html')

@app.route('/fileUpload', methods=['GET', 'POST'])
def upload_file():
    #return render_template('imgshow.html')
    if request.method == 'POST':
        f = request.files['file']
        #upload = request.files.getlist('file')
        #for f in upload:
        f.save('./static/img/'+secure_filename(f.filename))
        #return render_template("imgshow.html", filename=image_file)
    return render_template('image.html')
if __name__ == '__main__':
    app.run(host='0.0.0.0', port = 8080, debug=True)

