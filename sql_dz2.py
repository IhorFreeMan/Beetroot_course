# -*- coding: utf-8 -*-
"""
Task 1

Joins

Use the sample SQLite database hr.db (same database you used in the previous lesson for homework tasks)

As a solution to HW, create a file named: task1.sql with all SQL queries:



write a query in SQL to display the first name, last name, department number, and department name for each employee
write a query in SQL to display the first and last name, department, city, and state province for each employee
write a query in SQL to display the first name, last name, department number, and department name, for all employees for departments 80 or 40
write a query in SQL to display all departments including those where does not have any employee
write a query in SQL to display the first name of all employees including the first name of their manager
write a query in SQL to display the job title, full name (first and last name ) of the employee, and the difference between the maximum salary for the job and the salary of the employee
write a query in SQL to display the job title and the average salary of employees
write a query in SQL to display the full name (first and last name), and salary of those employees who work in any department located in London
write a query in SQL to display the department name and the number of employees in each department

"""
import sqlite3


def s_department():
    """
    write a query in SQL to display the first name, last name, department number,
    and department name for each employee
    """

    employ = []
    try:
        conn = sqlite3.connect('hr.db')
        res = conn.execute(
            """SELECT e.first_name, e.last_name, d.department_name
            FROM employees e
            INNER JOIN department d ON e.department_id = d.department_id;""")

        for i in res.fetchall():
            employ.append(i)

        conn.close()
        return employ

    except Exception as s:
        return f"Error!! {s}"


def s_location():
    """
    write a query in SQL to display the first and last name, department, city,
    and state province for each employee
    """

    employ = []
    try:
        conn = sqlite3.connect('hr.db')
        res = conn.execute(
            """SELECT e.first_name, e.last_name, d.department_name, l.city, l.state_province
            FROM employees e
            INNER JOIN department d ON e.department_id = d.department_id
            INNER JOIN locations l ON d.location_id = l.location_id
            
            ;""")

        for i in res.fetchall():
            employ.append(i)

        conn.close()
        return employ

    except Exception as s:
        return f"Error!! {s}"



def s_departments():
    """
    write a query in SQL to display the first name, last name,
    department number, and department name, for all employees for departments 80 or 40
    """

    employ = []
    try:
        conn = sqlite3.connect('hr.db')
        res = conn.execute(
            """SELECT e.first_name, e.last_name, ds.department_id, ds.depart_name
            FROM employees e
            INNER JOIN departments ds ON e.department_id = ds.department_id
            WHERE ds.department_id = 80 or ds.department_id = 40

            ;""")

        for i in res.fetchall():
            employ.append(i)

        conn.close()
        return employ

    except Exception as s:
        return f"Error!! {s}"


def all_departments():
    """
    4. write a query in SQL to display all departments including those where does not have any employee
    """

    employ = []
    try:
        conn = sqlite3.connect('hr.db')
        res = conn.execute(
            """SELECT ds.department_id, ds.depart_name
            FROM departments ds 
            ;""")

        for i in res.fetchall():
            employ.append(i)

        conn.close()
        return employ

    except Exception as s:
        return f"Error!! {s}"

if __name__ == '__main__':
    # for i in s_department():
    #     print(i)

    # for i in s_location():
    #     print(i)

    # for i in s_departments():
    #     print(i)

    for i in all_departments():
        print(i)
