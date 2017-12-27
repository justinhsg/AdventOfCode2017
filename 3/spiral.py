with open("input.txt", "r") as infile:
    input = int(infile.read().strip())
answerfound = False

#Arbitrary number for layers. This value must be greater than Part 1 or else part 1 will give 0 as an answer.
layers = 300;
sides = layers*2+1
grid = [[0 for i in range(sides)] for i in range(sides)]
grid2 = [[0 for i in range(sides)] for i in range(sides)]


middle = int((sides-1)/2)
grid[middle][middle] = 1
grid2[middle][middle] = 1
x = middle
y = middle

#This stores the value of the 4 corners of each layer
fc= [0, 0, 0 ,0]

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
#iterating through each layer

dx1 = [-1, -1,  0,  1,  1,  1,  0, -1]
dy1 = [ 0, -1, -1, -1,  0,  1,  1,  1]
lastsq = 1
acc = 2
x+=dx[3]
y+=dy[3]
part1 = 0
part2 = 0

for i in range(1,layers+1):
    for j in range(1,5):
        fc[j-1] = lastsq+ (i*2)*j
    lastsq = fc[3]
    while(acc<=lastsq):
        grid[x][y] = acc
        
        #This is the way to solve for Part 1. However, not doing it by code is way easier (and faster)
        if(grid[x][y] == input):
            part1 = int(abs(x-middle) + abs(y-middle))
            answerfound = True
            break
            
        #Part 2
        if(part2 == 0):
            for k in range(8):
                nx = x +  dx1[k]
                ny = y + dy1[k]
                if(nx>=0 and nx <sides and ny >=0 and ny < sides):
                    grid2[x][y] += grid2[nx][ny]    
            if(grid2[x][y]>input):
                part2 = grid2[x][y]
        
        #This moves to the next square
        if(acc<fc[0]):
            x+=dx[0]
            y+=dy[0]
        elif(acc<fc[1]):
            x+=dx[1]
            y+=dy[1]
        elif(acc<fc[2]):
            x+=dx[2]
            y+=dy[2]
        elif(acc<=fc[3]):
            x+=dx[3]
            y+=dy[3]
        acc += 1
        
    if(answerfound):
        break
print("Part 1: {}\nPart 2: {}".format(int(part1), int(part2)))
        