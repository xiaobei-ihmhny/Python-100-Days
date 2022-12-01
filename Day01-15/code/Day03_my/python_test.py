"""
分支结构进行身份验证

version: 1.0
author: xiaobei
"""
# username = input('请输入用户名：')
# password = input('请输入密码：')
#
# # 判断当前的用户名是否为：tietie， 密码是否为：123456
# print('username=%s, password=%s' % (username, password))
# if username == 'tietie' and password == '123456':
#     print("身份验证成功！")
# else:
#     print("身份验证失败！")


"""
分段函数不求值

        3x - 5  (x > 1)
f(x) =  x + 2   (-1 <= x <= 1)
        5x + 3  (x < -1)
        
version: 1.0
author: xiaobei
"""

# x = float(input('请输入x的值：'))
#
# # 根据x的具体值来决定走什么逻辑
# if x > 1:
#     y = 3 * x - 5
# elif x >= -1:
#     y = x + 2
# else:
#     y = 5 * x + 3
# print(f'y的值为：{y:.2f}')


"""
分段函数不求值（嵌套）

        3x - 5  (x > 1)
f(x) =  x + 2   (-1 <= x <= 1)
        5x + 3  (x < -1)

version: 1.0
author: xiaobei
"""

# x = float(input('请输入x的值：'))
#
# if x > 1:
#     y = 3 * x + 5
# else:
#     if x >= -1:
#         y = x +2
#     else:
#         y = 5 * x + 3
# print('f(%.2f) = %.2f' % (x, y))


"""
练习1：英制单位英寸与公制单位厘米互换

1英寸 = 2.54 厘米

version: 1.0
author: xiaobei
"""

# value = float(input('请输入长度：'))
# unit = input('请输入单位（可选：in/英寸/cm/厘米）:')
#
# if unit == 'in' or unit == '英寸':
#     print('%.2f 英寸 = %.2f 厘米' % (value, value * 2.58))
# elif unit == 'cm' or unit == '厘米':
#     print(f'{value} 厘米 = {value / 2.58} 英寸')
# else:
#     print('请输入正确的单位!')


"""
练习2：百分制成绩转换为等级制成绩。

要求：如果输入的成绩在
    90分以上（含90分）输出A；
    80分-90分（不含90分）输出B；
    70分-80分（不含80分）输出C；
    60分-70分（不含70分）输出D；
    60分以下输出E。

version: 1.0
author: xiaobei
"""

# score = float(input('请输入你的分数：'))
#
# if score >= 90:
#     l = 'A'
# elif score >= 80:
#     l = 'B'
# elif score >= 70:
#     l = 'C'
# elif score >= 60:
#     l = 'D'
# else:
#     l = 'E'
#
# print(f'您的分数为：{score:.2f}，对应的等级是：{l}')



"""
 练习3：输入三条边长，如果能构成三角形就计算周长和面积

version: 1.0
author: xiaobei
"""


x = float(input('请输入第一条边x:'))
y = float(input('请输入第二条边y:'))
z = float(input('请输入第三条边z:'))

# 判断当前给到的三条边是否可构成三角形，条件：任意两边之和大于第三边
x_y = x + y
x_z = x + z
y_z = y + z
if x_y > z and x_z > y and y_z > x:
    print('当前边长满足构成三角形的条件')
    c = x + y + z
    p = c / 2
    a = (p * (p - x) * (p - y) * (p - z)) ** (1/2)
    print('当前三角形的周长为：%.2f 面积为：%.2f' % (c, a))
else:
    print('当前边长不满足构成三角形的条件！')