from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time

browser = webdriver.Chrome()
url = 'http://www.geetest.com/exp.html'
browser.get(url)
wait = WebDriverWait(browser,10)
submit = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#captcha div.geetest_btn')))
time.sleep(2)
submit.click()
time.sleep(3)
browser.close()
