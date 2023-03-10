from abc import ABC, abstractmethod


class ImCoffeeShop(ABC):
    @abstractmethod
    def create_coffee_shop(self):
        pass

    @abstractmethod
    def create_barista(self):
        pass

class CoffeeShop(ImCoffeeShop):
    def __init__(self):
        self.menu = {}
        self.coffee_toppings = {}

    def create_coffee_shop(self):
        return TypesCoffee()

    def create_barista(self):
        return Barista()

    def add_menu(self, file):
        with open(file, "r") as f:
            for i in f:
                l = i.strip().split("-")
                if len(l) == 2:
                    self.menu[l[0].strip()] = l[1].strip()

    def add_topping(self, file):
        with open(file, "r") as f:
            for i in f:
                l = i.strip().split("-")
                if len(l) == 2:
                    self.coffee_toppings[l[0].strip()] = l[1].strip()


class TypesCoffee:

    def __init__(self, toppings=None):
        self.toppings = toppings

    def americano_coffee(self):
        self.name = "Americano coffee"
        return [self.name, self.toppings]

    def latte_coffee(self):
        self.name = "Latte coffee"
        return [self.name, self.toppings]

    def cappuccino_coffee(self):
        self.name = "Cappuccino"
        return [self.name, self.toppings]



class Barista:
    def __init__(self):
        self.salary = 0
        self.create_coffee = None

    def create(self, create_coffee: TypesCoffee):
        self.salary += 1
        self.create_coffee = create_coffee
        # print(self.create_coffee.toppings)

        return self.create_coffee



class Order:
    def __init__(self):
        self.order = {}
        self.index = 1

    def set_coffee(self, coffee):
        self.order[self.index] = coffee
        self.index += 1

    def get_order(self):
        return self.order


# client code
def checkFactory(coffeehouse):
    print('Tasty coffee')
    coffeehouse.create_coffee_shop()
    coffeehouse.add_menu("menu.txt")
    coffeehouse.add_topping("toping.txt")
    boob_barista = coffeehouse.create_barista()


    # menu
    print(f"{20 * '_'}\nMenu:")
    for kay, value in coffeehouse.menu.items():
        print(f"{kay} - {value} usd")

     # order1
    order1 = Order()
    order1.set_coffee(boob_barista.create(TypesCoffee(toppings=["milk", "sugar"])).americano_coffee())
    order1.set_coffee(boob_barista.create(TypesCoffee(toppings=["cinnamon"])).latte_coffee())
    order1.set_coffee(boob_barista.create(TypesCoffee(toppings=["sugar"])).cappuccino_coffee())
    order1.set_coffee(boob_barista.create(TypesCoffee()).cappuccino_coffee())

    print(f"{20 * '_'}\nOrder:")

    # check
    chek = 0
    for kay, value in order1.order.items():
        s_toping = 0
        if value[1]:
            for toping in value[1]:
                s_toping += int(coffeehouse.coffee_toppings.get(toping))

        print(f"{value[0], value[1]} - {coffeehouse.menu.get(value[0])} usd, toping - {s_toping} usd")

        chek += int(coffeehouse.menu.get(value[0]))
        chek+=s_toping
    print("tootal: ", chek, "usd")

    print("barista salary: ", boob_barista.salary, "usd")


if __name__ == "__main__":
    checkFactory(CoffeeShop())