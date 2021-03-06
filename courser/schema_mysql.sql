CREATE TABLE IF NOT EXISTS User (
    id INTEGER PRIMARY KEY AUTO_INCREMENT,
    username CHAR(60) UNIQUE NOT NULL,
    password TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS Role (
    id INTEGER PRIMARY KEY AUTO_INCREMENT,
    name CHAR(60) UNIQUE NOT NULL,
    description TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS UserRole (
    user_id INTEGER NOT NULL REFERENCES User(id),
    role_id INTEGER NOT NULL REFERENCES Role(id),
    PRIMARY KEY (user_id, role_id)
);

CREATE TABLE IF NOT EXISTS Student (
    id INTEGER PRIMARY KEY AUTO_INCREMENT,
    name TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS Course (
    id INTEGER PRIMARY KEY AUTO_INCREMENT,
    title TEXT NOT NULL,
    credits INTEGER NOT NULL,
    description TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS Teacher (
    id INTEGER PRIMARY KEY AUTO_INCREMENT,
    name TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS Section (
    id INTEGER PRIMARY KEY AUTO_INCREMENT,
    course_id INTEGER NOT NULL REFERENCES Course(id),
    teacher_id INTEGER NOT NULL References Teacher(id)
);

CREATE TABLE IF NOT EXISTS Enrolment (
    student_id INTEGER REFERENCES User(id),
    section_id INTEGER REFERENCES Section(id),
    grade      NUMERIC NOT NULL,
    PRIMARY KEY (student_id, section_id)
);