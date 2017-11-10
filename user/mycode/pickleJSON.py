#!/usr/bin/env python
#endcoding: utf-8
import os
import json

try:
    import  cPickle as pickle
except ImportError:
    import pickle

d = dict(name="wyq",addr="beijing",hob="sports")
a  = pickle.dumps(d)

f = open(os.getcwd()+'/text.txt', 'ab')
pickle.dump(d,f)
f.close()

#dumps 全部序列化 loads 全部反序列化

json.dumps(d)
print json.loads(json.dumps(d))
