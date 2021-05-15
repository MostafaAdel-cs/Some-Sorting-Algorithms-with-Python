import time
from SortingO_N2 import BubbleSort
from SortingO_N2 import InsertionSort
from SortingO_N2 import SelectionSort
from SortingO_NLog_N import Heap
from SortingO_NLog_N import MergeSort
from SortingO_NLog_N import QuickSort
import sys
import numpy as np

# adjust n to for different array sizes
n = 100000
randNums = np.random.randint(0, 100, n)

print('O(n^2) Algorithms times:')
theList = randNums.copy()
start = time.time()
BubbleSort.sortArray(theList)
end = time.time()
print(f'\tBubble Sort: {end - start}')

theList = randNums.copy()
start = time.time()
InsertionSort.sortArray(theList)
end = time.time()
print(f'\tInsertion Sort: {end - start}')

theList = randNums.copy()
start = time.time()
SelectionSort.sortArray(theList)
end = time.time()
print(f'\tSelection Sort: {end - start}')

print('======================================================')

print('O(n*log(n)) Algorithms times:')

theList = randNums.copy()
start = time.time()
Heap.heapSort(theList)
end = time.time()
print(f'\tHeap Sort: {end - start}')

theList = randNums.copy()
start = time.time()
MergeSort.sortArray(theList)
end = time.time()
print(f'\tMerge Sort: {end - start}')

theList = randNums.copy()
start = time.time()
QuickSort.sortArrayRecursively(theList)
end = time.time()
print(f'\tQuick Recursively Sort: {end - start}')

# uncomment to see iterative quick sort but it is slow
# due to not optimizing at low values of n
# use insertion sort when n gets low

"""
theList = randNums.copy()
start = time.time()
QuickSort.sortArrayIteratively(theList)
end = time.time()
print(f'\tQuick Iteratively Sort: {end - start}')
"""
