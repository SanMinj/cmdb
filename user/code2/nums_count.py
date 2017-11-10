#encoding:utf-8
chars = ['a', 'b', 'c', 'c', 'a', 'c', 'b', 'a', 'c', 1, 2]
char = raw_input('please input char:')
cnt = 0
for c in chars:
    if c == char:
        cnt += 1

print '%s:%d' % (char, cnt)