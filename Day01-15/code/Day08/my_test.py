from math import sqrt


class Point(object):

    def __init__(self, x=0, y=0):
        """
        初始化方法
        :param x: 横坐标
        :param y: 纵坐标
        """
        self.x = x
        self.y = y

    def move_to(self, x, y):
        """
        移动到指定位置

        :param x: 横坐标
        :param y: 纵坐标
        """
        self.x = x
        self.y = y

    def move_by(self, dx, dy):
        """
        移动指定的增量

        :param dx: 横坐标的增量
        :param dy: 纵检票的增量
        """
        self.x += dx
        self.y += dy

    def distance_to(self, other):
        """
        计算两个点之间的距离
        :param other: 另一个点
        """
        return sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)

    def __str__(self):
        return '(%s, %s)' % (str(self.x), str(self.y))


def main():
    p1 = Point(2, 5)
    p2 = Point()
    print(p1)
    print(p2)
    p2.move_by(-1, 9)
    print(p2)
    print(p2.distance_to(p1))


if __name__ == '__main__':
    main()
