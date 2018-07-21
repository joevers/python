'''
使用urllib.request请求一个网页内容,并将其打印

'''

from urllib import request

if __name__ == '__main__':

    url = "https://baike.baidu.com/item/url/110640?fr=aladdin"
    # 打开相应的URL并把相应的页面作为返回
    rsp = request.urlopen(url)

    html = rsp.read()

    # 解码
    html = html.decode()

    print(html)