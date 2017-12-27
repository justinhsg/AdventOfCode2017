with open("input.txt", "r") as infile:
    port = infile.read().split("\n") 
    
nport = len(port)
porlis = [[] for i in range(51)]
for i in range(nport):
    io = list(map(int,port[i].split("/")))
    porlis[io[0]].append([io[1],i])
    if(io[0] != io[1]):
        porlis[io[1]].append([io[0],i])
  
    

    
def dfs(ulis, lp, c):
    nm = c
    for i in porlis[lp]:
        tport = i
        
        if(ulis[tport[1]] == 0):
            newlis = [i for i in ulis]
            newlis[tport[1]] = 1
            np = tport[0]
            nc = c+lp+np
            tmax = dfs(newlis, np, nc)
            nm = max(nm,tmax)
    return nm
part1 = dfs([0 for i in range(nport)], 0, 0)


maxl = 0
maxlis = []
def dfs2(ulis, lp, l):
    global maxl
    global maxlis
    for i in porlis[lp]:
        tport = i
        if(ulis[tport[1]] == 0):
            newlis = [i for i in ulis]
            newlis[tport[1]] = 1
            np = tport[0]
            nl = l+1
            if(nl == maxl):
                maxlis.append([i for i in newlis])
            if(nl > maxl):
                maxlis = []
                maxl = nl
                maxlis.append([i for i in newlis])
            dfs2(newlis, np, nl)
    return
dfs2([0 for i in range(nport)], 0, 0)
part2 = 0
for j in maxlis:
    a = 0
    for i in range(nport):
        if j[i] == 1:
            a += sum(list(map(int, port[i].split("/"))))
    part2 = max(part2, a)
print("Part 1: {}\nPart 2: {}".format(part1, part2))
