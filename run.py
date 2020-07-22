from flask import Flask,render_template,request
app=Flask(__name__,template_folder='template',static_folder='template')

@app.route('/')
def home():
	return render_template('input.html')


if __name__=='__main__':
	app.run(debug=True)