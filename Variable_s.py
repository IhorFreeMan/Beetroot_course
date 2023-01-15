# -*- coding: utf-8 -*-

""" Task 1 """
from datetime import datetime

my_name = input("Ввиди своє ім'я: ")
date_now = datetime.now()
day = datetime.strptime(str(date_now), '%Y-%m-%d %H:%M:%S.%f').strftime('%A')

print(f"Good day {my_name}! {day} is a perfect day to learn some python.")

""" Task 2 """
first_name = input("Ввиди ім'я: ")
last_name = input("Ввиди прізвище ім'я: ")

print(first_name, last_name, sep=" ")

""" Task 3 """
enter_number_1 = int(input("Введи число 1: "))
enter_number_2 = int(input("Введи число 2: "))

print(enter_number_1 + enter_number_2)    # Addition
print(enter_number_1 - enter_number_2)    # Subtraction
print(enter_number_1 / enter_number_2)    # Division
print(enter_number_1 * enter_number_2)    # Multiplication
print(enter_number_1 ** enter_number_2)   # Exponent (Power)
print(enter_number_1 % enter_number_2)    # Modulus
print(enter_number_1 // enter_number_2)   # Floor division
