import sqlite3

# Connect to SQLite database
conn = sqlite3.connect('major_req_updated.db')
cursor = conn.cursor()

# Create tables
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Majors (
        major_id INTEGER PRIMARY KEY,
        major_name TEXT
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS Courses (
        course_id INTEGER PRIMARY KEY,
        course_name TEXT,
        credits INTEGER
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS MajorRequirements (
        requirement_id INTEGER PRIMARY KEY,
        major_id INTEGER,
        course_id INTEGER,
        FOREIGN KEY (major_id) REFERENCES Majors(major_id),
        FOREIGN KEY (course_id) REFERENCES Courses(course_id)
    )
''')

# insert to major
cursor.execute('''
    INSERT OR IGNORE INTO Majors (major_id, major_name) 
    VALUES (1, 'Computer Science')
''')

cursor.execute('''
    INSERT OR IGNORE INTO Courses (course_id, course_name, credits) 
    VALUES (1, 'CS 1', 9)
''')
cursor.execute('''
    INSERT OR IGNORE INTO Courses (course_id, course_name, credits) 
    VALUES (2, 'CS 1X', 9)
''')
cursor.execute('''
    INSERT OR IGNORE INTO Courses (course_id, course_name, credits) 
    VALUES (3, 'CS 2', 9)
''')
cursor.execute('''
    INSERT OR IGNORE INTO Courses (course_id, course_name, credits) 
    VALUES (4, 'CS 3', 9)
''')
cursor.execute('''
    INSERT OR IGNORE INTO Courses (course_id, course_name, credits) 
    VALUES (5, 'CS 4', 9)
''')

cursor.execute('''
    INSERT OR IGNORE INTO Courses (course_id, course_name, credits) 
    VALUES (6, 'CS 21', 9)
''')
cursor.execute('''
    INSERT OR IGNORE INTO Courses (course_id, course_name, credits) 
    VALUES (7, 'CS 24', 9)
''')
cursor.execute('''
    INSERT OR IGNORE INTO Courses (course_id, course_name, credits) 
    VALUES (8, 'CS 38', 9)
''')

# Insert Major Requirements for CS fundamental courses
cursor.execute('''
    INSERT OR IGNORE INTO MajorRequirements (major_id, course_id)
    VALUES (1, 1)
''')
cursor.execute('''
    INSERT OR IGNORE INTO MajorRequirements (major_id, course_id)
    VALUES (1, 2)
''')
cursor.execute('''
    INSERT OR IGNORE INTO MajorRequirements (major_id, course_id)
    VALUES (1, 3)
''')
cursor.execute('''
    INSERT OR IGNORE INTO MajorRequirements (major_id, course_id)
    VALUES (1, 4)
''')
cursor.execute('''
    INSERT OR IGNORE INTO MajorRequirements (major_id, course_id)
    VALUES (1, 5)
''')

# Insert Major Requirements for Intermediate CS courses
cursor.execute('''
    INSERT OR IGNORE INTO MajorRequirements (major_id, course_id)
    VALUES (1, 6)
''')
cursor.execute('''
    INSERT OR IGNORE INTO MajorRequirements (major_id, course_id)
    VALUES (1, 7)
''')
cursor.execute('''
    INSERT OR IGNORE INTO MajorRequirements (major_id, course_id)
    VALUES (1, 8)
''')



conn.commit()
conn.close()
