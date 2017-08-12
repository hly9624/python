#!/usr/bin/env python

i = 2

while i <= 100:
    n = 0
    b = 2
    while b <= i / 2:
        if i % b == 0:
            n = 1
            break
        b += 1
    if n == 0:
        print "%d"%i,

    i += 1
print ""
