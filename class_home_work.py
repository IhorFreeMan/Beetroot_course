# -*- coding: utf-8 -*-


"""
Task 1

A Person class

Make a class called Person. Make the __init__() method take firstname,
lastname, and age as parameters and add them as attributes. Make another method called talk()
which makes prints a greeting from the person containing, for example like this: 'Hello,
my name is Carl Johnson and I'm 26 years old'.
"""


class Person:
    def __init__(self, last_name, first_name, age):
        self.last_name = last_name
        self.first_name = first_name
        self.age = age

    def talk(self) -> str:
        return f"Hello,my name is {self.first_name} {self.last_name} and I’m {self.age} years old"


"""
Task 2

Doggy age

Create a class Dog with class attribute `age_factor` equals to 7. 
Make __init__() which takes values for a dog’s age. 
Then create a method `human_age` which returns the dog’s age in human equivalent.
"""


class Dog:
    def __init__(self, age_dog=0.0):
        self._age_factor = 7
        self.age_dog = age_dog


    def human_age(self) -> str:
        return f"dog’s age in human equivalent {self.age_dog * self._age_factor}"


class TVController:

    def __init__(self, channels: list):
        self.channel = channels
        self.now_chenl = 1
        self._len_channels = len(channels)

    def first_channel(self) -> str:
        """ - turns on the first channel from the list."""
        self.now_chenl = 1
        return self.channel[0]

    def last_channel(self) -> str:
        """- turns on the last channel from the list."""
        self.now_chenl = self._len_channels
        return self.channel[-1]

    def turn_channel(self, n) -> str:
        """- turns on the N channel. Pay attention that the channel numbers start from 1, not from 0. """
        self.now_chenl = self.channel.index(self.channel[n - 1])
        return self.channel[n - 1]

    def next_channel(self) -> str:
        """- turns on the next channel. If the current channel is the last one, turns on the first channel."""

        if self._len_channels > self.now_chenl:
            self.now_chenl += 1
            return self.channel[self.now_chenl-1]
        else:
            self.now_chenl = 1
            return self.channel[0]

    def previous_channel(self) -> str:
        """- turns on the previous channel. If the current channel is the first one, turns on the last channel."""
        if 0 < self.now_chenl < self._len_channels:
            self.now_chenl -= 1
            return self.channel[self.now_chenl]
        else:
            self.now_chenl = self._len_channels - 1
            return self.channel[-1]

    def current_channel(self) -> str:
        """ - returns the name of the current channel."""
        return self.channel[self.now_chenl]

    def is_exist(self, n) -> str:
        """- gets 1 argument - the number N or the string 'name' and returns 'Yes', if the channel N or 'name'
        exists in the list, or "No" - in the other case."""
        if isinstance(n, int) and 0 > n <= self._len_channels:
            return "Yes"
        elif isinstance(n, str) and n.upper() in self.channel:
            return "Yes"
        else:
            return "No"


if __name__ == '__main__':
    print("Task 1\n")
    CarlJohonson = Person("Johnson", "Carl", 26)
    print(CarlJohonson.talk())

    print("\nTask 2\n")
    VinstonDog = Dog(0.3)
    print(VinstonDog.human_age())

    print("\nTask 3\n")
    CHANNELS = ["BBC", "Discovery", "TV1000"]
    controller = TVController(CHANNELS)
    # assert controller.first_channel() == "BBC"
    # assert controller.last_channel() == "TV1000"
    # assert controller.turn_channel(1) == "BBC"
    # assert controller.next_channel() == "Discovery"
    #
    # assert controller.previous_channel() == "BBC"
    # assert controller.current_channel() == "BBC"
    # assert controller.is_exist(4) == "No"
    # assert controller.is_exist("BBC") == "Yes"

