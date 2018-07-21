 #  包含一个学生类
 #  一个sayhello函数
 #  一个打印语句

class Student():
    def __init__(self, name="NoName", age = 18 ):
         self.name = name
         self.age = age
    def say(self):
         print("My name is {0}.".format(self.name))


def sayhello():
    print("欢迎来到图灵学院")

# 此语句是指只有在执行此模块时才执行下述语句, 被导入调用的时候不执行此语句
# 建议 此判断语句一直作为程序的入口
if __name__ == "__main__":
    print("我是模块P01呀,叫我干毛")

