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

s1 = Students(id = '1', name = 'Max', surname = 'Brooks', age = '24', city = 'Spb')
s1.save()
s2 = Students(id = '2', name = 'John', surname = 'Stones', age = '15', city = 'Spb')
s2.save()
s3 = Students(id = '3', name = 'Andy', surname = 'Wings', age = '45', city = 'Manchester')
s3.save()
s4 = Students(id = '4', name = 'Kate', surname = 'Brooks', age = '34', city = 'Spb')
s4.save()

c1 = Courses(id = '1', name = 'python', time_start = '21.07.21', time_end = '21.08.21')
c1.save()
c2 = Courses(id = '1', name = 'java', time_start = '13.07.21', time_end = '16.08.21')
c2.save()

sc1 = StudentCourses(student_id = '1', course_id = '1')
sc1.save()
sc2 = StudentCourses(student_id = '2', course_id = '1')
sc2.save()
sc3 = StudentCourses(student_id = '3', course_id = '1')
sc3.save()
sc4 = StudentCourses(student_id = '4', course_id = '2')
sc4.save()

students_more30 = Students.select().where(Students.age > 30)
students_python = Students.select().join(StudentCourses).join(Courses).where(Courses.name == 'python')
students_python_spb = Students.select().join(StudentCourses).join(Courses).where((Courses.name == 'python') and (Students.city == 'Spb'))

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

