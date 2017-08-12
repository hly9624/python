#!/usr/bin/env python
#coding=utf-8

#定义位置参数的函数
def fun(a,b):
    print a,b

fun(1,2)

#设置参数默认值
def fun1(a,b =5):  # 有默认值的形参必须在没有形参的后面
    print a,b

fun1(1)

#定义收集参数的函数

def fun2(*a):
    print a

fun2(1,2,3,4,5,6)

#收集字典参数函数

def fun3(**a):
    print a

fun3(a = 1,b = 2,c = 3)
