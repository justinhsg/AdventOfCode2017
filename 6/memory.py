with open("input.txt", "r") as infile:
    comm = list(map(int, infile.read().split("\t")))

def charint(c):
    return ord(c)-97
def intchar(i):
    return chr(i+97)

def realloc():
    highest = [0, -1]
    for i in range(len(comm)):
        if(comm[i]>highest[0]):
            highest = [comm[i], i]
    curpos = highest[1]
    excess = comm[curpos]
    comm[curpos] = 0
    while(excess!=0):
        curpos = (curpos+1)%len(comm)
        comm[curpos] += 1
        excess -= 1

def cseed():
    seed = ""
    for i in comm:
        seed += intchar(i)
    return seed
    
part1 = 0
cset = set()
cset.add(cseed())
while(True):
    realloc()
    part1 += 1
    cset.add(cseed())
    if(len(cset) - part1 != 1):
        break

loop = cseed()
part2 = 0
while(True):
    realloc()
    part2+=1
    if (cseed() == loop):
        break

print("Part 1: {}\nPart 2: {}".format(int(part1), int(part2))) 