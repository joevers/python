from selenium import webdriver

browser = webdriver.Chrome()
url = "https://www.zhihu.com/explore"
browser.get(url)

logo = browser.find_element_by_id("zh-top-link-logo")
print(logo)
print(logo.get_attribute('class'))
print("=="*20)
t = browser.find_element_by_id('zu-top-add-question')
print(t.text)
print(t.id)
print(t.location)
print(t.tag_name)
print(t.size)