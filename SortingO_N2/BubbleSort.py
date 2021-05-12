def SortArray( theList ):
    n=len( theList )
    for i in range(1,n):
        flag=0
        for j in range(0,n-i):
            if theList[j]>theList[j+1]:
                theList[j],theList[j+1]=theList[j+1],theList[j]
                flag=1
        if flag==0:
            break
    return None