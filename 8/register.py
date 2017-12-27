with open("input.txt", "r") as infile:
    commands = infile.read().split("\n")
proc = [i.split(" ") for i in commands]
n = commands.__len__()

regint = dict()
intreg = ["" for i in range(25)]
vals = [0 for i in range(25)]
regcount = 0

for i in proc:
    if(i[0] not in regint.keys()):
        intreg[regcount] = i[0]
        regint[i[0]] = regcount
        regcount += 1


passed = 0
maxi = 0
for i in proc:
    
    query = i[4]
    comp = i[5]
    val = int(i[6])
    mod = i[1]
    amt = int(i[2])
    ori = i[0]
    todo = False
    if(query not in regint.keys()):
        regint[query] = 0
    if(comp == "==" and vals[regint[query]] == val):
        todo = True
    elif (comp == "<" and vals[regint[query]] < val):
        todo = True
    elif (comp == ">" and vals[regint[query]] > val):
        todo = True
    elif (comp == "<=" and vals[regint[query]] <= val):
        todo = True
    elif (comp == ">=" and vals[regint[query]] >= val):
        todo = True
    elif (comp == "!=" and vals[regint[query]] != val):
        todo = True
    if(todo):
        passed+=1
        if(mod == "inc"):
            vals[regint[ori]] += amt
        elif(mod == "dec"):
            vals[regint[ori]] -= amt
        maxi = max(maxi, max(vals))
        
part1 = max(vals)
part2 = maxi
print("Part 1: {}\nPart 2: {}".format(part1, part2))         