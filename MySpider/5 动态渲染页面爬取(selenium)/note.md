# selenium
- 基本使用
    - 案例v1
- 声明浏览器对象
    - 1  
        from selenium import webdriver
        
        browser = webdriver.Chrome()   谷歌浏览器
        browser = webdriver.Firefox()   火狐浏览器
        browser = webdriver.Edge()      Edge浏览器
        browser = webdriver.PhantomJS()     无界面浏览器
        
- 访问页面
    - 1 
        from selenium import webdriver
        
        browser = webdriver.Chrome() 
        browser.get('https://www.baidu.com')  打开百度页面
        print(browser.page_source)   获取页面源代码
        browser.close()   关闭浏览器
        
- 查找节点
    - 单个节点
        - find_element_by_xxx("")
        - find_element(By.xxx, "")
    - 多个节点
        - find_elements_by_xxx("")
        - find_elements(By.xxx, "")   
        
- 节点交互
    - 输入文字  使用  send_keys()
    - 清空文字  使用  clear()
    - 点击按钮  使用  click()
    
- 动作链
    - 鼠标拖拽
        -   browser = webdriver.Chrome()
            url=""
            browser.get(url)
            browser.switch_to.frame('iframeResult')  打开一个拖拽实例
            source = browser.find_element_by_css_selector('#draggable')  选中拖拽的节点
            target = browser.find_element_by_css_selector('#droppable')  选中拖拽的目标点
            actions = ActionChains(browser)   声明ActionChains对象并赋值为actions
            actions.drag_and_drop(source, target)   调用drag_an_drop方法
            actions.perform()   执行

- 执行JavsScript
    - 下拉进度条   使用execute_script()方法即可实现
        - 案例v3
    - 使用execute_script()方法来实现JavaScript
    
- 获取节点信息
    - 案例v4
    - 获取属性
        - 使用get_attribute()方法来获取节点属性,前提是先选取节点
    - 获取文本值
        - 每个WebElement节点都有text属性,直接调用即可
    - 获取 id  位置  标签名   大小
        - 获取节点id  使用id属性
        - 获取节点在页面中的相对位置  使用location属性
        - 获取标签名称   使用tag_name属性
        - 获取节点大小   使用size属性
        
        
- 切换Frame
    - 案例v5
    - 网页中有一种节点叫做iframe,也就是Frame,相当与页面的子页面,他的结构和外部网页结构完全一致
      selenium打开页面后,它默认是在父级Frame中操作,
      而此时页面中存在子Frame,则不能获取到子Frame中的节点
      这时候就需要使用switch_to.frame()方法来切换Frame
        
        
- 延时等待
    - 隐式等待
        - 案例v6
    - 显示等待
        - 案例v7
        - 等待条件及含义    参看P259
        
- 前进和后退
    - 前进   使用forward()方法
    - 后退   使用back()方法
    - 案例v8
    
- cookies
    - 案例v9 
    - 获取   添加   删除
    - 使用 get_cookies()  add_cookies()  delete_all_cookies()
    
    
- 选项卡管理
    - 案例v10
    
            import time
            from selenium import webdriver
            
            browser = webdriver.Chrome()
            browser.get('https://www.baidu.com')            
            browser.execute_script('window.open()')
                - 调用execute_script()方法,传入window.open()这个JavaScript语句打开新的选项卡
            print(browser.window_handles)
                - 调用window_handles属性获取当前开启的所有选项卡
            browser.switch_to_window(browser.window_handles[1])
                - 调用switch_to_window方法切换选项卡,  window_handles[]索引选项卡
            browser.get('https://www.taobao.com')
            time.sleep(1)
            browser.switch_to_window(browser.window_handles[0])
            browser.get('https://python.org')
            
            
- 异常处理
    - 使用try  except来捕获异常