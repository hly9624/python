#!/usr/bin/env python

def fun(n):
    for i in n:
        for j in n:
            if j % 2 != 0 & i % 2 == 0:
                i,j = j,i
    print i

l = [1,2,3,4,5,6,7,8,9]
fun(l)
