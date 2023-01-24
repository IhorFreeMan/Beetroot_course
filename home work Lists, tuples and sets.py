# -*- coding: utf-8 -*-
import random

"""
Task 1

The greatest number

Write a Python program to get the largest number from a list of random numbers with the length of 10

Constraints: use only while loop and random module to generate numbers

"""


def greatest_number():
    """greatest number"""

    n = 10
    m = []
    while n >= 1:
        random_number = random.randrange(1, 10)
        m.append(random_number)
        n -= 1

    sorted_numbers = sorted(m)

    return print(f"Найбільше число зі списку {m} це -", sorted_numbers[-1])


"""
Task 2

Exclusive common numbers.

Generate 2 lists with the length of 10 with random integers from 1 to 10, and make a third list containing the common integers between the 2 initial lists without any duplicates.

Constraints: use only while loop and random module to generate numbers
"""


def exclusive_common_numbers():
    """Exclusive common numbers"""
    n = 10
    list_a = []
    list_b = []
    while n >= 1:
        random_number_a = random.randrange(1, 10)
        random_number_b = random.randrange(1, 10)
        list_a.append(random_number_a)
        list_b.append(random_number_b)
        n -= 1

    list_c = list_a + list_b

    result = set(list_c)

    return print(
        f"\nСтворено списоки випадкових чисел \n{list_a} \nта {list_b} \nз них сформовано загальний, без дублів {result}. \n")


"""
Task 3

Extracting numbers.

Make a list that contains all integers from 1 to 100, then find all integers from the list that are divisible by 7 but not a multiple of 5, and store them in a separate list. Finally, print the list.

Constraint: use only while loop for iteration
"""


def extracting_numbers():
    """Extracting numbers."""
    n = 100
    result = []
    while n >= 1:
        if n % 7 == 0 and n % 5 != 0:
             result.append(n)
        n -= 1
    return print(f"\nЧисла, які діляться на 7, але не кратні 5 з діапазону 100:\n {result[::-1]}")





if __name__ == "__main__":
    greatest_number()
    exclusive_common_numbers()
    extracting_numbers()
