#!/usr/bin/env python

def div(a,b):
    try:
        return a / b
    except (ZeroDivisionError,TypeError) as e:
        print "e >>>>>>>>>>>",e
        return "division error or type error"

result = div(3,0)
print result
