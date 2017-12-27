import queue
infile = open("input.txt", "r")
inputs = infile.read().rstrip("\n")
part1 = 0

grid = [[0 for j in range(128)] for i in range(128)]

for z in range(128):
    key = inputs+"-"+str(z)
    convkey = list(map(ord, key))
    convkey.extend((17, 31, 73, 47, 23))
    liz = [i for i in range(256)]
    curpos = 0
    tliz = [0 for i in range(256)]
    skip = 0
    for t in range(64):
        for i in convkey:
            tlen = i
            for j in range(tlen):
                tliz[j] = liz[(curpos+j)%256]
            for j in range(tlen):
                liz[(curpos+j)%256] = tliz[tlen-1-j]
            curpos = (curpos + tlen+skip)%256
            skip += 1
    #hashing
    binstr = ""
    for i in range(16):
        tmp = 0
        for t in liz[16*i:16*i+16]:
            tmp = tmp ^ t
        binstr = binstr + bin(tmp)[2:].zfill(8)
    #for i in range(128):
    #    if(binstr[i]=="1"):
    #        grid[z]=1
    grid[z] = list(map(int,binstr))
    part1 += binstr.count("1")



dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
part2 = 0
cue = queue.Queue()
for t in range(1):
    for i in range(128):
        for j in range(128):
            if(grid[i][j] == 1):
                part2 += 1
                x = i
                y = j
                cue.put([x,y])
                while(not cue.empty()):
                    curpos = cue.get()
                    cx = curpos[0]
                    cy = curpos[1]
                    if(grid[cx][cy] == 1):
                        grid[cx][cy] = 0
                        for k in range(4):
                            nx = cx+dx[k]
                            ny = cy+dy[k]
                            if(nx in range(128) and ny in range(128) and grid[nx][ny] == 1):
                                cue.put([nx,ny])
                                
print("Part 1: {}\nPart 2: {}".format(part1, part2))
infile.close()