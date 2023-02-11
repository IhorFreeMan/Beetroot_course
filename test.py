# -*- coding: utf-8 -*-
from functools import wraps


def firstdec(func):
    @wraps(func)
    def wrep():
        print("first")
        func()
        print("twy")

    return wrep


@firstdec
def test():
    """Sam test"""
    print("test")


def add_brake_log(size=2):
    def add_break_log_dec(func):
        @wraps(func)
        def wrep(*args, **kwargs):
            for _ in range(size):
                print(('_' * 80))
            func(*args, **kwargs)
            for _ in range(size):
                print('_' * 80)

        return wrep

    return add_break_log_dec


@add_brake_log(size=1)
def test():
    """Sam test"""
    print("test")


def mas_a(a):

    def sam_b(b):
        sam_b.coun += 1
        return a * b
    sam_b.coun = 0
    return sam_b

import time
def time_f(f):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = f(*args, **kwargs)
        end = time.time()
        print(f.__name__, " took ", str((end - start)*1000) + " ms")
        return result
    return wrapper


@time_f
def skuea_number(skuea_list: list):
    m = []
    for i in skuea_list:
        m.append(i**2)
    return m


def my_decorator(func):
    def wrapper():
        print("До")
        func()
        print("після")
    return wrapper

import functools
def do_twice(func):
    @functools.wraps(func)
    def wrapper_do_twice(*args, **kwargs):
        func(*args, **kwargs)
        return func(*args, **kwargs)
    return wrapper_do_twice

# @my_decorator
# def say_whee():
#     print("Whee!")


@do_twice
def say_whee():
    print("Whee!")



def repeat(num_times):
    def decorator_repeat(func):
        @functools.wraps(func)
        def wrapper_repeat(*args, **kwargs):
            for _ in range(num_times):
                value = func(*args, **kwargs)
            return value
        return wrapper_repeat
    return decorator_repeat

# @do_twice
@repeat(num_times=4)
def greet(name):
    print(f"Hello {name}")

@do_twice
def return_greeting(name):
    print("Creating greeting")
    return f"Hi {name}"


def decorator(func):
    @functools.wraps(func)
    def wrapper_decorator(*args, **kwargs):
        # Do something before
        value = func(*args, **kwargs)
        # Do something after
        return value
    return wrapper_decorator

import time

def timer(func):
    """Print the runtime of the decorated function"""
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()    # 1
        value = func(*args, **kwargs)
        end_time = time.perf_counter()      # 2
        run_time = end_time - start_time    # 3
        print(f"Finished {func.__name__!r} in {run_time:.4f} secs")
        return value
    return wrapper_timer

@timer
def waste_some_time(num_times):
    for _ in range(num_times):
        sum([i**2 for i in range(10000)])



def debug(func):
    """Print the function signature and return value"""
    @functools.wraps(func)
    def wrapper_debug(*args, **kwargs):
        args_repr = [repr(a) for a in args]                      # 1
        kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]  # 2
        signature = ", ".join(args_repr + kwargs_repr)           # 3
        print(f"Calling {func.__name__}({signature})")
        value = func(*args, **kwargs)
        print(f"{func.__name__!r} returned {value!r}")           # 4
        return value
    return wrapper_debug




@debug
def make_greeting(name, age=None):
    if age is None:
        return f"Howdy {name}!"
    else:
        return f"Whoa {name}! {age} already, you are growing up!"



def slow_down(func):
    """Sleep 1 second before calling the function"""
    @functools.wraps(func)
    def wrapper_slow_down(*args, **kwargs):
        time.sleep(1)
        return func(*args, **kwargs)
    return wrapper_slow_down

@slow_down
def countdown(from_number):
    if from_number < 1:
        print("Liftoff!")
    else:
        print(from_number)
        countdown(from_number - 1)





def count_calls(func):
    @functools.wraps(func)
    def wrapper_count_calls(*args, **kwargs):
        wrapper_count_calls.num_calls += 1
        print(f"Call {wrapper_count_calls.num_calls} of {func.__name__!r}")
        return func(*args, **kwargs)
    wrapper_count_calls.num_calls = 0
    return wrapper_count_calls

@count_calls
def say_whee():
    print("Whee!")


@count_calls
def fibonacci(num):
    if num < 2:
        return num
    return fibonacci(num - 1) + fibonacci(num - 2)



def cache(func):
    """Keep a cache of previous function calls"""
    @functools.wraps(func)
    def wrapper_cache(*args, **kwargs):
        cache_key = args + tuple(kwargs.items())
        if cache_key not in wrapper_cache.cache:
            wrapper_cache.cache[cache_key] = func(*args, **kwargs)
        return wrapper_cache.cache[cache_key]
    wrapper_cache.cache = dict()
    return wrapper_cache

@cache
@count_calls
def fibonacci(num):
    if num < 2:
        return num
    return fibonacci(num - 1) + fibonacci(num - 2)

if __name__ == "__main__":
    # test.__name__
    # #print(test.__doc__)
    # help(test)

    # print(locals())
    # forst_decorator = firstdec(test)
    # forst_decorator()
    # test()
    # help(test)
    # test()
    # sam_c = mas_a(2)
    # sam_c(4)
    # sam_c(5)
    # sam_c(6)
    # print(sam_c.coun, "coun")
    # m = []
    # for i in range(100):
    #     m.append(i+1)
    #
    # decorator_f = skuea_number(m)
    # # print(m)
    # print(decorator_f)
    # say_whee()
    # greet("Ihor")
    # hi_adam = return_greeting("Adam")
    # print(hi_adam)

    # print(say_whee.__name__)
    # help(say_whee)

    # print(waste_some_time(99))

    # make_greeting("Ihor", 31)
    # countdown(3)
    # say_whee()
    # say_whee()
    # say_whee()
    print(fibonacci(10))
    pass
