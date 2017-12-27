with open("input.txt", "r") as infile:
    text = infile.read().rstrip("\n")
while(text.find("!")!=-1):
    ignore = text.find("!")
    text = text[:ignore] + text[ignore+2:]

    
garbage = 0
while(text.find("<")!=-1):
    starti = text.find("<")
    endi = text.find(">")
    garbage += endi - starti - 1
    text = text[:starti] + text[endi+1:]

curscore = 0
multiplier = 1
for i in text:
    if(i == "{"):
        curscore += multiplier
        multiplier += 1
    if(i == "}"):
        multiplier -= 1
part1 = curscore
part2 = garbage
print("Part 1: {}\nPart 2: {}".format(part1, part2)) 