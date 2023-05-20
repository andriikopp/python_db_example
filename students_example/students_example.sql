DROP DATABASE IF EXISTS students_example;
CREATE DATABASE students_example;

USE students_example;

CREATE TABLE student (
	s_id INT AUTO_INCREMENT PRIMARY KEY,
	s_firstname VARCHAR(100) NOT NULL,
	s_lastname VARCHAR(100) NOT NULL,
	s_email VARCHAR(255) NOT NULL,
	s_phonenum VARCHAR(20) NOT NULL,
	s_birthdate DATE NOT NULL
);

CREATE TABLE student_performance (
	sp_id INT AUTO_INCREMENT PRIMARY KEY,
	s_id INT NOT NULL,
	sp_course VARCHAR(100) NOT NULL,
	sp_grade INT NOT NULL,
	sp_timestamp DATETIME NOT NULL,
	CHECK (sp_grade >= 0 AND sp_grade <= 100),
	FOREIGN KEY (s_id) REFERENCES student(s_id)
);

INSERT INTO student (s_firstname, s_lastname, s_email, s_phonenum, s_birthdate) VALUES
('John', 'Doe', 'johndoe@example.com', '1234567890', '1995-07-15'),
('Jane', 'Smith', 'janesmith@example.com', '9876543210', '1998-03-21'),
('Michael', 'Johnson', 'michaeljohnson@example.com', '5555555555', '1997-09-10'),
('Emily', 'Williams', 'emilywilliams@example.com', '1111111111', '1996-12-05'),
('David', 'Brown', 'davidbrown@example.com', '9999999999', '1999-08-29');

INSERT INTO student_performance (s_id, sp_course, sp_grade, sp_timestamp) VALUES
(1, 'Math', 80, '2023-04-01 09:00:00'),
(1, 'Science', 90, '2023-04-02 10:30:00'),
(2, 'English', 85, '2023-04-03 14:15:00'),
(3, 'Math', 95, '2023-04-04 11:45:00'),
(3, 'History', 75, '2023-04-05 13:30:00'),
(4, 'Science', 88, '2023-04-06 10:00:00'),
(4, 'Math', 92, '2023-04-07 11:30:00'),
(4, 'English', 78, '2023-04-08 13:15:00'),
(5, 'History', 83, '2023-04-09 14:45:00'),
(5, 'Science', 91, '2023-04-10 12:30:00'),
(2, 'Math', 87, '2023-04-11 09:45:00'),
(2, 'Science', 76, '2023-04-12 11:00:00'),
(1, 'English', 84, '2023-04-13 14:30:00'),
(3, 'History', 79, '2023-04-14 10:15:00'),
(4, 'Science', 93, '2023-04-15 12:45:00'),
(5, 'Math', 86, '2023-04-16 09:30:00'),
(2, 'English', 81, '2023-04-17 11:45:00'),
(1, 'Science', 89, '2023-04-18 14:00:00'),
(4, 'History', 82, '2023-04-19 10:45:00'),
(3, 'Math', 94, '2023-04-20 12:00:00');
