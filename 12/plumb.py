import queue
with open("input.txt", "r") as infile:
    inputs = infile.read().split("\n")

nPipes = len(inputs)
cue = queue.Queue()
visited = [0 for i in range(nPipes)]
adjlist = [[] for i in range(nPipes)]

for i in inputs:
    procced = i.split(" <-> ")
    home = int(procced[0])
    away = list(map(int,procced[1].split(", ")))
    for j in away:
        adjlist[home].append(j)
        adjlist[j].append(home)

part1 = 0
part2 = 0
for i in range(nPipes):
    if (visited[i] == 0):
        part2 += 1
        cue.put(i)
        curnode = i
        visited[i] = 1
        while( not cue.empty()):
            curnode = cue.get()
            if(i == 0):
                part1 += 1
            for dest in adjlist[curnode]:
                if (visited[dest] == 0):
                    cue.put(dest)
                    visited[dest] = 1
print("Part 1: {}\nPart 2: {}".format(part1, part2))