import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

from flask import Flask,render_template,url_for,request,redirect
from werkzeug.utils import secure_filename
import tensorflow
import os
from app import *

app=Flask(__name__,template_folder='template')

@app.route('/')
@app.route('/input')
def home():
	return render_template('input.html')

@app.route('/prototype')
def about():
	return render_template('prototype.html')

@app.route('/',methods = ['GET', 'POST'])
def upload_audio():
    genre = ""
    prob1 = ""
    name=""
    if request.method == "POST":
        if request.files:

            audio = request.files["audio"]
            name = audio.filename
            audio.save('data/audio.mp3')

            #call your function below and pass the same path as above static/audio.mp3
            genre = main('data/audio.mp3')
            prob1 =probability('data/audio.mp3')
    return render_template('input.html', genre = genre , prob1 = prob1, name=name)


if __name__=='__main__':
	app.run(debug=True)


