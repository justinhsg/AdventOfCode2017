import queue
with open("input.txt", "r") as infile:
    comm = infile.read().split("\n")


names = ["" for i in range(len(comm))]
weight = [0 for i in range(len(comm))]
balance = [0 for i in range(len(comm))]

asso = [[] for i in range(len(comm))]
revasso = [[] for i in range(len(comm))]
dnames = dict()

for i in range(len(comm)):
    tname = comm[i].split(" ")[0]
    names[i] = tname
    dnames[tname] = i
    weight[i] = int(comm[i].split(" ")[1][1:-1])
       
for i in range(len(comm)):
    if("->" in comm[i]):
        sources = comm[i].split(" -> ")[1].split(", ")
        for j in sources:
            asso[dnames[j]].append(i)
            revasso[i].append(dnames[j])
        
    

curP = 0
root = -1
#Part 1
while(True):
    if(len(asso[curP])==0):
        root = curP
        break
    curP = asso[curP][0]
    
#Part 2
def checkweight(i):
    if(balance[i]!= 0):
        return balance[i]
    if(len(revasso[i])==0):
        balance[i] = weight[i]
    else:
        balance[i] = weight[i]
        for j in revasso[i]:
            balance[i] += checkweight(int(j))
    return balance[i]
checkweight(root)

def checkdeficit(i, l):
    if(len(revasso[i]) == 0):
        return l
    weights = []
    for j in revasso[i]:
        weights.append(balance[j])
    if(max(weights) - min(weights) != 0):
        l.append(i)
    for j in revasso[i]:
        checkdeficit(j, l)
    return l

problemparent = checkdeficit(root, [])[-1]
problemweights = [balance[i] for i in revasso[problemparent]]

def mostcommon(l):
    return max(set(l), key=l.count)
def leastcommon(l):
    return min(set(l), key=l.count)

wrongweight = leastcommon(problemweights)
correctweight = mostcommon(problemweights)
problemchild = revasso[problemparent][problemweights.index(wrongweight)]

part1 = names[root]
part2 = correctweight - wrongweight + weight[problemchild]
print("Part 1: {}\nPart 2: {}".format(part1, part2)) 