# -*- coding: utf-8 -*-

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


def add_words():
    """
    Додаємо слова з масиву words у файл

    """
    my_file = open("words.txt", "w")

    for word in range(len(words)):
        my_file.writelines(words[word] + "\n")
    my_file.close()



def read_words(file):
    my_file = open(file, "r")
    for word in my_file:
        print(word)
    my_file.close()


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




if __name__ == '__main__':
    # add_words()                                      # Додаємо слова з масиву words у файл
    # read_words("words.txt")
    # print(check_word_in_file("words.txt", "Woman"))  # Перевіряємо чи є слово в файлі
    # print(latina_letar("ллл"))                       # Перевіряємо чи всі літери латинського алфавіту
    # print(chec_user_word("Woman"))                     # Перевіряємо чи відповідає критеріям введене користувачем слово
    # add_word_to_file("words.txt", "user_word")
    user_word = input(">>> ")
    add_word_to_file("words.txt", user_word)

