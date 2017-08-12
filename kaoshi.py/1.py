#!/usr/bin/env python
#coding=utf-8

def addrs(a,b,c):
    try:
        l = a + b + c
        print l

    except TypeError as e:
        print "e>>",e
        return "division error or type error"

result = addrs('a',2,3)
print result
