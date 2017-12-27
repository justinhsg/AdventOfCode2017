with open ("input.txt", "r") as infile:
    raw = infile.read().split("\n")

ins = int(raw[1].split()[-2])
tape = [0 for i in range(ins+1)]
pt = 0
checksum = 0
state = (raw[0].split()[-1][-2]).lower()

def moveright():
    global pt
    pt += 1

def moveleft():
    global pt
    pt -= 1

for i in range(ins):
    #The entire tape below is based on reading the input and interpreting it manually.
    #TODO: Make this dynamic
    if (state == 'a'):
        if(tape[pt] == 0):
            tape[pt] = 1
            checksum += 1
            moveright()
            state = 'b'
        else:
            tape[pt] = 0
            checksum -= 1
            moveleft()
            state = 'c'
    elif (state == 'b'):
        if(tape[pt] == 0):
            tape[pt] = 1
            checksum += 1
            moveleft()
            state = 'a'
        else:
            moveright()
            state = 'd'
    elif (state == 'c'):
        if(tape[pt] == 0):
            moveleft()
            state = 'b'
        else:
            tape[pt] = 0
            checksum -= 1
            moveleft()
            state = 'e'
    elif (state == 'd'):
        if(tape[pt] == 0):
            tape[pt] = 1
            checksum += 1
            moveright()
            state = 'a'
        else:
            tape[pt] = 0
            checksum -= 1
            moveright()
            state = 'b'
    elif (state == 'e'):
        if(tape[pt] == 0):
            tape[pt] = 1
            checksum += 1
            moveleft()
            state = 'f'
        else:
            moveleft()
            state = 'c'
    elif (state == 'f'):
        if(tape[pt] == 0):
            tape[pt] = 1
            checksum += 1
            moveright()
            state = 'd'
        else:
            moveright()
            state = 'a'
print("Answer: {}".format(checksum))
            








