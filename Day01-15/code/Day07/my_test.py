"""
字符串
"""

# s1 = 'hello, world!'
# s2 = "hello, world!"
# # 三个双引号或单引号开头的字符串可以折行
# s3 = """
# hello,
# world
# """
# print(s1, s2, s3, end='')


# list1 = [1, 2, 5, 8, 10]
# for index in range(len(list1)):
#     print(list1[index])
# print()
# for ele in list1:
#     print(ele)
# print()
# for index, ele in enumerate(list1):
#     print(index, ele)


# 列表操作 添加、移除元素
# list1 = [1, 2, 5, 8, 10]
# list1.append(100)
# list1.insert(1, 200)
# list1 += [400, 800]
# list1.extend([500, 1000])
# print(list1)
# print(len(list1))
# if 3 in list1:
#     list1.remove(3)
# if 200 in list1:
#     list1.remove(200)
# print(list1)
# # 从指定位置删除
# list1.pop(0)
# list1.pop(len(list1) - 1)
# print(list1)
# list1.clear()
# print(list1)


# 列表切片操作
# list1 = ['tietie', 'pangpang', 'wangcai', 'facai']
# list1 += ['heihei', 'dahuang']
# print(list1)
# list2 = list1[:]
# print(list2)
# list3 = list1[1:2]
# print(list3)
# list4 = list1[-3:-1]
# print(list4)
# list5 = list1[::-1]
# print(list5)


# 列表排序操作
# list1 = ['tietie', 'pangpang', 'dahuang', 'tiantian']
# list2 = sorted(list1)
# list3 = sorted(list1, reverse=True)
# list4 = sorted(list1, key=len)
# print(list1)
# print(list2)
# print(list3)
# print(list4)
# list1.sort(reverse=True)
# print(list1)

# 生成器和生成式
# import sys
#
# f = [x for x in range(1, 10)]
# print(f)
# f = [x + y for x in 'ABCDE' for y in '12345']
# print(f)
#
# f = [x ** 2 for x in range(1, 1000)]
# print(sys.getsizeof(f))
# print(f)
#
# f = (x ** 2 for x in range(1, 1000))
# print(sys.getsizeof(f))
# print(f)
#
# for val in f:
#     print(val)

# def fib(n):
#     a, b = 0, 1
#     for _ in range(n):
#         a, b = b, a + b
#         yield a
#
# def main():
#     for val in fib(20):
#         print(val)
#
# if __name__ == '__main__':
#     main()


# 使用元组

# 定义元组

# t = ('中国', '澳门', '香港', '台湾', True, 666)
# print(t)
# print(t[0])
# print(t[-1])
# for mem in t:
#     print(mem)
# # 元组类型数据不支持修改
# # t[0] = 20
# # 元组可重新引用新的元组
# t = ('world', 'china', 'henan', 4103, True, False)
# print(t)
# # 将元组转换为列表
# address = list(t)
# print(address)
# # 列表可以修改
# address[0] = 'All world'
# address[3] = 41
# print(address)
# # 将列表转换为元组
# fruits_list = ['apple', 'orange', 'banana']
# fruits_tuple = tuple(fruits_list)
# print(fruits_tuple)


# 使用集合

# 创建集合的字面量语法
# set1 = {1, 2, 3, 3, 3, 2}
# print(set1)
# print('length = ', len(set1))
# # 创建集合的构造器语法
# set2 = set(range(1, 10))
# set3 = set((1, 2, 3, 3, 2, 1))
# print(set2, set3)
# # 创建集合的推导式语法
# set4 = {num for num in range(1, 100) if num % 3 == 0 and num % 5 == 0}
# print(set4)
#
# # 向集合中添加或删除元素
# set1.add(4)
# set1.add(5)
# set2.update([11, 12])
# set2.discard(5)
# if 4 in set3:
#     set3.remove(4)
# print('set1 = ', set1)
# print('set2 = ', set2)
# print(set3.pop())  # pop是从前面删除一个并获取删除的元素
# print('set3 = ', set3)
#
# # 集合的成员、交集、并集、差集等运算。
# print('set1 & set2 = ', set1 & set2)
# print('set1.intersection(set2) = ', set1.intersection(set2))
# print('set1 | set2 = ', set1 | set2)
# print('set1.union(set2) = ', set1.union(set2))
# print('set1 - set2 = ', set1 - set2)
# print('set1.difference(set2) = ', set1.difference(set2))
# print('set1 ^ set2 = ', set1 ^ set2)
# print('set1.symmetric_difference(set2) = ', set1.symmetric_difference(set2))
# # 判断子集和超集
# print(set2 <= set1)
# print(set2.issubset(set1))
# print(set3 <= set1)
# print(set3.issubset(set1))
# print(set1 >= set2)
# print(set1.issuperset(set2))
# print(set1 >= set3)
# print(set1.issuperset(set3))


# 使用字典

# 创建字典的字面量语法
# scores = {'xiaobei': 18, 'tietie': 2, 'pangpang': 3, 4: 20}
# print(scores)
# # 创建字典的构建器语法
# items1 = dict(one=1, two=2, three=3, four=4)
# # 通过zip函数将两个字典压成一个
# items2 = dict(zip(['a', 'b', 'c'], '123'))
# # 创建字典的推导式语法
# items3 = {num: num ** 2 for num in range(1, 10)}
# print('items1 = ', items1)
# print('items2 = ', items2)
# print('items3 = ', items3)
# # 通过键获取字典中的值
# print(scores['xiaobei'])
# print(items1['one'])
# # 遍历字典中的所有键
# for key in scores:
#     print(f'{key}:{scores[key]}')
# # 更新字典中的元素
# scores['xiaobei'] = 30
# scores[4] = 'goods'
# scores.update(小贝=31, 拿铁=2)
# print(scores)
# if '小贝' in scores:
#     print(scores['小贝'])
# # 通过get方法获取指定键对应的值并给出默认值
# print(scores.get('小贝', 10))
# # 删除字典中的元素
# print(scores.popitem())  # 貌似是从后往前删除
# print(scores.popitem())
# print(scores.pop('拿铁', 1))
# # 清空字典
# scores.clear()
# print(scores)


import os
import time


def pao_ma_deng():
    content = '北京欢迎你为你开天辟地......'
    while True:
        # 清空屏幕
        os.system('cls')
        print(content)
        time.sleep(0.2)
        content = content[1:] + content[0]


import random


def verification_code():
    all_code = ('A', 'B', 'a', 'b', 1, 2, 3, 4, 5, 6, 7, 8, 9, 0)
    num = 6
    for i in range(6):
        index = random.randint(0, 13)
        print(all_code[index], end='')
    print()


def generate_code(code_len=4):
    """
    生成指定长度的验证码

    :param code_len：验证码的长度（默认4个字符）

    :return: 由大小写字母和数字构成的随机验证码
    """
    all_chars = '012345679abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    last_pos = len(all_chars) - 1
    code = ''
    for _ in range(code_len):
        index = random.randint(0, last_pos)
        code += all_chars[index]
    return code


def get_suffix(filename, need_dot=False):
    """
    给定一个文件名，返回文件名的后缀

    :param filename: 文件名
    :param need_dot: 返回的后缀名是否需要带点
    :return 文件的后缀名
    """
    pos = filename.rfind('.')
    if 0 < pos < len(filename) - 1:
        index = pos if need_dot else pos + 1
        return filename[index:]
    else:
        return ''


def search_needed_tuple(_list):
    """
    设计一个函数返回传入的列表中最大和第二大的元素的值。
    :param _list 传入的列表
    :return 该列表中最大和第二大的元素的值
    """
    if len(_list) >= 2:
        sorted_list = sorted(_list, reverse=True)
        result = (sorted_list[0], sorted_list[1])
        return result
    else:
        return tuple(_list)


def max2(x):
    m1, m2 = (x[0], x[1]) if x[0] > x[1] else (x[1], x[0])
    for index in range(2, len(x)):
        if x[index] > m1:
            m2 = m1
            m1 = x[index]
        elif x[index] > m2:
            m2 = x[index]
    return m1, m2


def leap_year(year):
    """
    判断当前年份是否是闰年

    :param year 年份
    :return 闰年返回true,平年返回false
    """
    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0


def witch_day_of_year(year, month, day):
    """
    计算当前时间是当年的第几天

    :param year 年份
    :param month 月份
    :param day 天
    :return 当前日期是当年的第几天
    """
    days_of_month = [
        [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31],
        [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    ][leap_year(year)]
    total_day = 0
    for index in range(month - 1):
        total_day += days_of_month[index]
    return total_day + day


def yanghui():
    """
    TODO 是否需要再关注呢？
    """
    num = int(input('Number of rows: '))
    yh = [[]] * num
    for row in range(len(yh)):
        yh[row] = [None] * (row + 1)
        for col in range(len(yh[row])):
            if col == 0 or col == row:
                yh[row][col] = 1
            else:
                yh[row][col] = yh[row - 1][col] + yh[row - 1][col - 1]
            print(yh[row][col], end='\t')
        print()


def double_boll():
    """
    双色球选号

    """
    result = []
    # 红球
    for index in range(6):
        random_int = random.randint(1, 34)
        while True:
            if random_int in result:
                random_int = random.randint(1, 34)
            else:
                break
        result.append(random_int)
    # 蓝球
    random_blue = random.randint(1, 17)
    return sorted(result), random_blue


# if __name__ == '__main__':
    # print(generate_code(6))
    # print(get_suffix('/export/Logs/demo.log', True))
    # print(search_needed_tuple([1, 2, 10, 20, 100, 50]))
    # max2 = max2([1, 2, 10, 20, 100, 50])
    # print(max2)
    # print(type(max2))
    # print(witch_day_of_year(1980, 11, 28))
    # print(witch_day_of_year(1981, 12, 31))
    # print(witch_day_of_year(2018, 1, 1))
    # print(witch_day_of_year(2016, 3, 1))
    # yanghui()
    # print(double_boll())
