#!/usr/bin/env python3

def fun(a,b = 10,*c,d = 100):
    print (a)
    print (b)
    print (c)
    print (d)

fun(1,2,3,4,5,d =6)




def fun1(a,b = 10,*c,d = 100,**e):
    print (a)
    print (b)
    print (c)
    print (d)
    print (e)

fun1(2,3,4,5,6,7,e = 8,f = 9,d =12)
