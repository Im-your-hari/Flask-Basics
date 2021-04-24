from flask import Flask,render_template

app=Flask(__name__)

@app.route('/')
def primary():
	return render_template('primary.html')

@app.route('/about/')
def about():
	return render_template('about.html')

if __name__=='__main__':
	app.run(debug=True)