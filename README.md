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

`flask_fff` will take this and transform it right into a basic html form.

# `COMING SOON`
