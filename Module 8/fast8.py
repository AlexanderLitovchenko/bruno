from peewee import *

conn = SqliteDatabase('db1.sqlite')

class Students(Model):

	id = IntegerField(column_name = 'id', unique = True)
	name = CharField(column_name = 'name')
	surname = CharField(column_name = 'surname')
	age = IntegerField(column_name = 'age')
	city = CharField(column_name = 'city')

	class Meta:
		database = conn


class Courses(Model):
	
	id = PrimaryKeyField(column_name = 'id', unique = True)
	name = CharField(column_name = 'name')
	time_start = CharField(column_name = 'time_start')
	time_end = CharField(column_name = 'time_end')

	class Meta:
		database = conn


class StudentCourses(Model):

	student_id = ForeignKeyField(Students, column_name = 'student_id')
	course_id = ForeignKeyField(Courses, column_name = 'course_id', )

	class Meta:
		database = conn

Students.create_table()
Courses.create_table()
StudentCourses.create_table()

students = [
{ 'id': 1, 'name':'Max', 'surname':'Brooks', 'age': 24, 'city':'Spb'},
{'id': 2, 'name':'John', 'surname':'Stones', 'age': 15, 'city':'Spb'},
{'id': 3, 'name':'Andy', 'surname':'Wings', 'age': 45, 'city':'Manchester'},
{'id': 4, 'name':'Kate', 'surname':'Brooks', 'age': 34, 'city':'Spb'}
]

courses = [
{'id':1, 'name':'python', 'data_start':'21.07.21', 'data_end':'21.08.21'},
{'id':2, 'name':'java', 'data_start':'13.07.21', 'data_end':'16.08.21'}
]

student_courses = [
{ 'student_id': 1, 'course_id': 1},
{ 'student_id': 2, 'course_id': 1},
{ 'student_id': 3, 'course_id': 1},
{ 'student_id': 4, 'course_id': 2}
]

Students.insert_many(students).execute()
Courses.insert_many(courses).execute()
StudentCourses.insert_many(student_courses).execute()

for student in students_more30:
	print(student.name, end = ' ')
print('\n')

for student in students_python:
	print(student.name, end = ' ')
print('\n')

for student in students_python_spb:
	print(student.name, end = ' ')
print('\n')
conn.close()