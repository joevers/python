# XPath
- 在XML文件中查找信息的一套规则/语言,根据XML的元素或者属性进行遍历
- http://www.w3school.com.cn

# XPath 开发工具
- 开源的XPath表达式编辑工具: XMLQuire
- Chrmoe插件: XPath Helper
- firefox插件: XPath Checker

# 选取节点
- nodename: 选取此节点的所有子节点
- /:  从根节点开始选取
- // :  选取节点,不考虑位置
- . :  选取当前的节点
- .. :  选取当前节点的父亲节点
- @ :  选取属性
- xpath中查找一般按照路径方法查找

        School/Teacher: 返回Teacher节点
        School/Student:  返回两个Student节点
        //Student: 选取所有的Student节点,不考虑位置
        School/Age: 选取School后代中所有的age节点
        //@Other : 选取Other属性
        //Age[@Detail]: 选取带有属性Detail的Age元素
        
# 谓语 - Predicates
- /School/Student[1]: 选取School下面的第一个Student节点
- /School/Student[last()] : 选取School下面的最后一个Student节点
- /School/Student[last()-1] : 选取School下面的倒数第二个Student节点
- /School/Student[position()<3] : 选取School下面的前两个Student节点
- //Student[@score]: 选取带有属性score的Student节点
- //Student[@score="99"]: 选取带有属性score并且属性值是99的Student节点
- //Student[@score]/age: 选取带有属性score的Student节点的子节点age

# XPath的一些操作
- | : 或者
        
        //Student[@score] | //Teacher : 选取带有属性score的Student节点和Teacher节点
- 其余不常见的XPath运算符号+,-,*,div,>,< 等等   