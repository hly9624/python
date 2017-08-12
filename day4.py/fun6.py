#!/usr/bin/env python
#coding=utf-8

def fun(a,b,*c):
    print a
    print b
    print c

fun(1,2,3,4,5,6)


#1.无默认值的形参在有默认值的形参前面
#2.有默认值的形参在 * 前面
#3.* 在 ** 的前面
def fun1(a,b = 7,*c,**d):
    print a
    print b
    print c
    print d

fun1(1,2,3,4,5,6,c = 7,d = 8)
