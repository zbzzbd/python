#Python学习日志

##2016-07-23学习日志
#####1.python 文件O/I 读取文件知识： 基本要点是 先使用open() 方法创建一个文件对象，使用文件对象中的
  read 进行读取每个字节，readline() 读取每行，readLines()读取所有行
  write进行写入，Close() 关闭文件，tell（）告诉读取位置， seek()设置读取位置
#####2.应用：使用Python 进行解析LOG日志：  data = [line.split(' ') for line in self.fo.readlines()]
