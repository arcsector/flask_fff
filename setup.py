from setuptools import setup

setup(
	name='flask_fff',
	description='Flask - Form Follows Function',
	long_description='Flask - Form Follows Function is a module which allows you to spin up a webform based on a python function quickly.',
	url='https://github.com/arcsector/flask_fff',
	author='arcsector',
	author_email='george.haraksin@laverne.edu',
	version=0.1
	license='BSD License',
	packages=[
		'flask>1.0',
		'flask_wtf',
		'wtforms',
		'inspect'
	]
)
