# -*- coding: utf-8 -*-
import requests

"""
Task 1

Robots.txt

Download and save to file robots.txt from wikipedia, twitter websites etc.
"""


def download(url, name_file="robots.txt"):
    # відправляємо GET-запит до URL-адреси
    response = requests.get(url)

    # отримуємо вміст відповіді
    content = response.content

    # зберігаємо вміст до файлу
    with open(name_file, "wb") as f:
        f.write(content)


"""
Task 2

Load data

Download all comments from a subreddit of your choice using URL: https://api.pushshift.io/reddit/comment/search/ . 

As a result, store all comments in chronological order in JSON and dump it to a file.
"""

from pprint import pprint
import json


def get_list_user_reddit():
    url = f"https://api.pushshift.io/reddit/comment/search"
    response = requests.get(url)
    data = response.json()
    users = data['data']
    us = []
    for i in users:
        us.append(i.get("subreddit"))
    return us


def reddit(username):
    response = requests.get(url=f"https://api.pushshift.io/reddit/comment/search", params={
        "subreddit": username,
    })

    data = response.json()

    comments = data["data"]
    # pprint(comments)
    comments = sorted(comments, key=lambda x: x["created_utc"])
    with open("comments.json", "w") as f:
        json.dump(comments, f)


"""
Task 3

The Weather app

Write a console application which takes as an input a city name and returns current weather in 
the format of your choice. For the current task, you can choose any weather API or website or use openweathermap.org
"""
from bs4 import BeautifulSoup


def weather(city):
    url = f"https://sinoptik.ua/погода-{city}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.content
        html = BeautifulSoup(data, 'html.parser')
        for el in html.select('#content'):
            t_min = el.select('.temperature .min')[0].text
            t_max = el.select('.temperature .max')[0].text
            text = el.select('.wDescription .description')[0].text
        return "Привет, погода на сегодня:\n" + t_min + ', ' + t_max + '\n' + text
    else:
        print(response.status_code)


if __name__ == '__main__':
    print(f"{20 * '_'}\nTask 1\n")
    # встановлюємо URL-адресу до веб-сайту Twitter
    url = "https://twitter.com/robots.txt"
    download(url)

    print(f"{20 * '_'}\nTask 2\n")

    pprint(get_list_user_reddit())
    reddit("television")

    print(f"{20 * '_'}\nTask 3\n")
    print(weather("кропивницкий"))
