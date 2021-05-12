def sortArray(theList: list):
    quickSort(theList, 0, len(theList) - 1)
    return None


def quickSort(theList: list, first, last):
    if first < last:
        q = partition(theList, first, last)
        quickSort(theList, first, q - 1)
        quickSort(theList, q + 1, last)


def partition(theList: list, first, last):
    lastS1 = first
    firstUnknown = first + 1
    while firstUnknown <= last:
        if theList[firstUnknown] < theList[first]:
            theList[firstUnknown], theList[lastS1] = theList[lastS1], theList[firstUnknown]
        firstUnknown = firstUnknown + 1
    theList[first], theList[lastS1] = theList[lastS1], theList[first]
    return lastS1
