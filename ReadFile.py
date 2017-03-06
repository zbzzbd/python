#-*- coding:UTF-8 -*-
import os

class  ReadFile(object):

    def __init__(self,fileName):
        self.fileName= fileName
        self.fo = open(fileName, "r")

    def Write_File(self,str):
        self.fo.write(str)

    def Set_seek_position(self,index):
        position=self.fo.seek(index)

    def Read_Content(self,index):
        str = self.fo.read(index)
        return str

    def Close_File(self):
        self.fo.close()

    def Tell_positjion(self):
        return self.fo.tell()

    def Rename_file(self,newFileName):
        try:
            os.rename(self.fileName,newFileName)
        except WindowsError:
            print "系统调用失败"

    def Read_Line(self):
        data = [line.split(' ') for line in self.fo.readlines()]
        return data


    def Read_line_file(self):
        for line in self.fo.readlines():
            if line.find("com.wuba"):
                self.fo1=open("log.txt","wb")
                self.fo1.write(line)





    def Parsing_sort_count(self,data):
        count_200=0
        count_300=0
        count=0
        for d in data:
            print d[0]
            if d[0]=='200':
                count_200+=1
            elif d[0]=='300':
                count_300+=1
            else:
                count+=1

        return count,count_200,count_300

if __name__=="__main__":
    file= ReadFile("androdlog.txt")
    file.Read_line_file()
    #file.Write_File("my home is")
    #print file.Read_Content(2)
    #print file.Tell_positjion()
    #file.Rename_file("text.txt")
    """
    print file.Parsing_sort_count(data)
    file.Close_File()
    """

