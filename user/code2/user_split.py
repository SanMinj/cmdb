#encoding: utf-8

handler = open('user.txt', 'r')
s = handler.read()
handler.close()

rt_list = []
for user in s.split(','):
    name, uid = user.split(':')
    rt_list.append((name, int(uid)))
print rt_list