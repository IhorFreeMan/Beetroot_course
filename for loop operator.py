# -*- coding: utf-8 -*-

"""
Task 1

"""


def same_dict(same_str):
    """
    Make a program that has some sentence (a string) on input and returns
     a dict containing all unique words as keys and the number of occurrences as values.
    """
    list_ours_words = same_str.split(" ")
    list_ours_words = list(filter(None, list_ours_words))  # прибираємо пусті строки

    len_list_ours_words = len(list_ours_words)

    dict_words = {}
    # створюємо словарь з наших слів (or dict.fromkeys(list_ours_words, 0))
    for i in range(len_list_ours_words):
        dict_words[list_ours_words[i]] = 0

    # рахуємо кількість повторень слів
    for i in range(len_list_ours_words):
        # якщо елемент в словнику додаємо 1
        if list_ours_words[i] in dict_words:
            dict_words[list_ours_words[i]] += 1

    return dict_words


"""
Task 2

"""


def business_logic(stock_dict, prices_dict):
    """
    Compute the total price of the stock where the total price is
    the sum of the price of an item multiplied by the quantity of this exact item.
    """
    total_price = {}

    for kay, value in stock_dict.items():
        total_price[kay] = stock_dict.get(kay) * prices_dict.get(kay)

    return total_price


if __name__ == "__main__":
    str_words = "hello hello I I    4 4 4  6 6 6 8 8 8"
    print("Task 1", same_dict(str_words))

    stock = {
        "banana": 6,
        "apple": 0,
        "orange": 32,
        "pear": 15
    }
    prices = {
        "banana": 4,
        "apple": 2,
        "orange": 1.5,
        "pear": 3
    }

    print("Task 2", business_logic(stock, prices))
