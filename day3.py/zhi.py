#!/usr/bin/env python

l = [[1,5,7,3],[8,12,9,34],[6,32,67,89]]

outlen = len(l)
inlen = len(l[0])

for i in l:
    for j in l:
        print j,
    print ""

i = j = 0
x = y = 0
max = l[0][0]

while i < outlen:
    j = 0
    while j < inlen:
        if l[i][j] > max:
            max = l[i][j]
            x,y = i,j
        j += 1
    i += 1

print "l[%d][%d] = %d"%(x,y,max)
