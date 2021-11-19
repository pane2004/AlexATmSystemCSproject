#Insertion Sort
def insertSort(array, compare):
    for i in range(1, len(array)):
        key = array[i]
        j = i

        while j > 0 and compare(array[j-1], key):
            array[j] = array[j-1]
            j -= 1
        array[j] = key
    
    return array

#Selection Sort
def selectionSort(array, compare):
    for i in range(len(array)):
        key = i
        for j in range (i+1, len(array)):
            if compare(array[key], array[j]):
                key = j 
        array[i], array[key] = array[key], array[i]
    return array

#Binary Search
def binarySearch(array, target, start, end):
    if start > end:
        return -1
    
    mid = (start + end)//2
    if array[mid]._user == target:
        return mid
    
    if target < array[mid]._user:
        return binarySearch(array, target, start, mid-1)
    else: 
        return binarySearch(array, target, mid+1, end)
    
#Linear Search
def linearSearch(array, target):
    for i in range(0, len(array)-1):
        if array[i]._user == target:
            return i
    return -1