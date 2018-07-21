# 格式化文件储存
- xml, json
- 为了解决不同设备之间的信息交换
- xml
- json

#xml文件
- xml,  可扩展标记语言
    - 标记语言: 语言中使用尖括号括起来的文本字符串标记
    - 可标记: 用户可以自己定义需要的标记
    - 例如:
            
            <Teacher>
            自定义标记Teacher
            在两个标记之间任何内容都应该跟Teacher相关
            </Teacher>
    - 是w3c组织制定的一个标准
    - xml描述的是数据的本身,即数据的结构和语义
    - HTML侧重于如何显示web页面中的数据
- XML文档的构成
    - 处理指令(可以认为一个文件内只有一个处理指令)
        - 最多只有一行
        - 必须出现在第一行
        - 内容是与xml本身处理相关的一些声明或者指令
        - 以xml关键字开头
        - 一般用于声明XML的版本和采用的编码
            - version属性是必须的
            - encoding属性用来支出xml解释器使用的编码
    - 根元素(一个文件内只有一个根元素)
        - 在整个xml文件中, 可以把它看做一个树型结构
        - 根元素有且只能有一个
    - 子元素
    - 属性
    - 内容
        - 表明标签所储存的信息
    - 注释
        - 起到说明作用的信息
        - 注释不能嵌套在标签里
        - 只有在注释的开始和结尾使用双短横线
        - 三短横线只能出现在注释的开头而不能用在结尾
                
                <name> <!--wang--> </name> 可以
                <name <!--wabg-->> </name> 不可以, 注释在标签内
                
                <!--my-name-wang--> 可以, 注释内容可以有一个短横线
                <!--my--name--wang-->  不可以, 双短横线只能出现在开头或者结尾
                
                <!---my-name-->  可以,三短横线只能出现在开头
                <!---my-name--->   不可以,三短横线只能出现在开头

- 保留字符的处理                
    - xml中使用的符号可能跟实际符号相冲突,典型就是左右尖括号
    - 使用实体引用(EntityReference)来表示保留字符
            
            <score> score>80 </score>  有错误, xml中不能出现 >
            <scroe> score&gt;80 </score>  使用实体引用
    - 把含有保留字符的部分放在CDATA块内部, CDTAT块把内部信息视为不需要转义
            
            <![CDATA[
               select name,age
               from Student
               where score>88
               ]]> 
               
    - 常用的需要转义的保留字符和对应实体应用
         
        - &: &amp;
        - <: &lt;
        - >: &gt;
        - ': &apos;
        - ": &quot;
        - 一共有五个, 每个实体引用都以 & 开头并且以 ; 结尾 
        
- xml标签的命名规则
    - Pascal命名法
    - 用单词表示, 第一个字母大写
    - 大小写严格区分
    - 配对的标签必须一致
    
- 命名空间
    - 为了防止命名冲突
        
        <Student>
            <name>qiao</name>
            <age>18 </age>
        </Student>
        <Room> 
            <name>dong</name>
            <location>1-23-1</location>
        </Room>
        
    - 如果归并上述两个内容信息, 会产生冲突
          
         <School>
                <name>qiao</name>
                <age>18</age>
            <naem>dong</name>
            <location>1-23-1</location>
         </School>
    - 为了避免冲突,需要给可能冲突的元素添加命名空间
    -xmlns: xml name space 的缩写
    
         <School xmlns:student="http://my_student" xmlns="http://my_room">
                <student:name>qiao</student:name>
                <age>18</age>
            <room:naem>dong</room:name>
            <location>1-23-1</location>
         </School>
         
# xml访问

##读取
- XML读取分为两个主要技术, SAX     DOM
- SAX(Simple API for XML):
    - 基于事件驱动的API
    - 利用SAX解析文档设计到解析器和事件处理两部分
    - 特点:
        - 快
        - 流式读取
- DOM
    - 是w3c规定的XML的编程接口
    - 一个xml文件再缓存中以树形结构保存, 读取
    - 用途
        - 定位浏览xml任何一个节点信息
        - 添加删除相应内容
    - minidom
    
    - etree
    
- xml文件写入
    - 更改
        - ele.set : 修改属性
        - ele.append : 添加子元素
        - ele.remove : 删除元素
    - 生成创建
        - SubElement
        - minidom
        - etree
        
        
        
        
### JSON
- 轻量级的数据交换格式
- json格式是一个键值对形式的数据集
    - key: 字符串
    - value: 字符串, 数字, 列表, json
    - json使用大括号包裹
    - 键值对直接用逗号隔开
    
    
- json和python格式的对应
    - 字符串:字符串
    - 数字:数字
    - 队列:list
    - 对象:dict
    - 布尔值:布尔值
- python for json
    - json包
    - json和python对象的转换
        - json.dumps():对数据编码,把python格式表示成json格式
        - json.loads():对数据编码,把json格式转换成python格式
    - python读取json文件
        - json.dump():把内容写入文件
        - json.load():把json文件内容读入python   