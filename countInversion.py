
input = []
with open("./input.in", "r") as infile:
    for line in infile:
        input.append(int(line))

total = 0
def countInversions(input):
    global total
    if len(input) == 1: return input
    mid = len(input)//2
    in1 = countInversions(input[0:mid])
    in2 = countInversions(input[mid:])
    p1 = 0
    p2 = 0
    sortedArray = []
    while (p1 != len(in1) or p2 != len(in2)):
        if (p1 == len(in1)): 
            sortedArray.append(in2[p2])
            p2 += 1
        elif (p2 == len(in2)):
            sortedArray.append(in1[p1])
            p1 += 1
        elif (in2[p2] < in1[p1]):
            sortedArray.append(in2[p2])
            p2 += 1
            total += (len(in1)-p1)
        else:
            sortedArray.append(in1[p1])
            p1 += 1
    return sortedArray


countInversions(input)
print(total)