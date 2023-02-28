# -*- coding: utf-8 -*-
def make_country(name_country, capital):
    """
    Creating a dictionary.
    Create a function called make_country, which takes in a country’s name and capital as parameters.
    Then create a dictionary from those two, with ‘name’ as a key and ‘capital’ as a parameter.
    Make the function print out the values of the dictionary to make sure that it works as intended.
    """
    country = dict()
    country[capital] = name_country
    return country.get(capital)



print(make_country("Україна", "Київ"))