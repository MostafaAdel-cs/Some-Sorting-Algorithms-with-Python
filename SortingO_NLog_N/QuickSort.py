import random


def sortArrayRecursively(theList: list):
    quickSort(theList, 0, len(theList) - 1)
    return None


# optimized using tail recursion and randomizing pivot
def quickSort(theList: list, first, last):
    if first < last:
        pivot = randomPartition(theList, first, last)
        if pivot - first < pivot - last:
            quickSort(theList, first, pivot - 1)
            first = pivot + 1
        else:
            quickSort(theList, pivot + 1, last)
            last = pivot - 1
    return None


def sortArrayIteratively(theList: list):
    iterativeQuickSort(theList, 0, len(theList) - 1)
    return None


def iterativeQuickSort(theList: list, first, last):
    stack = [None] * len(theList)
    # Allocating stack size
    top = -1
    stack.append(first)
    stack.append(last)
    top = top + 2
    while top >= 0:

        l = stack.pop()
        f = stack.pop()
        top = top - 2
        p = partition(theList, f, l)

        if p - 1 > f:
            stack.append(first)
            stack.append(p - 1)
            top = top + 2
        if p + 1 < l:
            stack.append(p + 1)
            stack.append(last)
            top = top + 2
    return None


def randomPartition(theList: list, first, last):
    i = random.randint(first, last)
    theList[last], theList[i] = theList[i], theList[last]
    return partition(theList, first, last)


def partition(theList: list, first, last):
    pivot = theList[last]
    i = first - 1
    for j in range(first, last):
        if theList[j] <= pivot:
            i = i + 1
            theList[i], theList[j] = theList[j], theList[i]
    theList[i + 1], theList[last] = theList[last], theList[i + 1]
    return i + 1
