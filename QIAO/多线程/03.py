# 使用多线程
import time
import _thread as thread



def loop1(in1):
    # ctime 得到当前时间
    print("Start loop 1 at: ", time.ctime())
    # 把参数打印出来
    print("我是参数" , in1)
    # 睡眠多长时间  单位是秒
    time.sleep(6)
    print("End loop 1 at: ", time.ctime())


def loop2(in1, in2):
    # ctime 得到当前时间
    print("Start loop 2 at: ", time.ctime())
    # 吧参数in1, in2 打印出来,代表使用
    print("我是参数" , in1, in2)
    # 睡眠多长时间  单位是秒
    time.sleep(4)
    print("End loop 2 at: ", time.ctime())


def main():
    print("Starting at: ", time.ctime())
    # 启动多线程的意思是用多线程去执行某个函数
    # 启动多线程函数为 start_new_thead
    # 参数两个, 一个是需要运行的函数名, 第二是函数的参数作为元祖使用, 为空则使用空元祖
    # 注意: 如果函数只有一个参数,需要参数后有一个逗号
    thread.start_new_thread(loop1, ("王老大", ))

    thread.start_new_thread(loop2, ("王二小", "王小二"))

    print("All done at: ", time.ctime())

if __name__ == '__main__':
    main()
    while True:
        time.sleep(1)