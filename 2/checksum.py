with open("input.txt", "r") as infile:
    part1 = 0
    part2 = 0
    for i in infile:
        tline = list(map(int, i.split("\t")))
        
        #Solution for Part 1
        part1 += (max(tline) - min(tline))
        
        #solution for Part 2
        for j in range(len(tline)):
            for k in range(j+1,len(tline)):
                if(tline[k]%tline[j]==0):
                    part2 += tline[k]/tline[j]
                    break
                elif(tline[j]%tline[k]==0):
                    part2 += tline[j]/tline[k]
                    break
    print("Part 1: {}\nPart 2: {}".format(int(part1), int(part2)))