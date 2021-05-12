def heapSort(theList: list):
    buildMaxHeap(theList)
    size = len(theList)
    for i in range(len(theList)-1, 0, -1):
        theList[0], theList[i] = theList[i], theList[0]
        size = size - 1
        maxHeapify(theList, 0, size)
    return None


def buildMaxHeap(theList: list):
    for i in range(len(theList) // 2, -1, -1):
        maxHeapify(theList, i)
    return None


def maxHeapify(theList: list, i, size=0):
    l = left(i)
    r = right(i)
    if size == 0:
        size = len(theList)
    if l <= size - 1 and theList[l] > theList[i]:
        largest = l
    else:
        largest = i
    if r <= size - 1 and theList[r] > theList[largest]:
        largest = r
    if largest != i:
        theList[i], theList[largest] = theList[largest], theList[i]
        maxHeapify(theList, largest, size)
    return None


def left(i):
    return 2 * i + 1


def right(i):
    return 2 * i + 2
