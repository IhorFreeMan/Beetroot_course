# -*- coding: utf-8 -*-


"""
Task 1

Write a Python program to detect the number of local variables declared in a function.
"""


def h(x: list) -> list:
    a = "a"
    b = []
    c = {}
    n = [a, b, c, x]
    return n


def y(x: list) -> list:
    a = "a"
    b = []
    c = {}
    n = [a, b, c, x]
    return locals()


"""
Task 2

Write a Python program to access a function inside a function (Tips: use function, which returns another function)
"""


def function_1():
    print("I am 'function_1'")

    def function_2():
        print("I am 'function_2'")

    return function_2()


"""
Task 3

Write a function called `choose_func` which takes a list of nums and 2 callback functions. 
If all nums inside the list are positive, execute the first function on that list and return the result of it.
Otherwise, return the result of the second one
"""


def square_nums(nums):
    return [num ** 2 for num in nums]


def remove_negatives(nums):
    return [num for num in nums if num > 0]


def choose_func(nums: list, func1, func2):
    flag = True
    for n in nums:
        if n < 0:
            flag = False
    if flag:
        return square_nums(nums)
    else:
        return remove_negatives(nums)


if __name__ == '__main__':
    print("Task 1")
    print(h.__code__.co_nlocals)
    print(y([12]))
    print("Task 2")
    function_1()
    print("Task 3")
    nums1 = [1, 2, 3, 4, 5]
    nums2 = [1, -2, 3, -4, 5]
    assert choose_func(nums1, square_nums, remove_negatives) == [1, 4, 9, 16, 25]
    assert choose_func(nums2, square_nums, remove_negatives) == [1, 3, 5]
