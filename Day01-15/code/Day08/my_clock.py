import time


class Clock(object):

    def __init__(self, hour=0, minute=0, second=0):
        """
        初始化信息
        :param hour:时
        :param minute:分
        :param second:秒
        """
        self._hour = hour
        self._minute = minute
        self._second = second

    # 显示当前时间
    @staticmethod
    def show_time():
        print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

    def run(self):
        self._second += 1
        if self._second == 60:
            self._second = 0
            self._minute += 1
            if self._minute == 60:
                self._minute = 0
                self._hour += 1
                if self._hour == 24:
                    self._hour = 0

    def show(self):
        """显示时间"""
        return '%02d:%02d:%02d' % (self._hour, self._minute, self._second)


def main():
    clock = Clock(23, 59, 58)
    while True:
        print(clock.show())
        time.sleep(1)
        clock.run()


if __name__ == '__main__':
    main()
