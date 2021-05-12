def SortArray( theList ):
    n=len(theList)
    for i in range(1,n):
        key=theList[i]
        hole=i
        while hole>0 and theList[hole-1]>key:
            theList[hole]=theList[hole-1]
            hole=hole-1
        theList[hole]=key
    return None