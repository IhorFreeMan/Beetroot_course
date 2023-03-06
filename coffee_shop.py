# -*- coding: utf-8 -*-
from abc import ABC, abstractmethod


class ImCoffeeShop(ABC):
    @abstractmethod
    def create_coffee_shop(self):
        pass


class CoffeeShop(ImCoffeeShop):
    def __init__(self):
        self.menu = {
            "Americano coffee": 10,
            "Latte coffee": 14,
            "Cappuccino": 15,
        }

    def create_coffee_shop(self):
        return TypesCoffee()


class TypesCoffee:
    def americano_coffee(self):
        self.name = "Americano coffee",
        return self.name

    def latte_coffee(self):
        self.name = "Latte coffee",
        return self.name

    def cappuccino_coffee(self):
        self.name = "Cappuccino"
        return self.name


class Barista:
    def __init__(self):
        self.salary = 0

    def create(self, create_coffee: TypesCoffee()):
        self.salary += 1
        self.create_coffee = create_coffee
        return self.create_coffee


class Order:
    def __init__(self):
        self.order = {}
        self.index = 1

    def set_coffee(self, coffee):
        # print(coffee)
        self.order[self.index] = coffee
        self.index += 1


# client code
def checkFactory(coffeehouse):
    print('Tasty coffee')
    coffeehouse.create_coffee_shop()

    # menu
    print(f"{20 * '_'}\nMenu:")
    for kay, value in coffeehouse.menu.items():
        print(f"{kay} - {value} usd")

    # barista
    boob_barista = Barista()

    # order1
    order1 = Order()
    order1.set_coffee(boob_barista.create(TypesCoffee()).americano_coffee()[0])
    order1.set_coffee(boob_barista.create(TypesCoffee()).latte_coffee()[0])
    order1.set_coffee(boob_barista.create(TypesCoffee()).latte_coffee()[0])

    print(f"{20 * '_'}\nOrder:")
    # check
    chek = 0
    for kay, value in order1.order.items():
        print(f"{value} - {coffeehouse.menu.get(value)} usd")
        chek += coffeehouse.menu.get(value)
    print("tootal: ", chek, "usd")

    print("barista salary: ", boob_barista.salary, "usd")


if __name__ == "__main__":
    checkFactory(CoffeeShop())
