from random import randint
from time import time
import numpy as np
from timeit import repeat

ARRAY_LEN = 10000


def time_algo(algo, array):
    setup_code = f"from __main__ import {algo}" \
        if algo != "sorted" else ""

    stmt = f"{algo}({array})"

    times = repeat(setup=setup_code, stmt=stmt, repeat=3, number=10)

    print(f"Algorithm: {algo}. Minimum execution time: {min(times)}")


def bubble_sort(array):
    n = len(array)

    for i in range(n):
        sort_complete = True

        for j in range(n - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                sort_complete = False

        if sort_complete:
            break

    return array


def insert_sort(array):
    for i in range(1, len(array)):
        item_to_sort = array[i]
        j = i - 1

        while j >= 0 and array[j] > item_to_sort:
            array[j + 1] = array[j]
            j -= 1

        array[j + 1] = item_to_sort

    return array


def merge_arrays(left, right):
    if len(left) == 0:
        return right

    if len(right) == 0:
        return left

    result = []
    index_left = index_right = 0

    while len(result) < len(left) + len(right):
        if left[index_left] < right[index_right]:
            result.append(left[index_left])
            index_left += 1
        else:
            result.append(right[index_right])
            index_right += 1

        if index_right == len(right):
            result += left[index_left:]
            break

        if index_left == len(left):
            result += right[index_right:]
            break

    return result


def merge_sort(array):
    if len(array) < 2:
        return array

    midpoint = len(array) // 2

    return merge_arrays(
        left=merge_sort(array[:midpoint]),
        right=merge_sort(array[midpoint:])
    )


def quicksort(array):
    if len(array) < 2:
        return array

    low, same, high = [], [], []

    pivot_elem = array[randint(0, len(array) - 1)]

    for i in array:
        if i < pivot_elem:
            low.append(i)
        elif i == pivot_elem:
            same.append(i)
        elif i > pivot_elem:
            high.append(i)

    return quicksort(low), same, quicksort(high)


def main():
    random_array = [randint(0, 1000) for i in range(ARRAY_LEN)]

    # time_algo("NAME OF SORT ALGO HERE", random_array)


if __name__ == "__main__":
    main()
