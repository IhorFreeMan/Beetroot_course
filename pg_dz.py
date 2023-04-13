# -*- coding: utf-8 -*-
import psycopg2


def search_managers():
    """
    5 write a query in SQL to display the first name of all employees including the first name of their manager
    """
    employ = []
    try:
        # Connect to your postgres DB
        conn = psycopg2.connect(host="3.71.99.74", port=5433, database="hr", user="postgres", password="RootBeet-101")

        # Open a cursor to perform database operations
        cur = conn.cursor()

        # Execute a query
        cur.execute("""SELECT
         e.c2 AS employee_first_name, 
         m.c2 AS manager_first_name
         FROM employees e
         LEFT JOIN employees m ON e.c10 = m.c1;
         
         """)

        for i in cur.fetchall():
            employ.append(i)

        cur.close()
        return employ
    except Exception as s:
        return f"Error!! {s}"


def search_job_title():
    """
    6 write a query in SQL to display the job title, full name (first and last name ) of the employee,
    and the difference between the maximum salary for the job and the salary of the employee
    """
    employ = []
    try:
        # Connect to your postgres DB
        conn = psycopg2.connect(host="3.71.99.74", port=5433, database="hr", user="postgres", password="RootBeet-101")

        # Open a cursor to perform database operations
        cur = conn.cursor()

        # Execute a query
        cur.execute("""
        SELECT 
        j.job_title, 
        CONCAT(e.c2, ' ', e.c3) AS full_name, 
        (j.max_salary - e.c8) AS salary_diff
        FROM employees e
        JOIN jobs j ON e.c7= j.job_id;
         """)

        for i in cur.fetchall():
            employ.append(i)

        cur.close()
        return employ
    except Exception as s:
        return f"Error!! {s}"



if __name__ == '__main__':
    # for i in search_managers():
    #     print(i)

    for i in search_job_title():
        print(i)
