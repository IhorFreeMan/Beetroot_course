# -*- coding: utf-8 -*-

""" Task 1 """


def gypsy_queen(some_str):
    """ String manipulation """

    some_str = str(some_str)
    len_some_str = len(some_str)

    # Якщо строчка рівна чи білша 4-х
    if len_some_str >= 4:
        result = some_str[:2] + some_str[-2:]

    # Якщо строчка рівна 2-м
    elif len_some_str == 2:
        result = some_str + some_str

    # Якщо строчка менша 2-х
    elif len_some_str == 1:
        result = ""

    else:
        result = some_str

    return result


""" Task 2 """


def checks_phone_number(number):
    """The valid phone number program"""

    number = str(number)
    len_number = len(number)

    if number.isdigit() and len_number == 10:
        result = f"{number} - the phone number is correct"
    else:
        result = f"{number} - the phone number is not valid"

    return result


""" Task 3 """

import random


def math_quiz_program():
    """The math quiz program"""
    number_a = random.randrange(1, 10)
    number_b = random.randrange(1, 10)

    print("answer the expression")
    result = number_a + number_b
    answer = int(input(f"{number_a} + {number_b} = "))
    if answer == result:
        print("Correct answer")
    else:
        print("Sorry, the answer is not correct")
        print(f"Correct answer {result}")
    return 0


"""Task 4"""


def name_check(name):
    """The name check"""
    name = str(name)
    name = name.lower()

    print("The program should compare with the saved")
    name_verify = str(input("input name to verify: "))

    if name == name_verify.lower():
        print("Correct")
    else:
        print("Not correct")


if __name__ == "__main__":
    print(gypsy_queen("helloworld"))
    print(gypsy_queen("my"))
    print(gypsy_queen("x"))
    print(checks_phone_number('0600123456'))
    math_quiz_program()
    name_check("Ihor")
