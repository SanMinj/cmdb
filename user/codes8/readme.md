1. 复习  20
    class ClassName(object):
        attr_class_define

        def method(self, *args, **kwargs):
            pass

        @classmethod
        def cmethod(cls):
            pass

        @staticmethod
        def smethod():
            pass

    class Child(Parent):
        attr_class_define

        def __init__(self, *args, **kwargs):
            super(Child, self).__init__(*args, **kwargs)
            self.name = 'xxx'
            pass

        def getName(self):
            return self.name



2. 作业  10
    增、删、改、查
    增加: 表，增加的字段不一样
    更新: 表，更新的字段不一样

3. 新课程
    a. 模块
    d. 监控，获取主机上的cpu，内存使用率 ip
    c. agent => server
    d. server 接收，存储
    f. 展示highcharts

182.61.42.4
root
1qaz@WSX

a. 模块
    0) 百度, google, pypi, 问人
    1) pip install xxxx
    2) import
    3) dir()
    4) help()
    5) 用

i. os
    listdir
    path模块

    system/popen


    
把/home/woniu/class09/kk/11目录中的所有文件路径放在list中

def getfiles(dirpath):
    _rt_list = []
    遍历 拿出文件夹下所有的文件名(name)
    path = dirpath + '/' + name
    文件
        return []
    目录
        _rt_list.extends(getfiles(path))
    return _rt_list


sys

argparse
time/datetime

unix
struct_time
str
datetime

hashlib => md5
logging, traceback.format_exc()

* paramiko => ssh
    cmd & scp
getpass

agent 
ip
ifconfig

cpu 使用率: (1 - id) * 100
top -n 1

内存使用率: (1 - (buffer + free) / total) * 100
/proc/memifno


psutil

restapi
http请求 规范
一切皆资源
resources

GET /resources/<pk>/
    /resources/
    获取资源

POST /resources/
    cpu=xxx&ram=xxx&time=xxx&ip=xxx
    cpu=xxx
    ram=xxx
    time=xxx
    ip=xxx
    {"cpu" : xxx, "ram" : xxx, "time" : "xxx", "ip":""}
    创建/添加资源 

PUT /resources/<pk>/
    cpu=xxx&ram=xxx&time=xxx&ip=xxx
    cpu=xxx
    ram=xxx
    time=xxx
    ip=xxx
    {"cpu" : xxx, "ram" : xxx, "time" : "xxx", "ip":""}
    创建/更新资源
    pk存在: 更新
    pk不存在: 创建

DELETE /resources/<pk>/


CREATE table performs(
    id bigint primary key auto_increment,
    ip varchar(128),
    cpu float,
    ram float,
    time datetime
)engine=innodb default charset=utf8;









作业
1. asset的采购时间改成%Y-%m-%d
2. 添加用户，修改用户密码改为md5_str函数
3. 今天的课程上的做完

4. web执行命令
    form 提交ip, port, username, password, cmds=> ssh.py 获取结果显示
                管理员的密码=>  