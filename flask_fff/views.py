"""
Routes and views for the flask application.
"""
from .routes import CreateForm
from datetime import datetime
from flask import render_template, Flask

app=Flask(__name__)

@app.route('/')
def createform():
	return CreateForm()

@app.route('/home')
def home():
	"""Renders the home page."""
	return render_template(
		'index.html',
		title='Home Page',
		year=datetime.now().year,
	)

@app.route('/contact')
def contact():
	"""Renders the contact page."""
	return render_template(
		'contact.html',
		title='Contact',
		year=datetime.now().year,
		message='Your contact page.'
	)

@app.route('/about')
def about():
	"""Renders the about page."""
	return render_template(
		'about.html',
		title='About',
		year=datetime.now().year,
		message='Your application description page.'
	)