#encoding: utf-8

path = 'test.txt'
handle = open(path, 'r')
for line in handle:
    print '[%s]' % line
handle.close()