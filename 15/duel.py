with open("input.txt") as infile:
    proc = infile.read().split("\n")



gena = int(proc[0][24:])
genb = int(proc[1][24:])
similar = 0

for i in range(40000000):
    gena = (gena*16807)%2147483647
    genb = (genb*48271)%2147483647
    if(gena&0xFFFF == genb&0xFFFF):
        similar += 1

part1 = similar
gena = int(proc[0][24:])
genb = int(proc[1][24:])
similar = 0
for i in range(5000000):
    gena = (gena*16807)%2147483647
    while(gena%4!=0):
        gena = (gena*16807)%2147483647
    genb = (genb*48271)%2147483647
    while(genb%8!=0):
        genb = (genb*48271)%2147483647
    if(gena&0xFFFF == genb&0xFFFF):
        similar += 1
part2 = similar

print("Part 1: {}\nPart 2: {}".format(part1, part2))