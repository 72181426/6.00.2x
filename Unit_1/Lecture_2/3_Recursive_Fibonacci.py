import sys
import os
import random

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from Lecture_1.Greedy_Algorithms import Food
from Lecture_2.1_Brute_Force_Algorithms import testMaxVal


"CODE TO TRY LARGER EXAMPLES"


def buildLargeMenu(numItems, maxVal, maxCost):
    items = []
    for i in range(numItems):
        items.append(
            Food(str(i), random.randint(1, maxVal), random.randint(1, maxCost))
        )
    return items


for numItems in (5, 10, 15, 20, 25, 30, 35, 40, 45):
    items = buildLargeMenu(numItems, 90, 250)
    testMaxVal(items, 750, False)


"RECURSIVE IMPLEMENTATION OF FIBONACCI"


def fib(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


"USING A MEMO TO COMPUTE FIBONNACI"


def fastFib(n, memo={}):
    """Assumes n is an int >= 0, memo used only by
    recursive calls
    Returns Fibonacci of n"""
    if n == 0 or n == 1:
        return 1
    try:
        return memo[n]
    except KeyError:
        result = fastFib(n - 1, memo) + fastFib(n - 2, memo)
        memo[n] = result
        return result


for i in range(121):
    print("fib(" + str(i) + ") =", fastFib(i))
