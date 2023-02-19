# -*- coding: utf-8 -*-
from abc import ABC, abstractmethod


# абстрактна фабрика
class IAmGameOfTrones(ABC):
    @abstractmethod
    def create_scene(self):
        pass

    @abstractmethod
    def mountains_of_essos(self):
        pass

    @abstractmethod
    def create_people(self):
        pass


# створюємо конкретне місці
class PlaceEssos(IAmGameOfTrones):
    # місця в Ессосі
    def create_scene(self):
        return TypesOfMountain()

    # гори
    def mountains_of_essos(self):
        return TypesOfStreet()

    # люди
    def create_people(self):
        return SpecificOfPeople()


# абстрактна гора
class IAmAMountain(ABC):
    # вершина гори
    @abstractmethod
    def mountain_top(self):
        pass

    # долини
    @abstractmethod
    def valley(self):
        pass

    # печера
    @abstractmethod
    def cave(self):
        pass


# конкретна гора
class TypesOfMountain(IAmAMountain):
    def mountain_top(self):
        print("гора Матері")

    def valley(self):
        print("долина Миру")

    def cave(self):
        print("печера Страху")


# абстрактна дорога
class IAmAStreet(ABC):
    @abstractmethod
    def Area(self):
        pass

    @abstractmethod
    def Highway(self):
        pass


# конкретна дорога
class TypesOfStreet(IAmAStreet):
    def Area(self):
        print('Площа Відпочинку')

    def Highway(self):
        print('Шлях подорожувальників')


# абстракт., люди
class IAmApeople(ABC):
    @abstractmethod
    def men(self):
        pass

    @abstractmethod
    def women(self):
        pass


# люди
class SpecificOfPeople(IAmApeople):
    def women(self):
        return print('Кхал Дрого')

    def men(self):
        return print('Дейнерис Таргариен')


# client code
def checkFactory(factory):
    print('Ессос')

    mountain = factory.mountains_of_essos()
    mountain.Area()

    scene = factory.create_scene()
    scene.valley()
    # scene.cave()

    people = factory.create_people()
    people.men()
    people.women()


if __name__ == "__main__":
    checkFactory(PlaceEssos())
