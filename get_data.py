import sqlite3

# database connection
conn = sqlite3.connect('major_requirements.db')
cursor = conn.cursor()

# display all majors
cursor.execute('SELECT * FROM Majors')
majors = cursor.fetchall()
print("Majors:")
for major in majors:
    print(major)

# display courses
cursor.execute('SELECT * FROM Courses')
courses = cursor.fetchall()
print("\nCourses:")
for course in courses:
    print(course)


conn.commit()
conn.close()
