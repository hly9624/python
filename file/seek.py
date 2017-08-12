# coding=utf-8

f = open('file','r+')

s = f.read(6)

print f.tell()    #显示字符串位置
# f.seek(6)    #seek文件位置偏移  6:代表偏移量  0:默认值重文件开头
# f.seek(6,1)          #1是当前位置开始
f.seek(-7,2)          #2是从结尾开始
print f.read(6)
