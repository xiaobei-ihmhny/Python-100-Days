"""
输入圆的半径计算周长和面积
"""
import math

r = float(input("请输入圆的半径："))
c = 2 * math.pi * r
a = math.pi * r * r
print("半径为：%.1f的圆的周长为：%.1f，面积为：%.1f" % (r, c, a))
print(f'半径为：{r:.1f}的圆的周长为：{c:.1f}，面积为：{a:.4f}')
