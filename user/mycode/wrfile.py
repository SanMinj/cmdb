#!/usr/bin/env python
#encoding: utf-8
import os


print os.getcwd()

f = open(os.getcwd()+'/text.txt', 'r')
for i in f.readlines():
    print i
f.close()
print "-"*40

# read()会一次性读取文件的全部内容

with open(os.getcwd()+'/text.txt', 'r') as f:
    #print f.read()
    arr = f.readlines()
print arr
print arr[0].strip("")


# w 清空写, wb 二进制写, a 追加

_hander = open(os.getcwd()+'/text.txt', 'a')
_hander.write("nihao\nwangyqing")
_hander.close()


