# 初始化tcp / init tcp
import socket
import re
import os
import time
import gevent

home_dir = 'folder_for_http_server'  # 设置工作目录/Set working directory
head = 'HTTP/1.1 200 OK \nServer: Python \nConnection:close \n Content-Length:200\t\n\n'
head404 = 'HTTP/1.1 404 NOT Found \nServer: Python \nConnection:close \n Content-Length:200\t\n\n'
tcp_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


def read_file(file_name):
    file_name = home_dir + file_name
    print('file to open: ' + file_name)
    try:
        f = open(file_name, 'rb')
        c = f.read()
        f.close()
        return c
    except Exception:
        return '<h1>404 not found <h1>'.encode('utf-8')


def send(client, req_path):
    try:
        return_content = read_file(req_path)
        client.send(head.encode('utf-8'))
        client.send(return_content)
        print('data sent')
    except Exception:  # 404错误信息/404 error info
        client.send(head404.encode('utf-8'))
        client.send(read_file('404.html'))
        print('catch a 404:' + req_path)
    client.close()


# 端口复用


# 绑定端口/bind port
ip_port = ('', 8000)
tcp_server.bind(ip_port)

# 被动模式/passive mode
tcp_server.listen(128)


# 监听/ listen


def proc():
    # 接受/accept clients
    client, addr = tcp_server.accept()

    # 接收数据/receive data
    rec_data = client.recv(1024)
    rec_text = rec_data.decode('utf-8', errors='ignore')
    print('接收到请求:%s\n' % rec_text)

    # 数据处理/data processing
    try:

        tmp = re.match('GET .+?.+ HTTP/1.1', rec_text).group()  # 获取请求路径
    except BaseException:
        if re.match('GET .+ HTTP/1.1', rec_text):
            tmp = re.match('GET .+ HTTP/1.1', rec_text).group()  # 获取请求路径
        else:
            return
    req_path = re.sub('GET\s|\sHTTP/1.1', '', tmp)

    print('请求目录req_path：' + req_path)
    # 判断是否为文件/ request a file or directory?

    print(os.path.isfile(home_dir + req_path))

    if req_path.find('?'):
        req_path = req_path.split('?')[0]  # '?' 检测

    if os.path.isfile(home_dir + req_path):
        # 是文件,打开发送文件数据/ if file,send file
        send(client, req_path)
    else:
        # 若请求的只是路径,打开目录下index文件发送/ if directory open index file

        if req_path.endswith('/'):  # 判断请求路径结尾是否带‘/’  /is end with /?
            send(client, req_path + 'index.html')
        else:
            send(client, req_path + '/index.html')


while True:
    g1 = gevent.spawn(proc)
# g2 = gevent.spawn(proc)

#
    g1.join()
# g2.join()



# GET / HTTP/1.1
# User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppfleWebKit/537.36 (KHTML, like Gecko)\
#  Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134
# Accept-Language: zh-Hans-CN,zh-Hans;q=0.8,en-GB;q=0.5,en;q=0.3
# Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
# Upgrade-Insecure-Requests: 1
# Accept-Encoding: gzip, deflate
# Host: localhost
# Connection: Keep-Alive


# 返回数据