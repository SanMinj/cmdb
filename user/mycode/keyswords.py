#! /usr/bin/env python
#encoding: utf-8

'''
*name 必须在 **name 之前

**name 接受一个字典
*name  接受一个数组
'''

def cheeseshop(kind, *arguments, **keywords):
    print "-- Do you have any", kind, "?"
    print "-- I'm sorry, we're all out of", kind
    for arg in arguments:
        print arg
    print "-" * 40
    keys = sorted(keywords.keys())
    for kw in keys:
        print kw, ":", keywords[kw]

cheeseshop("Limburger", "It's very runny, sir.",
           "It's really very, VERY runny, sir.",
           shopkeeper='Michael Palin',
           client="John Cleese",
           sketch="Cheese Shop Sketch")
cheeseshop("apple","a","b",name="nihao",add="beijing")



list(range(3, 6))            # normal call with separate arguments
#[3, 4, 5]
args = [3, 6]
list(range(*args))            # call with arguments unpacked from a list
#[3, 4, 5]
#你可以在调用函数时加一个 * 操作符来自动把参数列表拆开




print "-" * 40
def parrot(voltage, state='a stiff', action='voom'):
    print "-- This parrot wouldn't", action,
    print "if you put", voltage, "volts through it.",
    print "E's", state, "!"
d = {"voltage": "four million", "state": "bleedin' demised", "action": "VOOM"}
parrot(**d)
# ** 操作符分拆关键字参数为字典

a = lambda x,y:x*y
print a(3,4)

#列表生成器
print [x * x for x in range(1, 11) if x % 2 == 0]
print '-'*50
print ''.join(['aaa',' ','bbbb','cccc'])