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