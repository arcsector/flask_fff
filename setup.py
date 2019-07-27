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
		zip_safe=False,
	include_package_data=True,
	platforms='any',
	packages=find_packages(),
	license='BSD License',
	install_requires=[
		'flask>1.0.0',
		'flask_wtf',
		'wtforms'
	],
	classifiers=[
		'Development Status :: 3 - Alpha',
		'Environment :: Web Environment',
		'Framework :: Flask',
		'Intended Audience :: Developers',
		'License :: OSI Approved :: BSD License',
		'Operating System :: OS Independent',
		'Programming Language :: Python',
		'Programming Language :: Python :: 2',
		'Programming Language :: Python :: 2.7',
		'Programming Language :: Python :: 3',
		'Programming Language :: Python :: 3.4',
		'Programming Language :: Python :: 3.5',
		'Programming Language :: Python :: 3.6',
		'Programming Language :: Python :: Implementation :: CPython',
		'Programming Language :: Python :: Implementation :: PyPy',
		'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
		'Topic :: Software Development :: Libraries :: Python Modules'
	]
)
