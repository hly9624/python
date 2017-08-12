#!/usr/bin/env python
#coding=utf-8

def fun(a,b):
    print a,b

#位置传参
fun(1,2)

#关键字传参
fun(a = 2,b = 3)

# * 传参

l = [7,8]
fun(*l)

# **传参

d = {'a':9,'b':6}
fun(**d)
