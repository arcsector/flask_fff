from flask import Flask, render_template, flash, request, redirect, url_for, send_file, g, session
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField, SelectField, BooleanField, SelectMultipleField, IntegerField, PasswordField, FormField, FieldList
from flask_wtf import FlaskForm
from .__init__ import ArbitraryPasser
from flask_wtf.file import FileField, FileRequired
from traceback import format_exc
from inspect import signature, Signature
import logging
import re

log = logging.basicConfig()

#=============== DEF FORM CLASSES ===============#
class SubForm(Form):
	placeholder = TextField()

class CreateBaseForm(Form):
	object_type = SelectField("Please fill out the form:", choices=list(ArbitraryPasser.keys()), validators=[validators.required()])
	object_form = FormField(SubForm)

def updatesubform(form_obj, func_obj, function_name) -> dict:
	if 'placeholder' in dir(form_obj):
		del form_obj.placeholder
	buttonlist = {}
	create_function = func_obj
	sig = signature(create_function)
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
			log('attr not set: ' + str(vartype))
	#print(buttonlist)
	return buttonlist

#def createminorform(stix_obj, function_name):
#	global MinorForm
#	MinorForm = type('MinorForm', (Form,), {})
#	buttonlist = updatesubform(MinorForm, stix_obj, function_name)
#	if buttonlist:
#		print("there's more buttons ya idiot: {}".format(buttonlist))
#

def createsubform(object_typ, func_obj):
    creation_function_name = object_typ
	btnlist = updatesubform(SubForm, func_obj, creation_function_name)
	#session['buttonlist'] = btnlist
	setattr(CreateStix1Form, 'object_form', FormField(SubForm))
	form = CreateBaseForm(request.form)
	return btnlist, form

def CreateForm():
    form = CreateBaseForm(request.form)
    if request.method == 'POST':
        object_typ = request.form['object_type']
        btnlist, form = createsubform(object_typ, ArbitraryPasser.func_dict[object_typ])
        return render_template("base.html", form=form)
    return render_template("base.html", form=form)