from sys import getrecursionlimit, setrecursionlimit
from timeit import timeit

setrecursionlimit(2000)
print(getrecursionlimit())

def factorial(n):
    print(f"factorial() called with n = {n}")
    return_value = 1 if n <= 1 else n * factorial(n -1)
    print(f"-> factorial({n}) returns {return_value}")
    return return_value


def factorial_iteratively (n):
    return_value = 1
    for i in range(2, n + 1):
        return_value *= i
    return return_value


setup_string = """
def factorial(n):
    return 1 if n <= 1 else n * factorial(n - 1)
"""

print(f"Recursive: {timeit("factorial(4)"), setup=setup_string, number=10000000}")

setup_string = """
def factorial(n):
    return_value = 1
    for i in range(2, n + 1):
        return_value *= i
    return return_value
"""

print(f"Iterative: {timeit("factorial(4)"), setup=setup_string, number=10000000}")


def is_palindrome(word):
    """Return True if word is a palindrome, False if not."""
    if len(word) <= 1:
        return True
    else:
        return word[0] == word[-1] and is_palindrome(word[1:-1])
    

import statistics

def quicksort(numbers):
    if len(numbers) <= 1:
        return numbers
    else:
        pivot = statistics.median(
            [
                numbers[0],
                numbers[len(numbers) // 2],
                numbers[-1]
            ]
        )
        items_less, pivot_items, items_greater = (
            [n for n in numbers if n < pivot],
            [n for n in numbers if n == pivot],
            [n for n in numbers if n > pivot]
        )

        return (
            quicksort(items_less) +
            pivot_items +
            quicksort(items_greater)
        )