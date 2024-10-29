import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from Lecture_1.Greedy_Algorithms import Food, buildMenu, testGreedys

"BRUTE FORCE ALGORITHMS"


def maxVal(toConsider, avail):
    """Assumes toConsider a list of items,
            avail a weight
    Returns a tuple of the total value of a
    solution to 0/1 knapsack problem and
    the items of that solution"""
    if toConsider == [] or avail == 0:
        result = (0, ())
    elif toConsider[0].getCost() > avail:
        # Explore right branch only
        result = maxVal(toConsider[1:], avail)
    else:
        nextItem = toConsider[0]
        # Explore left branch
        withVal, withToTake = maxVal(toConsider[1:], avail - nextItem.getCost())
        withVal += nextItem.getValue()
        # Explore right branch
        withoutVal, withoutToTake = maxVal(toConsider[1:], avail)
        # Explore better branch
        if withVal > withoutVal:
            result = (withVal, withToTake + (nextItem,))
        else:
            result = (withoutVal, withoutToTake)
    return result


def testMaxVal(foods, maxUnits, printItems=True):
    print("Use search tree to alocate", maxUnits, "calories")
    val, taken = maxVal(foods, maxUnits)
    print("Total value of items taken =", val)
    if printItems:
        for item in taken:
            print("  ", item)


names = ["wine", "beer", "pizza", "burger", "fries", "cola", "apple", "donut", "cake"]
values = [89, 90, 95, 100, 90, 79, 50, 10]
calories = [123, 154, 258, 354, 365, 150, 95, 195]
foods = buildMenu(names, values, calories)

testGreedys(foods, 750)
print("")
testMaxVal(foods, 750)
