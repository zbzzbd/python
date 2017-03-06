# -*-coding:utf-8 -*-

if __name__=='__main__':
    person = {"l1":18,"wang":50,"zhang":20,"sun":22}
    m = 'l1'
    for key in person.keys():
        if person[m] < person[key]:
            m = key

    print '%s,%d' %(m,person[m])