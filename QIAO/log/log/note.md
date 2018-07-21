# LOG
- logging
- logging 模块提供模块级别的函数记录日志
- 包括四大组件

## 1. 日志相关概念
- 日志
- 日志的级别(level)
    - 不同的用户关注不同的程序信息
    - DEBUG
    - INFO
    - NOTICE
    - WARNING
    - ERROR
    - CRITICAL
    - ALERT
    - EMERGENCY
- IO 操作=>不要频繁操作
- LOG的作用
    - 调试
    - 了解软件的运行状况
    - 分析定位问题
- 日志信息
    - time
    - 地点
    - level
    - 内容
- 成熟的第三方日志
    - log4j
    - log4php
    - logging
# logging模块
- 日志级别
    - 级别可自定义
    - DEBUG
    - INFO
    - WARNING
    - ERROR
    - CRITICAL
- 初始化/写日志实例需要指定级别, 只有级别等于或者高于指定级别才被记录
- 使用方式
    - 直接使用logging(封装了其他组件) 
    - logging四大组件直接定制
    
# 2.1 logging模块级别的日志
- 使用以下几个函数      (注:kwargs 是指键对值)
    - logging.debug(msg, *args, **kwargs)  创建一条级别为DEBUG的日志记录
    - logging.info(msg, *args, **kwargs)   创建一条级别为INFO的日志记录
    - logging.warning(msg, *args, **kwargs)  创建一条级别为WARNING的日志记录
    - logging.error(msg, *args, **kwargs)  创建一条级别为ERROR的日志记录
    - logging.critical(msg, *args, **kwargs)  创建一条级别为CRITICAL的日志记录
    - logging.log(level, *args, **kwargs)  创建一条级别为level的日志记录
    - logging.basicConfig(**kwargs)    对 root logger 进行一次性配置
    
- logging.basicConfig(**kwargs)    对 root logger 进行一次性配置
    - 只在第一次调用的时候起作用
    - 若果不配置logger, 则使用默认值
        - 输出: sys.stderr
        - 级别: WARNING
        - 格式: level:log_name:content
- 案例 01
- format参数


# 2.2 logging模块的处理流程
- 四大组件
    - 日志器(Logger): 产生日志的一个接口
    - 处理器(Handler): 把产生的日志发送到相应的目的地
    - 过滤器(Filter): 更精细的控制那些日志输出
    - 格式器(Formatter): 对输出信息进行格式化
- Logger
    - 产生一个日志
    - 操作
    
                 见课程笔记
   
    - 如何得到一个logger对象
        - 实例化
        - logging.getLogger()
        
- Handler
    - 把log发送到指定位置
    - 方法
        - setLevel
        - setFormat
        - addFilter, removeFilter
    - 不需要直接使用, Handler是基类
    
            具体见课程笔记
    
- Format类
    - 可以直接实例化
    - 可以继承Format添加特殊类型
    - 三个参数
        - fmt
        - datefmt
        - style
- Filter类
    - 可以被Handler和Logger使用
    - 控制传递过来的信息的具体内容                                