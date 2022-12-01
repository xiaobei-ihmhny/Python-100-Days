"""
输入年份判断是不是闰年
"""

y = int(input('请输入年份：'))
leap_year = (y % 4 == 0 & y % 100 != 0) | (y % 400 == 0)
if leap_year:
    print("年份%d是闰年" % y)
else:
    print("年份%d不是闰年" % y)
