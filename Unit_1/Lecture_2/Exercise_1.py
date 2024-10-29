def yieldAllCombos(items):
    """
    Generates all combinations of N items into two bags, whereby each
    item is in one or zero bags.

    Yields a tuple, (bag1, bag2), where each bag is represented as
    a list of which item(s) are in each bag.
    """

    N = len(items)
    # enumerate the 2**N possible combinations
    for i in range(2**N):
        combo1 = []
        for j in range(N):
            # test bit jth of integer i
            if (i >> j) % 2 == 1:
                combo1.append(items[j])
        lista1 = [element for element in items if element not in combo1]
        M = len(lista1)
        for k in range(2**M):
            combo2 = []
            for m in range(M):
                if (k >> m) % 2 == 1:
                    combo2.append(lista1[m])
            yield combo1, combo2
