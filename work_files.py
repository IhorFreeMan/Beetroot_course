# -*- coding: utf-8 -*-
"""
Task 1

Files
Write a script that creates a new output file called myfile.txt and writes the string "Hello file world!" in it.
Then write another script that opens myfile.txt, and reads and prints its contents.
Run your two scripts from the system command line.
Does the new file show up in the directory where you ran your scripts?
What if you add a different directory path to the filename passed to open?
Note: file write methods do not add newline characters to your strings; add an explicit ‘\n’
at the end of the string if you want to fully terminate the line in the file.
"""


def create_myfile(myfile="myfile.txt", text=""):
    with open(myfile, "a") as myfile:
        myfile.write(text)


def read_myfile(file):
    with open(file, "r") as myfile:
        print(myfile.read())


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
import os


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
            telbook.update(data)
            with open(file, mode='w', encoding="utf-8") as tel_book:
                json.dump(telbook, tel_book, indent=2)
                print("information added")
        else:
            print("Error, the subscriber exists")

    except FileNotFoundError:
        with open(file, mode='w', encoding="utf-8") as tel_book:
            json.dump(telbook, tel_book, indent=2)
            print("information added")


def search_first_name(file, first_name):
    """
    Search by first name
    """
    result = []
    data = read_tel_book(file)

    for key, value in data.items():
        if data[key][0].get("first_name").lower() == first_name.strip().lower():
            result.append((key, data[key][0].values()))
    return result


def search_last_name(file, last_name):
    """
    Search by last name
    """
    result = []
    data = read_tel_book(file)
    for key, value in data.items():
        if data[key][0].get("last_name").lower() == last_name.strip().lower():
            result.append((key, data[key][0].values()))
    return result


def search_full_name(file, first_name, last_name):
    """
    Search by full name
    """
    if search_first_name(file, first_name) and search_last_name(file, last_name):
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


def search_city(file, city):
    """
    Search citi
    """
    data = read_tel_book(file)

    result = []
    for key, value in data.items():
        if data[key][0].get("city").lower() == city.strip().lower():
            result.append((key, data[key][0].values()))
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
        print(f"number del {telephone_number}")
    except KeyError:
        print("Error!!! Number in tk is missing")


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
            print("information has been updated")
    except KeyError:
        print("Error!!! Number in tk is missing")


if __name__ == "__main__":
    # print("Task 1")
    create_myfile(text="Hello file world!\n")
    read_myfile("myfile.txt")
    print("Task 2")

    add_data_tel_book("my_tel_book.json", "380666543345", "Lenon", last_name="John", city="London", region="England")
    add_data_tel_book("my_tel_book.json", "380666543346", "McCartney", last_name="James", city="Liverpool",
                      region="England")
    add_data_tel_book("my_tel_book.json", "380666543347", "Harrison", last_name="George ", city="Liverpool",
                      region="England")
    add_data_tel_book("my_tel_book.json", "380666543348", "Ringo", last_name="Starr", city="Liverpool",
                      region="England")
    print(read_tel_book("my_tel_book.json"))
    print(search_first_name("my_tel_book.json", "Ringo"))
    print(search_last_name("my_tel_book.json", last_name="George"))
    print(search_full_name("my_tel_book.json", first_name="Lenon", last_name="John"))
    print(search_telephone_number("my_tel_book.json", telephone_number=380666543348))
    print(search_city("my_tel_book.json", city="Liverpool"))
    del_data_tel_book("my_tel_book.json", telephone_number=380666543349)
    update_tel_book("my_tel_book.json", 380666543348, notes="Bitls", first_name="Ihor")
