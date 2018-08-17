
import requests
from lxml import etree
from requests.exceptions import RequestException
import time
import os
from hashlib import md5
import re


def get_one_page(offset):
    try:
        headers = {
            'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko)'
                         ' Chrome/68.0.3440.84 Safari/537.36',
        }
        url = 'https://www.241nn.com/htm/piclist9/' + str(offset) + '.htm'
        response = requests.get(url=url,headers=headers)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        return None

def parse_one_page(html):
    html = etree.HTML(html)
    items1 = html.xpath('//div[@class="box list channel"]//ul//a/@href')
    # items2 = html.xpath('//div[@class="box list channel"]//ul/a/text()')
    for item1 in items1:
        #print(item1)
        new_url = "https://www.241nn.com/htm/piclist9" + str(item1)
        print(new_url)
        response = requests.get(url=new_url)
        html = response.text
        # results = re.findall('<img.*?src="(.*?)">', html, re.S)
        html = etree.HTML(html)
        url_images = html.xpath('//div[@class="wrap mt10"]//img/@src')
        for url_image in url_images:
            print(url_image)


def save_image(item1):
        new_url = "https://www.241nn.com/htm/piclist9/" + str(item1)
        print(new_url)
        response = requests.get(url=new_url)
        if response.status_code == 200:
            html = response.text
            #results = re.findall('<img.*?src="(.*?)">', html, re.S)
            html = etree.HTML(html)
            url_images = html.xpath('//div[@class="wrap mt10"]//img/@src')
            for url_image in url_images:
                yield {
                    'b':url_image
                }

def main(offset):
    html = get_one_page(offset)
    parse_one_page(html)



if __name__ == '__main__':
    for i in range(1,2):
        main(offset=i)
        time.sleep(1)