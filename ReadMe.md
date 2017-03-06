#Python学习日志

##2016-09-01
####1. json 格式的解析： 使用demjson包，
使用encode： 将PYTHON对象编码成JSON字符串
 data = [ { 'a' : 1, 'b' : 2, 'c' : 3, 'd' : 4, 'e' : 5 } ]
 json = demjson.encode(data)
 最后效果：[{"a":1,"b":2,"c":3,"d":4,"e":5}]

 decode:将字符串转化成JSON对象
    json = '{"a":1,"b":2,"c":3,"d":4,"e":5}';text = demjson.decode(json)

##2016-8-20
####1.sokect,套接字，向网络发送请求护着应答网络请求，使主机进程之间可以实现通信
建立sokect的过程：
#####服务器：
    (1)建立SOKCET（tcp_Conn=socket.socket(socket.AF_INET,socket.SOCK_STREAM)）
    (2)绑定IP地址与端口（ tcp_Conn.bind((self.ip,self.port))）
    （3）无限监听状态（tcp_Conn.listen(20) 20是指的接受报文的长度）
    （4）cinfo,caddr = tcp_Conn.accept()
    （5）cinfo.recv(1024) 接收TCP数据，数据以字符串形式返回
   注意：socket.AF_INET：使用INTERNET 地址进行通讯 SOCKET.AF_UNIX:UNIX_SOKCET 文件形式实现通讯
   socket.SOCK_STREAM： 使用TCP协议流式套接字
   socket.
#####客户端：
     （1）创建sokcet，socket.socket(socket.AF_INET,socket.SOCK_STREAM))
     （2）建立连接：client_sokcet.connect((self.server_ip,self.ser_port))
     （3）发送内容client_sokcet.send('hello world')
      (4)接收内容：data = client_sokcet.recv(1024)


##2016-08-19
#####1.链接数据库，首先建立连接对象MYSQL.connect，然后创建游标对象conn.cur()，基于游标发送请求cur.execute()，获取结果cur.fetchone()
然后关闭游标cur.close()

#####2.cur.callpro() 调用存储过程函数
#####3.批量插入： sqlInsert="insert into tab1(name) value (%s)",cur.execute(sqlinsert,'zbz')
如果是多个值，直接使用元组的方式插入：cur.execute(sqlinsert,('zbz','tom'))
#####4.插入多行时，使用cur.executemany(sqlinsert,[('zbz'),('tom')])

#####5.python -c "print 'hello world'"，，格式：python -c CMD命令
-V 跟踪导入， -V阻止导入站点目录


##2016-08-18
#####
#####1.python 面向对象三大原则： 封装、继承、多态
#####2.try except  else ，try finally（清理工作、关闭服务器，关闭文件，断开发服务器等）
#####3.一般情况下site-package 目录下存在的包是第三方扩展包的安装路径
#####4.耦合性：1）尽可能通过参数，以及通过return 产生输出 2）尽量减少全局变量
（3）不能在函数中修改类型参数
（4）避免直接修改另一个模块中的变量
#####5.yield 生成器：函数中自定义yield,返回一个生成器对象

##2016-08-01
#####1.json.dumps(data)  # 将PYTHON对象转化成字符串
#####2.json.loads(data)   #把字符串转化成Python 对象
##2016-07-23
#####1.python 文件O/I 读取文件知识： 基本要点是 先使用open() 方法创建一个文件对象，使用文件对象中的
  read 进行读取每个字节，readline() 读取每行，readLines()读取所有行
  write进行写入，Close() 关闭文件，tell（）告诉读取位置， seek()设置读取位置
#####2.应用：使用Python 进行解析LOG日志：  data = [line.split(' ') for line in self.fo.readlines()]