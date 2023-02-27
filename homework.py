# -*- coding: utf-8 -*-

"""
Task 1

Create your own implementation of a built-in function enumerate, named `with_index`, which takes two parameters:
`iterable` and `start`, default is 0. Tips: see the documentation for the enumerate function
"""


def with_index(iterable, start=0):
    for i in range(len(iterable)):
        yield start, iterable[i]
        start += 1


"""
Task 2

Create your own implementation of a built-in function range, named in_range(), which takes three parameters:
`start`, `end`, and optional step. Tips: See the documentation for `range` function
"""


def in_range(start, stop, step=1):
    current = start
    while current < stop:
        yield current
        current += step


"""
Task 3

Create your own implementation of an iterable, which could be used inside for-in loop. 
Also, add logic for retrieving elements using square brackets syntax.
"""


class MyIterable:
    def __init__(self, data):
        self.data = data
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.data):
            raise StopIteration
        rez = self.data[self.index]
        self.index += 1
        return rez

    def __getitem__(self, index):
        return self.data[index]


if __name__ == "__main__":
    s = ['string1', 'string2', 'string3']

    print(f"{20 * '_'}\nTask 1\n")
    print(list(with_index(s)))

    print(f"{20 * '_'}\nTask 2\n")

    for i in in_range(1, 10, 2):
        print(i)

    print(f"{20 * '_'}\nTask 3\n")

    l = ["a", "b", "c", "d", "e"]

    print(MyIterable.__dict__)
    print(MyIterable(l).__dict__)

    for i in MyIterable(l):
        print(i)

    print(MyIterable(l)[2])
