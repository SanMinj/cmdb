#encoding: utf-8
import  sys
from collections import Iterable

dic_t = {"a":"1","b":"2","c":"3"}
for i,k in dic_t.items():
    print "%s == %s" % (i,k)

list_tmp=[]
for value in dic_t.itervalues():
    list_tmp.append(value)
print dict(zip(('a','b','c'),list_tmp))

arr_t = [('a',1),('b',2),('c',3)]
print arr_t

print isinstance('abc', Iterable)

for i, value in enumerate(['A', 'B', 'C']):
    print i,value



for i,k in arr_t:
    print "%s == %s" % (i, k)

num = int(raw_input("please input a num : "))
str = ''
if num < 0:
    str = 'num < 0'
elif num ==0:
    str = 'num =0'
else:
    str = 'num > 0'

print str
print sys.argv[0]

