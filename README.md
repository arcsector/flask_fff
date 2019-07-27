# Flask - Form Follows Function
Flask - Form Follows Function is a module that allows you to create forms directly from python functions.

# Installation
Install with:
```bash
git clone https://github.com/arcsector/flask_fff
cd flask_fff/
sudo python3 setup.py install
```

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

`flask_fff` will take this and transform it right into a basic wtform with a few small modifications, so that you can just drop it into your html template and go.

First we initialize the class from our flask app:
```python
from flask import Flask
from flask_fff import fff

app = Flask(__name__)

# initializing flask_fff
FFF = fff(app)

@app.route('/', methods=['GET','POST'])
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
