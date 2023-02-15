# -*- coding: utf-8 -*-

"""
Task 1

School

Make a class structure in python representing people at school. Make a base class called Person,
a class called Student, and another one called Teacher. Try to find as many methods and attributes
as you can which belong to different classes, and keep in mind which are common and which are not.
For example, the name should be a Person attribute, while salary should only be available to the teacher.

"""


class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age


class Student(Person):
    def __init__(self, first_name, last_name, age, faculty, course=1):
        super().__init__(first_name, last_name, age)
        self.course = course
        self.faculty = faculty
        self.skill = ""

    def get_skill(self):
        return self.skill

    def set_skill(self, skill) -> str:
        self.skill = skill
        return f"Student: {self.first_name} {self.last_name}"


class Teacher(Person):
    def __init__(self, first_name, last_name, age, faculty, salary: int = 200):
        super().__init__(first_name, last_name, age)
        self.salary = salary
        self.students = []
        self.faculty = faculty

    def get_students(self) -> list:
        return self.students

    def set_study_student(self, studen_t):
        self.students.append(studen_t)

    def __str__(self):
        return f"Teacher: {self.first_name} {self.last_name}"


"""
Task 2

Mathematician

Implement a class Mathematician which is a helper class for doing math operations on lists
The class doesn't take any attributes and only has methods:
"""


class Mathematician:

    def square_nums(self, sam_list) -> list:
        """takes a list of integers and returns the list of squares"""
        return [ii ** 2 for ii in sam_list]

    def remove_positives(self, sam_list) -> list:
        """takes a list of integers and returns it without positive numbers"""
        return [ii for ii in sam_list if ii < 0]

    def filter_leaps(self, sam_list) -> list:
        """takes a list of dates (integers) and removes those that are not 'leap years'"""
        return [year for year in sam_list if (year % 4 == 0 and year % 100 != 0 or year % 400 == 0)]


"""
Task 3

Product Store

Write a class Product that has three attributes:
"""


class Product:
    DISCOUNT = 0

    def __init__(self, typ_e, name, price):
        self.type = typ_e
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name}"


class ProductStore:

    def __init__(self):
        self.product = dict()
        self.money = 0

    def add(self, product, amount):
        """adds a specified quantity of a single product with a predefined price premium for your store(30 percent)"""
        product.price = product.price + (product.price * 30) / 100
        self.product[product.name] = [product.type, product.name, product.price, amount]

    def set_discount(self, percent, identifier_type):
        """identifier, percent, identifier_type=’name’) - adds a discount for all products"""
        for kay, value in self.product.items():
            if value[0] == identifier_type:
                total_discount = (self.product.get(kay)[2] * percent) / 100
                self.product.get(kay)[2] -= total_discount

    def sell_product(self, product_name, amount):
        """removes a particular amount of products from the store if available, in other case raises an error.
        It also increments income if the sell_product method succeeds."""
        if self.product.get(product_name)[3] > amount:
            self.product.get(product_name)[3] -= amount
            price_per_product_unit = self.product.get(product_name)[2]
            self.money = price_per_product_unit * amount
        else:
            raise Exception("Sorry, there is no product")

    def get_income(self):
        """returns amount of many earned by ProductStore instance."""
        return self.money

    def get_all_products(self):
        """returns information about all available products in the store."""
        return {kay: value for (kay, value) in self.product.items()}

    def get_product_info(self, product_name):
        """returns a tuple with product name and amount of items in the store."""
        return product_name, self.product.get(product_name)[3]


"""
Task 4

Custom exception

Create your custom exception named `CustomException`, you can inherit from base Exception class, 
but extend its functionality to log every error message to a file named `logs.txt`. 
Tips: Use __init__ method to extend functionality for saving messages to file
"""


class CustomException(Exception):
    def __init__(self, message, value):
        message = f'{value} is not a number'
        super().__init__(message)
        self.sam_value = message
        self.logs()

    def logs(self):
        with open("logs.txt", "a") as file:
            file.write(f'{self.sam_value}')


if __name__ == '__main__':
    print("Task 1")
    jac_brown = Student("Brown", "Jac", 18, "history")
    lisa_green = Student("Green", "Lisa", 17, "history")
    teacher_mr_black = Teacher("Black", "John", 34, "history")

    print(teacher_mr_black)

    # study the student
    teacher_mr_black.set_study_student(jac_brown.set_skill(3))
    teacher_mr_black.set_study_student(lisa_green.set_skill(5))

    # studied students
    print(f"{jac_brown.first_name} вивчив {jac_brown.faculty}  на оцінку: {jac_brown.get_skill()} .")
    print(f"{lisa_green.first_name} вивчила {lisa_green.faculty} на оцінку: {lisa_green.get_skill()} .")

    print("            Our class:")
    for student in teacher_mr_black.get_students():
        print(student)

    print("\nTask 2\n")

    m = Mathematician()

    assert m.square_nums([7, 11, 5, 4]) == [49, 121, 25, 16]
    assert m.remove_positives([26, -11, -8, 13, -90]) == [-11, -8, -90]
    assert m.filter_leaps([2001, 1884, 1995, 2003, 2020]) == [1884, 2020]

    print("\nTask 3\n")

    p = Product("Sport", "Football T-Shirt", 100)
    p2 = Product("Food", "Ramen", 1.5)
    s = ProductStore()
    s.add(p, 10)
    s.add(p2, 300)
    s.sell_product("Ramen", 10)
    assert s.get_product_info("Ramen") == ("Ramen", 290)
    # print(s.product.get("Ramen"))
    # print(s.get_product_info("Ramen"))
    # print(s.get_income())
    # print(s.get_all_products())
    # s.set_discount(percent=10, identifier_type="Sport")
    # print(s.get_all_products())

    print("\nTask 4\n")

    m = [1, 2, 3, 4, 5, "six", 7]

    for i in m:
        if isinstance(i, str):
            raise CustomException("Exception occured.", i)
        else:
            print(i)
