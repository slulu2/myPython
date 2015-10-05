
import requests
import urllib
import re


def getHtml(url):
    page = urllib.request.urlopen(url)
    html = page.read()
    return html

def getImage(html):
    reg = r'"900" src="(.*?\.jpg)" pi'.encode("GBK")
    # print(type(reg))
    imgre = re.compile(reg)
    # print(imgre)
    imglist = re.findall(imgre, html)
    print(imglist)
    x=0
    imgurl2 = ''
    for imgurl in imglist:
        # imgurl2 = imgurl.decode('utf-8')
        print(x)
        imgurl2 = imgurl.decode()
        # print(type(imgurl2))
        urllib.request.urlretrieve(imgurl2, '%s.jpg' % x)
        x += 1
    print("OK!")

    # return imglist



html = getHtml("http://tieba.baidu.com/p/4046378949?pn=1")
getImage(html)
