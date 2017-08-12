class A(object):
    def __getattr__(self,name):
        print "you use getattr no attr %s"%name
        return "no"

    def __setattr__(self,name,value):
        print "you use setattr"
        self.__dict__[name] = value

    def __delattr__(self,name):
        print "you use delattr"

a = A()

print a.k
a.x = "set x"

del a.k
