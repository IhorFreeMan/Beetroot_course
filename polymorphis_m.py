# -*- coding: utf-8 -*-
"""
Task 1

Method overloading.

Create a base class named Animal with a method called talk and then create two subclasses: Dog and Cat,
and make their own implementation of the method talk be different. For instance, Dog’s can be to print ‘woof woof’,
while Cat’s can be to print ‘meow’.
Also, create a simple generic function, which takes as input instance of a Cat or Dog classes and performs talk
method on input parameter.
"""
from datetime import datetime


class Animal:

    def talk(self):
        pass


class Dog(Animal):
    def talk(self):
        return "woof woof"

    def __str__(self):
        return f"Im dog,"


class Cat(Animal):
    def talk(self):
        return "meow"

    def __str__(self):
        return f"Im cat,"


def animal_talk(animal):
    print(animal.talk())





"""
Task 2

Library

Write a class structure that implements a library. Classes:
1) Library - name, books = [], authors = []
2) Book - name, year, author (author must be an instance of Author class)
3) Author - name, country, birthday, books = []

Library class

Methods:
- new_book(name: str, year: int, author: Author) - returns an instance of Book class and adds the book to the books list for the current library.
- group_by_author(author: Author) - returns a list of all books grouped by the specified author
- group_by_year(year: int) - returns a list of all the books grouped by the specified year

All 3 classes must have a readable __repr__ and __str__ methods.

Also, the book class should have a class variable which holds the amount of all existing books
"""


class Author:
    def __init__(self, name: str, country: str, birthday: datetime):
        self.name = name
        self.country = country
        self.birthday = birthday
        self.books = []

    def add_book(self, b_ook):
        self.books.append(b_ook)

    def __str__(self):
        return f"{self.name}"

    def __repr__(self):
        return f"{self.name}, {self.country}, {self.birthday}, {self.books}"


class Book:
    empCount = 0

    def __init__(self, name: str, year: int, author: Author):
        self.name = name
        self.year = year
        self.author = author
        Book.empCount += 1

    def new_book(self) -> list:
        return [self.name, self.year, self.author]

    def __str__(self):
        return f"{self.name}"

    def __repr__(self):
        return f"{self.name}, {self.year}, {self.author}"


class Library:
    def __init__(self, name: str, books: list, authors: list):
        self.name = name
        self.books = books
        self.authors = authors

    def group_by_author(self, autho_r) -> dict:

        """returns a list of all books grouped by the specified author"""
        d = {}
        for autor in self.authors:
            if str(autor) == autho_r:
                d[autor.name] = [str(i) for i in autor.books if i != str(autor.name)]
        return d

    def group_by_year(self, year: int) -> list:
        """returns a list of all the books grouped by the specified year"""
        rezalt = []
        for i in self.books:
            if i[1] == year:
                rezalt.append((i[0], i[1]))
        return rezalt

    def __str__(self):
        return f"{self.name}"

    def __repr__(self):
        return f"{self.name}, {self.books} {self.authors}"


"""
Fraction

Створіть клас Fraction, який буде представляти всю базову арифметичну логіку для дробів (+, -, /, *) 
з належною перевіркою й обробкою помилок. Потрібно додати магічні методи для математичних операцій 
та операції порівняння між об'єктами класу Fraction
"""

import math


class Fraction:
    def __init__(self, a=None, b=None):
        self.a = a
        self.b = b

    def __add__(self, other):
        if isinstance(other, Fraction):

            aut = self.b * other.b // math.gcd(self.b, other.b)
            aut1 = ((aut // self.b) * self.a) + ((aut // other.b) * other.a)

            return self.__class__(aut1, aut)
        else:
            raise Exception("Sorry, there is no 'Fraction'")

    def __sub__(self, other):
        if isinstance(other, Fraction):

            aut = self.b * other.b // math.gcd(self.b, other.b)
            aut1 = ((aut // self.b) * self.a) - ((aut // other.b) * other.a)

            return aut1, aut
        else:
            raise Exception("Sorry, there is no 'Fraction'")

    def __mul__(self, other):
        if isinstance(other, Fraction):

            aut = self.a * other.a
            aut1 = self.b * other.b

            return aut, aut1
        else:
            raise Exception("Sorry, there is no 'Fraction'")

    def __floordiv__(self, other):
        if isinstance(other, Fraction):

            aut = self.a * other.b
            aut1 = self.b * other.a

            return aut, aut1
        else:
            raise Exception("Sorry, there is no 'Fraction'")


if __name__ == '__main__':
    print("Task 1\n")
    pluto = Dog()
    tom = Cat()
    animal_talk(pluto)
    animal_talk(tom)
    print(f"{20 * '_'}\nTask 2\n")

    jules_vern = Author(name="Jules Vern", country="France", birthday=datetime(1828, 2, 8))
    book1 = Book(name="Journey to the center of the earth", year=1864, author=jules_vern)
    book2 = Book(name="From Earth to the Moon", year=1864, author=jules_vern)
    jules_vern.add_book(book1)
    jules_vern.add_book(book2)

    agatha_christie = Author(name="Agatha Christie", country="United Kingdom", birthday=datetime(1890, 9, 15))
    book3 = Book(name="Murder on the Orient Express", year=1934, author=agatha_christie)
    book4 = Book(name="Death on the Nile", year=1937, author=agatha_christie)
    agatha_christie.add_book(book3)
    agatha_christie.add_book(book4)

    list_books = [book1.new_book(), book3.new_book(), book4.new_book(), book2.new_book()]

    sam_library = Library(name="sci-fi", books=list_books, authors=[jules_vern, agatha_christie])

    #  returns a list of all books grouped by the specified author
    print(sam_library.group_by_author("Jules Vern"))

    # Book class should have a class variable which holds the amount of all existing books
    print("Books : ", Book.empCount)

    # returns a list of all the books grouped by the specified year
    for i in sam_library.group_by_year(1864):
        print(i)

    print(f"{20 * '_'}\nTask 3\n")
    x = Fraction(1, 2)
    y = Fraction(1, 4)
    print(x + y)
    assert x + y == Fraction(3, 4)
    x = Fraction(2, 5)
    y = Fraction(1, 2)
    print(x - y)
    # assert x + y == Fraction(3, 4)
    x = Fraction(2, 5)
    y = Fraction(1, 2)
    print(x * y)
    print(x // y)
