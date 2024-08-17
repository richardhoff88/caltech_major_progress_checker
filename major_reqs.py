import sqlite3

# Connect to SQLite database
conn = sqlite3.connect('major_requirements.db')
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

# Insert data into Majors
cursor.execute('''
    INSERT OR IGNORE INTO Majors (major_id, major_name) 
    VALUES (1, 'Computer Science')
''')

# Insert data into Courses
cursor.execute('''
    INSERT OR IGNORE INTO Courses (course_id, course_name, credits) 
    VALUES (1, 'Intro to Programming Methods', 9)
''')

cursor.execute('''
    INSERT OR IGNORE INTO Courses (course_id, course_name, credits) 
    VALUES (2, 'Programming Methods', 9)
''')

# Insert data into MajorRequirements
cursor.execute('''
    INSERT OR IGNORE INTO MajorRequirements (major_id, course_id)
    VALUES (1, 1)
''')

cursor.execute('''
    INSERT OR IGNORE INTO MajorRequirements (major_id, course_id)
    VALUES (1, 2)
''')

conn.commit()
conn.close()
