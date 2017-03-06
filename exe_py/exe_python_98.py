#-*-coding:utf-8 -*-

def save_file(parameter,file_name):
    parameter1=str(parameter)
    parameter=parameter1.upper()
    fp = open(file_name,'w')
    fp.write(parameter)
    fp.close()

def read_file(file_name):
    fp = open(file_name,'r')
    print fp.read()
    fp.close()

def wirte_order_chr(filename,parameter):
    fp=open(file_name,'w')
    if  parameter!='#':

        fp.write(parameter)
    else:
        fp.close()
        print "退出写入"


if __name__ == '__main__':
    string = raw_input('please input a string:\n')
    file_name='text.txt'
    save_file(string,file_name)
    read_file(file_name)
    wirte_order_chr(file_name,string)


