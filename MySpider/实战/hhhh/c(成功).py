import requests
import re
import urllib
from requests.exceptions import RequestException
from lxml import etree



headers = {
            'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/68.0.3440.106 Safari/537.36',
            'Cookies':'__cfduid=df1a6ac07d4987ef517012601eda27bac1535098180;'
                      ' Hm_lvt_767e27c6fc5a7b6a90ba665ed5f7559b=1535097992,1535098758; Hm_lpvt_767e27c6fc5a7b6a90ba665ed5f7559b=1535098764'

        }


# 获取页面信息
def getHtml(url):
    html = requests.get(url=url, headers=headers).text
    return html

#通过正则获取图片
def getImg(html):
    reg = 'src="(.*?)"><br>'
    imgre = re.compile(reg)
    imglist = re.findall(imgre,html)
   # print(imglist)
    return imglist

def getUrl(offset):
    try:
        url = 'https://www.513ii.com/htm/piclist1/' + str(offset) + '.htm'
        response = requests.get(url=url,headers=headers)
        html = etree.HTML(response.text)
        items = html.xpath('//div[@class="mainArea"]//ul/li/a/@href')
        for item in items:
            # print(item1)
            new_url = "https://www.513ii.com" + str(item)
            # print(new_url)
            yield new_url

    except RequestException:
        return None

def main(offset):
    x=0
    for url in getUrl(offset):
        print(url)
        html = getHtml(url)
        list=getImg(html)
        #循环把图片存到本地
        # x = 0
        for imgurl in list:
            #print(imgurl)
            print(x)
            opener = urllib.request.build_opener()
            opener.addheaders = [('User-Agent',
                                  'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]
            urllib.request.install_opener(opener)
            urllib.request.urlretrieve(imgurl, './images/%s.jpg'% x)
            x+=1


if __name__ == '__main__':
    for i in range(1, 2):
        main(offset=i)

