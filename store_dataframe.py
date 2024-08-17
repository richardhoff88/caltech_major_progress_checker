import sqlite3
import pandas as pd

conn = sqlite3.connect('major_requirements.db')
cursor = conn.cursor()

cursor.execute('SELECT * FROM Majors')
majors = cursor.fetchall()
majors_df = pd.DataFrame(majors, columns=['major_id', 'major_name'])

cursor.execute('SELECT * FROM Courses')
courses = cursor.fetchall()
courses_df = pd.DataFrame(courses, columns=['course_id', 'course_name', 'credits'])

# get major requirements
cursor.execute('''
    SELECT major_id, course_id
    FROM MajorRequirements
''')
major_requirements = cursor.fetchall()
major_requirements_df = pd.DataFrame(major_requirements, columns=['major_id', 'course_id'])

merged_df = pd.merge(major_requirements_df, majors_df, on='major_id')
final_df = pd.merge(merged_df, courses_df, on='course_id')
final_df = final_df[['major_name', 'course_name', 'credits']]

final_df = final_df.drop_duplicates()

print (final_df)
conn.close()
