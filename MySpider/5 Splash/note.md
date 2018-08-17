# 安装Splash
- 首先安装Decoker
    - 安装网址:  https://docs.docker.com/install/linux/docker-ce/ubuntu/#set-up-the-repository
    - 较旧版本的Docker被称为docker或docker-engine。如果已安装，请卸载它们：
      $ sudo apt-get remove docker docker-engine docker.io
    - 更新apt包索引：
      $ sudo apt-get update
    - 安装包以允许apt通过HTTPS使用存储库：   
      $ sudo apt-get install \
        apt-transport-https \
        ca-certificates \
        curl \
        software-properties-common
    -  添加Docker的官方GPG密钥：    
      $ curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
    
       9DC8 5822 9FC7 DD38 854A E2D8 8D81 803C 0EBF CD88通过搜索指纹的最后8个字符，验证您现在拥有带指纹的密钥 。
    
       $ sudo apt-key fingerprint 0EBFCD88
        - 出现以下
        pub   4096R/0EBFCD88 2017-02-22
              Key fingerprint = 9DC8 5822 9FC7 DD38 854A  E2D8 8D81 803C 0EBF CD88
        uid                  Docker Release (CE deb) <docker@docker.com>
        sub   4096R/F273FCD8 2017-02-22
    - 使用以下命令设置稳定存储库。即使您还想从边缘或测试存储库安装构建，您始终需要稳定的存储库。
      要添加边缘或 测试存储库，请在下面的命令中的单词后添加单词或（或两者）。edgeteststable
      $ sudo add-apt-repository \
        "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
        $(lsb_release -cs) \
        stable"
        
    - 更新apt包索引。
        $ sudo apt-get update
    - 安装最新版本的Docker CE，或转到下一步安装特定版本：
        $ sudo apt-get install docker-ce
    - 要安装特定版本的Docker CE，请列出repo中的可用版本，然后选择并安装：一个。列出您的仓库中可用的版本：
        $ apt-cache madison docker-ce
          docker-ce | 18.03.0~ce-0~ubuntu | https://download.docker.com/linux/ubuntu xenial/stab
        - 安装指定的版本
            $ sudo apt-get install docker-ce=<VERSION>
    - 通过运行hello-world 映像验证是否正确安装了Docker CE 。
        $ sudo docker run hello-world
    - 配置Docker
        - https://docs.docker.com/install/linux/linux-postinstall/#manage-docker-as-a-non-root-user

- 安装Splash
    - 安装
        - sudo docker pull scrapinghub/splash
    - 启动
        - sudo docker run -p 8050:8050 -p 5023:5023 scrapinghub/splash
    - Splash现在在端口8050（http）和5023（telnet）上的0.0.0.0处可用。
    
    


# Splash Lua脚本
- 入口及返回值
- 异步处理
- Lua脚本语法  见 : http://www.runoob.com/lua/lua-basic-syntax.html
    
# Splash对象属性
- args    获取加载时配置的参数
- js_enabled    是否执行JavaScript代码   默认为true
- resource_tiomeout     设置加载的超时时间  如果设置为0或nil,代表不检测超时
- image_enabled     是否加载图片    默认为True
- plugins_enabled       是否开启浏览器插件   默认为false
- scroll_position       控制页面的上下左右滚动
    
# Splash对象的方法
- go 
  - ok, reason = splash:go{url, baseurl=nil, headers=nil, http_method="GET"
                         body=nil, formdata=nil}
    - url : 请求的url
    - baseurl: 可选参数,默认为空,表示资源加载相对路径
    - headers: 可选参数,默认为空,表示请求头
    - http_method: 可选参数,默认为GET,同时支持POST
    - body : 可选参数,默认为空,发POST请求时的表单数据
    - formdata: 可选参数,默认为空,发POST请求时的表单数据
- wait()
  - ok, reason = splash:wait{time, cancel_on_redirect=false, cancel_on_error=true}
    - time : 等待的秒数
    - cancel_on_redirect : 可选参数,默认为false,表示如果发生了重定向就停止等待,并返回重定向结果
    - cancel_on_error : 可选参数,默认为false, 表示如果发生了加载错误,就停止等待
- jsfunc()
    - 次方法可以直接调用JavaSprict定义的方法,但是所调用的方法需要用双中括号包围
    -   
        function main(splash, args)
            local get_div_count = splash:jsfunc([[
            function(){
                var body = document.body;
                var divs = body.getElementsByTagName('div');
                return divs.length;
            }
            ]])
            splash:go("https://www.baidu.com")
            return("There are %s DIVs"):format(
            get_div_count())
        end
- evaljs()
    - 此方法可以执行JavaScript代码,并返回最后一条JavaScript语句的返回结果
      - result = splash:evaljs(js)
      - 使用以下方法获取页面标题
        - local title = splash:evaljs("document.title")
- runjs()
    - 此方法可以执行JavaScript代码,偏向与执行某些动作或声明某些方法
    - P271
- autoload()
    - 此方法可以设置每个页面访问时自动加载的对象
        - reason = splash:autoload{source_or_url, source=nil, url=nil}
            - source_or_url : JavaScript代码或者JavaScript库链接
            - source: Javascript代码
            - url: JavaScript库链接
- call_later()
    - 此方法可以通过设置定时任务和延池时间来实现任务延迟执行,并且可以在执行前通过cancel()方法重新执行定时任务
    - 示例
         function main(splash, args)
            local snapshots = {}
            local timer = splash:call_later(function()
                snapshots["a"] = splash:png()
                splash:wait(1.0)
                snapshots["b"] = splash:png()
            end, 0.2)
            splash:go("https://www.taobao.com")
            splash:wait(3.0)
            return snapshots
        end
- http_get()        
    - 此方法可以模拟发送HTTP的GET请求
    - response = splash:http_get{url, headers=nil, follow_redirects=true}
        - url: 请求URL
        - follow_redirects: 表示是否启动自动重定向,默认为true
- http_post()
    - 模拟发送POST请求
    - response = splash:http_post{url, headers=nil, follow_redirects=true, body=nil}
        - body: 可选参数,即表单数据,默认为空
- set_content()
    - 使用此方法来设置页面的内容
    -  
        function main(splash)
            assert(splash:set_content("<html><body><h1>hello</h1></body></html>"))
            return splash:png()
        end
- html()        
    - 使用此方法获取网页源代码
        -  
            function main(splash)
                splash:go("http://www.baidu.com")
                return splash:html()
            end
- png()
    - 获取png格式的网页截图
- jepg()
    - 获取jepg格式的网页截图
- har()
    - 获取网页加载过程描述
    - 
            function main(splash, args)
                splash:go("http://www.baidu.com")
                return splash:har()
            end
- url()
    - 获取当前正在访问的url
- get_cookies()
    - 获取当前页面的cookies
- add_cookie()
    - 为当前页面添加cookie
- clear_cookies()
    - 清除所有的cookies
- get_viewport_size()
    - 获取当前浏览器页面的大小,即宽高
- set_viewport_size()
    - 设置当前浏览器页面的大小,即宽高
- set_viewport_full()
    - 设置浏览器全屏显示
    -
            function main(splash)
                splash:set_viewport_full()
                assert(splash:go("http://www.baidu.com"))
                return splash:png()
            end
- set_user_agent()
    - 设置浏览器的User-Agnet
- set_custom_headers()
    - 设置请求头
- select()
    - 选中符合条件的地一个节点,参数是CSS选择器
- select_all()
    - 选中所有符合条件的节点,参数是CSS选择器
- mouse_click()
    - 模拟鼠标点击操作
    
        function main(splash)
            splash:go("http://www.baidu.com")
            input = splash:select("#kw")
            input:send_text('Splash')
            submit = splash:select('#su')
            submit:mouse_click()
            splash:wait(3)
            return splash:png()
        end
    
    
# Splash API调用
- 与python程序结合使用并抓取JavaScript渲染的页面
- render.html
    - 案例v1
    - 此接口用于获取HTML代码, 接口地址就是Splash的运行地址加此接口名称
        - http://localhost:8050/render.html?url=https://www.baidu.com
    - 此接口还可以指定其他参数, 例如通过wait指定等待秒数
        - http://localhost:8050/render.html?url=https://www.baidu.com&wait=5
    - 此接口还支持代理设置,图片加载设置,Headers设置,请求方法设置,具体用法参考官方文档
        - 官方文档:https://splash.readthedocs.io/en/stable/api.html#render-html
- render.png
    - 案例v1
    - 此接口可以获取网页截图
    - 此接口可以通过width和height来控制宽高
        - http://localhost:8050/render.png?url=https://www.taobao.com&wait=5&width=1000&height=700
- render.jpeg
    - 与render.png类似, 多了参数quality,用来设置图片质量
- render.har
    - 获取页面加载的HAR数据
- render.json 
    - 此接口包含了前面接口的所有功能,返回的是json格式
        - http://localhost:8050/render.json?url=https://www.baidu.com
    - 可以传入不同参数控制其返回结果
        - http://localhost:8050/render.json?url=https://www.baidu.com&html=1&har=1
- execute   
    - 案例v2
    - 此接口为最强大的接口,使用此接口可以实现与Lua脚本的对接
        - 使用quote()方法将脚本进行URL转码
  
  
  
        
# Splash负载均衡配置
- 详见P286
