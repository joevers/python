# 概述
- Robots协议
    - 也称作爬虫协议, 机器人协议
    - 用来告诉爬虫和搜索引擎那些页面可以抓取 哪些不可以抓取
    - 通常是一个叫 robots.txt的文件
    - 一般放在网站的根目录下
    - 当搜索爬虫访问一个站点时,他会检查这个站点是否存在robots.txt文件
        如果存在,搜索爬虫会根据其中定义的范围来爬取
        如果没有这个文件,搜索爬虫便会访问所有可以直接访问的页面
- robots样例
        
        User-Agent:*
        Disallow:/
        Allow:/public/
        
        - User-Agent 描述了搜索爬虫的名称  设为*则表示所有爬虫都可以  只少指定一条
        - Disallow 指定不允许抓取的目录 设置为 / 表示所有页面都不可以抓取
        - Allow  一般和Disallow一起使用不会单独使用  设为/public/表示所有页面不允许抓取,但可以抓取public页面
    
    - 禁止所有爬虫访问任何目录
        User-Agent:*
        Disallow:/
    - 允许所有爬虫访问任何目录
        User-Agent:*
        Disallow:
    - 禁止所有爬虫访问网站某些目录
        User-Agent:*
        Disallow:/private/
        Disallow:/tmp/
    - 只允许某一个爬虫访问
        User-Agent:WebCrawler
        Disallow:
        User-Agent:*
        Disallow:/
- 爬虫名称
    - 见书本p120
- robotparser
    - 常用方法:
    - set_url() 用来设置robots.txt的链接
    - read() 这个方法执行一个读取和分析的操作,一定要执行此操作
    - parse() 解析robots.txt文件
    - can_fetch()  判断是否可以抓取这个URL
    - mtime()  返回的是上次抓取的分析robots.txt的时间
    - modified()  将当前时间设置为上次抓取和分析的时间