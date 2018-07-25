from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys


# 可能需要手动添加路径
driver = webdriver.Chrome()

url = "http://www.baidu.com"

driver.get(url)

text = driver.find_element_by_id('wrapper').text

print(text)
print(driver.title)
# 得到页面截图
driver.save_screenshot('index.png')

# id="kw" 的是百度的输入框,我们得到输入框的ui元素都直接输入"大熊猫"
driver.find_element_by_id('kw').send_keys(u"大熊猫")

# id="su"是百度的搜索按钮,click模拟点击
driver.find_element_by_id('su').click()

time.sleep(5)
driver.save_screenshot("daxiongmao.png")

# 获取当前页面的cookie
print(driver.get_cookies())

# 模拟输入两个按键  ctrl + a
driver.find_element_by_id('kw').send_keys(Keys.CONTROL, 'a')

# ctrl + x是剪切快捷键
driver.find_element_by_id('kw').send_keys(Keys.CONTROL, 'x')

driver.find_element_by_id('kw').send_keys(u'航空母舰')
driver.save_screenshot('hangmu.png')

driver.find_element_by_id('su').send_keys(Keys.RETURN)

time.sleep(5)
driver.save_screenshot('hangmu2.png')

# 清空输入框, clear
driver.find_element_by_id('kw').clear()
driver.save_screenshot('qingkong.png')

# 关闭浏览器
driver.quit()