import random
import time
def iterations():
    items = {}

    numEdges = 0

    with open("./contractions.in", "r") as infile:
        for line in infile:
            for i, v in enumerate(line.split()):
                if (i == 0): 
                    head = int(v)-1
                    items[head] = []
                else: 
                    items[head].append(int(v)-1)
                    numEdges += 1


    def contract(node1, node2):
        nonlocal numEdges
        #print (node1, node2)
        if (node1 == node2):
            print( " SAME NODES ")
            exit(1)

        for i in items.keys():
            for j, edge in enumerate(items[i]):
                if (edge == node2): items[i][j] = node1

        newEdges = []
        for edge in items[node1]:
            if (edge != node1):
                newEdges.append(edge)
            else: numEdges -= 1
        items[node1] = [i for i in newEdges]

        node2edges = items[node2]
        del items[node2]
        
        for i in node2edges:
            if (i != node1): items[node1].append(i)
            else: numEdges -= 1


    while (len(items.keys()) != 2):
        edge = random.randint(0, numEdges-1)
        
        for head in items.keys():
            if len(items[head]) > edge: break
            edge -= len(items[head])

        node1 = head
        node2 = items[head][edge]
        contract(node1, node2)

    return len(items[node1])

start = time.time()
minCut = float('inf')
for i in range(200**2):
    cut = iterations()
    if cut < minCut: minCut = cut
print(time.time()-start)
print(minCut)

        