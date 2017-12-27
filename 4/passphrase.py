with open("input.txt", "r") as infile:
    part1 = 0
    part2 = 0
    for i in infile:
        #part 1
        words = i.strip().split()
        if (len(words) == len(set(words))):
            part1 += 1
            
        #part 2
        words2 = ['' for j in range(len(words))]
        for j in range(len(words2)):
            words2[j] = ''.join(sorted(words[j]))
        if (len(words) == len(set(words2))):
            part2 += 1

    print("Part 1: {}\nPart 2: {}".format(int(part1), int(part2)))