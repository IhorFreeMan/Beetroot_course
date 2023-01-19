# -*- coding: utf-8 -*-


month = input("Введіть місяць вашого народження: ")  # Any value

month = int(month)

if month == 1 or month == 2 or month == 12:
    print("Ви народились зимою")

elif month == 3 or month == 4 or month == 5:
    print("Ви народились висною")

elif month == 6 or month == 7 or month == 8:
    print("Ви народились літом")

elif month == 9 or month == 10 or month == 11:
    print("Ви народились осінню")
else:
    print("Існує лише 12 місяців")
