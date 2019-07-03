from flask import Flask, render_template, flash, request, redirect, url_for, current_app
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField, SelectField, BooleanField, SelectMultipleField, IntegerField, PasswordField, FormField, FieldList, DateTimeField, DateField, FloatField
from flask_wtf import FlaskForm
from .__init__ import ArbitraryPasser
from flask_wtf.file import FileField, FileRequired
from traceback import format_exc
from inspect import signature, Signature
import logging
import re
from datetime import datetime, date

log = logging.basicConfig()

class FFF(object):
	def __init__(self, app=None):
		self.app = app
		if app:
			self.init_app(app)

	def init_app(self, app):
		app.config.setdefault('form_template', 'base.html')
		app.teardown_appcontext(self.teardown)
	
	def create_forms(self):
		form_dict = {}
		for rule in current_app.url_map.iter_rules():
			func_name = rule.endpoint
			func = current_app.view_fucntions[func_name]
			form_dict[func_name] = self.create_form(func)
		return form_dict
	
	def create_form(self, func):
		class form_obj(Form):
			pass
		sig = signature(func)
		params = sig.parameters
		for varname in params.keys():
			vartype = params[varname].annotation
			if vartype == int:
				setattr(form_obj, varname, IntegerField(varname+':'))
			elif vartype == str:
				setattr(form_obj, varname, TextField(varname+':'))
			elif vartype == float:
				setattr(form_obj, varname, FloatField(varname+':'))
			elif vartype == bool:
				setattr(form_obj, varname, BooleanField(varname))
			elif vartype == datetime:
				setattr(form_obj, varname, DateTimeField(varname+":"))
			elif vartype == date:
				setattr(form_obj, varname, DateField(varname+":"))
			#elif vartype == list:
			#	# get minor object specifications
			#	minor_func = func_obj.minor_object_list[varname]
			#	# if it's a string, it's the name of the function which means we
			#	# need to dedicate it's own form to it with dynamic buttons, but
			#	# if it's a list, it's a list of options which are predefined, so
			#	# we just slot it into the SubForm like a normal parameter
			#	if type(minor_func) == str:
			#		minor_params = signature(getattr(func_obj, minor_func)).parameters
			#		#structure of buttonlist:
			#		#{'minor_func':[('minor_func_varname','minor_func_var_annotation')]}
			#		buttonlist[minor_func] = [(i, minor_params[i].annotation) for i in minor_params.keys()]
			#	elif type(minor_func) == list:
			#		setattr(form_obj, varname, SelectMultipleField(varname+':', choices=[(i, i) for i in minor_func]))
			else:
				raise ValueError('attr not set: ' + str(vartype))
		return form_obj
