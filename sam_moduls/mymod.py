# -*- coding: utf-8 -*-


def count_lines(name):
    f = open(name, 'r')
    sum_a = 0
    for line in f:
        # print(line)
        sum_a += 1
    return print("counts the number of lines: ", sum_a)


def count_chars(name):
    f = open(name, 'r')
    m = []
    for line in f:
        word_s = line.strip()
        m.append((word_s, len(word_s)))
    return print(f"counts the number of characters: {m}")


def test(name):
    print(name)
    count_lines(name)
    count_chars(name)
    return 0



if __name__ == '__main__':
    # count_lines(name)
    # count_chars(name)
    # test(name)
    pass

