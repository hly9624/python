#!/usr/bin/env python
#coding=utf-8

def div(a,b):
    try:
        return a / b
    except ZeroDivisionError:
        return "zero can not be divsion"
result = div(3,0)
print result
