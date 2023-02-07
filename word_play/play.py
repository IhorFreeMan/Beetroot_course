# -*- coding: utf-8 -*-
import random
import json

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


def add_words(file="words.txt"):
    """
    Додаємо слова з масиву words у файл
    """
    my_file = open(file, "w")

    for word in range(len(words)):
        my_file.writelines(words[word] + "\n")
    my_file.close()


def read_words(file):
    my_file = open(file, "r")

    words = [i.strip() for i in my_file]
    for word in my_file:
        print(word)
    my_file.close()
    return words


def check_word_in_file(file, user_word):
    """
    Перевіряємо чи є слово в файлі
    """
    my_file = open(file, "r")
    result = str()
    for word in my_file:
        if word.strip().lower() == user_word.strip().lower():
            result = f"{user_word} - this word is in the file {file}"
    my_file.close()
    if result:
        return result
    else:
        return False


def latina_letar(user_word):
    """
    check whether the letters are Latin
    """
    for letter in user_word:
        letter = letter.lower()

        if ord(letter) <= 97 or ord(letter) >= 122:
            return False
        else:
            return True


def chec_user_word(wor_d):
    """
    Перевіряємо слово що вводить user
    """
    if len(wor_d) == 5 and latina_letar(wor_d):
        return wor_d
    else:
        return 0


def add_word_to_file(file, user_word):
    if len(user_word) == 5:
        if latina_letar(user_word):
            if check_word_in_file(file, user_word) == False:
                with open(file, "a") as my_file:
                    my_file.writelines(user_word.title() + '\n')
                print("word is added to the file")
            else:
                print(check_word_in_file(file, user_word))
        else:
            print("non-Latin characters are present")
    else:
        print("word length is not equal to 5")


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


def points(sam: str) -> int:
    """! 20 points
     ? 10 points
    """
    result = 0
    for i in sam:
        if i == "!":
            result += 20
        if i == "?":
            result += 10
    return result


def play_main(files):
    random_word = random.choice(read_words(files)).lower()
    print("###", random_word)

    user_word = str()

    n = 0
    point = 0
    print()
    while n < 6 and user_word != random_word:
        user_word = input(">>> ").lower()
        choice(user_word, random_word)
        r_choice = choice(user_word, random_word)
        point += points(r_choice)
        print(r_choice)
        n += 1

    else:
        result = {"output": choice(user_word, random_word),
                  "points": point // n,
                  "random_words": random_word.title(),
                  }
        return result


def add_jsos_data(game: dict, file="game_result.json"):
    with open(file, mode='w', encoding="utf-8") as f:
        json.dump(game, f, indent=2)
        print(f"the result of the game is recorded in a {file}")



if __name__ == '__main__':
    # add_words()                                      # Додаємо слова з масиву words у файл
    # read_words("words.txt")
    # print(check_word_in_file("words.txt", "Woman"))  # Перевіряємо чи є слово в файлі
    # print(latina_letar("ллл"))                       # Перевіряємо чи всі літери латинського алфавіту
    # print(chec_user_word("Woman"))                     # Перевіряємо чи відповідає критеріям введене користувачем слово
    # add_word_to_file("words.txt", "user_word")
    user_word = input(">>> ")
    add_word_to_file("words.txt", user_word)
