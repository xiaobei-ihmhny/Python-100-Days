"""
### @property装饰器

之前我们讨论过Python中属性和方法访问权限的问题，虽然我们不建议将属性设置为私有的，但是如果直接将属性暴露给外界也是有问题的，
比如我们没有办法检查赋给属性的值是否有效。我们之前的建议是将属性命名以单下划线开头，
通过这种方式来暗示属性是受保护的，不建议外界直接访问，那么如果想访问属性可以通过属性的getter（访问器）和setter（修改器）方法进行对应的操作。
如果要做到这点，就可以考虑使用@property包装器来包装getter和setter方法，使得对属性的访问既安全又方便，代码如下所示。

### __slots__魔法

我们讲到这里，不知道大家是否已经意识到，Python是一门[动态语言](https://zh.wikipedia.org/wiki/%E5%8A%A8%E6%80%81%E8%AF%AD%E8%A8%80)。
通常，动态语言允许我们在程序运行时给对象绑定新的属性或方法，当然也可以对已经绑定的属性和方法进行解绑定。
但是如果我们需要限定自定义类型的对象只能绑定某些属性，
可以通过在类中定义__slots__变量来进行限定。需要注意的是__slots__的限定只对当前类的对象生效，对子类并不起任何作用。
"""


class Person(object):

    # 可以通过 __slots__ 来限定 Person 对象绑定的属性
    __slots__ = ('_name', '_age', '_gender')

    def __init__(self, name, age=0):
        self._name = name
        self._age = age

    # 访问器 getter 方法
    @property
    def name(self):
        return self._name

    # 访问器 setter 方法
    @property
    def age(self):
        return self._age

    # 修改器 - setter 方法
    """
    正确使用 setter 方法的前提是：
    1. 存在setter方法
    2. setter方法上有相关注解
    1、2 缺一不可
    """

    @age.setter
    def age(self, age):
        self._age = age

    # toString 方法
    def __str__(self):
        return '[%s, %d]' % (self._name, self._age)

    # 玩耍
    def play(self):
        if self._age <= 16:
            print('%s正在玩五子棋.' % self._name)
        else:
            print('%s正在玩斗地主.' % self._name)


def main():
    p1 = Person('xiaobei', 18)
    p2 = Person('tietie', 1)
    p1.age = 20
    # python 为动态语言，可以给对象绑定新的属性或方法
    p1._gender = '男'
    # p2.name = 'natie'
    print(p1, p2)
    p1.play()
    p2.play()


if __name__ == '__main__':
    main()
