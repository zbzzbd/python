#-*- coding:utf-8 -*-
"""
爬虫
"""
import urllib
import  re
class PaChong(object):


    def getHtml(self,url):
        page = urllib.urlopen(url)
        html = page.read()
        print html
        return html

    def get_img(self,html):
        reg = r'src=".+\.jpg">'
        imgre =re.compile(reg)
        imglist=re.findall(imgre,html)
        #x=0
        #for imgurl in imglist:
            #urllib.urlretrieve(imgurl,'%s.png'%x)
            #x+=1
        print len(imglist)
        return imglist

if __name__ =="__main__":
    page=PaChong()
    pagehtml=page.getHtml('http://www.ggang.cn')
    if pagehtml:

        page.get_img(pagehtml)