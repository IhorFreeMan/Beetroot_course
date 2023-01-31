# -*- coding: utf-8 -*-

"""
Task 1

Write a function called oops that explicitly raises an IndexError exception when called.
Then write another function that calls oops inside a try/except state­ment to catch the error.
What happens if you change oops to raise KeyError instead of IndexError?
"""


def oops():
    m = [1, 2, 3]
    return m[3]


"""
Task 2

Write a function that takes in two numbers from the user via input(), 
call the numbers a and b, and then returns the value of squared a divided by b, 
construct a try-except block which raises an exception if the two values given by the input function were not numbers,
and if value b was zero (cannot divide by zero).    
"""


def my_exeptions():
    a = int(input(">>> "))
    b = int(input(">>> "))
    result = a**2 / b
    return result



if __name__ == "__main__":
    print("\nTask 1")
    try:
        print(oops())
    except IndexError:
        print("oops")
    # except KeyError:
    #     print("oops")
    print("\nTask 2")

    try:
        print(my_exeptions())
    except ZeroDivisionError:
        print("Не можна ділити на 0")
    except ValueError:
        print("Ви не ввели змінну")
    finally:
        print("my_exeptions відпрацювала")

