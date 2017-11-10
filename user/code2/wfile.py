#encoding: utf-8

handler = open('user2.txt', 'w')
handler.writelines(['kk:123,woniu:12,ada:564', ',kk:123,woniu:12,ada:564', ',kk:123,woniu:12,ada:564'])
handler.close()