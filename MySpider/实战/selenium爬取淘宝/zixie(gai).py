from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from urllib.parse import quote
from pyquery import PyQuery as pq
import pymongo
import time



client = pymongo.MongoClient(host='localhost', port=27017)
db = client.taobao
collection = db.products

browser = webdriver.Chrome()
wait = WebDriverWait(browser,10)
KEYWORD = 'iPad'

def index_page(page):
    print("正在爬取第", page, "页")
    try:
        if page == 1:
            url = "https://s.taobao.com/search?q="+quote(KEYWORD)
            browser.get(url)
            time.sleep(5)
            #input = wait.until(
            #    EC.presence_of_element_located((By.CSS_SELECTOR, '#spudetail-pager div.form > input')))
            button = wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, '#spudetail-pager div.form > '
                                                           'span.btn.J_Submit')))
            button.click()
            time.sleep(2)
        if page > 1:
            input = wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, '#mainsrp-pager div.form > input')))
            submit = wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, '#mainsrp-pager div.form > '
                                                             'span.btn')))
            input.clear()
            input.send_keys(page)
            submit.click()
        wait.until(
            EC.text_to_be_present_in_element((By.CSS_SELECTOR, '#mainsrp-pager li.item.active'
                                                               ' > span'),str(page)))
        wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '.m-itemlist .items .item')))
        get_products()
    except TimeoutException:
        index_page(page)


def get_products():
    html = browser.page_source
    doc = pq(html)
    items = doc('.m-itemlist .items .item').items()
    for item in items:
        product = {
            'image':item.find('.pic .img').attr('data-src'),
            'price':item.find('.price').text(),
            'deal':item.find('.deal-cnt').text(),
            'title':item.find('.title').text(),
            'shop':item.find('.shop').text(),
            'location':item.find('.location').text()
        }
        print(product)
        save_products(product)

def save_products(result):
    try:
        if collection.insert(result):
            print("储存MongoDB成功")
    except Exception:
        print("储存失败")

if __name__ == '__main__':
    for i in range(1,5):
        index_page(i)
    browser.close()
