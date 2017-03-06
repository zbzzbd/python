#-*- coding:utf-8 -*-

"""
文件的读取
"""

class ReadFile(object):


    def Open_file(self,filename,Read_type):
        f=None
        content=""

        try:
            f=open(filename,Read_type)
            content=f.read()
        except IOError,e:
            print '文件打开异常',e
        finally:
             if f is not None:
                 f.close()
        return content




if __name__ =="__main__":
    file=ReadFile()
    content=file.Open_file('test.txt','r')
    print content
