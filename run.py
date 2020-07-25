from flask import Flask,render_template,url_for,request,redirect
from werkzeug.utils import secure_filename
import os
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
    if request.method == "POST":
        if request.files:

            audio = request.files["audio"]

            audio.save('static/audio.mp3')

            #call your functio below and pass the same path as above static/audio.mp3
            genre = "Pop"
    return render_template('input.html', genre = genre)


if __name__=='__main__':
	app.run(debug=True)
