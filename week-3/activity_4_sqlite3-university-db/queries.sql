-- Question 1: How many students are registered in each course?

-- LEFT JOIN keeps a course in the result even if
-- no students are enrolled in that course.

SELECT
    s.SUBJECT_CODE,
    COUNT(e.STUDENT_NUM) AS Registered_Students
FROM SUBJECTS s
LEFT JOIN ENROLLMENT e
    ON s.SUBJECT_CODE = e.SUBJECT_CODE
GROUP BY s.SUBJECT_CODE;


-- Question 2: List names and IDs of students
-- enrolled in more than 1 course.

-- HAVING filters the grouped results after COUNT().

SELECT
    s.NID AS Student_ID,
    s.F_NAME || ' ' || s.L_NAME AS Full_Name,
    COUNT(e.SUBJECT_CODE) AS Enrolled_Courses_Count
FROM student s
JOIN ENROLLMENT e
    ON s.NID = e.STUDENT_NUM
GROUP BY s.NID, s.F_NAME, s.L_NAME
HAVING COUNT(e.SUBJECT_CODE) > 1;
