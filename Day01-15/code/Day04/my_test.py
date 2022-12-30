"""
用for循环实现1-100求和

author: xiaobei
"""
# sum = 0
# for x in range(101):
#     sum += x
# print('1+2+...+100 = %d' % sum)


"""
用for循环实现1-100之间的偶数求和

author: xiaobei
"""
# sum = 0
# for x in range(2, 101, 2):
#     sum += x
# print(sum)


"""
用for循环实现1-100之间的偶数求和

author: xiaobei
"""
# sum = 0
# for x in range(1, 101):
#     if x % 2 == 0:
#         sum += x
# print(sum)


"""
猜数字游戏

规则是：计算机出一个1到100之间的随机数，玩家输入自己猜的数字，计算机给出对应的提示信息（大一点、小一点或猜对了），
如果玩家猜中了数字，计算机提示用户一共猜了多少次，游戏结束，否则游戏继续。

author: xiaobei
"""

# import random
# # 随机获得一个数
# ran = random.randint(1, 100)
# guess = int(input('请猜测：'))
# times = 1
# while guess != ran:
#     if guess > ran:
#         print('小一点')
#     else:
#         print('大一点')
#     times += 1
#     guess = int(input('请再猜：'))
# print('恭喜你，猜对了！一共猜了 %d 次！' % times)

# import random
# answer = random.randint(1, 100)
# counter = 0
# while True:
#     counter += 1
#     guess = int(input('请输入：'))
#     if guess < answer:
#         print('大一点')
#     elif guess > answer:
#         print('小一点')
#     else:
#         print('恭喜你，猜对了')
#         break
# print('您一共猜了%d次' % counter)
# if counter > 7:
#     print('您的智商余额不足了啊')

"""
输出乘法口诀表(九九表)

author: xiaobei
"""

# for x in range(1, 10):
#     line = ''
#     for y in range(1, x + 1):
#         line += "{} * {} = {} ".format(y, x, x * y)
#     print(line)

# for i in range(1, 10):
#     for j in range(1, i + 1):
#         print('%d * %d = %d' % (i, j, i * j), end='\t')
#     print()


"""
输入一个正整数判断它是不是素数

提示：素数指的是只能被1和自身整除的大于1的整数。
"""
# from math import sqrt
#
# num = int(input("请输入一个正整数："))
# end = int(sqrt(num))
# is_prime = True
# for x in range(2, end + 1):
#     if num % x == 0:
#         is_prime = False
#         break
# if is_prime and num != 1:
#     print("数字%d是素数" % num)
# else:
#     print("数字%d不是素数" % num)


"""
输入两个正整数，计算他们的最大公约数和最小公倍数

两个数的最大公约数是两个数的公共因子中最大的那个数；
两个数的最小公倍数则是能够同时被两个数整除的最小的那个数。

"""
# a = int(input("请输入第一个数："))
# b = int(input("请输入第二个数："))
#
# print('%d 和 %d 的最大分约数为：' % (a, b))
# while True:
#     temp = a % b
#     if temp == 0:
#         min = b
#         break
#     else:
#         a = b
#         b = temp
# print('%d' % min)

# x = int(input('x = '))
# y = int(input('y = '))
# # 如果 x > y 就交换
# if x > y:
#     # 通过下面的操作将y的赋值给x，将x的值赋值给y
#     x, y = y, x
# # 从两个数中较小的数开始做递减的循环
# for f in range(x, 0, -1):
#     if x % f == 0 and y % f == 0:
#         print('%d 和 %d 的最大公约数为：%d' % (x, y, f))
#         print('%d 和 %d 的最小公倍数为：%d' % (x, y, x * y // f))

"""
练习3：打印如下所示的三角形图案

*
**
***
****
*****

    *
   **
  ***
 ****
*****


    *
   ***
  *****
 *******
*********

"""

# for x in range(6):
#     r = ''
#     for y in range(x):
#         r += '*'
#     print(r)
#
# for x in range(1, 6):
#     r = ''
#     for s in range(5 - x, 0, -1):
#         r += ' '
#     for y in range(1, x + 1):
#         r += '*'
#     print(r)
#
# for x in range(1, 10, 2):
#     temp = (9 - x) // 2
#     rr = ''
#     for s in range(temp):
#         rr += ' '
#     for r in range(x):
#         rr += '*'
#     for s in range(temp):
#         rr += ' '
#     print(rr)

line = int(input("请输入行数："))
for i in range(line):
    for _ in range(i + 1):
        print('*', end='')
    print()

print('=======================')

for i in range(line):
    for j in range(line - i - 1):
        print(' ', end='')
    for k in range(i + 1):
        print('*', end='')
    print()

print('=======================')

for i in range(line):
    x = 2 * i + 1
    for j in range(line - i - 1):
        print(' ', end='')
    for _ in range(x):
        print('*', end='')
    print()
