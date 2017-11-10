#!/usr/bin/env python
#encoding: utf-8


class Studen(object):
    def __init__(self,name,addr):
        self.name=name
        self.addr=addr

    def getinfo(self):
        print "getinfo name:%s,addr:%s" % (self.name ,self.addr)

s1 = Studen("wyq","beijing")
s1.getinfo()


class Fruit(object):
    def __init__(self):
        self.name = "apple"
        self.proaddr = "beiing"

    def __repr__(self):
        return "this is %s class" % self.name


f = Fruit()
print f
print f.name




