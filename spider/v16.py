from urllib import request,parse
from http import cookiejar

# 创建cookie的实例

cookie = cookiejar.MozillaCookieJar(filename)
cookie.load("cookie.txt", ignore_expires=True, ignore_discard=True)

# 生成 cookie的管理器
cookie_handler = request.HTTPCookieProcessor(cookie)
#创建http请求管理器
http_handler = request.HTTPHandler()

#生成https请求管理器
https_handler = request.HTTPSHandler()

# 创建请求管理器
opener = request.build_opener(http_handler, https_handler, cookie_handler)

def getHomePage():
    url = "http://www.renren.com/(隐私地址)"

    # 如果已经执行了login函数, 则opener自动已经包含了相应的cookie的值
    rsp = opener.open(url)

    html = rsp.read().decode()
    with open("rsp.html", "w") as f:
        f.write(html)

if __name__ == '__main__':
    getHomePage()