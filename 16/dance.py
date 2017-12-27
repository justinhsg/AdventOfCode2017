with open("input.txt", "r") as infile:
    #converts input to array of strings
    processed = infile.read().split(",")
#stores length of input
inlen = processed.__len__()



def charint(c):
    return ord(c)-97
def intchar(i):
    return chr(i+97)

#stores a list lpos, where lpos[i] is the program at pos i
#stores a list lprog, where lprog[i] is the position of program i (a->0 etc)
lprog = list(range(16))
lpos = list(range(16))


def liztoans(liz):
    txt = ""
    for i in range(16):
        txt += intchar(liz[i])
    return txt
    
def updatepos():
    for i in range(16):
        t = lprog[i]
        lpos[t] = i
def updateprog():
    for i in range(16):
        t = lpos[i]
        lprog[t] = i

dances = []
part1 = ""
part2 = ""
x = 0
while(True):
    for q in processed:
        q = q.rstrip("\n")
        pre = q[0]
        post = q[1:]
        if(pre=='s'):
            for i in range(16):
                t = lprog[i]
                lprog[i] = (t+int(post))%16
            updatepos()
        else:
            pair = q[1:].split("/")
        if(pre=='x'):
            fir = int(pair[0])
            sec = int(pair[1])
            t = lpos[fir]
            lpos[fir] = lpos[sec]
            lpos[sec] = t
            updateprog()
        elif(pre=='p'):
            fir = charint(pair[0])
            sec = charint(pair[1])
            t = lprog[fir]
            lprog[fir] = lprog[sec]
            lprog[sec] = t
            updatepos()
    if(x==0):
        part1 = liztoans(lpos)
    if(liztoans(lpos) in dances):
        break
    else:
        dances.append(liztoans(lpos))
        x+=1
part2 = dances[1000000000%x-1]
print("Part 1: {}\nPart 2: {}".format(part1, part2))