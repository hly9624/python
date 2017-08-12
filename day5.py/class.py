#!/usr/bin/env python
#coding=utf-8
class Person(object):
    def __init__(self,name,age = 14):
        self.name = name
        self.age  = age
    #age = 10


    def color(self,c):
        print "%s is %s,he is %d"%(self.name,c,self.age)


boy1 = Person("Jame",16)

#boy1.age = 13

print boy1.age

print boy1.name

boy1.face = "帅"    #可以定义私有属性,只可以自己用,不改变类

boy1.color("pink")

print boy1.face

print "==============================="

boy2 = Person("Lilei")

print boy2.age

print boy2.name

boy2.color("pink")

print "=============================="

#print  Person.age     #类可以直接调用固有属性
#print  Person.color   #类不可以直接调用方法
