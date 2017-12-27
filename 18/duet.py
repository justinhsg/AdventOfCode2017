from collections import deque, defaultdict

with open("in.txt", "r") as infile:
    commands = [i.split(" ") for i in infile.read().split("\n")]

pt = 0
reg = dict()
mem = dict()
part1 = 0
while(True):
    if(pt < 0 or pt >= len(commands)):
        break
    treg = commands[pt][1]
    tq = commands[pt][0]
    if(len(commands[pt]) == 3):
        tval = commands[pt][2].strip()
        if(tval.lstrip("-").isnumeric()):
            tval = int(tval)
        else:
            if(tval not in reg.keys()):
                reg[tval] = 0
                tval = 0
            else:
                tval = reg[tval]
    if(treg not in reg.keys()):
        reg[treg] = 0
    if(tq == "set"):
        reg[treg] = tval
        pt += 1
        continue
    elif(tq == "snd"):
        tval = reg[treg]
        mem[treg] = tval
        pt += 1
        continue
    elif(tq == "add"):
        reg[treg] += tval
        pt += 1
        continue
    elif(tq == "mul"):
        reg[treg] *= tval
        pt+=1
        continue
    elif(tq == "mod"):
        reg[treg] = reg[treg]%tval
        pt+=1
        continue
    elif(tq == "rcv"):
        if(treg not in mem.keys()):
            pt+=1
            continue
        else:
            part1 = mem[treg]
            break
            pt+=1
            continue
    elif(tq == "jgz"):
        if(reg[treg] > 0):
            pt += tval
        else:
            pt+=1
        continue
    else:
        continue

regd0 = defaultdict(int)
regd1 = defaultdict(int)
q0 = deque()
q1 = deque()
regd0["p"] = 0
regd1["p"] = 1


def proc(regd, inq, outq):
    def val(i):
        try:
            return int(i)
        except:
            return regd[i]
    while (regd["pt"] >= 0 and regd["pt"] <len(commands)):
        clist = commands[regd["pt"]]
        if(clist[0] == "rcv"):
            if(len(inq) == 0):
                return True
            regd[clist[1]] = val(inq.popleft())
        if(clist[0] == "jgz"):
            if(val(clist[1])>0):
                regd["pt"] += val(clist[2])
                continue
        if(clist[0] == "set"):
            regd[clist[1]] = val(clist[2])
        elif(clist[0] == "add"):
            regd[clist[1]] += val(clist[2])    
        elif(clist[0] == "mul"):
            regd[clist[1]] *= val(clist[2])
        elif(clist[0] == "mod"):
            regd[clist[1]] %= val(clist[2])
        elif(clist[0] == "snd"):
            outq.append(val(clist[1]))  
            regd["count"] += 1
        regd["pt"]+=1
    return False
    
            
while(True):
    if not proc(regd1, q1, q0):
        break
    if not proc(regd0, q0, q1):
        break
    if len(q1) == 0 and len(q0) == 0:
        break
part2 = regd1["count"]
print("Part 1: {}\nPart 2: {}".format(part1, part2))