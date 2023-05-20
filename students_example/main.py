"""
Q1. Retrieve the count of students in each course from the student_performance table, ordered by the course count in descending order.

Q2. Retrieve the average grade for each student from the student_performance table, ordered by the average grade in descending order.

Q3. Retrieve the student's first name, last name, and the number of courses they have taken, considering only students who have taken more than 3 courses, from the student and student_performance tables, ordered by the number of courses in descending order.

Q4. Retrieve the average grade for each course, considering only courses with an average grade above 80, from the student_performance table, ordered by the average grade in descending order.

Q5. Retrieve the student's first name, last name, and the course in which they scored the maximum grade, from the student and student_performance tables, ordered by the student's last name.
"""

import mysql.connector as mysql
import pandas as pd


def get_ordered_students_by_courses(conn):
    """Retrieve the count of students in each course from the student_performance table, ordered by the course count in descending order."""
    
    query = """SELECT
                    sp_course AS Course,
                    COUNT(s_id) AS Students
                FROM
                    student_performance
                GROUP BY
                    Course
                ORDER BY
                    Students DESC"""
    
    return pd.read_sql(query, conn)


def get_students_average_grades(conn):
    """Retrieve the average grade for each student from the student_performance table, ordered by the average grade in descending order."""
    
    query = """SELECT
                    CONCAT(s_lastname, CONCAT(' ', s_firstname)) AS Student,
                    AVG(sp_grade) AS AverageGrade
                FROM
                    student INNER JOIN student_performance USING (s_id)
                GROUP BY
                    Student
                ORDER BY
                    AverageGrade DESC"""
    
    return pd.read_sql(query, conn)
    

def get_students_taken_courses(conn):
    """Retrieve the student's first name, last name, and the number of courses they have taken, considering only students who have taken more than 3 courses, from the student and student_performance tables, ordered by the number of courses in descending order."""
    
    query = """SELECT
                    CONCAT(s_lastname, CONCAT(' ', s_firstname)) AS Student,
                    COUNT(sp_id) AS Courses
                FROM
                    student INNER JOIN student_performance USING (s_id)
                GROUP BY
                    Student
                HAVING
                    Courses > 3
                ORDER BY
                    Courses DESC"""
    
    return pd.read_sql(query, conn)
    

def get_courses_average_grades(conn):
    """Retrieve the average grade for each course, considering only courses with an average grade above 80, from the student_performance table, ordered by the average grade in descending order."""

    query = """SELECT
                    sp_course AS Course,
                    AVG(sp_grade) AS AverageGrade
                FROM
                    student_performance
                GROUP BY
                    Course
                HAVING
                    AverageGrade > 80
                ORDER BY
                    AverageGrade DESC"""
    
    return pd.read_sql(query, conn)


def get_students_max_grades(conn):
    """Retrieve the student's first name, last name, and the course in which they scored the maximum grade, from the student and student_performance tables, ordered by the student's last name."""
    
    query = """SELECT
                    CONCAT(s_lastname, CONCAT(' ', s_firstname)) AS Student,
                    sp_course AS Course,
                    sp_grade AS Grade
                FROM
                    student INNER JOIN student_performance as main_sp USING (s_id)
                WHERE
                    sp_grade = (SELECT
                                MAX(sp_grade)
                            FROM
                                student_performance
                            WHERE
                                s_id = main_sp.s_id)
                ORDER BY
                    Student"""
    
    return pd.read_sql(query, conn)


def main():
    conn = mysql.connect(
        host="localhost",
        database="students_example",
        user="root",
        password=""
    )

    df_list = []
    df_list.append(get_ordered_students_by_courses(conn))
    df_list.append(get_students_average_grades(conn))
    df_list.append(get_students_taken_courses(conn))
    df_list.append(get_courses_average_grades(conn))
    df_list.append(get_students_max_grades(conn))
    
    for num in range(0, len(df_list)):
        df_list[num].to_csv(f"output/query{num + 1}.csv")


if __name__ == "__main__":
    main()
