# -*- coding: utf-8 -*-


"""

Реалізувати алгоритм бінарного пошуку за допомогою рекурсії.

Прочитати про Fibonacci search та імплементуйте його за допомогою Python. Визначте складність алгоритму та порівняйте його з бінарним пошуком
"""
import time

def timer(func):
    """Print the runtime of the decorated function"""
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()    # 1
        value = func(*args, **kwargs)
        end_time = time.perf_counter()      # 2
        run_time = (end_time - start_time) * 1000    # 3
        print(f"Finished {func.__name__!r} in {run_time:.4f} ms")
        return value
    return wrapper_timer

@timer
def bin_search(target, sequence, first, last):
    """
    Бінарний пошук - це алгоритм пошуку елементу в відсортованому масиві шляхом порівняння шуканого елементу з
    елементом в середині масиву і визначенням того, в якому напрямку продовжувати пошук.

    """
    if first > last:
        return False
    else:
        mid = (last + first) // 2
        if sequence[mid] == target:
            return True
        elif target < sequence[mid]:
            return bin_search(target, sequence, first, mid - 1)
        else:
            return bin_search(target, sequence, mid + 1, last)

@timer
def fibonacci_search(arr, x):
    n = len(arr)

    # Ініціалізація чисел Фібоначчі
    fib2 = 0
    fib1 = 1
    fib = fib2 + fib1

    # Знаходимо найбільше число Фібоначчі, що менше або дорівнює розміру масиву
    while fib < n:
        fib2 = fib1
        fib1 = fib
        fib = fib2 + fib1

    # Початкові значення "offset" і "mid"
    offset = -1
    while fib > 1:
        # Зменшуємо число Фібоначчі до меншого числа
        i = min(offset + fib2, n - 1)

        # Якщо елемент менший за середину, зменшуємо число Фібоначчі і використовуємо ліву частину масиву
        if arr[i] > x:
            fib = fib2
            fib1 = fib1 - fib2
            fib2 = fib - fib1
        # Якщо елемент більший за середину, зменшуємо число Фібоначчі і використовуємо праву частину масиву
        elif arr[i] < x:
            fib = fib1
            fib1 = fib2
            fib2 = fib - fib1
            offset = i
        # Якщо елемент знайдений, повертаємо індекс
        else:
            return True

    # Перевірка останнього елемента
    if fib1 and arr[offset + 1] == x:
        return offset + 1

    # Якщо елемент не знайдений, повертаємо -1
    return -1


if __name__ == "__main__":
    m = []
    for i in range(1000):
        m.append(i)
    import random
    rand_numb = random.randrange(1, 1000) # випадкове число від 1 до 1000
    print(bin_search(rand_numb, m, 0, len(m)))  # Логарифмічна складність - O(logn)

    print(fibonacci_search(m, rand_numb))  # Логарифмічна складність - O(logn)
