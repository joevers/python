# Django
- 环境
    - python3.6
    - django1.8
- 参考资料
    - https://yiyibooks.cn
    - django架站的16堂课

# 环境搭建
- anaconda+pycharm
- anaconda使用
    - conda list:显示当前环境安装包
    - conda env list: 显示安装的虚拟环境列表
    - conda create -n env_name(虚拟环境的名称) python=3.6  安装虚拟环境
    - 激活conda的虚拟环境
        - (linux)source activate env_name
        - (win)activate env_name
    - pip install django==1.8
    
# 后台需要的流程

# 创建第一个django程序
- 命令行启动
    - 进入django所在文件夹打开命令终端
    - django-admin startproject tulingxueyuan
    - cd tulingxueyuan (进入新建的django项目文件夹)
    - python manage.py runserver   
- pycharm启动
    - 需要配置
    - 配置环境
    
# 路由系统-urls
- 创建APP
    - APP: 负责一个具体业务或者一类具体业务的模块
    - 创建: python manage.py startapp teacher

- 路由
    - 按照具体的请求url,导入到相应的业务处理模块的一个功能
    - django的信息控制中枢
    - 本质上是接受的URL和相应的处理模块的一个映射
    - 在接受url请求的匹配上使用了RE
    - URL的具体格式如urls.py中所示
- 需要关注的两点:
    - 接受的url是什么,即如何使用RE对传入的URL进行匹配
    - 已知URL匹配到哪个处理模块
    
- url匹配规则
    - 从上往下一个一个比对
    - url格式是分级格式,则按照级别一级一级往下比对,主要对应url包含子url的情况
    - 子url被调用,则不会返回到主url    
        - `/one/two/three/`
    - 正则以r开头,表示不需要转义,注意尖号(^)(从头开始匹配)和美元符号($)(以什么结尾)
        - `/one/two/three` 配对 r'^one/
        - `/oo/one/two/three` 不匹配 r'^one/"
        - `/one/two/three/` 匹配 r'^three/$'
        - `/oo/one/two/three/oo/` 不匹配 r'^three/$"
        - 开头不需要有反斜杠
    - 如果从上向下都没有找到合适的匹配内容,则报错
    
# 注意: URL后必须加逗号
    
# 2. 正常映射
- 把某一个符合RE的URL映射到失误处理函数中去
    - 举例    参看Django/tulingxueyuan/tulingxueyuan/urls.py与/teacher/views.py
    
# 3. url中带参数映射
- 在事件处理代码中需要由url传入参数,  例如 /myurl/param 中的param
- 参数都是字符串形式,需要整数等形式需要自行转换
- 举例    参看Django/tulingxueyuan/tulingxueyuan/urls.py与/teacher/views.dy

# 4. URL在app中处理
- 如果所有应用URL都集中tulingxueyuan/urls.py中,可能导致文件的臃肿
- 可以把urls的具体功能逐渐分散到每个app中
    - 从django.conf.urls 导入 include
    - 注意此时RE部分的写法
    - 添加include导入
- 使用方法
    - 确保include被导入
    - 写主路由的开头url
    - 写子路由
    - 编写views函数
- 同样可以使用参数
# 5. url中的嵌套参数
- 捕获某个参数的一部分
    - 例如 URL  /index/page-3 , 需要捕获数字3作为参数
        
        url(r'index_1/(page-(\d+)/)?$', sv.myindex_1),  # 不太好
        url(r'index_2/(?:page-(?P<page_number>\d+)/)?$', sv.myondex_2)  # 好
        
    - 上述例子会得到两个参数, 但  ?: 表明忽略此参数 
    
# 6. 传递额外参数
- 参数不仅仅来自URL,还可能是我们自定义的内容
    
    url(r'extrem/$', sv.extremParam, {'name':'liuying'}),
    
- 附加参数同样使用与include语句, 此时对include内所有都添加

# 7. URL的反向解析
- 防止硬编码
- 本质上是对每一个URL进行命名
- 以后再编码代码中使用URL的值,原则上都应该使用反向解析



# views 视图
- 内容在tulingxueyuan_views中
# 1. 视图概述
- 视图即视图函数,接受web请求并返回web响应的事物处理函数
- 响应指符合http协议要求的任何内容, 包括json,string,html等
- 本章忽略事务处理,重点在如何返回处理结果
# 2. 其他简单的视图
- django.http给我们提供类很多和HttpResponse类似的简单视图,
- 通过查看django.http代码我们知道
- 此类视图使用方法基本类似，可以通过return语句作为直接反馈返回给浏览器
- Http404为Exception子类，所以需要raise使用
# 3. HttpResponse详解
- 方法
    - init:使用页面内容实例化HttpResponse对象
    - write(content): 以文件的方式写
    - flush(): 以文件的方式输出缓存区
    - set_cookie(key, value="", max_age=None, expires=None): 设置cookie:
        - key,value都是字符串类型
        - max_age是一个整数,表示在指定秒数后过期
        - expires是一个datetime或timedelta对象,会话将在这个指定的日期/时间过期,
        - max_age与expires二选一
        - 如果不指定过期时间,则两个星期后过期
    - delete_cookie(key):删除指定的key和Cookie,如果key不存在则什么也不发生
    
# 4. HttpResponseRedirect
- 重定向,服务器端跳转
- 构造函数的第一个参数用来指定重定向的地址
- 案例  /tulingxueyuanviews/urls/url(r'^v10_1/', v.v10_1),url(r'^v10_2/', v.v10_2),url(r'^v11/', v.v11, name="v11"),    

# 5. Request
- Request介绍
    - 服务器接收到http协议的请求后,会根据报文创建HttpRequest对象
    - 视图函数的第一个参数是HttpRequest对象
    - 在django.http模块中定义了HttpRequest对象的API
- 属性
    - 下面除非特别说明,属性都是只读的
    - path: 一个字符串,表示请求的页面的完整路径,不包含域名
    - method: 一个字符串,表示请求使用的http方法,常用值包括: 'get'  'post'
    - encoding: 一个字符串,表示提交的数据的编码方式
        - 如果为None则表示使用浏览器的默认设置,一般为utf-8
        - 这个属性是可写的,可以通过修改它来修改访问表单数据使用的编码
    - GET: 一个类似与字典的对象,包含GET请求方式的所有参数
    - POST: 一个类似与字典的对象,包含post请求方式的所有参数
    - FILES: 一个类似于字典的对象,包含所有的上传文件
    - COOKIES: 一个标准的python字典,包含所有的cookie值, 键和值
    - session: 一个既可读又可写的类似于字典的对象,表示当前的会话
               - 只有当django启用会话的支持时才可用
               - 详细内容见"状态保持"
    - 方法
        - is_ajax():如果请求是通过XMLHttpRequest发起的,则返回True
        
    - QueryDict对象
        - 定义在django.http.QueryDict
        - request对象的属性GET  POST都是QueryDict类型的对象
        - 与python字典不同,QueryDict类型的对象用来处理同一个键带有多个值的情况
        - 方法get():根据键获取值
            - 只能获取键的一个值
            - 如果一个键同时拥有多个值,则获取最后一个值
        - 方法getlist():根据键获取值
            - 将键的值以列表返回,可以获取一个键的多个值
    - GET属性
        - QueryDict类型的对象
        - 包含get请求方式的所有参数
        - 与url请求地址中的参数对应,位于?后面
        - 参数的格式是键值对, 如 key1=value1
        - 多个参数之间,使用&链接, 如key1=value1&key=value2
        - 键是开发人员定下来的,值是可变的
    - POST属性
        - QueryDict类型的对象
        - 包含post请求方式的所有参数
        - 与form表单中的控件对应
        - 表单中控件必须有name属性, name为键,value为值
            - checkbox存在一键多值的问题
        - 键是开发人员定下来的,值是可变的
    
- 手动编写视图
    - 实验目的:
        - 利用django快捷函数手动编写视图处理函数
        - 编写过程中理解视图运行原理
    - 分析:
        - django把所有请求信息封装入request
        - django通过 urls模块把相应请求跟事件处理函数连接起来,并把request作为参数传入
        - 在相应的处理函数中,我们需要完成两部分
            - 处理业务
            - 把结果封装并返回,我们可以简单使用HttpResponse
        - 本案例不介绍业务处理,把目光集中在如何渲染结果并返回
    - render
        - 使用模板和一个给定的上下文环境,返回一个渲染过的HttpResponse
        - request: django的传入请求
        - template_name: 模板名称
        - content_instance: 上下文环境
        - 案例参看 teacher_views/teacher_app/views/render_test
    - render_to_response
        - 根据给定的上下文字典渲染给定模板,返回渲染后的HttpResponse
        
- 系统内建视图
    - 系统内建视图,可以直接使用
    - 404
        - default.page_not_found(request, template_name="404.html")
        - 系统引发Http404时发出
        - 默认传递request_path变量给模板,即导致错误的URL
        - DEBUG=True则不会调用404, 取而代之的是调试信息(DEBUG在settings中)
        - 404视图会被传递一个RequestContext对象并且可以访问模板上下文处理器提供的变量
- 基于类的视图
    - 参看教学笔记
    
# Models 模型
- ORM
    - ObjectRelationMap: 把面向对象思想转换成关系数据库思想
    - 类对应表格
    - 类中的属性对应表中的字段
    - 在应用中的models.py文件中定义class
    - 所有需要使用ORM的class都必须是models.Model的子类
    - class中的所有属性对应表格中的字段
    - 字段的类型都必须使用modles.xxx 不能使用python中的类型
    - 在django中,models负责跟数据库交互
- django链接数据库
    - 自带默认数据库Sqlite3
        - 关系型数据库
        - 轻量级
    - 建议开发用sqlite3,部署用Mysql之类数据库
    
        - 切换数据库在settings中进行设置
             
            # django链接mysql
            DATABASES = [
                'default' = {
                    'ENGINE' : 'django.db.backends.mysql',
                    'NAME' : '数据库名',
                    'PASSWORD' : '数据库密码',
                    'HOST' : '127.0.0.1',
                    'PORT' : '3306',
                }
            ] 
            
        - 需要在项目文件下的__init__文件中导入pymysql包
    
# models类的使用
- 定义和数据库表映射的类
    - 在应用中的models.py文件中定义class
    - 所有需要使用ORM的class都必须是models.Model的子类
    - class中的所有属性对应表格中的字段
    - 字段的类型都必须使用models.xxx不能使用python的类型
- 字段常用的参数
    - 1.max_length :规定数值的最大长度
    - 2.blank : 是否允许字段为空,默认不允许
    - 3.null : 在DB中控制是否保存为null,默认为false
    - 4.default :默认值
    - 5.unique : 唯一
    - 6.verbose_name : 假名
- 数据库的迁移
    - 1. 在命令行中,生成数据迁移的语句(生成sql的语句)
        - python3 manage.py makemigrations
        
    - 2. 在命令行中, 输入数据迁移指令
        - python3 manage.py migrate
        
        ps: 如果迁移中没有出现变化或者报错,可以尝试强制迁移
        强制迁移命令
            python3 manage.py makemigrations 应用名
            python3 manage.py migrate 应用名
    - 3.对于默认数据库,为了避免混乱,如果数据库中没有数据,删除自带的sqlite3数据库
    
    
# 1.查看数据库中的数据(详见课程笔记)
- 1.启动命令行: python3 manage.py shell
    ps:注意点: 对orm的操作分为静态函数和非静态函数两种,
- 2.在命令行中导入对应的映射类
    from 应用.models import 类名
- 3.使用objects属性操作数据库 .objects 是模型中实际和数据库进行交互的
- 4.查询命令
    - 类名.objects.all()查询数据库表中的所有内容,返回的结果是一个QuerySet类型
    - 类名.objects.filter(条件)
# 2. 添加数据
- 对象 = 类()  # 使用类实例化对象
- 对象.属性 = 值  # 给对应的对象的属性赋值
- 对象.save()  # 必须要执行保存操作,否则数据没有进入数据库
- python manage.py shell  命令行中添加数据

- 具体过程
    '''
    from  应用名.models  import 类名
    from myapp.models import Teacher
    
    
    - 实例化对象
    t = Teacher()
    
    - 给对象的属性赋值
    t.name = "张三"
    t.age = 18
    t.adress = "北京"
    
    - 保存数据
    t.save()
    
    '''
    
- 常见的查找方法
1.通用查找格式: 属性名 __(用下面的内容) = 值  
    - gt : 大于   例: t = Teacher.objects.filter(age__gt=18)
    - gte : 大于等于
    - lt : 小于
    - lte : 小于等于
    - range : 范围
    - year : 年份
    - isnull : 是否为空
2. 查找等于指定值的格式: 属性名 = 值
3. 模糊查找:  属性名__(使用下面的内容) = 值
    - exact : 精确等于
    - iexact : 不区分大小写
    - contains : 包含
    - startwith : 以...开头
    - endwith : 以...结尾