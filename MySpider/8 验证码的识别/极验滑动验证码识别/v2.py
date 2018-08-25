from selenium import  webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from PIL import Image
from io import BytesIO
import time



EMAIL = '15632681735@163.com'
PASSWORD = 'ye4wolf'

class CrackGeetest():
    # 初始化对象
    def __init__(self):
        self.url = 'https://account.geetest.com/login'
        self.browser = webdriver.Chrome()
        self.wait = WebDriverWait(self.browser, 20)
        self.email = EMAIL
        self.password = PASSWORD

    def __del__(self):
        self.browser.close()


    def get_geetest_button(self):
        '''
        获取初始验证按钮

        :return: 按钮对象
        '''
        button = self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'geetest_radar_tip')))
        return button

    # 获取验证码位置
    def get_position(self):
        '''
        获取验证码位置
        :return: 验证码位置元纽
        '''
        img = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'geetest_canvas_img')))
        time.sleep(2)
        location = img.location
        size = img.size
        top, bottom, left, right = location['y'], location['y']+size['height'], \
                                   location['x'], location['x']+size['width']
        return (top, button, left, right)



    def get_screenshot(self):
        '''
        获取网页截图
        :return: 截图对象
        '''
        screenshot = self.browser.get_screenshot_as_png()
        screenshot = Image.open(BytesIO(screenshot))
        return screenshot


    def get_slider(self):
        '''
        获取滑块
        :return:滑块对象
        '''
        slider = self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'geetest_slider_button')))
        return slider

    #
    def get_geetest_image(self,name='captcha.png'):
        '''
        获取验证码图片
        :param name:
        :return: 图片对象
        '''
        top, bottom, left, right = self.get_position()
        print('验证码位置:',top,bottom,left,right)
        screenshot = self.get_screenshot()
        captcha = screenshot.crop((left,top,right,bottom))
        captcha.save(name)
        return captcha

    def open(self):
        self.browser.get(self.url)
        email = self.wait.until(EC.presence_of_element_located((By.ID,'email')))
        password = self.wait.until(EC.presence_of_element_located((By.ID, 'password')))
        email.send_keys(self.email)
        password.send_keys(self.password)







button = self.get_geetest_button()
button.click()
