# -*- coding: utf-8 -*-

#读取EXCEL 数据
import xlrd

class ReadAndWriteExcel:

    def __init__(self):
        self.FilePath=None
        self.sheetName=None
        self.data=None

    """
    设置文件的路径并打开excel文件
    """
    def Set_ExcelPath(self,filePath):
        self.FilePath=filePath
        self.data = xlrd.open_workbook(self.FilePath,'r+b')

    """
    读取EXCEL某行某列的值
    """
    def ReadExecl(self,SheetName,row_index,column_index):
        table = self.data.sheets()[0]
        table1 = self.data.sheet_by_name(SheetName).cell(row_index,column_index)
        print 'sheet %s' %table1
        return table1


    if __name__=='__main__':
        Set_ExcelPath('D:\\code\\ganggang_test\\test.xls')
        ReadExecl('Sheet1',0,3)