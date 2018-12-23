from sortedcontainers import SortedDict

graph = [[] for i in range(200)]
weights = [1000000 for i in range(200)]
weights[0] = 0
with open("./d.in", "r") as infile:
    for line in infile:
        l = line.split()
        index = int(l[0])-1
        for j in l[1:]:
            l2 = j.split(',')
            graph[index].append([int(l2[0])-1, int(l2[1])])

seen = set()
heap = SortedDict([(0, 0)])
while len(seen) != 200:
    n = heap.popitem(0)
    while n[1] in seen:
        n = heap.popitem(0)
    seen.add(n[1])
    for i in graph[n[1]]:
        if weights[n[1]]+i[1] < weights[i[0]]: weights[i[0]] = weights[n[1]] + i[1]
        heap[weights[i[0]]] = i[0] 

ans = []

counter = 0
with open("./c.in", "r") as infile:
    for line in infile:
        if counter%2 == 0:
            ans.append([int(line.split()[0]), int(line.split()[1])])
        counter += 1

ans.sort()

for i in range(1, 200):
    print(ans[i-1], weights[i])

