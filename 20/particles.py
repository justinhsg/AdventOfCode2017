from math import isclose,sqrt
from collections import defaultdict
with open("input.txt", "r") as infile:
    particles = infile.read().split("\n") 
npart = len(particles)
processed = []


for i in range(npart):
    tstr = particles[i].split(", ")
    tpart = []
    for j in range(len(tstr)):
        coords = list(map(int,tstr[j][3:-1].split(",")))
        tpart.append(coords)
    processed.append(tpart)


    
quads = []
for i in range(npart):
    tpq = []
    for j in range(3):
        tcq = [0.5*processed[i][2][j], processed[i][1][j]+0.5*processed[i][2][j], processed[i][0][j]]
        #[[x^2, x, x^0], [y^2,y,y^0], [z^2,z,z^0]]
        tpq.append(tcq)
    quads.append(tpq)

part1 = -1
max2 = 10000000000
max1 = 10000000000
max0 = 10000000000
for i in range(npart):
    t2 = 0
    t1 = 0
    t0 = 0
    for j in range(3):
        t2 += abs(quads[i][j][0])
        t1 += abs(quads[i][j][1])
        t0 += abs(quads[i][j][2])
    if(t2 > max2):
        continue
    elif(t2 == max2 and t1 > max1):
        continue
    elif(t2 == max2 and t1 == max1 and t0 > max0):
        continue
    else:
        max2 = t2
        max1 = t1
        max0 = t0
        part1 = i
        continue




exists = [True for i in range(npart)]
collisions = defaultdict(set)
def isint(q):
    return isclose(q, int(q))
def solveQuad(q1, q2):
    a,b,c = q1[0]-q2[0], q1[1] - q2[1], q1[2] - q2[2]
    if(a == 0 and b != 0):
        troot = (-c)/b
        if(isint(troot) and int(troot)>=0):
            return [int(troot)]
        else:
            return None
    if(a==0 and b==0):
        if(c==0):
            return [0]
        else:
            return None
    if((b**2 - 4*a*c) < 0):
        return None
    else:
        roots = []
        tsqrt = sqrt(b**2 - 4*a*c)
        root1 = (-b-tsqrt)/(2*a)
        root2 = (-b+tsqrt)/(2*a)
        if(isint(root1) and root1>=0):
            roots.append(int(root1))
        if(isint(root2) and root2>=0 and int(root2) != int(root1)):
            roots.append(int(root2))
            
        if(len(roots)==0):
            return None
        else:
            return roots

for i in range(npart):
    for j in range(i+1,npart):
        #xroots
        xroots = solveQuad(quads[i][0], quads[j][0])
        if(xroots == None):
            continue
        yroots = solveQuad(quads[i][1], quads[j][1])
        if(yroots == None):
            continue
        zroots = solveQuad(quads[i][2], quads[j][2])
        if(zroots == None):
            continue
        sx = set(xroots)
        sy = set(yroots)
        sz = set(zroots)
        if(len(sx&sy&sz) == 0):
            continue
        coll = min(sx&sy&sz)
        collisions[coll].add(i)
        collisions[coll].add(j)

for sortedk in sorted(collisions.keys()):
    tset = collisions[sortedk].copy()
    tset2 = tset.copy()
    for i in tset:
        if(not exists[i]):
            tset2.remove(i)
    if(len(tset2) <= 1):
        continue
    for i in tset2:
        exists[i] = False
part2 = exists.count(True)

print("Part 1: {}\nPart 2: {}".format(part1, part2))