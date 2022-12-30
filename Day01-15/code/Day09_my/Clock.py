"""
和静态方法比较类似，Python还可以在类中定义类方法，类方法的第一个参数约定名为cls，
它代表的是当前类相关的信息的对象（类本身也是一个对象，有的地方也称之为类的元数据对象），
通过这个参数我们可以获取和类相关的信息并且可以创建出类的对象，代码如下所示。
"""
import time


class Clock(object):

    def __init__(self, hour=0, minute=0, sec=0):
        self._hour = hour
        self._minute = minute
        self._sec = sec

    @classmethod
    def now(cls):
        current_time = time.localtime(time.time())
        return cls(current_time.tm_hour, current_time.tm_min, current_time.tm_sec)

    def run(self):
        """走字"""
        self._sec += 1
        if self._sec == 60:
            self._sec = 0
            self._minute += 1
            if self._minute == 60:
                self._minute = 0
                self._hour += 1
                if self._hour == 24:
                    self._hour = 0

    def show(self):
        """显示时间"""
        return '%02d:%02d:%02d' % (self._hour, self._minute, self._sec)


def main():
    # 通过类方法创建对象并获取系统时间
    clock = Clock.now()
    while True:
        print(clock.show())
        time.sleep(1)
        clock.run()


if __name__ == '__main__':
    main()
