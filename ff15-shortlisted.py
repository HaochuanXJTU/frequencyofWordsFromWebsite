import urllib2
from bs4 import BeautifulSoup

page_list = list()
url_dict = dict()

for i in range(1,9):
    i = str(i)
    page_list.append("http://fotofilmic.com/ff15-shortlisted/page/" + i + "/")

for i in page_list:
    url = i
    user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
    headers = {'User-Agent': user_agent}
    request = urllib2.Request(url, headers=headers)

    response = urllib2.urlopen(request)
    bsObj = BeautifulSoup(response.read())
    before = bsObj.find_all("div", class_="portfolio-item-wrap")

    for text in before:
        url_ = text.find("a")["href"]
        name = url_.split("=")[1]
        url_dict[name] = url_

# print url_dict
print url_dict.__len__()

for i in url_dict:
    print i
    url = url_dict[i]
    user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
    headers = {'User-Agent': user_agent}
    request = urllib2.Request(url, headers=headers)

    response = urllib2.urlopen(request)
    bsObj = BeautifulSoup(response.read())
    before = bsObj.find("div", class_="content-wrap")

    minddle = before.find_all("p")

    print minddle[0].get_text()
    print minddle[2].get_text()