# -*- coding: utf-8 -*-
"""
Task 1

Practice asynchronous code

Create a separate asynchronous code to calculate Fibonacci, factorial, squares and cubic for an input number.
Schedule the execution of this code using asyncio.gather for a list of integers from 1 to 10. You need to get four
lists of results from corresponding functions.

Rewrite the code to use simple functions to get the same results but using a multiprocessing library.
Time the execution of both realizations, explore the results, what realization is more effective, why did you get a
 result like this.
"""

import asyncio
import time

async def fibonacci_async(n):
    if n <= 1:
        return n
    else:
        return await fibonacci_async(n - 1) + await fibonacci_async(n - 2)


async def factorial_async(n):
    if n == 0:
        return 1
    else:
        return n * await factorial_async(n - 1)


async def square_async(n):
    return n ** 2


async def cubic_async(n):
    return n ** 3


async def main():
    results_fibonacci = await asyncio.gather(
        *[fibonacci_async(i) for i in range(1, 11)]
    )
    results_factorial = await asyncio.gather(
        *[factorial_async(i) for i in range(1, 11)]
    )
    results_square = await asyncio.gather(
        *[square_async(i) for i in range(1, 11)]
    )
    results_cubic = await asyncio.gather(
        *[cubic_async(i) for i in range(1, 11)]
    )

    print("Fibonacci:", results_fibonacci)
    print("Factorial:", results_factorial)
    print("Square:", results_square)
    print("Cubic:", results_cubic)


import multiprocessing


def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


def square(n):
    return n ** 2


def cubic(n):
    return n ** 3


def compute_results():
    with multiprocessing.Pool() as pool:
        results_fibonacci = pool.map(fibonacci, range(1, 11))
        results_factorial = pool.map(factorial, range(1, 11))
        results_square = pool.map(square, range(1, 11))
        results_cubic = pool.map(cubic, range(1, 11))

    print("Fibonacci:", results_fibonacci)
    print("Factorial:", results_factorial)
    print("Square:", results_square)
    print("Cubic:", results_cubic)




"""
Task 2

Requests using asyncio and aiohttp

Download all comments from a subreddit of your choice using URL: https://api.pushshift.io/reddit/comment/search/ . 

As a result, store all comments in chronological order in JSON and dump them to a file. For this task use asyncio 
and aiohttp libraries for making requests to Reddit API.
"""

import aiohttp
import json

async def main_aiohttp(username):

    async with aiohttp.ClientSession() as session:
        async with session.get(url=f"https://api.pushshift.io/reddit/comment/search", params={
        "subreddit": username,
    })as response:

            data = await response.json()

            comments = data["data"]
            # pprint(comments)
            comments = sorted(comments, key=lambda x: x["created_utc"])
            with open("comments.json", "w") as f:
                json.dump(comments, f)



if __name__ == '__main__':
    print(f"{20 * '_'}\nTask 1\n")
    start_time_asyncio = time.time()
    asyncio.run(main())
    print("asyncio:", time.time() - start_time_asyncio)

    start_time_multi = time.time()
    compute_results()
    print("multiprocessing:", time.time() - start_time_multi)

    print(f"{20 * '_'}\nTask 2\n")
    asyncio.run(main_aiohttp("television"))


