#-*-coding:utf-8 -*-

import socket
import os
import re

class Sever_sockert:
    """
    1.创建套接字对象
    """

    def __init__(self,ip,port):
        self.ip= ip
        self.port = port

    def  socket_create(self):

        tcp_Conn=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        #绑定IP地址及端口
        tcp_Conn.bind((self.ip,self.port))
        #接受长度 20
        tcp_Conn.listen(20)
        while True:

            cinfo,caddr = tcp_Conn.accept()
            print "Get a connection from %s" %caddr[0]
            data = cinfo.recv(1024)
            print "Receive data: %s" %data
            cinfo.send("echo: " +data)
            cinfo.close()

if __name__=="__main__":
    sco=Sever_sockert('127.0.0.1',8023).socket_create()



