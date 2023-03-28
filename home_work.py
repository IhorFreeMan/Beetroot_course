# -*- coding: utf-8 -*-
"""
Task 1

A bubble sort can be modified to “bubble” in both directions. The first pass moves “up” the list and
the second pass moves “down.” This alternating pattern continues until no more passes are necessary.
Implement this variation and describe under what circumstances it might be appropriate.
"""


def bidirectional_bubble_sort(A):
    n = len(A)
    left = 0
    right = n - 1
    while left < right:
        # Move "up" the list
        for i in range(left, right):
            if A[i] > A[i + 1]:
                A[i], A[i + 1] = A[i + 1], A[i]
        right -= 1
        # Move "down" the list
        for i in range(right, left, -1):
            if A[i] < A[i - 1]:
                A[i], A[i - 1] = A[i - 1], A[i]
        left += 1
    return A


"""
Task 2

Implement the mergeSort function without using the slice operator.
"""


def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2

        left_half = []
        for i in range(mid):
            left_half.append(arr[i])

        right_half = []
        for i in range(mid, len(arr)):
            right_half.append(arr[i])

        # сортуємо ліву та праву половини списку рекурсивно
        merge_sort(left_half)
        merge_sort(right_half)

        # об'єднуємо результати
        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

    return arr


"""
Task 3

One way to improve the quicksort is to use an insertion sort on lists that are small in length 
(call it the “partition limit”). Why does this make sense? Re-implement the quicksort and use it to sort 
a random list of integers. Perform analysis using different list sizes for the partition limit.
"""


def quicksort(arr, partition_limit=6):
    if len(arr) <= 1:
        return arr

    if len(arr) <= partition_limit:
        return insertion_sort(arr)

    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quicksort(left) + middle + quicksort(right)

def insertion_sort(array):
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1
        while j >= 0 and array[j] > key:
            array[j+1] = array[j]
            j -= 1
        array[j+1] = key
    return array


if __name__ == '__main__':
    # print(f"{20 * '_'}\nTask 1\n")
    m = [3, 2, 1, 5, 4, 7, 6, 8, 9, 10]
    # # годиться коли список майже відсортований вже з самого початку
    # print(bidirectional_bubble_sort(m))
    #
    # print(f"{20 * '_'}\nTask 2\n")
    # print(merge_sort(m))

    print(f"{20 * '_'}\nTask 3\n")
    """
    Сортування вставками має менший накладний розхід, ніж швидке сортування, що означає, що воно працює швидше для 
    невеликих списків. Швидке сортування має найгірший часовий складність O(n^2), який може відбуватися, 
    коли опорний елемент вибраний або найменший, або найбільший елемент у списку, і список вже відсортований 
    або майже відсортований. Сортування вставками також має найгірший часовий складність O(n^2), але 
    воно працює краще, ніж швидке сортування, коли список майже відсортований.
    """
    import random
    test_list = [random.randint(1, 100) for _ in range(23)]
    sorted_list = quicksort(test_list)
    print(sorted_list)
