"""
The flask application package.
"""

from flask import Flask, session
from .runserver import run_app
app = Flask(__name__)

import Wrapper_to_Form.views

class ArbitraryPasser():
		func_dict = {}

def create_route(port=5555, **kwargs):
	err = [callable(func) for func in kwargs.values()]
	if False in err:
		raise ValueError("All argument values must be functions")
	err = [type(funcname) == str for funcname in session]
	if False in err:
		raise ValueError("All argument keys must be strings")
	#session['func_names'] = list(kwargs.keys())
	setattr(ArbitraryPasser, 'func_dict', kwargs)
	run_app(port, app)
