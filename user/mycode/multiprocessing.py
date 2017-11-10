#!/usr/bin/env python
#encoding: utf-8

import os
import multiprocessing

#print "process  %s start" % os.getpid()
#pid = os.fork()
#if pid==0:
#    print 'I am child process (%s) and my parent is %s.' % (os.getpid(), os.getppid())
#else:
#    print 'I (%s) just created a child process (%s).' % (os.getpid(), pid)

# 子进程永远返回0
# 但是fork()调用一次，返回两次，因为操作系统自动把当前进程（称为父进程）复制了一份（称为子进程），然后，分别在父进程和子进程内返回


def run_fun(name):
    print "this is %s runid--> %s" % (name ,os.getpid())

if __name__=='__main__':
    print 'Parent process %s.' % os.getpid()
    p = multiprocessing.Process(target=run_fun, args=('test',))
    print 'Process will start.'
    p.start()
    p.join()
    print 'Process end.'