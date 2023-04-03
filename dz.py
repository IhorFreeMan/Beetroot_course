# -*- coding: utf-8 -*-
from concurrent.futures import ProcessPoolExecutor
from time import time

"""
Task 1
We have the following input list of numbers, some of them are prime. You need to create a utility function that takes as input a number and returns a bool, whether it is prime or not.



Use ThreadPoolExecutor and ProcessPoolExecutor to create different concurrent implementations for filtering NUMBERS.

Compare the results and performance of each of them.
"""
NUMBERS = [
   2,  # prime
   1099726899285419,
   1570341764013157,  # prime
   1637027521802551,  # prime
   1880450821379411,  # prime
   1893530391196711,  # prime
   2447109360961063,  # prime
   3,  # prime
   2772290760589219,  # prime
   3033700317376073,  # prime
   4350190374376723,
   4350190491008389,  # prime
   4350190491008390,
   4350222956688319,
   2447120421950803,
   5,  # prime
]


def is_prime(n):
    """отриммуємо прості числа"""

    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def primes_processpool(numbers):
    with ProcessPoolExecutor() as executor:
        return list(executor.map(is_prime, numbers))


"""
Task 2

Requests using concurrent and multiprocessing libraries

Download all comments from a subreddit of your choice using URL: https://api.pushshift.io/reddit/comment/search/ . 

As a result, store all comments in chronological order in JSON and dump it to a file. For this task use concurrent 
and multiprocessing libraries for making requests to Reddit API.
"""


if __name__ == '__main__':
    start_time = time()
    print(primes_processpool(NUMBERS))
    print(f"Час виконання: {time() - start_time} секунд")