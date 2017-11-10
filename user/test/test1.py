#encoding: utf-8

key = ('a','b','d')
val = ('1','2','3')

#a = key[1:]
arr = [('a',1),('b',2)]
dic = [dict(zip(key,val))]

value = range(3)
print dic[0]
for key , val in arr:
    #print "k is {key}".format(key= key)
    #print "v is {val}".format(val=val)
    print "k is %s , va is %s"  %(key , val)
#print value

#change return color
def G(s):
    return "%s[32;2m%s%s[0m"%(chr(27), s, chr(27))
def A(s):
    return "%s[36;2m%s%s[0m"%(chr(27), s, chr(27))
def R(s):
    return "%s[31;2m%s%s[0m"%(chr(27), s, chr(27))

def test(m):
    return A(m)

a = test("hello world")
print a
va = ['abcd','dddd']
print va.index('abcd')


