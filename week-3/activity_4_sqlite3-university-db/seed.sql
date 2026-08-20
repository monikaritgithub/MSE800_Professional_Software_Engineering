-- STUDENTS
INSERT INTO student
(NID, F_NAME, L_NAME, B_DATE, ADDRESS, EMAIL_ADDRESS)
VALUES
(1, 'John', 'Doe', '1990-01-01', '123 Main St', 'john.doe@example.com'),
(2, 'Monika', 'Bhandari', '1991-02-03', '124 Main St', 'monika.bhandari@example.com'),
(3, 'Jane', 'Smith', '1992-03-04', '125 Main St', 'jane.smith@example.com'),
(4, 'Michael', 'Johnson', '1993-04-05', '126 Main St', 'michael.johnson@example.com'),
(5, 'Emily', 'Davis', '1994-05-06', '127 Main St', 'emily.davis@example.com');


-- SUBJECTS / COURSES
INSERT INTO SUBJECTS
(SUBJECT_CODE, SUBJECT_UNIT, SUBJECT_UCFS)
VALUES
(101, 3, 4),
(102, 4, 5),
(103, 2, 3);


-- LECTURERS
INSERT INTO LECTURER
(L_ID, L_LASTNAME, L_FIRSTNAME, L_EMAIL, L_ADDRESS)
VALUES
(1, 'Mohammad', 'Norouzifard', 'Norouzifard@example.com', '456 Oak Ave'),
(2, 'Johnson', 'Michael', 'michael.johnson@example.com', '789 Pine Rd');


-- ENROLLMENTS
INSERT INTO ENROLLMENT
(STUDENT_NUM, DATE_OF_ENROLLMENT, SUBJECT_CODE, CGPA)
VALUES
(1, '2023-09-01', 101, 3.5),
(1, '2023-09-01', 102, 3.5),
(2, '2023-09-01', 102, 3.0),
(2, '2023-09-01', 103, 3.0),
(3, '2023-09-01', 103, 3.8),
(4, '2023-09-01', 101, 3.2),
(5, '2023-09-01', 102, 3.7);


-- LECTURES
INSERT INTO Lecture
(CCA, Lecture_name, Lecturer_ID, Subject_Code, Date, Time)
VALUES
(1, 'Introduction to Programming', 1, 101, '2023-09-01', '10:00 AM'),
(2, 'Data Structures', 2, 102, '2023-09-02', '11:00 AM'),
(3, 'Database Systems', 1, 103, '2023-09-03', '12:00 PM'),
(4, 'Operating Systems', 2, 101, '2023-09-04', '01:00 PM'),
(5, 'Computer Networks', 1, 102, '2023-09-05', '02:00 PM');