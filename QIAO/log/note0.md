# 导入模块
- 导入以数字命名的模块的时候,需要借助importlib导入
    - 例如 A = importlib.import_module("01")

- 语法
    import module_name
    module_name.function_name
    module_name.class_name
    
- 用法
    - import 模块  as 别名   (给模块起一个方便简单的别名)
    - from module_name import func_name, class_name (从固定的模块导入特定的类, 函数,使用的时候直接使用,不用加前缀)
    - from module_name import * (导入模块的所有内容) 
      
- if __name__ == "__main__" 的使用
    - 可以有效避免模块代码被导入的时候被动执行的问题
    - 建议所有程序的入口都以此代码为入口

# 模块的搜索路径和储存
- 什么是模块的搜索路径:
    - 加载模块的时候,系统会在哪些地方搜索此模块
- 系统默认的模块的搜索路径
        import sys 
        sys.path 属性可以获取路径列表
        # 案例p03.py
- 添加搜索路径
        sys.path.append(dir)
- 模块的加载顺序
    1. 上搜索内存中已加载好的模块
    2. 搜搜Python的内置模块
    3. 搜索sys.path路径
    
# 包
- 包是一种组织管理代码的方式,包里面存放的是模块
- 用于讲模块包含在一起的文件夹就是包
- 自定义包的结构
        |---包
        |---|--- __init__.py  包的标志文件
        |---|--- 模块1
        |---|--- 模块2 
        |---|--- 子包(子文件夹)
        |---|---|--- __init__.py   包的标志文件
        |---|---|--- 模块1
        |---|---|--- 模块2 
        
- 包的导入操作
    - import package_name 
        - 直接导入一个包, 可以使用__init__.py中的内容
        - 使用方式是:
                package_name.func_name
                package_name.class_name.func.name()
        - 此种方式的访问内容
    - import package_name as x (取一个简单方便的别名)
        - 注意此方法是默认对__init__.py内容的导入
        
    - import package.module
        - 导入包中某一个具体的模块
        - 使用方法
                package.module.func_name
                package.module.class.fun()
                package.module.class.var
                
- from... import 导入
    - from package import module1, module2, module3...
    - 此种方法不执行'__init__'的内容
            from pkg01 import p01
            p01.sayhello()
    - from package import *
        - 导入当前包'__init__.py'文件中所有的函数和类
        - 使用方法
                function_name()
                class_name.func_name()      
                class_name.var
                
- from package.module import *
    - 导入包中指定的模块的所有内容
    - 使用方法
            func_name()                
            class_name.func_name()
            
- 在开发环境中经常会用到所有其他模块,可以再当前包中直接导入其他模块的内容
    - import 完整的包或者模块的路径
   
- '__all__' 的用法
    - 在使用from package import * 的时候, * 可以导入所有内容
    - '__init__.py'中如果文件为空, 或者没有'__all__', 那么只可以把'__init__'中的内容导入
    - '__init__' 如果设置了'__all__'的值, 那么则按照'__all__'指定的子包或者模块进行加载,如
    此则不会载入'__init__'中的内容
    - '__all__'=['module1', 'module2', 'package1'......] 
    
# 命名空间
- 用于区分不同位置不同功能但相同名称的函数或者变量的一个特定的前缀
- 作用是防止命名冲突              