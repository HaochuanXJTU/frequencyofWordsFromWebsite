# -*- coding:utf-8 -*-
import urllib2
from bs4 import BeautifulSoup

html = urllib2.urlopen("http://www.life-framer.com/collection/")
bsObj = BeautifulSoup(html.read())

list = bsObj.find_all("h3")

ZiDian = dict()

for i in list:
    if not i.find("a") == None:
        ZiDian[i.find("a").get_text()] = i.find("a")["href"]



for i in ZiDian:
    second_html = urllib2.urlopen(ZiDian[i])
    bsObj = BeautifulSoup(second_html.read())
    WenZi = bsObj.find("div", class_="fusion-column-wrapper")
    print i
    QuanWen = WenZi.find_all("p")

    for j in QuanWen:
        if j.get_text() == " " or j.get_text() == "":
            continue
        print j.get_text()



