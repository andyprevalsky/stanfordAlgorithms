import heapq

medianz = []
res = 0

with open("./median.txt", "r") as infile:
    maxHeap = []
    minHeap = []
    count = 0

    v1 = int(infile.readline())
    medianz.append(v1)
    res += v1

    v2 = int (infile.readline())
    if (v1 > v2): v1, v2 = v2, v1 
    medianz.append(v1)
    res += v1


    heapq.heappush(maxHeap, -v1)
    heapq.heappush(minHeap, v2)
    for line in infile:
        v = int(line)
        maxTop = -heapq.nsmallest(1, maxHeap)[0]
        if (v > maxTop): heapq.heappush(minHeap, v)
        else: heapq.heappush(maxHeap, -v)
        if (len(maxHeap) > len(minHeap) + 1): heapq.heappush(minHeap, -heapq.heappop(maxHeap))
        elif (len(minHeap) > len(maxHeap) + 1): heapq.heappush(maxHeap, -heapq.heappop(minHeap))
        
        maxTop = -heapq.nsmallest(1, maxHeap)[0]
        minTop = heapq.nsmallest(1, minHeap)[0] 
        median = maxTop
        if (len(minHeap) > len(maxHeap)): median = minTop
        medianz.append(median)
        res += median

print(res%10000)
print(medianz[0:100])
