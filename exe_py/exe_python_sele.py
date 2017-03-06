#-*-coding:utf-8-*-
from selenium import webdriver


def _get_base_url(url):

    if '/' in url:
        print url.split('/')
        print '*'.join(url.split('/'))[:]
        print '*'.join(url.split('/'))[:-1]
        url = '/'.join(url.split('/'))[:-1]
    return url

if __name__ == "__main__":
    url ="http://sso.ggang.cn/SSoOperater/SSoLoginIndex?url=http://user.ggang.cn/"
    u= _get_base_url(url)
    print u.encode("utf-8")