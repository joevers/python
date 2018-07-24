'''
处理js加密代码

'''
'''
通过查找,找到了js代码中的操作代码

1. 这个是计算salt的代码  r = "" + ((new Date).getTime() + parseInt(10 * Math.random(), 10))
2.  sign  :           i = n.md5("fanyideskweb" + t + r + "ebSeFb%=XZ%T[KZ)c(sy!")
md5一共需要四个参数, 第一个和第四个是固定的字符串, 第三个是salt, 第二个是.... 
经过查找, 第二个参数就是 输入的单词
'''



def getSalt():
    '''
    salt的公式是:  "" + ((new Date).getTime() + parseInt(10 * Math.random(), 10))
    把他翻译成python代码

    在浏览器中按F12,在console中运行 (new Data).getTime 与 parseInt(10 * Math.random(), 10)
    :return:
    '''

    import time, random

    salt = int(time.time()*1000) + random.randint(0,10)

    return salt

def getMd5(v):
    import hashlib

    md5 = hashlib.md5()

    # update需要一个bytes格式参数
    md5.update(v.encode("utf-8"))
    sign = md5.hexdigest()

    return  sign

def getSign(key, salt):

    sign = "fanyideskweb" + key + str(salt) + "ebSeFb%=XZ%T[KZ)c(sy!"
    sign = getMd5(sign)

    return sign

from urllib import  request, parse

def youdao(key):

    url = "http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"
    salt = getSalt()

    data = {

        "i": key,
        "from": "AUTO",
        "to": "AUTO",
        "smartresult": "dict",
        "client": "fanyideskweb",
        "salt": str(salt),
        "sign": getSign(key, salt),
        "doctype": "json",
        "version": "2.1",
        "keyfrom": "fanyi.web",
        "action": "FY_BY_REALTIME",
        "typoResult": "false"
    }

    # print(data)
    # 参数data需要bytes格式
    data = parse.urlencode(data).encode()
    headers = {
        "Accept": "application/json, text/javascript, */*; q=0.01",
        #"Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Connection": "keep-alive",
        "Content-Length": len(data),
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        # cookie 可以没有
        "Cookie": "OUTFOX_SEARCH_USER_ID=-673535459@10.169.0.83; OUTFOX_SEARCH_USER_ID_NCOO=158631331.28507355; fanyi-ad-id=47865; fanyi-ad-closed=1; _ntes_nnid=24d1323425b5ad693aba9e9859bb503c,1532249235767; JSESSIONID=aaac3Ck9Ewkid9BRTNetw; ___rl__test__cookies=1532307123094",
        "Host": "fanyi.youdao.com",
        "Origin": "http://fanyi.youdao.com",
        "Referer": "http://fanyi.youdao.com/",
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",
        "X-Requested-With": "XMLHttpRequest",
    }

    req = request.Request(url, data=data, headers=headers)

    rsp = request.urlopen(req)

    html = rsp.read().decode()
    print(html)

if __name__ == '__main__':
    youdao("girl")