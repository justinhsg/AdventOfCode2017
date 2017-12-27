with open("input.txt", "r") as infile:
    rawinput = infile.read().split()

comm = list(map(int, rawinput))
comm2 = list(comm)

coml = len(comm)

cur = 0
part1 = 0
#Part 1
while(cur in range(coml)):
    tc = comm[cur]
    comm[cur] += 1
    cur += tc
    part1 += 1


cur2 = 0;
part2 = 0;
#Part 2
while(cur2 in range(coml)):
    tc2 = comm2[cur2]
    if(tc2 >= 3):
        comm2[cur2] -= 1
    else:
        comm2[cur2] += 1
    cur2 += tc2
    part2 += 1

print("Part 1: {}\nPart 2: {}".format(int(part1), int(part2))) 



