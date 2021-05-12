def sortArray(theList: list):
    n = len(theList)
    for i in range(0, n - 1):
        iMin = i
        for j in range(i + 1, n):
            if theList[j] < theList[iMin]:
                iMin = j
        if i != iMin:
            theList[i], theList[iMin] = theList[iMin], theList[i]
    return None
