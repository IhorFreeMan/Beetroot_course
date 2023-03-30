# -*- coding: utf-8 -*-
import threading

"""
Task 1

A shared counter

Make a class called Counter, and make it a subclass of the Thread class in the Threading module.
Make the class have two global variables, one called counter set to 0, and another called rounds set to 100.000.
Now implement the run() method, let it include a simple for-loop that iterates through rounds (e.i. 100.000 times)
and for each time increments the value of the counter by 1. Create 2 instances of the thread and start them, then
join them and check the result of the counter, it should be 200.000, right? Run it a couple of times and consider
some different reasons why you get the answer that you get.
"""

class Counter(threading.Thread):
    counter = 0
    rounds = 100000

    def run(self):
        for i in range(self.rounds):
            Counter.counter += 1

    def __repr__(self):
       return str(Counter.counter)



"""
Task 2

Echo server with threading

Create a socket echo server which handles each connection in a separate Thread
"""


"""
Task 3

Requests using multiprocessing

Download all comments from a subreddit of your choice using URL: https://api.pushshift.io/reddit/comment/search/ . 

As a result, store all comments in chronological order in JSON and dump it to a file. For this task use Threads for making requests to reddit API.


"""
import requests
import json
from multiprocessing.pool import ThreadPool



def download_comments():
    url = f"https://api.pushshift.io/reddit/comment/search"
    response = requests.get(url)
    data = response.json()
    comments = data['data']
    return comments



if __name__ == '__main__':
    print(f"{20 * '_'}\nTask 1\n")
    thread1 = Counter()
    thread2 = Counter()

    thread1.start()
    thread2.start()

    print(Counter())

    print(f"{20 * '_'}\nTask 3\n")

    t = download_comments()
    subreddit = t[0].get("subreddit")  # беремо першого subreddit
    print(subreddit)
    # print(t[2].get("subreddit"))
    # print(t[2].get("created_utc"))
    # print(t[2].get("body"))

    comments = ThreadPool(4).map(download_comments, [subreddit] * 4)
    print(comments)
    # all_comments = [comment for sublist in comments for comment in sublist]
    # all_comments = sorted(all_comments, key=lambda x: x['created_utc'])
    # with open(f"{subreddit}_comments.json", "w") as f:
    #     json.dump(all_comments, f)