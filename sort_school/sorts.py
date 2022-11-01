import streamlit as st
import time

def bubble(arr, x, t):
    i = 0
    flag = False
    min = 0
    while i < len(arr) - 1:
        if arr[i] > arr[i+1]:
            x.plot(arr)
            time.sleep(t)
            arr[i], arr[i+1] = arr[i+1], arr[i]
            flag = True
        i += 1
        if flag and i == len(arr) - 1:
            flag = False
            i = min
    x.plot(arr)
    time.sleep(t)
            

def selection(arr, x, t):
    for i in range(len(arr)):
        min_ind = i
        for j in range(i, len(arr)):
            cur_ind = j
            if arr[min_ind] > arr[cur_ind]:
                min_ind = cur_ind
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
        x.plot(B)
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
    for i in range(n-1, -1, -1):
        arr[i], arr[0] = arr[0], arr[i]  # swap
        heapify(arr, i, 0, x, t)

    if arr[0] > arr[2]:
        arr[0], arr[2] = arr[2], arr[0]
    x.plot(arr)
    time.sleep(t)

    if arr[0] > arr[1]:
        arr[0], arr[1] = arr[1], arr[0]
    x.plot(arr)
    time.sleep(t)


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

r = {
    "Bubble Sort": "O(n^2)",
    "Selection Sort": "O(n^2)",
    "Insertion Sort": "O(n^2)",
    "Cycle Sort": "O(n^2)",
    "Merge Sort": "O(nlog(n))",
    'Heap Sort': "O(nlog(n))",
    'Quick Sort': "O(n^2)",
}

a = {
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
    "Selection Sort": "Often the first attempt at writing a sorting algorithm",
    "Insertion Sort": "Easy to write and pragmatic to use",
    "Cycle Sort": "Moves each element at most once",
    "Merge Sort": "Recursion(Recursion(Recursion(Recursion(Recursion(Recursion...",
    'Heap Sort': "When in doubt, it's either hash or heap",
    'Quick Sort': "It's all in the name",
}

p = {
    "Bubble Sort": "A simple comparison based sorting algorithm that allows the largest elements to bubble to the top. \n\nWhile usually slower than other comparable runtime algorithms it works best for lists that are almost sorted.",
    "Selection Sort": "This algorithm picks the smallest element each time and moves it to the beginning. \n\n Slower on average because it needs to scan the remainder of the array each time.",
    "Insertion Sort": "Faster in implementation than selection because it moves each element down to its correct place. ",
    "Cycle Sort": "Used when writing to memory is costly, especially on expensive hardware. \n\nThe fastest algorithm in this app as it does not bottleneck the writing to screen process.",
    "Merge Sort": "Uses two arrays, one to split the array and sort a certain level, and the other to merge the previously split array into. \n\nThis provides an imcomplete view of only one array as a result.",
    'Heap Sort': "Takes advantage of heap properties to turn the array into a heap and then constantly extract the largest element. \n\nA smarter version of selection sort, this algorthim always has the same worst case scenario making it very desirable.",
    'Quick Sort': "A finnicky algorithm that repeatedly partitions the array based on a pivot. \n\n The science of choosing this pivot is complicated, but when done right, it is tough to beat.",
}
