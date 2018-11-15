import math

array = []

with open("qs.in", "r") as infile:
    for line in infile:
        array.append(int(line))

comparisons = 0
def quickSort(l, r):
    global comparisons
    if l >= r-1: return
    subjects = [[array[l], l], [array[r-1], r-1], [array[math.ceil((r-l)/2)-1+l], math.ceil((r-l)/2)-1+l]]
    subjects.sort()
    pivot = subjects[0][1] #can be any of the items depending on which element is wanted
    array[pivot], array[l] = array[l], array[pivot]
    pivot = l
    j = l+1
    for i in range(l+1, r):
        if array[i] < array[pivot]: 
            array[j], array[i] = array[i], array[j]
            j += 1
    pos = array[pivot]-1
    array[pivot], array[pos] = array[pos], array[pivot]
    if (array[pos] != l): 
        adder = array[pos]-1-l-1
        if adder > 0:
            comparisons += (array[pos]-1-l)-1
        quickSort(l, array[pos]-1)
    if (array[pos] != r): 
        adder = r-array[pos]-1
        if adder > 0:
            comparisons += (r-array[pos])-1
        quickSort(array[pos], r)


comparisons += len(array)-1
quickSort(0, len(array))

print(comparisons)