"""
寻找水仙花数

水仙花数也被称为超完全数字不变数、自恋数、自幂数、阿姆斯特朗数，它是一个3位数，该数字每个位上数字的立方之和正好等于它本身，
"""

# result = []
# for k in range(100, 1000):
#     i = list(str(k))
#     s = 0
#     for x in i:
#         x = int(x)
#         s += x ** 3
#     if s == k:
#         result.append(k)
# print(f'水仙花数有：{result}')
# 水仙花数有：[153, 370, 371, 407]

# for num in range(100, 1000):
#     low = num % 10
#     mid = num // 10 % 10
#     high = num // 100
#     if low ** 3 + mid ** 3 + high ** 3 == num:
#         print(num)
#

"""
正整数的反转

# _1 = num // 1 % 10
# _2 = num // 10 % 10
# _3 = num // 100 % 10
# _4 = num // 1000 % 10
# _5 = num // 10000 % 10
# print(f'{_1}, {_2}, {_3}, {_4}, {_5}')
"""

# num = int(input("num = "))
# reversed_num = 0
# while num > 0:
#     reversed_num = reversed_num * 10 + num % 10
#     num //= 10
# print(reversed_num)

"""
百钱百鸡问题。

百钱百鸡是我国古代数学家[张丘建](https://baike.baidu.com/item/%E5%BC%A0%E4%B8%98%E5%BB%BA/10246238)
在《算经》一书中提出的数学问题：
鸡翁一值钱五，鸡母一值钱三，鸡雏三值钱一。
百钱买百鸡，问鸡翁、鸡母、鸡雏各几何？
翻译成现代文是：
公鸡5元一只，母鸡3元一只，小鸡1元三只，用100块钱买一百只鸡，问公鸡、母鸡、小鸡各有多少只？

5x + 3y + z/3 = 100
x + y + z = 100
15x + 9y + z = 300
14x + 8y = 200
7x + 4y = 100
x = 4 y = 18 z = 78
"""

# for x in range(20):
#     for y in range(33):
#         z = 100 - x - y
#         if 5 * x + 3 * y + z / 3 == 100:
#             print('x = %d, y = %d, z = %d' % (x, y, z))


"""
Craps赌博游戏
我们设定玩家开始游戏时有1000元的赌注
游戏结束的条件是玩家输光所有的赌注

说明：CRAPS又称花旗骰，是美国拉斯维加斯非常受欢迎的一种的桌上赌博游戏。
该游戏使用两粒骰子，玩家通过摇两粒骰子获得点数进行游戏。
简单的规则是：
玩家第一次摇骰子如果摇出了7点或11点，玩家胜；
玩家第一次如果摇出2点、3点或12点，庄家胜；
其他点数玩家继续摇骰子，如果玩家摇出了7点，庄家胜；
如果玩家摇出了第一次摇的点数，玩家胜；
其他点数，玩家继续要骰子，直到分出胜负。
"""
# import random
#
# total = 1000
# r1 = random.randint(1, 6)
# r2 = random.randint(1, 6)
# s = r1 + r2
# r = r1 + r2
# i = 1
# while total > 0:
#     print('当前进行次数为：%d，第一次点数为：%d, 当前玩家的点数为：%d, 金额为：%d' % (i, s, r, total))
#     if i == 1 and (r == 7 or r == 11):
#         # 玩家胜利
#         total += 1000
#     elif i == 1 and (r == 2 or r == 3 or r == 12):
#         total -= 1000
#     elif i > 1 and r == 7:
#         total -= 100
#     elif i > 1 and r == s:
#         total += 1000
#     r1 = random.randint(1, 6)
#     r2 = random.randint(1, 6)
#     r = r1 + r2
#     i += 1

# from random import randint
#
# money = 1000
# while money > 0:
#     print("您总资产为：%d" % money)
#     while True:
#         debt = int(input("请下注："))
#         if 0 < debt <= money:
#             break
#     first = randint(1, 6) + randint(1, 6)
#     print('您摇出了%d点' % first)
#     if first == 7 or first == 11:
#         print('玩家胜!')
#         money += debt
#     elif first == 2 or first == 3 or first == 12:
#         print('庄家胜')
#         money -= debt
#     else:
#         while True:
#             current = randint(1, 6) + randint(1, 6)
#             print('您摇出了%d点' % current)
#             if current == 7:
#                 print('庄家胜')
#                 money -= debt
#                 break
#             elif current == first:
#                 print('玩家胜!')
#                 money += debt
#                 break
# print("你破产了。。。")


"""
生成 斐波那契数列 的前20个数。

斐波那契数列（Fibonacci sequence），又称黄金分割数列，
是意大利数学家莱昂纳多·斐波那契（Leonardoda Fibonacci）在《计算之书》中提出一个在理想假设条件下兔子成长率的问题而引入的数列，所以这个数列也被戏称为"兔子数列";。
斐波那契数列的特点是数列的前两个数都是1，从第三个数开始，每个数都是它前面两个数的和，
形如：1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ...。斐波那契数列在现代物理、准晶体结构、化学等领域都有直接的应用。
"""
# length = int(input('需要生成斐波那契数列的长度为：'))
# a = 1
# b = 1
# print('1, 1', end='')
# for _ in range(2, length):
#     temp = a + b
#     a = b
#     b = temp
#     print(f', {temp}', end='')
# print()

"""
找出10000以内的完美数

完美数又称为完全数或完备数，它的所有的真因子（即除了自身以外的因子）的和（即因子函数）恰好等于它本身。
例如：6（$6=1+2+3$）和28（$28=1+2+4+7+14$）就是完美数。完美数有很多神奇的特性，有兴趣的可以自行了解。

完美数 6，其真因子有 [1, 2, 3]
完美数 28，其真因子有 [1, 2, 4, 7, 14]
完美数 496，其真因子有 [1, 2, 4, 8, 16, 31, 62, 124, 248]
完美数 8128，其真因子有 [1, 2, 4, 8, 16, 32, 64, 127, 254, 508, 1016, 2032, 4064]
"""

# num = int(input('请输入完美数的最大值：'))
# for i in range(1, num + 1):
#     # 首先算出当前数字的所有真因子
#     j = i // 2
#     s = 0
#     arr = []
#     for k in range(1, j + 1):
#         if i % k == 0:
#             s += k
#             arr.append(k)
#     if s == i:
#         print('完美数 %d，其真因子有 ' % i, end='')
#         print(arr)

"""
输出100以内的素数

素数指的是只能被1和自身整除的正整数（不包括1）。

3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 
"""

# num = int(input('请输入素数的最大值：'))
# for i in range(2, num + 1):
#     temp = 0
#     for j in range(2, i):
#         temp = j
#         if i % j == 0:
#             break
#     if temp == i - 1:
#         print('%d, ' % i, end='')

