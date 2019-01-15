input = []
with open("./m.in", "r") as infile:
    for line in infile:
        input.append(int(line))
input.sort()

seen = [0 for i in range(20001)]

p1 = 0
p2 = len(input)-1
r = 10000
l = -10000

while (p1 < p2):
    if (input[p1] + input[p2] > r): p2 -= 1
    elif (input[p1] + input[p2] < l): p1 += 1
    else: 
        seen[input[p1] + input[p2] + 10000] = 1 
        sp1 = p1
        sp2 = p2
        p2 -= 1
        while (p1 != p2 and input[p1] + input[p2] > l):
            seen[input[p1] + input[p2] + 10000] = 1
            p2 -= 1
        p2 = sp2
        p1 += 1
        while (p1 != p2 and input[p1] + input[p2] < r):
            seen[input[p1] + input[p2] + 10000] = 1
            p1 += 1
        p1 = sp1 + 1
        p2 = sp2 - 1

res = 0
for i in seen:
    if (i == 1): res += 1
print (res)

def twoSum(target):
    seen = set()
    for i in input:
        if (i in seen): return True
        seen.add(target-i)
    return False


# this solution takes much to long so above solution was implemented
res = 0
for i in range(-10000, 10001):
    print(i)
    if(twoSum(i)): res += 1
print (res)
