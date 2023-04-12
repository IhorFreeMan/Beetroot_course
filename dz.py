# -*- coding: utf-8 -*-

"""
Task 1

Create a table

Create a table of your choice inside the sample SQLite database, rename it, and add a new column. Insert
 a couple rows inside your table. Also, perform UPDATE and DELETE statements on inserted rows.

As a solution to this task, create a file named: task1.sql, with all the SQL statements
you have used to accomplish this task


"""
import sqlite3


def test_sql():
    conn = sqlite3.connect('task1')

    cur = conn.cursor()
    cur.execute("CREATE TABLE COMPANY(topic_id, topic_name)")

    conn.execute("INSERT INTO COMPANY (topic_id, topic_name) VALUES (1,'классика');")
    conn.execute("INSERT INTO COMPANY (topic_id, topic_name) VALUES (2,'лірика');")
    conn.commit()

    conn.execute("UPDATE COMPANY SET topic_name = ? WHERE topic_id = ?", ('музика', 2))
    conn.commit()

    conn.execute("DELETE FROM COMPANY WHERE topic_id = ?", (2,))
    conn.commit()

    res = conn.execute("SELECT * FROM COMPANY")

    print(res.fetchall())

    conn.close()


"""
Task 2

Select queries

Use the sample SQLite database hr.db

SQLite database hr.db link:
"""


def show_tables():
    """ показати назви таблиць"""
    tables = []
    # підключаємося до бази даних
    conn = sqlite3.connect('hr.db')

    # виконуємо запит до системної таблиці
    cursor = conn.execute("SELECT name FROM sqlite_master WHERE type='table';")

    # виводимо список назв таблиць
    for row in cursor:
        tables.append(row[0])

    # закриваємо з'єднання з базою даних
    conn.close()
    return tables


def add_user(name: str, email: str):
    try:
        conn = sqlite3.connect('hr.db')
        conn.execute("INSERT INTO USERS (NAME, EMAIL) VALUES (?,?);", (name, email))
        conn.commit()
        conn.close()
        return f"Додано: {name}, {email}"
    except Exception as s:
        return f"Error!! {s}"


def show_users():
    users = []
    conn = sqlite3.connect('hr.db')

    res = conn.execute("SELECT * FROM USERS")

    for i in res.fetchall():
        users.append(i)

    conn.close()
    return users


def update_user(mail: str, name: str):
    try:
        conn = sqlite3.connect('hr.db')
        conn.execute("UPDATE USERS SET email= ? WHERE name = ?", (mail, name))
        conn.commit()
        return f"Змінено: {mail} за імям {name}"
    except Exception as s:
        return f"Error!! {s}"


def delete_user(name):
    try:
        conn = sqlite3.connect('hr.db')
        conn.execute("DELETE FROM USERS WHERE name = ?", (name,))
        conn.commit()
        return f"Видалено юзераза імям {name}"
    except Exception as s:
        return f"Error!! {s}"


def employees(first_name):
    """
    write a query to display the names (first_name, last_name) using alias name "First Name",
    "Last Name" from the table of employees;
    """
    employ = []
    try:
        conn = sqlite3.connect('hr2.db')
        res = conn.execute("SELECT first_name, last_name FROM employees WHERE first_name = ?", (first_name,))
        for i in res.fetchall():
            employ.append(i)
        conn.close()
        return employ

    except Exception as s:
        return f"Error!! {s}"


def department_id_employee(department_id):
    """write a query to get the unique department ID from the employee table"""
    employ = []
    try:
        conn = sqlite3.connect('hr2.db')
        res = conn.execute("SELECT first_name, last_name FROM employees WHERE department_id = ?", (department_id,))
        for i in res.fetchall():
            employ.append(i)
        conn.close()
        return employ

    except Exception as s:
        return f"Error!! {s}"

def sort_ful_name():
    """
    write a query to get all employee details from the employee table ordered by first name, descending
    """
    employ = []
    try:
        conn = sqlite3.connect('hr2.db')
        res = conn.execute("SELECT * FROM employees ORDER BY first_name DESC")
        for i in res.fetchall():
            employ.append(i)
        conn.close()
        return employ

    except Exception as s:
        return f"Error!! {s}"


def sort_pf():
    """
    write a query to get the names (first_name, last_name), salary, PF of all the employees
    (PF is calculated as 12% of salary)
    """
    employ = []
    try:
        conn = sqlite3.connect('hr2.db')
        res = conn.execute("SELECT first_name, last_name, salary, salary * 0.12 AS PF FROM employees;")
        for i in res.fetchall():
            employ.append(i)
        conn.close()
        return employ

    except Exception as s:
        return f"Error!! {s}"

def salary_max_min():
    """
    write a query to get the maximum and minimum salary from the employees table
    """
    employ = []
    try:
        conn = sqlite3.connect('hr2.db')
        res = conn.execute("SELECT MAX(salary) AS max_salary, MIN(salary) AS min_salary FROM employees;")
        for i in res.fetchall():
            employ.append(i)
        conn.close()
        return employ

    except Exception as s:
        return f"Error!! {s}"



def monthly_salary():
    """
    write a query to get a monthly salary (round 2 decimal places) of each and every employee
    """
    employ = []
    try:
        conn = sqlite3.connect('hr2.db')
        res = conn.execute("SELECT first_name, last_name, ROUND(salary / 12.0, 2) AS monthly_salary FROM employees;")
        for i in res.fetchall():
            employ.append(i)
        conn.close()
        return employ

    except Exception as s:
        return f"Error!! {s}"

if __name__ == '__main__':
    # print(f"{20 * '_'}\nTask 1\n")
    # test_sql()
    print(f"{20 * '_'}\nTask 2\n")
    # print(show_tables())
    # add_us = add_user("Жора1", "jora@mail.com")
    # print(add_us)
    # print(show_users())
    # print(update_user("jora22@mail.com", "Жора1"))
    # print(delete_user("Жора1"))
    #
    # print(employees("Steven"))
    # print(department_id_employee(100))
    # print(sort_ful_name())
    # for i in sort_ful_name():
    #     print(i)
    # for i in sort_pf():
    #     print(i)
    # print(salary_max_min())
    print(monthly_salary())



