#!/usr/bin/env python
#coding=utf-8
a = 5
b = 4

def fun():
    global a,b     #收集全局变量,以字典的形式打印
    a += 1
    b += 1
    print a,b

    c,d = 1,2
    return locals()   #收集局部变量,以字典的形式打印

print fun()
print a

print globals()
