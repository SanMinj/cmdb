#encoding: utf-8
names = ['woniu', 'kk', 'wd']
name = 'wd'
exists = False

for _name in names:
    if _name == name:
        exists = True
        break

if exists:
    print '在'
else:
    print '不在'

#list:访问, max, min, len