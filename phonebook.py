# -*- coding: utf-8 -*-
"""
Extend Phonebook application
Functionality of Phonebook application:
Add new entries
Search by first name
Search by last name
Search by full name
Search by telephone number
Search by city or state
Delete a record for a given telephone number
Update a record for a given telephone number
An option to exit the program

The first argument to the application should be the name of the phonebook.
Application should load JSON data, if it is present in the folder with application,
else raise an error. After the user exits, all data should be saved to loaded JSON.
"""

import json


def read_tel_book(file):
    with open(file) as f:
        file_content = f.read()
        data = json.loads(file_content)
        return data


def add_data_tel_book(file, phone_number, first_name, last_name="", city="", region="", notes=""):
    """
    Add new entries
    """
    telbook = {
        phone_number.strip(): [{
            "first_name": first_name.strip(),
            "last_name": last_name.strip(),
            "city": city.strip(),
            "region": region.strip(),
            "notes": notes.strip(),
        }
        ]
    }

    try:
        data = read_tel_book(file)
        if phone_number.strip() not in data:
            telbook.update(data)                                     # corrected
            with open(file, mode='w', encoding="utf-8") as tel_book:
                json.dump(telbook, tel_book, indent=2)
                return "information added"
        else:
            return "Error, the subscriber exists"

    except FileNotFoundError:
        with open(file, mode='w', encoding="utf-8") as tel_book:
            json.dump(telbook, tel_book, indent=2)
            return "information added"


def search_full_name(file, first_name, last_name):
    """
    Search by full name
    """
    if search(file, "first_name", first_name) and search(file, "last_name", last_name):
        return True
    else:
        return False


def search_telephone_number(file, telephone_number):
    """
    Search by telephone number
    """
    data = read_tel_book(file)
    if data.get(str(telephone_number)):
        return data.get(str(telephone_number))
    else:
        return False


def search(file, what_to_look, search):
    """
    Search citi
    """
    data = read_tel_book(file)

    result = {}
    for key, value in data.items():
        if data[key][0].get(what_to_look).lower() == search.strip().lower():
            result[key] = f"{data[key][0].get('first_name')} {data[key][0].get('last_name')} {data[key][0].get('region')} {data[key][0].get('city')}"
            # result.append((key, data[key][0].values()))
    return result


def del_data_tel_book(file, telephone_number):
    """
    Delete a record for a given telephone number
    """
    data = read_tel_book(file)
    try:
        data.pop(str(telephone_number))
        with open(file, mode='w', encoding="utf-8") as tel_book:
            json.dump(data, tel_book, indent=2)
        return f"number del {telephone_number}"
    except KeyError:
        return "Error!!! Number in tk is missing"


def update_tel_book(file, phone_number, first_name="", last_name="", city="", region="", notes=""):
    """Update a record for a given telephone number"""
    data = read_tel_book(file)
    try:
        if data.get(str(phone_number)):
            if len(first_name) != 0:
                data.get(str(phone_number))[0]["first_name"] = first_name

            if len(last_name) != 0:
                data.get(str(phone_number))[0]["last_name"] = last_name

            if len(city) != 0:
                data.get(str(phone_number))[0]["city"] = city

            if len(region) != 0:
                data.get(str(phone_number))[0]["region"] = region

            if len(notes) != 0:
                data.get(str(phone_number))[0]["notes"] = notes

            with open(file, mode='w', encoding="utf-8") as tel_book:
                json.dump(data, tel_book, indent=2)
            return "information has been updated"
    except KeyError:
        return "Error!!! Number in tk is missing"


if __name__ == "__main__":
    print("Task 2")

    add_data_tel_book("my_tel_book.json", "380666543345", "Lenon", last_name="John", city="London", region="England")
    add_data_tel_book("my_tel_book.json", "380666543346", "McCartney", last_name="James", city="Liverpool", region="England")
    add_data_tel_book("my_tel_book.json", "380666543347", "Harrison", last_name="George ", city="Liverpool",
                      region="England")
    add_data_tel_book("my_tel_book.json", "380666543348", "Ringo", last_name="Starr", city="Liverpool",
                      region="England")
    # print(read_tel_book("my_tel_book.json"))
    # print(search("my_tel_book.json", what_to_look="first_name", search="Ringo"))                           # first_name
    # print(search("my_tel_book.json", what_to_look="last_name", search="George"))                          # last_name
    # print(search_full_name("my_tel_book.json", first_name="Lenon", last_name="John"))
    # print(search_telephone_number("my_tel_book.json", telephone_number=380666543348))
    # print(search("my_tel_book.json", what_to_look="city", search="Liverpool"))                        # search_city
    # print(del_data_tel_book("my_tel_book.json", telephone_number=380666543349))
    # # # update_tel_book("my_tel_book.json", 380666543348, notes="Bitls", first_name="Ihor")