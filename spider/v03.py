'''
利用request下载页面
自动检测页面编码
'''

import urllib


if __name__ == '__main__':
    url = "https://baike.baidu.com/item/url/110640?fr=aladdin"

    rsp = urllib.request.urlopen(url)

    print(type(rsp))
    print(rsp)

    print("URL: {0}".format(rsp.geturl()))
    print("INFO:  {0}".format(rsp.info()))
    print("Code: {0}".format(rsp.getcode()))


    html = rsp.read()

    html = html.decode()

