infile = open("input.txt", "r")
#converts input to array of strings
steps = int(infile.read().rstrip("\n"))
#stores length of input

bu = [0]
curpos = 0
ans = 0
for i in range(1,50000000):
    newpos =(curpos+steps)%i
    if(newpos == 0):
        ans = i
    curpos = newpos+1
    if(i%10000000 == 0):
        print(i)
print(ans)
