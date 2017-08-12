#!/usr/bin/env python

n = input()

def choushu(a):
    while a % 5 == 0:
        a /= 5
    while a % 2 == 0:
        a /= 2
    while a % 3 == 0:
        a /= 3
    if a == 1:
        return True
    else:
        return False

l = []

for i in range(1,n + 1):
    if choushu(i):
        l.append(i)

print l
