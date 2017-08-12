#!/usr/bin/env python
#coding=utf-8

def div(a,b):
    try:
        return a / b
    except (ZeroDivisionError,TypeError):
        return "division erro or type error"
result = div(3,1)
print result
