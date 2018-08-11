# 选取节点
- nodename: 选取此节点的所有子节点
- /:  从根节点开始选取     从当前节点选取直接子节点
- // :  选取节点,不考虑位置    从当前节点选取所有子孙节点
- . :  选取当前的节点
- .. :  选取当前节点的父亲节点
- @ :  选取属性



- 安装lxml库
- from lxml import etree  
    - etree模块可以自动修正HTML文本
        - 调用tostring()方法即可输出修正后的HTML文本,但结果是bytes类型
        - 使用decode()方法转换为str类型
        - 修正html文件
            - html = etree.parse('./lujing', etree.HTMLParser())
        - 输出修正后的html文件
            - result = etree.tostring(html)
        - 使用XPath进行筛选
            - result = html.xpath('XPath语句')
    - 属性多值匹配使用contains
        - text = '''
             <li class="li li_fist"><a href="link.html>first</a></li>
            '
          html = etree.HTML(text)
          result = html.xpath('//li[contains(@class, li)]/a/text()')
        - 只有使用contains才能将所有包含li属性的class类找全
    - 多属性匹配(根据多个属性确定一个节点)使用运算符and链接即可
        - 运算符详细见p165
    - 按顺序选择 在中括号中传入索引的方法
        - html.xpath('//li[1]/a/text()')   地一个li节点
        - html.xpath('//li[last()]/a/text()')   最后一个li节点
        - html.xpath('//li[position()<3]/a/text()')   位置1  2 的节点
        - html.xpath('//li[last()-2]/a/text()')    倒数第三个节点
        - 索引的序号是从1开始的
    - 节点轴选择
        - 详见  http://www.w3school.com.cn/xpath/xpath_axes.asp
        - 
            轴名称	                   结果
            ancestor	            选取当前节点的所有先辈（父、祖父等）。
            ancestor-or-self	    选取当前节点的所有先辈（父、祖父等）以及当前节点本身。
            attribute	            选取当前节点的所有属性。
            child	                选取当前节点的所有子元素。
            descendant	            选取当前节点的所有后代元素（子、孙等）。
            descendant-or-self	    选取当前节点的所有后代元素（子、孙等）以及当前节点本身。
            following	            选取文档中当前节点的结束标签之后的所有节点。
            namespace	            选取当前节点的所有命名空间节点。
            parent	                选取当前节点的父节点。
            preceding	            选取文档中当前节点的开始标签之前的所有节点。
            preceding-sibling	    选取当前节点之前的所有同级节点。
            self	                选取当前节点。
        - 
             例子                 	     结果
            child::book	            选取所有属于当前节点的子元素的 book 节点。
            attribute::lang	        选取当前节点的 lang 属性。
            child::*	            选取当前节点的所有子元素。
            attribute::*	        选取当前节点的所有属性。
            child::text()	        选取当前节点的所有文本子节点。
            child::node()	        选取当前节点的所有子节点。
            descendant::book	    选取当前节点的所有 book 后代。
            ancestor::book	        选择当前节点的所有 book 先辈。
            ancestor-or-self::book	选取当前节点的所有 book 先辈以及当前节点（如果此节点是 book 节点）
            child::*/child::price	选取当前节点的所有 price 孙节点。
            