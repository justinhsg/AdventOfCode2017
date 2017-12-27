with open("input.txt", "r") as infile:
    map = infile.read().split("\n") 
rowl = len(map[0])
heil = len(map)

curR = 0
curC = 0
dir = "down"
prevR = 0
prevC = 0
for i in range(rowl):
    if(map[0][i] == "|"):
        curC = i
part1 = ""
part2 = 0
while(True):
    if(dir == "down"):
        for i in range(curR, heil):
            part2 += 1
            if(map[i][curC].isalpha()):
                part1+=map[i][curC]
            if(map[i][curC] == "+"):
                if(map[i][curC-1] == "-"):
                    dir = "left"
                    curR = i
                    curC = curC-1
                    break
                elif(map[i][curC+1] =="-"):
                    dir = "right"
                    curR = i
                    curC = curC+1
                    break
                else:
                    dir = "break"
                    break
            if(map[i][curC] == " "):
                dir = "break"
                break
        if(dir == "break"):
            break    
    elif(dir == "up"):
        for i in range(curR, 0, -1):
            part2 += 1
            if(map[i][curC].isalpha()):
                part1+=map[i][curC]
            if(map[i][curC] == "+"):
                if(map[i][curC-1] == "-"):
                    dir = "left"
                    curR = i
                    curC = curC-1
                    break
                elif(map[i][curC+1] =="-"):
                    dir = "right"
                    curR = i
                    curC = curC+1
                    break
                else:
                    dir = "break"
                    break
            if(map[i][curC] == " "):
                dir = "break"
                break
        if(dir == "break"):
            break   
    elif(dir == "right"):
        for i in range(curC, rowl):
            part2 += 1
            if(map[curR][i].isalpha()):
                part1+=map[curR][i]
            if(map[curR][i] == "+"):
                if(map[curR-1][i] == "|"):
                    dir = "up"
                    curC = i
                    curR = curR-1
                    break
                elif(map[curR+1][i] == "|"):
                    dir = "down"
                    curC = i
                    curR = curR+1
                    break
                else:
                    dir = "break"
                    break
            if(map[curR][i] == " "):
                dir = "break"
                break
        if(dir == "break"):
            break   
    elif(dir == "left"):
        for i in range(curC, 0, -1):
            part2 += 1
            if(map[curR][i].isalpha()):
                part1+=map[curR][i]
            if(map[curR][i] == "+"):
                if(map[curR-1][i] == "|"):
                    dir = "up"
                    curC = i
                    curR = curR-1
                    break
                elif(map[curR+1][i] == "|"):
                    dir = "down"
                    curC = i
                    curR = curR+1
                    break
                else:
                    dir = "break"
                    break
            if(map[curR][i] == " "):
                dir = "break"
                break
        if(dir == "break"):
            break   
    else:
        breakc
part2 -= 1
print("Part 1: {}\nPart 2: {}".format(part1, part2))