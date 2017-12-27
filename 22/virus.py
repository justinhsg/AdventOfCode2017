with open("input.txt", "r") as infile:
    grid = [list(i) for i in infile.read().split("\n")]
gsize = len(grid)
infected = set()
weakened = set()
flagged = set()
for x in range(gsize):
    for y in range(gsize):
        if(grid[x][y] == '#'):
            infected.add( (x,y) )
                             
cx = int((gsize-1)/2)
cy = int((gsize-1)/2)

face = 0

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

part1 = 0

for i in range(10000):
    if((cx, cy) in infected):
        face = (face+1)%4
        infected.remove((cx,cy))
    else:
        face = (face-1)%4
        infected.add((cx,cy))
        part1 += 1
    cx = cx+dx[face]
    cy = cy+dy[face]



cx = int((gsize-1)/2)
cy = int((gsize-1)/2)
face = 0
part2 = 0
infected.clear()

for x in range(gsize):
    for y in range(gsize):
        if(grid[x][y] == '#'):
            infected.add( (x,y) )
         
for i in range(10000000):
    if((cx, cy) in infected):
        face = (face+1)%4
        infected.remove((cx,cy))
        flagged.add((cx,cy))
    elif((cx, cy) in weakened):
        weakened.remove((cx,cy))
        infected.add((cx,cy))
        part2 += 1
    elif((cx,cy) in flagged):
        flagged.remove((cx,cy))
        face = (face+2)%4
    else:
        face = (face-1)%4
        weakened.add((cx,cy))
    cx = cx+dx[face]
    cy = cy+dy[face]

print("Part 1: {}\nPart 2: {}".format(part1, part2))        