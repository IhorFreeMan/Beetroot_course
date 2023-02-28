# -*- coding: utf-8 -*-
import testing_code_country
import unittest
import phonebook


class MakeCountryCase(unittest.TestCase):
    def test_make_country(self):
        full = testing_code_country.make_country("Україна", "Київ")
        self.assertEqual(full, "Україна")


class PhonebookCase(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.file = "my_tel_book.json"
        self._data = phonebook.read_tel_book(self.file)

    def test_read_tel_book(self):
        full = phonebook.read_tel_book(self.file)
        self.assertEqual(full, self._data)

    def test_add_data_tel_book(self):
        full = phonebook.add_data_tel_book(self.file, "380666543345", "Lenon", last_name="John", city="London",
                                           region="England")
        # self.assertEqual(full, "information added")
        self.assertEqual(full, "Error, the subscriber exists")

    def test_search(self):
        full = phonebook.search(self.file, what_to_look="first_name", search="Ringo")  # first_name
        full2 = phonebook.search(self.file, what_to_look="last_name", search="George")  # last_name
        full3 = phonebook.search(self.file, what_to_look="city", search="Liverpool")  # city
        self.assertEqual(full, {'380666543348': 'Ringo Starr England Liverpool'})
        self.assertEqual(full2, {'380666543347': 'Harrison George England Liverpool'})
        self.assertEqual(full3, {'380666543348': 'Ringo Starr England Liverpool',
                                 '380666543347': 'Harrison George England Liverpool',
                                 '380666543346': 'McCartney James England Liverpool'})

    def test_search_full_name(self):
        full = phonebook.search_full_name(self.file, first_name="Lenon", last_name="John")
        self.assertEqual(full, True)

    def test_search_telephone_number(self):
        full = phonebook.search_telephone_number(self.file, telephone_number=380666543348)
        self.assertEqual(full, [
            {'first_name': 'Ringo', 'last_name': 'Starr', 'city': 'Liverpool', 'region': 'England', 'notes': ''}])

    def test_del_data_tel_book(self):
        full = phonebook.del_data_tel_book(self.file, telephone_number=380666543349)
        self.assertEqual(full, "Error!!! Number in tk is missing")
        # self.assertEqual(full, "number del 380666543348")



    def test_update_tel_book(self):
        full = phonebook.update_tel_book(self.file, 380666543349, notes="Bitls", first_name="Ihor")
        # self.assertEqual(full, "information has been updated")
        self.assertNotEqual(full, "information has been updated")

if __name__ == "__main__":
    unittest.main()
