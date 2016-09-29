# -*- coding: utf-8 -*-
import xlrd
"""
从execl文件中获取数据，并获取数据，组合成JSON格式：

[{},{},{},{}]

"""
class RExecl(object):

    def __init__(self,filename):
        self.filename= filename
        self.workbook = xlrd.open_workbook(self.filename)
        self.list_menu=[]
        self.value=[]
        self.data=[]

    def ReadExcel_sheetnames(self):
        worksheets =self.workbook.sheet_names()
        print ('worksheets is %s' %worksheets)

    def Read_sheet_value(self):
        worksheet = self.workbook.sheet_by_index(0)
        num_rows = worksheet.nrows
        colns=worksheet.ncols
        for rown in range(num_rows):
            for clo in range(colns):
                if rown==0:
                    self.list_menu.append(worksheet.cell_value(rown,clo))
                else:
                    self.value.append(worksheet.cell_value(rown,clo))
            #使用zip方法，合成一个dict对象 key:value
            dic=dict(zip(self.list_menu, self.value))
            #把这个对象放入data数据中
            self.data.append(dic)
            #清空value的值，继续存放第二行数据
            self.value=[]
        return self.data[1:]
        #print   self.list_menu

    def list_zhongwen(self,list):
        print str(list).decode('string_escape')



if __name__=="__main__":
   testExcl= RExecl("D:\\code\\TikectGang\\keywordManager\\resource\\ticket1.xls")
   testExcl.ReadExcel_sheetnames()
   data=testExcl.Read_sheet_value()
   testExcl.list_zhongwen(data)