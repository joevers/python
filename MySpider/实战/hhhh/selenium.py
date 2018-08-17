import requests
from requests.exceptions import RequestException
from selenium import webdriver




def get_page(offset):
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

def selenium(url):
    browser = webdriver.Chrome()
    browser.get(url)
    input = browser.find_element_by_id('text_box')
    new_url = "https://www.241nn.com"+ input.text