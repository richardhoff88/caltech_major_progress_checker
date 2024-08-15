CREATE TABLE Majors (
    major_id INT PRIMARY KEY,
    major_name VARCHAR(255)
);

CREATE TABLE Courses (
    course_id INT PRIMARY KEY,
    course_name VARCHAR(255),
    credits INT
);

CREATE TABLE MajorRequirements (
    requirement_id INT PRIMARY KEY,
    major_id INT,
    course_id INT,
    required_grade CHAR(2),
    FOREIGN KEY (major_id) REFERENCES Majors(major_id),
    FOREIGN KEY (course_id) REFERENCES Courses(course_id)
);

CREATE TABLE Students (
    student_id INT PRIMARY KEY,
    name VARCHAR(255),
    major_id INT,
    FOREIGN KEY (major_id) REFERENCES Majors(major_id)
);

CREATE TABLE Transcripts (
    transcript_id INT PRIMARY KEY,
    student_id INT,
    course_id INT,
    grade CHAR(2),
    FOREIGN KEY (student_id) REFERENCES Students(student_id),
    FOREIGN KEY (course_id) REFERENCES Courses(course_id)
);
