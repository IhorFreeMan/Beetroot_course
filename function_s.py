# -*- coding: utf-8 -*-

"""Task 1"""


def favorite_movie(movie_title):
    """
    A simple function.
    Create a simple function called favorite_movie,
    which takes a string containing the name of your favorite movie.
    The function should then print “My favorite movie is named {name}”.
    """
    return print(f"My favorite movie is named {movie_title}")


"""Task 2"""


def make_country(name_country, capital):
    """
    Creating a dictionary.
    Create a function called make_country, which takes in a country’s name and capital as parameters.
    Then create a dictionary from those two, with ‘name’ as a key and ‘capital’ as a parameter.
    Make the function print out the values of the dictionary to make sure that it works as intended.
    """
    country = dict()
    country[capital] = name_country
    return print(country.get(capital))


"""Task 3"""


def make_operation(operator, *args):
    """
    Create a function called make_operation, which takes in a simple arithmetic operator as a first parameter
    (to keep things simple let it only be ‘+’, ‘-’ or ‘*’) and an arbitrary number of arguments (only numbers)
    as the second parameter. Then return the sum or product of all the numbers in the arbitrary parameter. For example:
    """

    result = 0
    flag = True
    if len(args) > 1:
        for numeric in args:

            if operator == "+":
                result += numeric

            if operator == "-":
                result -= numeric

            if operator == "*":
                if flag:
                    result = 1
                    flag = False
                result *= numeric

    return print(result)

words = [
    'Abuse', 'Adult', 'Agent', 'Anger', 'Apple', 'Award', 'Basis', 'Beach', 'Birth', 'Block', 'Blood', 'Board', 'Brain',
    'Bread', 'Break', 'Brown', 'Buyer', 'Cause', 'Chain', 'Chair', 'Chest', 'Chief', 'Child', 'China', 'Claim', 'Class',
    'Clock', 'Coach', 'Coast', 'Court', 'Cover', 'Cream', 'Crime', 'Cross', 'Crowd', 'Crown', 'Cycle', 'Dance', 'Death',
    'Depth', 'Doubt', 'Draft', 'Drama', 'Dream', 'Dress', 'Drink', 'Drive', 'Earth', 'Enemy', 'Entry', 'Error', 'Event',
    'Faith', 'Fault', 'Field', 'Fight', 'Final', 'Floor', 'Focus', 'Force', 'Frame', 'Frank', 'Front', 'Fruit', 'Glass',
    'Grant', 'Grass', 'Green', 'Group', 'Guide', 'Heart', 'Henry', 'Horse', 'Hotel', 'House', 'Image', 'Index', 'Input',
    'Issue', 'Japan', 'Jones', 'Judge', 'Knife', 'Laura', 'Layer', 'Level', 'Lewis', 'Light', 'Limit', 'Lunch', 'Major',
    'March', 'Match', 'Metal', 'Model', 'Money', 'Month', 'Motor', 'Mouth', 'Music', 'Night', 'Noise', 'North', 'Novel',
    'Nurse', 'Offer', 'Order', 'Other', 'Owner', 'Panel', 'Paper', 'Party', 'Peace', 'Peter', 'Phase', 'Phone', 'Piece',
    'Pilot', 'Pitch', 'Place', 'Plane', 'Plant', 'Plate', 'Point', 'Pound', 'Power', 'Press', 'Price', 'Pride', 'Prize',
    'Proof', 'Queen', 'Radio', 'Range', 'Ratio', 'Reply', 'Right', 'River', 'Round', 'Route', 'Rugby', 'Scale', 'Scene',
    'Scope', 'Score', 'Sense', 'Shape', 'Share', 'Sheep', 'Sheet', 'Shift', 'Shirt', 'Shock', 'Sight', 'Simon', 'Skill',
    'Sleep', 'Smile', 'Smith', 'Smoke', 'Sound', 'South', 'Space', 'Speed', 'Spite', 'Sport', 'Squad', 'Staff', 'Stage',
    'Start', 'State', 'Steam', 'Steel', 'Stock', 'Stone', 'Store', 'Study', 'Stuff', 'Style', 'Sugar', 'Table', 'Taste',
    'Terry', 'Theme', 'Thing', 'Title', 'Total', 'Touch', 'Tower', 'Track', 'Trade', 'Train', 'Trend', 'Trial', 'Trust',
    'Truth', 'Uncle', 'Union', 'Unity', 'Value', 'Video', 'Visit', 'Voice', 'Waste', 'Watch', 'Water', 'While', 'White',
    'Whole', 'Woman', 'World', 'Youth',
]

import random


def chec_word(wor_d):
    """
    Перевіряємо слово що вводить user
    """
    if len(wor_d) == 5 and wor_d.isalpha():
        return wor_d
    else:
        return 0


def choice(user_word, random_words):
    result = str()

    if chec_word(user_word):
        for i in range(5):
            # літера зустрічається
            if random_words[i] == user_word[i]:
                result += '!'

            # літера не зустрічається
            if random_words[i] != user_word[i] and (user_word[i] not in random_words[i + 1:len(random_words)]):
                result += '.'

            # літера зустрічається на іншому місці
            if random_words[i] != user_word[i] and (user_word[i] in random_words[i + 1:len(random_words)]):
                result += '?'

    return result


def main(random_words):
    random_words = random.choice(random_words).lower()

    user_word = str()

    n = 6
    while n > 0 and user_word != random_words:
        user_word = input(">>> ").lower()
        choice(user_word, random_words)
        print(choice(user_word, random_words))
        n -= 1

    else:
        print(f"output: {choice(user_word, random_words)}", f"points: {n}", f"random words is {random_words.title()}")



if __name__ == '__main__':
    favorite_movie("Interstellar")
    make_country("Україна", "Київ")
    make_operation("+", 7, 7, 2)
    make_operation("-", 5, 5, -10, -20)
    make_operation("*", 7, 6)
    print("####")
    main(words)
