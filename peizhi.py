import ConfigParser
import string, os, sys

def ReadConfig(path,name,str):
    config = ConfigParser.ConfigParser()
    config.read(path)
    url_path =config.get(name,str)
    return url_path

if __name__ =='__main__':
    s=ReadConfig("test.conf","zixun","2")
    print s
