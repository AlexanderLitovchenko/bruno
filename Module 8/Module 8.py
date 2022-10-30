import sqlite3 

conn = sqlite3.connect('database.sqlite')
cursor = conn.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS Students (id INT PRIMARY KEY, name Varchar(32), surname Varchar(32), age INT, city Varchar(32))")
cursor.execute("CREATE TABLE IF NOT EXISTS Courses (id INT PRIMARY KEY, name Varchar(32), time_start Varchar(32), time_end  Varchar(32))")

cursor.executemany("INSERT INTO Students (id, name, surname, age, city) VALUES (?, ?, ?, ?, ?)", 
[(1, 'Max', 'Brooks', 24, 'Spb'),
 (2,'John','Stones', 15,'Spb'),
 (3, 'Andy', 'Wings', 45, 'Manhester'),
 (4, 'Kate', 'Brooks', 34, 'Spb')])

cursor.executemany('''INSERT INTO Courses VALUES (?, ?, ?, ?)''',
[(1, 'python', '21.07.21', '21.08.21'),
(2, 'java', '13.07.21', '16.08.21')])

cursor.execute("CREATE TABLE IF NOT EXISTS Student_courses (student_id INT, course_id INT, FOREIGN KEY(student_id) REFERENCES Students(id), FOREIGN KEY(course_id) REFERENCES Courses(id))")
cursor.executemany('''INSERT INTO Student_courses VALUES (?, ?)''',
[(1, 1), (2, 1), (3, 1), (4, 2)])

conn.commit()

students_more30 = cursor.execute("SELECT name, surname, age FROM Students WHERE age > 30").fetchall()
print(students_more30)

students_python = cursor.execute('''SELECT Students.name, Courses.name 
									FROM Students, Courses, Student_Courses 
									WHERE (Student_courses.course_id) = 1 
									AND (Student_courses.course_id = courses.id) 
									AND (Student_courses.student_id = students.id)''').fetchall()
print(students_python)

students_python_spb = cursor.execute('''SELECT Students.name, Courses.name, Students.city 
									FROM Students, Courses, Student_Courses 
									WHERE (Student_courses.course_id) = 1 
									AND (Student_courses.course_id = courses.id) 
									AND (Student_courses.student_id = students.id)
									AND (Students.city = 'Spb') ''').fetchall()
print(students_python_spb)
