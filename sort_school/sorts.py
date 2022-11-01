import streamlit as st
import time

def bubble(arr, x, t):
    i = 0
    flag = False
    while i < len(arr) - 1:
        if arr[i] > arr[i+1]:
            x.plot(arr)
            time.sleep(t)
            arr[i], arr[i+1] = arr[i+1], arr[i]
            flag = True
        i += 1
        if flag and i == len(arr) - 1:
            flag = False
            i = 0
    x.plot(arr)
    time.sleep(t)
            

def selection(arr, x, t):
    for i in range(len(arr)):
        min_ind = i
        for j in range(i, len(arr)):
            if arr[min_ind] > arr[j]:
                min_ind = j
        arr[min_ind], arr[i] = arr[i], arr[min_ind]
        x.plot(arr)
        time.sleep(t)

def insertion(arr, x, t):
    i = 0
    max_ind = 0
    while max_ind < len(arr) - 1:
        max_ind += 1
        i = max_ind
        while arr[i] < arr[i-1]:
            arr[i], arr[i-1] = arr[i-1], arr[i]
            x.plot(arr)
            time.sleep(t)
            i -= 1
            if i == 0:
                break

# Shellsort

# Mergesort
def merge(A, x, t):
    B = A.copy()
    bottomUpMergeSort(A, B, x, t)

def bottomUpMergeSort(A, B, x, t):
    width = 1
    while width < len(A):
        i = 0
        while i < len(A):
            bottomUpMerge(A, i, min(i+width, len(A)), min(i+2*width, len(A)), B, x, t)
            i += 2 * width
        A, B = B, A
        width *= 2

def bottomUpMerge(A, iLeft, iRight, iEnd, B, x, t):
    i, j = iLeft, iRight
    # While there are elements in the left or right runs...
    for k in range(iLeft, iEnd):
        # If left run head exists and is <= existing right run head.
        if i < iRight and (j >= iEnd or A[i] <= A[j]):
            B[k] = A[i]
            i += 1
        else:
            B[k] = A[j]
            j += 1
        x.plot(B, A)
        time.sleep(t)
    

# Quicksort
def quick(arr, x, t):
    quicksort(arr, 0, len(arr)-1, x, t)

# Sorts a (portion of an) array, divides it into partitions, then sorts those
def quicksort(A, lo, hi, x, t):
  if lo >= 0 and hi >= 0 and lo < hi:
    p = partition(A, lo, hi, x, t) 
    quicksort(A, lo, p, x, t) # Note: the pivot is now included
    quicksort(A, p + 1, hi, x, t) 

# Divides array into two partitions
def partition(A, lo, hi, x, t):
  # Pivot value
  pivot = A[(hi + lo) // 2] # The value in the middle of the array

  # Left index
  i = lo - 1 

  # Right index
  j = hi + 1

  while True:
    # Move the left index to the right at least once and while the element at
    # the left index is less than the pivot
    i += 1
    while A[i] < pivot:
        i += 1
    
    # Move the right index to the left at least once and while the element at
    # the right index is greater than the pivot
    j -= 1
    while A[j] > pivot:
        j -= 1

    # If the indices crossed, return
    if i >= j:
        return j
    
    # Swap the elements at the left and right indices
    A[i], A[j] = A[j], A[i]
    x.plot(A)
    time.sleep(t)

# Heapsort 
def heap(arr, x, t):
    n = len(arr)
  
    # Build a maxheap.
    for i in range(n//2 - 1, -1, -1):
        heapify(arr, n, i, x, t)
  
    # One by one extract elements
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # swap
        x.plot(arr)
        time.sleep(t)
        heapify(arr, i, 0, x, t)


def heapify(arr, n, i, x, t):
    largest = i  # Initialize largest as root
    l = 2 * i + 1     # left = 2*i + 1
    r = 2 * i + 2     # right = 2*i + 2
  
    # See if left child of root exists and is
    # greater than root
    if l < n and arr[largest] < arr[l]:
        largest = l
  
    # See if right child of root exists and is
    # greater than root
    if r < n and arr[largest] < arr[r]:
        largest = r
  
    # Change root, if needed
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # swap
        x.plot(arr)
        time.sleep(t)
        # Heapify the root.
        heapify(arr, n, largest, x, t)


def cycle(vector, x, t):
    "Sort a vector in place and return the number of writes."
    writes = 0
 
    # Loop through the vector to find cycles to rotate.
    for cycleStart, item in enumerate(vector):
 
        # Find where to put the item.
        pos = cycleStart
        for item2 in vector[cycleStart + 1:]:
            if item2 < item:
                pos += 1
 
        # If the item is already there, this is not a cycle.
        if pos == cycleStart:
            continue
 
        # Otherwise, put the item there or right after any duplicates.
        while item == vector[pos]:
            pos += 1
        vector[pos], item = item, vector[pos]
        writes += 1
        x.plot(vector)
        time.sleep(t)

        # Rotate the rest of the cycle.
        while pos != cycleStart:
 
            # Find where to put the item.
            pos = cycleStart
            for item2 in vector[cycleStart + 1:]:
                if item2 < item:
                    pos += 1
 
            # Put the item there or right after any duplicates.
            while item == vector[pos]:
                pos += 1
            vector[pos], item = item, vector[pos]
            writes += 1
            x.plot(vector)
            time.sleep(t)
 
    return writes


d = {
    "Bubble Sort": bubble,
    "Selection Sort": selection,
    "Insertion Sort": insertion,
    "Cycle Sort": cycle,
    "Merge Sort": merge,
    'Heap Sort': heap,
    'Quick Sort': quick,
}

worst = {
    "Bubble Sort": r'''
    O(n^2)
    ''',
    "Selection Sort": "O(n^2)",
    "Insertion Sort": "O(n^2)",
    "Cycle Sort": "O(n^2)",
    "Merge Sort": "O(nlog(n))",
    'Heap Sort': "O(nlog(n))",
    'Quick Sort': "O(n^2)",
}

average = {
    "Bubble Sort": "O(n^2)",
    "Selection Sort": "O(n^2)",
    "Insertion Sort": "O(n^2)",
    "Cycle Sort": "O(n^2)",
    "Merge Sort": "O(nlog(n))",
    'Heap Sort': "O(nlog(n))",
    'Quick Sort': "O(nlog(n))",
}

s = {
    "Bubble Sort": "One of the first sorts you'll probably learn",
    "Selection Sort": "Probably your first attempt at sorting!",
    "Insertion Sort": "Easy to write and pragmatic to use",
    "Cycle Sort": "Moves each element at most once",
    "Merge Sort": "Recursion(Recursion(Recursion(Recursion(Recursion...",
    'Heap Sort': "When in doubt, it's either a hash or a heap",
    'Quick Sort': "It's all in the name",
}

p = {
    "Bubble Sort": 
    """
    A simple repeated pass comparison based sorting algorithm that allows the largest elements to gradually bubble to the top. 
    While usually slower than other comparable runtime algorithms it works best for lists that are almost sorted.
    """,
    "Selection Sort": 
    """
    This algorithm picks the smallest element each time and moves it to the beginning. 
    This tends to be slower because it needs to scan the remainder of the array each time to find the next smallest element and 
    so it always takes n(n-1)/2 comparisons.
    """,
    "Insertion Sort": 
    """
    This tends to be faster in implementation than selection sort because it builds am ascending portion of the array and moves each new 
    element down to its correct place which will not be the beginning in most cases.
    As a result, it takes fewer than n(n-1)/2 comparisons though it has the same worst case scenario.
    """,
    "Cycle Sort": 
    """
    This algorithm is used when writing to memory is costly, because it only moves each element once into its rightful place.
    As a result, it is probably the fastest algorithm in this app as it does not bottleneck the rendering with multiple updates to the screen.
    """,
    "Merge Sort": 
    """
    Merge sort uses two arrays, one that recursively splits and sorts the array, 
    and the other one to merge the previously split array into.
    The array to the left is the result of the partitions of the array to the right being merged together.
    """,
    'Heap Sort': """
    This algorithm takes advantage of the speed of building a heap to turn the array into a heap in place. 
    It then constantly extracts the largest element and moves it to the end.
    Since the algorithm performs similarly with all inputs, it is very reliable.
    """,
    'Quick Sort': 
    """
    This algorithm partitions the array based on a pivot value, and then recursively does the same to the new subpartitions. 
    If the pivot value is chosen so that it can equally divide the array, this algorithm can be very fast, but it's hard to figure out
    that pivot value without sorting the array. Choosing the element in the middle of the array works well enough most of the time 
    (close to random choice, but better for almost sorted cases).
    """,
}

code = {
    "Bubble Sort": 
    """
    def bubble(arr):
    i = 0
    flag = False
    min = 0
    while i < len(arr) - 1:
        if arr[i] > arr[i+1]: # if the current element is greater than the next
            arr[i], arr[i+1] = arr[i+1], arr[i] # swap (or bubble it up!)
            flag = True # track that something was bubbled in this run
        i += 1
        if flag and i == len(arr) - 1: # if something was bubbled in the last run, we check the whole array again
            flag = False 
            i = 0
        # we exit this loop only if we finish an iteration without bubbling anything (which means the array is sorted!)
    """,

    "Selection Sort": 
    """
    def selection(arr):
    for i in range(len(arr)): # i is the lowest position that is not sorted
        min_ind = i # the index of the smallest value in the array
        for j in range(i, len(arr)): # iterate over the remainder of the array
            if arr[min_ind] > arr[j]: # we have a new smallest value
                min_ind = j
        arr[min_ind], arr[i] = arr[i], arr[min_ind] # swap the smallest value into the lowest position
    """,

    "Insertion Sort": 
    """
    def insertion(arr):
    i = 0
    max_ind = 0 # stores the rightmost position of the ascending array
    while max_ind < len(arr) - 1:
        max_ind += 1
        i = max_ind
        while arr[i] < arr[i-1]: # if the new element is not in the right place
            arr[i], arr[i-1] = arr[i-1], arr[i] # move it down until it fits in the order
            i -= 1 
            if i == 0: # stop moving it down if it is the smallest element
                break
    """,

    "Cycle Sort": 
    """
    def cycle(vector):
    "Sort a vector in place and return the number of writes."
    writes = 0
 
    # Loop through the vector to find cycles to rotate.
    for cycleStart, item in enumerate(vector):
 
        # Find where to put the item.
        pos = cycleStart
        for item2 in vector[cycleStart + 1:]:
            if item2 < item:
                pos += 1
 
        # If the item is already there, this is not a cycle.
        if pos == cycleStart:
            continue
 
        # Otherwise, put the item there or right after any duplicates.
        while item == vector[pos]:
            pos += 1
        vector[pos], item = item, vector[pos]
        writes += 1

        # Rotate the rest of the cycle.
        while pos != cycleStart:
 
            # Find where to put the item.
            pos = cycleStart
            for item2 in vector[cycleStart + 1:]:
                if item2 < item:
                    pos += 1
 
            # Put the item there or right after any duplicates.
            while item == vector[pos]:
                pos += 1
            vector[pos], item = item, vector[pos]
            writes += 1
 
    return writes
    """,
    "Merge Sort": 
    """
def merge(A):
    B = A.copy()
    bottomUpMergeSort(A, B)

def bottomUpMergeSort(A, B):
    width = 1
    while width < len(A):
        i = 0
        while i < len(A):
            bottomUpMerge(A, i, min(i+width, len(A)), min(i+2*width, len(A)), B)
            i += 2 * width
        A, B = B, A
        width *= 2

def bottomUpMerge(A, iLeft, iRight, iEnd, B):
    i, j = iLeft, iRight
    # While there are elements in the left or right runs...
    for k in range(iLeft, iEnd):
        # If left run head exists and is <= existing right run head.
        if i < iRight and (j >= iEnd or A[i] <= A[j]):
            B[k] = A[i]
            i += 1
        else:
            B[k] = A[j]
            j += 1
    """,

    'Heap Sort': 
    """
    def heap(arr):
    n = len(arr)
  
    # Build a maxheap.
    for i in range(n//2 - 1, -1, -1):
        heapify(arr, n, i)
  
    # One by one extract elements
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # swap
        heapify(arr, i, 0)


    def heapify(arr, n, i):
    largest = i  # Initialize largest as root
    l = 2 * i + 1     # left = 2*i + 1
    r = 2 * i + 2     # right = 2*i + 2
  
    # See if left child of root exists and is
    # greater than root
    if l < n and arr[largest] < arr[l]:
        largest = l
  
    # See if right child of root exists and is
    # greater than root
    if r < n and arr[largest] < arr[r]:
        largest = r
  
    # Change root, if needed
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # swap
        # Heapify the root.
        heapify(arr, n, largest)
    """,

    'Quick Sort': 
    """
    # Quicksort wrapper function
    def quick(arr):
        quicksort(arr, 0, len(arr)-1)

    # Sorts a (portion of an) array, divides it into partitions, then sorts those
    def quicksort(A, lo, hi):
        if lo >= 0 and hi >= 0 and lo < hi:
            p = partition(A, lo, hi) 
            quicksort(A, lo, p) # Note: the pivot is now included
            quicksort(A, p + 1, hi) 

    # Divides array into two partitions while maintaining relative ordering
    def partition(A, lo, hi):
        # Pivot value
        pivot = A[(hi + lo) // 2] # The value in the middle of the array

        # Left index
        i = lo - 1 

        # Right index
        j = hi + 1

        while True:
            # Move the left index to the right at least once and while the element at
            # the left index is less than the pivot
            i += 1
            while A[i] < pivot:
                i += 1
            
            # Move the right index to the left at least once and while the element at
            # the right index is greater than the pivot
            j -= 1
            while A[j] > pivot:
                j -= 1
                # If the indices crossed, return
            if i >= j:
                return j
            
            # Swap the elements at the left and right indices
            A[i], A[j] = A[j], A[i]
    """,
}   
