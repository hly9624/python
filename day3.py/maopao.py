#!/usr/bin/env python

l = [2,5,3,1,4]

i = 0
n = len(l)

while i < n - 1:
    j = 0
    while j < n - i - 1:
        if l[j] > l[j + 1]:
            l[j],l[j + 1] = l[j+ 1],l[j]
        j += 1

    i += 1
print l
