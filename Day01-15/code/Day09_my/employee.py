"""
某公司有三种类型的员工 分别是部门经理、程序员和销售员
需要设计一个工资结算系统 根据提供的员工信息来计算月薪
部门经理的月薪是每月固定15000元
程序员的月薪按本月工作时间计算 每小时150元
销售员的月薪是1200元的底薪加上销售额5%的提成
"""
from abc import ABCMeta, abstractmethod


class Employee(object, metaclass=ABCMeta):

    def __init__(self, name):
        self._name = name

    @abstractmethod
    def pay(self):
        pass

    def __repr__(self):
        return '%s本月的工资为：%d' % (self._name, self.pay())


class Manager(Employee):

    def pay(self):
        return 15000


class Programmer(Employee):

    def __init__(self, name, work_hour=0):
        super(Programmer, self).__init__(name)
        self._work_hour = work_hour

    @property
    def work_hour(self):
        return self._work_hour

    @work_hour.setter
    def work_hour(self, work_hour):
        self._work_hour = work_hour if work_hour > 0 else 0

    def pay(self):
        return 150 * self._work_hour


class Salesman(Employee):

    def __init__(self, name, sales=0):
        super(Salesman, self).__init__(name)
        self._sales = sales

    @property
    def sales(self):
        return self._sales

    @sales.setter
    def sales(self, sales):
        self._sales = sales if sales > 0 else 0

    def pay(self):
        return 1200 + self._sales * 0.05


def main():
    name = input('请输入雇员姓名：')
    e_type = int(input("请输入雇员类型：（1 项目经理 2 程序员 3 销售员）"))
    if e_type == 1:
        m = Manager(name)
        print(m)
    elif e_type == 2:
        work_hour = int(input('请输入{}本月的工作时间（小时）'.format(name)))
        p = Programmer(name, work_hour)
        print(p)
    elif e_type == 3:
        sales = int(input('请输入{}本月的销售额：'.format(name)))
        s = Salesman(name)
        s.sales = sales
        print(s)
    else:
        print('请输入正确的雇员类型！')


if __name__ == '__main__':
    main()
