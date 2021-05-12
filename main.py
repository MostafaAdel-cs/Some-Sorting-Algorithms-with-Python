import time
from SortingO_N2 import InsertionSort
from SortingO_NLog_N import MergeSort
import sys

p=[6,3,9,1,5,4,7,2]
l=[1,3,6,9]
r=[2,4,5,7]
z=[1,2,3,4,5,6,7,8]

MergeSort.sortArray(p)
print('====================')
for i in p:
    print(i)
