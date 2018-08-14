from urllib.parse import urlencode
import requests
from pyquery import PyQuery as pq


base_url = "https://m.weibo.cn/api/container/getIndex?uid=2830678474&luicode=10000011&lfid=100103" \
           "type%3D3%26q%3D%E5%B4%94%E5%BA%86%E6%89%8D%26t%3D0&"

headers =  {
    'Host':'m.weibo.cn',
    'Referer':'https://m.weibo.cn/u/2830678474?uid=2830678474&luicode=10000011&lfid=100103type%3D3'
              '%26q%3D%E5%B4%94%E5%BA%86%E6%89%8D%26t%3D0',
    'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) '
                 'Chrome/68.0.3440.84 Safari/537.36',
    'X-Requested-With':'XMLHttpRequest',
}
def get_page(page):
    params = {
        'type':'uid',
        'value':'2830678474',
        'containerid':'1076032830678474',
        'page':page
    }

    url = base_url + urlencode(params)
    try:
        response = requests.get(url=url, headers=headers)
        if response.status_code == 200:
            return response.json(), page
    except requests.ConnectionError as e:
        print('Error:',e.args)



def parse_page(json, page:int):
    if json:
        items = json.get('data').get('cards')
        for index, item in enumerate(items):
            if page ==1 and index==1:
                continue
            else:
                item = item.get('mblog')
                weibo={}
                weibo['id'] = item.get('id')
                weibo['text'] = pq(item.get('text')).text()
                weibo['attitudes'] = item.get('attitudes_count')
                weibo['comment'] = item.get('comments_count')
                weibo['reposts'] = item.get('reposts_count')
                yield weibo

if __name__ == '__main__':
    for page in range(1,11):
        json = get_page(page)
        results = parse_page(*json)
        for result in results:
            print(result)