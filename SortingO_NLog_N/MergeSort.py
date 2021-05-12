def sortArray(theList: list):
    MergeSort(theList, 0, len(theList) - 1)
    return None


def MergeSort(theList: list, first, last):
    if first < last:
        mid = (first + last) // 2
        MergeSort(theList, first, mid)
        MergeSort(theList, mid + 1, last)
        left = []
        right = []
        for i in range(first, mid + 1):
            left.append(theList[i])
        for i in range(mid + 1, last + 1):
            right.append(theList[i])
        merge(left, right, theList, first)
    return None


# argument locationOfInsertion if not given the arrays will be merged in index 0 of original array
def merge(left: list, right: list, theList: list, locationOfInsertion=0):
    nL, nR = len(left), len(right)
    i, j, k = 0, 0, locationOfInsertion
    while i < nL and j < nR:
        if left[i] <= right[j]:
            theList[k], i, k = left[i], i + 1, k + 1
        else:
            theList[k], j, k = right[j], j + 1, k + 1
    while i < nL:
        theList[k], i, k = left[i], i + 1, k + 1
    while j < nR:
        theList[k], j, k = right[j], j + 1, k + 1
    return None
