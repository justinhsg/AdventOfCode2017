from collections import deque, defaultdict
with open("input.txt", "r") as infile:
    coms = [i.split(" ") for i in infile.read().split("\n")]
ncom = len(coms)
cop = defaultdict(int)
def val(i):
    try:
        return int(i)
    except:
        return cop[i]
pt = 0
part1 = 0
while(pt in range(ncom)):
    tc = coms[pt][0]
    if(tc == "jnz"):
        if(val(coms[pt][1]) != 0):
            pt += val(coms[pt][2])
        else:
            pt += 1
        continue
    if(tc == "set"):
        cop[coms[pt][1]] = val(coms[pt][2])
    elif(tc == "sub"):
        cop[coms[pt][1]] -= val(coms[pt][2])
    elif(tc == "mul"):
        cop[coms[pt][1]] *= val(coms[pt][2])
        part1 += 1
    pt += 1
    continue


part2 = 0
lb = 0 - int(coms[5][2]) + int(coms[0][2]) * int(coms[4][2])
ub = 0 - int(coms[5][2]) + int(coms[0][2]) * int(coms[4][2]) - int(coms[7][2]) + 1
step = 0 - int(coms[30][2])
for i in range(lb, ub, step):
    for j in range(2,i):
        if(i%j == 0):
            part2+=1
            break

print("Part 1: {}\nPart 2: {}".format(part1, part2))