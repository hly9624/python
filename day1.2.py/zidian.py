#!/usr/bin/env python
#coding=utf-8
#字典

d = {'a':1,'b':2,'c':3}

print d.values()   #获取所有的值
print d.keys()     #获取对应键的所有列表
print d.get('b')    #获取对应键的值
print d.has_key('a') #获取指定键,有返回true,无返回false
print d.pop('c')     #弹出对应的键
print d.popitem()    #随机删除字典中的一对键和值
print d.clear()       #删除字典内所有元素
