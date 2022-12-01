"""
这是一个测试程序
"""
# a = int(input('a = '))
# b = int(input('b= '))
# print('%d + %d = %d' % (a, b, a + b))
# print('%d - %d = %d' % (a, b, a - b))
# print('%d * %d = %d' % (a, b, a * b))
# print('%d / %d = %d' % (a, b, a / b))
# print('%d // %d = %d' % (a, b, a // b))  # 两个 // 表示整除
# print('%d %% %d = %d' % (a, b, a % b))  # a 对 b 取模
# print('%d ** %d = %d' % (a, b, a ** b))  # 相当于 a 的 b 次方，其中 ** 表示指数运算符


"""
赋值运算符
"""

a = 10
b = 3
a += b
a *= a + 2
print(a)

"""
比较运算符和逻辑运算符
"""

flag0 = 1 == 1
flag1 = 3 > 2
flag2 = 2 < 1
flag3 = flag1 and flag2
flag4 = flag1 or flag2
flag5 = not (1 != 2)
print('flag0 = ', flag0)    # flag0 = True
print('flag1 = ', flag1)    # flag1 = True
print('flag2 = ', flag2)    # flag2 = False
print('flag3 = ', flag3)    # flag3 = False
print('flag4 = ', flag4)    # flag4 = True
print('flag5 = ', flag5)    # flag5 = False
