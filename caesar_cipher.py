# -*- coding: utf-8 -*-
def encrypt_caesar(plaintext, shift):
    """
    Функція, що зашифровує вхідний текст за допомогою шифру Цезаря з ключем shift.

    """
    plaintext = plaintext.upper()
    ciphertext = ""
    for char in plaintext:
        if char.isalpha():
            # Знаходимо номер символу у таблиці ASCII
            char_code = ord(char)
            # Знаходимо номер нового символу
            new_char_code = (char_code - 65 + shift) % 26 + 65
            # Додаємо новий символ до зашифрованого тексту
            ciphertext += chr(new_char_code)
        else:
            # Якщо символ не є літерою, то додаємо його без змін
            ciphertext += char
    return ciphertext

def decrypt_caesar(ciphertext, shift):
    """
    Функція, що розшифровує вхідний текст зашифрований шифром Цезаря з ключем shift.
    """

    plaintext = ""
    plaintext = plaintext.upper()
    for char in ciphertext:
        if char.isalpha():
            # Знаходимо номер символу у таблиці ASCII
            char_code = ord(char)
            # Знаходимо номер відповідного символу у відкритому тексті
            old_char_code = (char_code - 65 - shift) % 26 + 65
            # Додаємо старий символ до розшифрованого тексту
            plaintext += chr(old_char_code)
        else:
            # Якщо символ не є літерою, то додаємо його без змін
            plaintext += char
    return plaintext


if __name__ == '__main__':
    h = encrypt_caesar("test", 3)
    hh = decrypt_caesar(h, 3)
    print(hh)  # HELLO