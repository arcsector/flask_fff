from setuptools import setup, find_packages

setup(
	name='Flask-FFF',
	description='Flask - Form Follows Function',
	long_description='Flask - Form Follows Function is a module which allows you to spin up a webform based on a python function quickly.',
	url='https://github.com/arcsector/flask_fff',
	author='arcsector',
	author_email='george.haraksin@laverne.edu',
	version=0.1,
	#py_modules=['flask_fff'],
	include_package_data=True,
	platforms='any',
	packages=find_packages(),
	license='BSD License',
	install_requires=[
		'flask>1.0.0',
		'flask_wtf',
		'wtforms'
	]
)
