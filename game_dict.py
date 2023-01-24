# -*- coding: utf-8 -*-
price_list = {
    "apple": 12.99,
    "orange": 14.99,
    "cherry": 26.25,
}

# product  ->  quantity
shopping_list = {}

shopping_list["orange"] = 3
shopping_list["cherry"] = 5
shopping_list["apple"] = 10

transaction = False
cart = {}

for kay in shopping_list:
    total_price = price_list.get(kay) * shopping_list.get(kay)
    cart[kay] = [shopping_list.get(kay), total_price]

# Після покупки
transaction = True
if transaction:
    print("check: \n")
    for key, value in cart.items():
        print(f"article: {key} amount: {value[0]} total price: {value[1]}\n")
