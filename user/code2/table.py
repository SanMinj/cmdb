#encoding: utf-8

a = '''
1 * 1 = 1   1 * 2 = 2   1 * 3 = 3                               1 * 9 = 9
2 * 1 = 2   2 * 2 = 4                                           2 * 9 = 18
3 * 1 = 3                                                       3                   
'''

for i in range(1, 10):
    for j in range(1, i + 1):
        print '%s * %s = %-2s' % (i, j, i * j),
    print ''

if xxxx:
    if语句

if xxxx:
    if语句
else:
    else语句

if xxx:
    if语句
elif xxx:
    elif语句
elif xxx:
    elif语句
else:
    else语句

while xxx:
    while语句

for x in 可遍历的元素:
    for语句

range(start, end)