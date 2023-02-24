# -*- coding: utf-8 -*-
import re

"""
Task 1

Create a class method named `validate`, which should be called from the `__init__` method to validate parameter email,
passed to the constructor. The logic inside the `validate` method could be to check if the passed email parameter
is a valid email string.

"""


class CheckYourMail:
    def __init__(self, mail: str):
        self.mail = mail

    @property
    def validate(self):
        """
        Checks the correctness of the email address format
        """
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return bool(re.match(pattern, self.mail))


"""
Task 2

Implement 2 classes, the first one is the Boss and the second one is the Worker.
Worker has a property 'boss', and its value must be an instance of Boss.
You can reassign this value, but you should check whether the new value is Boss. 
Each Boss has a list of his own workers. You should implement a method that allows you to add workers to a Boss. 
You're not allowed to add instances of Boss class to workers list directly via access to attribute, 
use getters and setters instead!

You can refactor the existing code.
"""


class Boss:
    def __init__(self, id_: int, name: str, company: str):
        self.id = id_
        self.name = name
        self.company = company
        self._workers = []

    def add_worker(self, worker: 'Worker'):
        if isinstance(worker, Worker):
            self._workers.append(worker)
            worker.boss = self
        else:
            raise ValueError("Worker must be an instance of Worker class.")

    def remove_worker(self, worker: 'Worker'):
        if isinstance(worker, Worker):
            worker.boss = None
        else:
            raise ValueError("Worker must be an instance of Worker class.")

    @property
    def workers(self):
        return self._workers


class Worker:
    def __init__(self, id_: int, name: str, company: str, boss: Boss = None):
        self.id = id_
        self.name = name
        self.company = company
        self.boss = boss

    def __str__(self):
        return f"{self.name}"


"""
Task 3

Write a class TypeDecorators which has several methods for converting results 
of functions to a specified type (if it's possible):
"""

from functools import wraps


class TypeDecorators:
    @staticmethod
    def to_int(func):
        def wrap(sam_str: str):
            return int(func(sam_str))

        return wrap

    @staticmethod
    def to_str(func):
        def wrap(sam):
            return str(func(sam))

        return wrap

    @staticmethod
    def to_bool(func):
        def wrap(sam):
            return bool(func(sam))

        return wrap

    @staticmethod
    def to_float(func):
        def wrap(sam):
            return float(func(sam))

        return wrap



if __name__ == "__main__":
    print(f"{20 * '_'}\nTask 1\n")

    my_mail = CheckYourMail("igor_freamen@gmail.com")
    print(my_mail.validate)

    print(f"{20 * '_'}\nTask 2\n")

    mr_jefferson = Boss(id_=1, name="Jefferson", company="ATB")

    jack = Worker(id_=1, name="Jack", company="ATB")
    bob = Worker(id_=2, name="Bob", company="ATB")
    alex = Worker(id_=3, name="Alex", company="ATB")
    mr_jefferson.add_worker(jack)
    mr_jefferson.add_worker(bob)
    mr_jefferson.add_worker(alex)

    for worker in mr_jefferson.workers:
        print(worker.name, worker.boss.name)

    print(f"{20 * '_'}\nTask 3\n")


    @TypeDecorators.to_int
    def do_nothing(string: str):
        return string

    @TypeDecorators.to_str
    def do_str(string: str):
        return string

    @TypeDecorators.to_bool
    def do_something(string: str):
        return string


    @TypeDecorators.to_float
    def do_something_else(string: str):
        return string

    assert do_nothing('25') == 25
    assert do_str(25) == "25"
    assert do_something('True') is True
    assert do_something_else('0.1234') == 0.1234
