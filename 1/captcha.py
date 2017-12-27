with open("input.txt", "r") as infile:
    processed = str(infile.read())


insize = len(processed)
part1=0
part2=0

for i in range(insize):
    #solution for part 1
    if(processed[(i+1)%insize]==processed[i]):
        part1+=int(processed[i])
        
    #solution for part 2
    if(processed[int(i+insize/2)%insize]==processed[i]):
        part2+=int(processed[i])
        
print("Part 1: {}\nPart 2: {}".format(part1, part2))