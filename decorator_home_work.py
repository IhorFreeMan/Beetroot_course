# -*- coding: utf-8 -*-
"""
Task 1

Write a decorator that prints a function with arguments passed to it.

NOTE! It should print the function, not the result of its execution!
"""


def logger(func):
    def wrapper(*args):
        print(func.__name__, args)
        return func(*args)

    return wrapper


@logger
def add(x, y):
    return x + y


@logger
def square_all(*args):
    return [arg ** 2 for arg in args]


"""
Task 2

Write a decorator that takes a list of stop words and replaces them with * inside the decorated function
"""


def stop_words(words: list):
    def decorator_repeat(func):

        def wrapper_repeat(nam):

            list_nam = func(nam).split()

            for word in range(len(list_nam)):
                if list_nam[word].replace("!", "") in words:
                    list_nam[word] = "*"
            value = (" ".join(list_nam))
            return value + '!'

        return wrapper_repeat

    return decorator_repeat


@stop_words(['pepsi', 'BMW'])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"


"""
Task 3

Write a decorator `arg_rules` that validates arguments passed to the function.
"""


def arg_rules(type_: type, max_length: int, contains: list):
    def decorator_repeat(func):
        def wrapper_repeat(*args):
            return None

    return decorator_repeat


# @arg_rules(type_=str, max_length=15, contains=['05', '@'])
# def create_slogan(name: str) -> str:
#     return f"{name} drinks pepsi in his brand new BMW!"



if __name__ == "__main__":
    # print("\n Task 1\n")
    # add(4, 5)
    # square_all(10)
    # print("\n Task 2\n")
    assert create_slogan("Steve") == "Steve drinks * in his brand new *!"
    print("\n Task 3\n")
    assert create_slogan('johndoe05@gmail.com') is False
    assert create_slogan('S@SH05') == 'S@SH05 drinks pepsi in his brand new BMW!'
    pass
