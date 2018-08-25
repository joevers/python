# urllib下的使用
- 案例v1
- 代理需要认证的时候
    - 在代理前面加入代理认证的用户名和密码
        - proxy = 'uesrname:password@111.155.116.245:8123'
        - username 是用户名   password 是密码
        
- 如果代理类型是SOCKS5类型
    - 案例v2
    
    

# requests 下的使用
- 案例v3
- 代理需要认证的时候
    - 在代理前面加入代理认证的用户名和密码
        - proxy = 'uesrname:password@111.155.116.245:8123'
        - username 是用户名   password 是密码
- 如果代理类型是SOCKS5类型
    - 案例v4
    - 也可以使用和urllib相同的方法
    
    
    
    
# selenium
- Chrome
    - 案例v5
    - 如果代理需要认证,设置比较麻烦
        - 参看P331
    
- PhantomJS
    - 案例v6
    - 代理需要认证的时候
        - 只需要加入--proxy-auth 选项即可
        - 案例v6