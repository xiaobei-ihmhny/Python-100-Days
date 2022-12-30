"""
模拟单线程下载
"""
import multiprocessing
import random
import time


def download_task1(filename):
    print('开始下载%s...' % filename)
    time_to_download = random.randint(5, 10)
    time.sleep(time_to_download)
    print('%s下载完成！耗费了%d秒' % (filename, time_to_download))


def download1():
    start = time.time()
    download_task1('Python从入门到精通！')
    download_task1('岛国电影.avi')
    end = time.time()
    print('总共耗费了%.2f秒' % (end - start))


# 使用多进程的方式
def download2():
    start = time.time()
    p1 = multiprocessing.Process(target=download_task1, args=('Python从入门到精通！',))
    p1.start()
    p2 = multiprocessing.Process(target=download_task1, args=('岛国电影.avi',))
    p2.start()
    p1.join()
    p2.join()
    end = time.time()
    print('总共耗费了%.2f秒' % (end - start))


# 两个进程输出的Ping和Pong加起来一共10个

counter = 0


def sub_task(string):
    global counter
    while counter < 10:
        print(string, end='', flush=True)
        counter += 1
        time.sleep(0.01)


def print1():
    multiprocessing.Process(target=sub_task, args=('Ping',)).start()
    multiprocessing.Process(target=sub_task, args=('Pong',)).start()


if __name__ == '__main__':
    # download1()
    # download2()
    print1()




