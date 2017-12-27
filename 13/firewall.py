with open("input.txt", "r") as infile:
    inputs = infile.read().split("\n")
    
proc = [list(map(int,i.split(": "))) for i in inputs]
nlayer = int(proc[-1][0])

layers=[0 for i in range(nlayer)]

part1 = 0
for i in proc:
    depth = i[0]
    layers = i[1]
    if(depth%((layers-1)*2) == 0):
        part1 = part1 + depth*layers



dp = [[i[0],(i[1]-1)*2] for i in proc ]

part2 = 0
while(True):
    caught = False
    for i in dp:
        if( (i[0]+part2) % i[1] == 0):
            caught = True
            break
    if(not caught):
        break
    part2 += 1
print("Part 1: {}\nPart 2: {}".format(part1, part2))