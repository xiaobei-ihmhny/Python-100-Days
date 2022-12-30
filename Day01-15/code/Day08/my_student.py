class Student(object):

    # __init__ 是一个特殊的方法用于在创建对象时进行初始化操作
    # 通过这个方法我们可以为学生对象绑定name和age两个属性
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # 定义普通方法
    def study(self, course_name):
        print('%s正在学习%s.' % (self.name, course_name))

    # 定义另一个普通方法
    def watch_movie(self):
        if self.age < 18:
            print('%s只能观看《能出没》.' % self.name)
        else:
            print('%s正在观看岛国爱情大电影.' % self.name)


# 测试方法
def main():
    # 创建学生对象并指定姓名和年龄
    stu = Student('xiaobei', 31)
    # 给学习对象发出学习指令
    stu.study('chinese')
    # 告诉学习对象可以休息一下
    stu.watch_movie()


if __name__ == '__main__':
    main()
