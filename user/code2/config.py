#encoding: utf-8

port = 8888
server = 'default'
servername = 'cmdb'
access_log = '/var/log/cmdb.log'
home = '/home/kk/www'
proxy_port = 9999

rh = open('nginx.tpl')
nginx_conf = rh.read().format(port=port, server=server, servername=servername, access_log=access_log, home=home, proxy_port=proxy_port)
rh.close()

handler = open('cmdb.conf', 'w')
handler.write(nginx_conf)
handler.close()

#作业
#1. web访问日志
#2. nginx配置文件模板 生成 固定项目配置
#3. copy文件
#4. 整理mm图
