# 1. 爬虫简介
- 两大特征
    - 能按作者要求下载数据或者内容
    - 能自动在网上流窜
- 三大步骤:
    - 下载网页
    - 提取正确的信息
    - 根据一定的规则自动跳到另外的网页执行上两步内容
- 爬虫分类
    - 通用爬虫
    - 专用爬虫(聚焦爬虫)
- Python网络包简介
    - python2.x : urllib,urllib2,urllib3,httplib,httplib2,requests
    - python3.x : urllib,urllib3,httplib2,requests
    - python2 : urllib和urllib2配合使用,或者requests
    - python3 : urllib, requests
    
# 2. urllib
- 包含模块
    - urllib.request : 打开和读取urls
    - urllib.error : 包含urllib.request产生的常见的错误,使用try捕捉
    - urllib.parse : 包含解析url的方法
    - urllib.robotparse: 解析robots.txt文件
    - 案例v01
- 网页编码问题解决
    - chardet 可以自动检测页面的编码格式, 但是可能有误
    - 安装charde
    - 案例v02
- urlopen 的返回对象

    - 案例v03
    - geturl: 返回请求对象的url
    - info: 请求反馈对象的meta信息
    - getcode: 返回的http code
    
- request.date  的使用
    - 访问网络的两种方法
        - get:
            - 利用参数给服务器传递参数
            - 参数为dict, 然后用parse编码
            - 案例v04
        - post
            - 一般向服务器传递参数使用
            - post是把信息自动加密处理
            - 我们如果想使用post信息,需要用到data参数
            - 使用post,意味着http的请求头可能需要更改:
                - Content-Type : application/x-www.form-urlencode
                - Content-Length: 数据长度
                - 简而言之, 一旦更改请求方法,请注意其他请求头部信息相适应
            - urllib.parse.urlencode可以将字符串自动转换成上面的
            - 案例v05
            - 为了更多的设置请求信息,单纯的通过urlopen函数已经不太好用了
            - 需要利用request.Request 类
            - 案例v06
            
- urllib.error
    - URLError产生的原因:
        - 没网
        - 服务器连接失败
        - 知不道指定服务器
        - 是OSError的子类
        - 案例v07
    - HTTPError,是URLError的子类
        - 案例v08
        
    - 两者区别:
        - HTTPError是对应的HTTP请求的返回码错误,如果返回错误码是400以上的,则引发HTTPError
        - URLError对应的一般是网络出现问题,包括url问题
        - 关系区别: OSError--URLError--HTTPError
        
- UserAgent
    - UserAgent: 用户代理, 简称UA, 属于heads的一部分,服务器通过UA来判断访问者的身份
    - 常见的UA值, 使用的时候可以直接复制粘贴, 也可以用浏览器访问的时候抓包
             
             
        - 见课程笔记
                  
             
    - 设置UA可以通过两种方式:
        - heads
        - add_header
        - 案例v09
        
- ProxyHandler处理(代理服务器)
    - 使用代理IP, 是爬虫常用的手段
    - 获取代理服务器的地址:
        - www.xicidaili.com
        - www.goubanjia.com
    - 代理用来隐藏真实身份,代理也不允许频繁访问某一个固定网站,所以,代理一定要很多很多
    - 基本使用步骤:
        - 1.设置代理地址
        - 2.创建ProxyHandler
        - 3.创建Opener
        - 4.安装Opener
    - 案例v10
    