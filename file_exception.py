# -*- coding:utf-8 -*-
try:
    fh=open("testfile","r")
    fh.write("testing file")

except IOError:
    print "Error 没有找到文件或读取文件失败"
else:
    print "内容写入文件成功"
    fh.close()

