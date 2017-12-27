with open("input.txt", "r") as infile:
    tinput = infile.read().strip()
commands = list(map(int ,tinput.split(",")))
    
    
#Part 1
liz = [i for i in range(256)]
curpos = 0
tliz = [0 for i in range(256)]
skip = 0

#Part 1
for i in commands:
    tlen = i
    for j in range(tlen):
        tliz[j] = liz[(curpos+j)%256]
    for j in range(tlen):
        liz[(curpos+j)%256] = tliz[tlen-1-j]
    curpos = (curpos + tlen+skip)%256
    skip += 1

part1 = liz[0] * liz[1]

def inttohex(i):
    fchar = i//16
    if(fchar<10):
        fchar = str(fchar)
    else:
        fchar = chr(fchar+87)
    schar = i%16
    if(schar<10):
        schar = str(schar)
    else:
        schar = chr(schar+87)
    return str(fchar+schar)
    
#Part2    
newc = list(map(ord, tinput))
newc.extend((17, 31, 73, 47, 23))
liz2 = [i for i in range(256)]
curpos2 = 0
tliz2 = [0 for i in range(256)]
skip2 = 0

for t in range(64):
    for i in newc:
        tlen = i
        for j in range(tlen):
            tliz2[j] = liz2[(curpos2+j)%256]
        for j in range(tlen):
            liz2[(curpos2+j)%256] = tliz2[tlen-1-j]
        curpos2 = (curpos2 + tlen+skip2)%256
        skip2 += 1

#hashing
dense = [0 for i in range(16)]
for i in range(16):
    tmp = 0

    for t in liz2[16*i:16*i+16]:
        tmp = tmp ^ t
    dense[i] = tmp


part2 = ""
for i in dense:
    part2 += inttohex(i)


print("Part 1: {}\nPart 2: {}".format(part1, part2)) 