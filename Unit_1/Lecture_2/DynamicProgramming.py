import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from Lecture_1.Greedy_Algorithms import Food
from Lecture_2.Recursive_Fibonacci import buildLargeMenu


def fastMaxVal(toConsider, avail, memo={}):
    """Assumes toConsider a list of subjects, avail a weight
    memo supplied by recursive calls
    Returns a tuple of the total value of a solution to the
    0/1 knapsack problemand the subjects of that solution"""
    if (len(toConsider), avail) in memo:
        result = memo[(len(toConsider), avail)]
    elif toConsider == [] or avail == 0:
        result(0, ())
    elif toConsider[0].getCost() > avail:
        # Explore the right branch only
        result = fastMaxVal(toConsider[1:], avail, memo)
    else:
        nextItem = toConsider[0]
        # Explore left branch
        withVal, withToTake = fastMaxVal(
            toConsider[1:], avail - nextItem.getCost(), memo
        )
        withVal += nextItem.getValue()
        # Explore right branch
        withoutVal, withoutToTake = fastMaxVal(toConsider[1:], avail, memo)
        # Choose better branch
        if withVal > withoutVal:
            result = (withVal, withToTake + (nextItem,))
        else:
            result = (withoutVal, withoutToTake)
    memo[(len(toConsider), avail)] = result
    return result


def testMaxVal(foods, maxUnits, algorithm, printItems=True):
    print("Menu contains", len(foods), "items")
    print("Use search tree to alocate", maxUnits, "calories")
    val, taken = algorithm(foods, maxUnits)
    if printItems:
        print("Total value of items taken =", val)
        for item in taken:
            print(" ", item)


for numItems in (5, 10, 15, 20, 25, 30, 35, 40, 45, 50):
    items = buildLargeMenu(numItems, 90, 250)
    testMaxVal(items, 750, fastMaxVal, False)
