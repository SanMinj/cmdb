#!/usr/bin/env python
#encoding: utf-8

import  logging
logging.basicConfig(level = logging.info())

print reduce(lambda x,y:x+y,map(lambda x: x*x,[1,2,3]))

def log(fun):
    def wrapper(*args, **kw):
        print "this is log"
        return fun(*args,**kw)
    return wrapper
def log2(txt):
    def log(fun):
        def wrapper(*args,**kw):
            print "this is %s" % txt
            return fun(*args,**kw)
        return wrapper
    return log

@log2('rizhi')
def add(*args):
    num = 0
    for i in args:
        num = num + i
    return num


print add(*[1,2,3])