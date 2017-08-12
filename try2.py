#!/usr/bin/env python

def div(a,b):
    try:
        c = a / b
    except ZeroDivisionError as e:
        return e
    except TypeError as a:
        return a
    else:
        print "else........"
    finally:
        print "finally......."
    return c
result = div(3,'a')
print result
