#!/usr/bin/env python

def funm(x):
    return x ** 2

def funf(x):
    return x > 2 and x < 5

def funr(x,y):
    return x + y

l = [1,2,3,4,5]
l1 = [6,7,8,9]

print map(funm,l)
print filter(funf,l)
print reduce(funr,l)
print zip(l,l1)
