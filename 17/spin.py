with open("input.txt", "r") as infile:
    #converts input to array of strings
    steps = int(infile.read().rstrip("\n"))
#stores length of input

bu = [0]
curpos = 0

for i in range(1,2018):
    newpos = (curpos+steps)%len(bu)
    bu.insert(newpos+1, i)
    curpos = newpos+1
part1 = bu[curpos+1]     


curpos = 0
part2 = 0
for i in range(1,50000000):
    newpos =(curpos+steps)%i
    if(newpos == 0):
        part2 = i
    curpos = newpos+1
print("Part 1: {}\nPart 2: {}".format(part1, part2))

    
