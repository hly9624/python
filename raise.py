#!/usr/bin/python
#coding=utf-8
class MyError(Exception):#创建一个异常类 自定义异常
    pass
s = raw_input()
try:
    if s == "error":
        print "This is my error"
        raise MyError("no error mesage")#raise触发异常 人为抛出异常
    else:
        print s
except MyError as e:
    print "Error mesage:"
    print e
