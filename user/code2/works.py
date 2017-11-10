#encoding: utf-8

'''

从命令行接收输
如果输入add，再进行接收，并将接收工作内容加入到works后面
如果输入do, 就打印works最前面内容，并进行移除
    如果works没有工作内容，提示没有工作内容
如果输入的是exit
    检查works中是否有工作内容, 如果有工作内容则提示，如果没有工作内容则退出
'''

works = []

while True:
    _action = raw_input('你要干嘛?(add=>添加, do=>执行):')
    if _action == 'add':
        _work = raw_input('请输入工作内容:')
        works.append(_work)
        #works.append(raw_input('请输入工作内容:'))
    elif _action == 'do':
        if len(works) == 0: # if not works:
            print '没有工作内容'
        else:
            print '工作内容:%s' % works.pop(0)
    elif _action == 'exit':
        if len(works) != 0: # if works:
            print '还有工作未完成, 你别跑'
        else:
            break
    else:
        print '你输入不正确!!!'
