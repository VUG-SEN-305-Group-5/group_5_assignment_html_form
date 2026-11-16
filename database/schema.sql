-- ============================================
-- Student Biodata System - Database Schema
-- ICAT Nigeria Phase II Project
-- DBMS: MySQL 8.0
-- ============================================

DROP DATABASE IF EXISTS student_biodata_db;
CREATE DATABASE student_biodata_db;
USE student_biodata_db;


-- --------------------------------------------
-- Table 1: departments
-- stores each department once, students point to it by id
-- --------------------------------------------
CREATE TABLE departments (
    department_id   INT AUTO_INCREMENT PRIMARY KEY,
    department_name VARCHAR(100) NOT NULL UNIQUE,
    faculty         VARCHAR(100) NOT NULL
);


-- --------------------------------------------
-- Table 2: students
-- biodata collected from the form
-- --------------------------------------------
CREATE TABLE students (
    student_id      INT AUTO_INCREMENT PRIMARY KEY,
    matric_no       VARCHAR(20)  NOT NULL UNIQUE,
    first_name      VARCHAR(50)  NOT NULL,
    last_name       VARCHAR(50)  NOT NULL,
    other_name      VARCHAR(50),
    email           VARCHAR(100) NOT NULL UNIQUE,
    phone           CHAR(11)     NOT NULL UNIQUE,
    date_of_birth   DATE         NOT NULL,
    gender          ENUM('Male', 'Female') NOT NULL,
    department_id   INT          NOT NULL,
    level           SMALLINT     NOT NULL,
    state_of_origin VARCHAR(50)  NOT NULL,
    address         VARCHAR(255),
    created_at      TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at      TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,

    CONSTRAINT fk_students_department
        FOREIGN KEY (department_id) REFERENCES departments(department_id)
        ON UPDATE CASCADE
        ON DELETE RESTRICT,

    CONSTRAINT chk_level CHECK (level IN (100, 200, 300, 400, 500)),
    CONSTRAINT chk_phone CHECK (phone REGEXP '^0[0-9]{10}$')
);


-- --------------------------------------------
-- Table 3: user_credentials
-- login details, kept separate from biodata
-- password is stored as a hash, never plain text
-- --------------------------------------------
CREATE TABLE user_credentials (
    credential_id   INT AUTO_INCREMENT PRIMARY KEY,
    student_id      INT          NOT NULL UNIQUE,   -- one login per student
    username        VARCHAR(50)  NOT NULL UNIQUE,
    password_hash   VARCHAR(255) NOT NULL,
    role            ENUM('student', 'admin') NOT NULL DEFAULT 'student',
    is_active       BOOLEAN      NOT NULL DEFAULT TRUE,
    last_login      DATETIME,
    created_at      TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT fk_credentials_student
        FOREIGN KEY (student_id) REFERENCES students(student_id)
        ON UPDATE CASCADE
        ON DELETE CASCADE      -- delete a student, their login goes too
);


-- ============================================
-- Sample data
-- ============================================

INSERT INTO departments (department_name, faculty) VALUES
('Software Engineering',   'Computing'),
('Computer Science',       'Computing'),
('Cyber Security',         'Computing'),
('Information Technology', 'Computing'),
('Data Science',           'Computing');

INSERT INTO students
(matric_no, first_name, last_name, other_name, email, phone, date_of_birth, gender, department_id, level, state_of_origin, address)
VALUES
('VUG/SEN/24/11362', 'Morenikeji', 'Olowo', 'David', 'keji@example.com',   '08012345678', '2005-03-14', 'Male',   1, 300, 'Kaduna', 'Bwari, Abuja'),
('VUG/CSC/24/10421', 'Chioma',     'Okeke', NULL,    'chioma@example.com', '08123456789', '2004-07-22', 'Female', 2, 300, 'Anambra', 'Kubwa, Abuja'),
('VUG/CYB/25/12007', 'Musa',       'Adamu', 'Ibrahim','musa@example.com',  '09034567812', '2006-01-09', 'Male',   3, 200, 'Kano',   NULL);

-- these are bcrypt hashes, not real passwords
INSERT INTO user_credentials (student_id, username, password_hash, role) VALUES
(1, 'keji.olowo',   '$2b$10$Xk9vQe1mF3pRz7LwT2yHUeJb8nC4dA6sG0hK5iM1oP3qR7tU9vW2a', 'admin'),
(2, 'chioma.okeke', '$2b$10$Lm4nB6vC8xZ1aS3dF5gH7jK9lP0oI2uY4tR6eW8qA1sD3fG5hJ7k', 'student'),
(3, 'musa.adamu',   '$2b$10$Qw2eR4tY6uI8oP0aS2dF4gH6jK8lZ1xC3vB5nM7qW9eR1tY3uI5o', 'student');


-- ============================================
-- Test queries (to show the relationships work)
-- ============================================

-- 1. all students with their department name (JOIN on foreign key)
SELECT s.matric_no,
       CONCAT(s.last_name, ' ', s.first_name) AS full_name,
       d.department_name,
       s.level
FROM students s
JOIN departments d ON s.department_id = d.department_id;

-- 2. login info joined with the student it belongs to
SELECT c.username, c.role, c.is_active, s.matric_no, s.email
FROM user_credentials c
JOIN students s ON c.student_id = s.student_id;

-- 3. number of students in each department
SELECT d.department_name, COUNT(s.student_id) AS total_students
FROM departments d
LEFT JOIN students s ON d.department_id = s.department_id
GROUP BY d.department_name;

-- 4. constraint tests - uncomment one at a time, each should FAIL
-- department 99 doesn't exist (foreign key):
-- INSERT INTO students (matric_no, first_name, last_name, email, phone, date_of_birth, gender, department_id, level, state_of_origin)
-- VALUES ('VUG/SEN/24/99999', 'Test', 'User', 'test@example.com', '08000000000', '2005-01-01', 'Male', 99, 300, 'Lagos');

-- duplicate matric number (unique):
-- INSERT INTO students (matric_no, first_name, last_name, email, phone, date_of_birth, gender, department_id, level, state_of_origin)
-- VALUES ('VUG/SEN/24/11362', 'Copy', 'Cat', 'copy@example.com', '08099999999', '2005-01-01', 'Male', 1, 300, 'Lagos');

-- level 350 is not allowed (check):
-- UPDATE students SET level = 350 WHERE student_id = 1;

-- 5. cascade test - deleting a student also deletes their login
-- DELETE FROM students WHERE student_id = 3;
-- SELECT * FROM user_credentials;   -- musa.adamu should be gone
