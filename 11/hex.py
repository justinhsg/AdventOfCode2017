with open("input.txt", "r") as infile:
    steps = infile.read().rstrip("\n").split(",")
nn = 0
ntn = 0
ns = 0
nts = 0
ne = 0
nw = 0
nne = 0
nsw = 0
nnw = 0
nse = 0
maxdisp = 0
for i in steps:
    if(i == "n"):
        nn += 1
        ntn += 1
    elif(i == "s"):
        ns += 1
        nts += 1
    elif(i == "ne"):
        nne += 1
        ne += 1
        nn += 0.5
    elif(i == "se"):
        nse += 1
        ne += 1
        ns += 0.5
    elif(i == "nw"):
        nw += 1
        nn += 0.5
        nnw += 1
    elif(i == "sw"):
        nsw += 1
        nw += 1
        ns += 0.5
    nd = nn - ns
    ed = ne - nw
    if(abs(ed) > abs(nd)):
        curdisp = abs(ed)
    else:
        curdisp = abs(ed) + abs(nd)-abs(ed/2)
    maxdisp = max(maxdisp,curdisp)
    

nd = nn - ns
ed = ne - nw

if(abs(ed) > abs(nd)):
    part1 = int(abs(ed))
else:
    part1 = int(abs(ed) + abs(nd-ed*0.5))
part2 = maxdisp
print("Part 1: {}\nPart 2: {}".format(part1, part2))