"""
计算阶乘
输入M和N计算C(M,N)


"""

# m = int(input('m = '))
# n = int(input('n = '))
# fm = 1
# for i in range(1, m + 1):
#     fm *= i
# fn = 1
# for i in range(1, n + 1):
#     fn *= i
# fm_n = 1
# for i in range(1, m - n + 1):
#     fm_n *= 1
# print(fm // fn // fm_n)


# import math
#
# def fac(num):
#     """求阶乘"""
#     result = 1
#     for i in range(1, num + 1):
#         result *= i
#     return result
#
#
# m = int(input('m = '))
# n = int(input('n = '))
# print(fac(m) // fac(n) // fac(m - n))
# print(math.factorial(m) // math.factorial(n) // math.factorial(m - n))


""" 函数的参数 """


# from random import randint
#
#
# def roll_dice(n = 2):
#     """摇色子"""
#     total = 0
#     for i in range(n):
#         total += randint(1, 6)
#     return total
#
#
# def add(a=0, b=0, c=0):
#     """三个数相加"""
#     return a + b + c
#
#
# print(roll_dice())
# print(roll_dice(3))
# print(add())
# print(add(1))
# print(add(1, 2))
# print(add(1, 2, 3))
# # 传递参数的时候可以不按顺序
# print(add(b = 1, a = 2, c = 3))


"""可变参数"""


# def addn(*args):
#     total = 0
#     for i in args:
#         total += i
#     return total
#
#
# # 在调用add函数时可以传递0个或多个参数
# print(addn(1))
# print(addn(1, 2))
# print(addn(1, 2, 3))
# print(addn(1, 2, 3, 4, 5))

# def foo():
#     print("这是一个foo函数")
#
#
# def foo():
#     print("这也是一个foo函数")
#
# foo()

# import module1
# import module2
#
# module1.foo()
# module2.foo()

# import module1 as m1
# import module2 as m2
#
# m1.foo()
# m2.foo()

# import module3

"""
练习1：实现计算求最大公约数和最小公倍数的函数。

author: xiaobei
"""


# def foo(m, n):
#     if m > n:
#         m, n = n, m
#     for i in range(m, 0, -1):
#         if m % i == 0 and n % i == 0:
#             print('%d 和 %d 的最大公约数为：%d' % (m, n, i))
#             print('%d 和 %d 的最小公倍数为：%d' % (m, n, m * n // i))


# def gcd(x, y):
#     """求最大公约数"""
#     (x, y) = (y, x) if x > y else (x, y)
#     for factor in range(x, 0, -1):
#         if x % factor == 0 and y % factor == 0:
#             return factor
#
# def lcm(x, y):
#     """计算最小公倍数"""
#     return x * y // gcd(x, y)


"""
实现判断一个数是不是回文数的函数。
"""


# def pn(x):
#     temp = x
#     reversed_num = 0
#     while x > 0:
#         reversed_num = reversed_num * 10 + x % 10
#         x //= 10
#     return temp == reversed_num
#
#
# num = int(input('num = '))
# pn = pn(num)
# if pn:
#     print('%d 是回文数' % num)
# else:
#     print('%d 不是回文数' % num)



"""
实现判断一个数是不是素数的函数。

素数指的是只能被1和自身整除的正整数（不包括1）。

author: xiaobei
"""


# def is_prime(num):
#     for i in range(2, int(num ** 0.5) + 1):
#         if num % i == 0:
#             return False
#     return num != 1


"""
写一个程序判断输入的正整数是不是回文素数。

author: xiaobei
"""

# def pn_is_prime(num):
#     """判断当前数字是否为回文数"""
#     temp = num
#     reverse_num = 0
#     while num > 0:
#         reverse_num = reverse_num * 10 + num % 10
#         num //= 10
#     if temp != reverse_num:
#         return False
#     else:
#         # 再来判断当前回文数是否为素数
#         for i in range(2, int(temp ** 0.5) + 1):
#             if temp % i == 0:
#                 return False
#         return temp != 1



