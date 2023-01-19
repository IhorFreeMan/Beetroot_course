# -*- coding: utf-8 -*-

"""
За допомогою циклу while, написати програму, що знаходить факторіал числа N.
Програма повинна починатися з рядка:
n = ...  # n is unsigned positive integer (n > 0)

"""

n = int(input("Введіть число -  "))
result = 1
i = 1

if n > 0:
    while i <= n:
        result = result * i
        i += 1

    print(n, '! = ', result, sep="")

else:
    print("n is unsigned positive integer (n > 0)")
