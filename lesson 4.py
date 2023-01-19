# -*- coding: utf-8 -*-
import random

"""
Task 1

The Guessing Game.

Write a program that generates a random number between 1 and 10 and lets the user guess what number was generated. The result should be sent back to the user via a print statement.

"""


def guessing_game():
    """The Guessing Game."""
    number_a = random.randrange(1, 10)
    player_number = int(input("Вгадайте число від 1 до 10: "))
    if number_a == player_number:
        print("Ви вгадали число")
    else:
        print(f"Ви не вгадали, це було число {number_a}")


"""
Task 2

The birthday greeting program.

Write a program that takes your name as input, and then your age as input and greets you with the following:

“Hello <name>, on your next birthday you’ll be <age+1> years”   
"""


def birthday_greeting():
    """The birthday greeting program."""
    your_name = input("Введи своє ім`я: ")
    your_age = int(input("Скільки тобі років: "))
    print(f"Hello {your_name}, on your next birthday you’ll be {your_age + 1} years")


"""
Task 3

Words combination

Create a program that reads an input string and then creates and prints 5 random strings from characters of the input string.

For example, the program obtained the word ‘hello’, so it should print 5 random strings(words) that combine characters 
"""


def words_combination():
    """Words combination"""
    random_word = input("Введи слово: ")
    len_random_word = len(random_word)
    result = []
    for i in range(5):
        word = ''
        for l in range(len_random_word):
            word += random_word[random.randrange(1, len_random_word)]
        result.append(word)

    print(result)


if __name__ == "__main__":
    guessing_game()
    birthday_greeting()
    words_combination()
