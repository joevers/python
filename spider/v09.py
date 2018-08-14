'''
访问一个网址
更改自己的UserAgent进行伪装

'''


from urllib import request, error

if __name__ == '__main__':
    url = "http://www.baidu.com"

    try:

        
        # 使用head方法伪装UA
        #headers = {}
        #headers['User-Agent'] = "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 UBrowser/5.6.12150.8 Safari/537.36"
        #req = 1 request.Request(url, headers=headers)
        

        # 使用add_header方法
        req = request.Request(url)
        req.add_header("User-Agent", "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36 Core/1.47.277.400 QQBrowser/9.4.7658.400")

        # 正常访问
        rsp = request.urlopen(req)
        html = rsp.read().decode()
        print(html)

    except error.URLError as e:
        print(e)

    except error.HTTPError as e:
        print(e)

    except Exception as e:
        print(e)

    print("Done......")