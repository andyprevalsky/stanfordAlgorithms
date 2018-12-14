
MAXN = 875714
neighborsNorm = [[] for i in range(MAXN)]
neighborsRev = [[] for i in range(MAXN)]
with open("./SCC.txt", "r") as infile:
    for line in infile:
        a, b = line.split()
        a = int(a)-1
        b = int(b)-1
        neighborsNorm[b].append(a)
        neighborsRev[a].append(b)

#first dfs through the reversed edges, marking ending times for each node
#next iterate through the ending times from last to first, keeping track of leaders
#next count largest grouping of leaders

timeEndings = [[0, i] for i in range(MAXN)]
memo = [0 for i in range(MAXN)]
endtime = 1
def dfsRev(root):
    global endtime
    if (memo[root] == 1): return
    memo[root] = 1
    for i in neighborsRev[root]:
        dfsRev(i)
    timeEndings[root][0] = endtime
    endtime += 1

leaders = [0 for i in range(MAXN)]

leader = 0
def dfsFor(root):
    if (memo[root] == 1): return
    memo[root] = 1
    global leader
    for i in neighborsNorm[root]:
        dfsFor(i)
    leaders[root] = leader


for i in range(len(neighborsRev)):
    dfsRev(i)

for i in range(len(memo)):
    memo[i] = 0

timeEndings.sort()
for i in reversed(timeEndings):
    leader = i[1]
    dfsFor(i[1])


leaderCount = [0 for i in range(MAXN)]
for i in leaders:
    leaderCount[i] += 1
leaderCount.sort()

print(leaderCount[-5::])




