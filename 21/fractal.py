with open("intxt.txt", "r") as infile:
    conv = [i.split(" => ") for i in infile.read().split("\n")]
raw0 = ".#./..#/###"

c2 = []
c3 = []

c2store = []
c3store = []

  
def ltos(l):
    return "/".join(["".join(i) for i in l])
    
def stol(s):
    return [list(i) for i in s.split("/")]




    
def flipv(s):
    return ltos(stol(s)[::-1])
def fliph(s):
    s = stol(s)
    op = []
    for i in s:
        op.append(i[::-1])
    return ltos(op)
def rotate(s):
    s = stol(s)
    op = [["" for i in range(len(s))] for i in range(len(s))]
    for i in range(len(s)):
        for j in range(len(s)):
            op[len(s)-j-1][i] = s[i][j]
    return ltos(op)

for i in range(6):
    inp = conv[i][0]
    out = conv[i][1]
    for i in range(4):
        inp = rotate(inp)
        if(inp not in c2store):
            c2store.append(inp)
            c2.append(out)
        if(fliph(inp) not in c2store):
            c2store.append(fliph(inp))
            c2.append(out)

for i in range(6,len(conv)):
    inp = conv[i][0]
    out = conv[i][1]
    for i in range(4):
        inp = rotate(inp)
        if(inp not in c2store):
            c3store.append(inp)
            c3.append(out)
        if(fliph(inp) not in c2store):
            c3store.append(fliph(inp))
            c3.append(out)


def horiadd(a,b):
    return [a[i] + b[i] for i in range(len(a))]
        
def match3(s):
    return stol(c3[c3store.index(ltos(s))])
        
def match2(s):
    return stol(c2[c2store.index(ltos(s))])
    
    
start = stol(raw0)
for i in range(18):        
    psize = len(start)        
    if(psize%2 == 0):
        nblocks = int(psize/2)
        finished = []
        for row in range(nblocks):
            trowblock = []
            for col in range(nblocks):
                tblock = [i[col*2:col*2+2] for i in start[row*2:row*2+2]]
                outblock = match2(tblock)
                if (trowblock == []):
                    trowblock = outblock
                else:
                    trowblock = horiadd(trowblock, outblock)
            finished = finished + trowblock
        start = finished
    else:
        nblocks = int(psize/3)
        finished = []
        for row in range(nblocks):
            trowblock = []
            for col in range(nblocks):
                tblock = [i[col*3:col*3+3] for i in start[row*3:row*3+3]]
                outblock = match3(tblock)
                if (trowblock == []):
                    trowblock = outblock
                else:
                    trowblock = horiadd(trowblock, outblock)
            finished = finished + trowblock
        start = finished
    if(i == 4):
        part1 = ltos(start).count("#")
    if(i == 17):
        part2 = ltos(start).count("#")
print("Part 1: {}\nPart 2: {}".format(part1, part2))
    