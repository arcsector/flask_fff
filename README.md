# Flask - Form Follows Function
Flask - Form Follows Function is a module that allows you to create forms directly from python functions.

# Usage
Take for example the following function; it takes annotated arguments which then returns the class `Student`:
```python
def createStudent(gpa: float, id: int, name: str, start_date: date, is_graduated: bool):
	class Student:
		gpa = gpa
		student_id = id
		name = name
		start_date = start_date
		is_graduated = is_graduated
	return Student
```

`flask_fff` will take this and transform it right into a basic html form with a few small modifications, so that you can just drop it into your app and go. Assuming a directory structure where you cloned the repo into the app, like so:
```
flask_app/
|-- flask_fff/
    |-- flask_fff.py
    |-- README.md
|-- app.py
|-- templates/
    |-- basic.html
```

First we initialize the class from our flask app:
```python
from flask import Flask
from flask_fff import 

app = Flask(__name__)

# initializing flask_fff


def createStudent(gpa: float, id: int, name: str, start_date: date, is_graduated: bool):
	form = 
	class Student:
		gpa = gpa
		student_id = id
		name = name
		start_date = start_date
		is_graduated = is_graduated
	return Student
```
We can directly put `createStudent` into `basic.html` without doing any form class defining:
