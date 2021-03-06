import threading

sum = 0
loopSum = 100000

def myAdd():
    global sum, loopSum
    for i in range(1, loopSum):
        sum += 1


def myMinu():
    global  sum, loopSum
    for i in range(1, loopSum):
        sum -= 1

if __name__ =="__main__":
    print("Starting......{0}".format(sum))

    # 开始执行多线程,看执行结果是否一样
    t1 = threading.Thread(target=myAdd, args=())

    t2 = threading.Thread(target=myMinu, args=())

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Done.....{0}",format(sum))

# 多执行几次,会发现每次结果都不一样
#  说明加减是不定的,发生了冲突