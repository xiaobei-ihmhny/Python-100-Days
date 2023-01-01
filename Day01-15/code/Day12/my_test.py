# 例子1：验证输入用户名和QQ号是否有效并给出对应的提示信息

"""
验证输入用户名和QQ号是否有效并给出对应的提示信息

要求：用户名必须由字母、数字或下划线构成且长度在6~20字符之间，QQ号5~12的数字且首位不能为0
"""

import re


def re1():
    username = input('请输入用户名：')
    password = input('请输入QQ号：')
    m1 = re.match(r'^\w{6,20}$', username)
    if not m1:
        print('请输入有效的用户名.')
    m2 = re.match(r'^[1-9]\d{4,11}$', password)
    if not m2:
        print('请输入有效的QQ号.')
    if m1 and m2:
        print('你输入的信息是有效的！')


# 例子二：从一段文字中提取出国内手机号码
"""
下面这张图是截止到2017年底，国内三家运营商推出的手机号段。

电信号段：133/153/180/181/189/177
联通号段：130/131/132/155/185/186/145/176
移动号段：134/135/136/137/138/139/150/152/157/158/159/182/183/184/187/188/147/178

整理后的号段：
130		150		180
131				181
132		152		182
133		153		183
134				184
135	145	155	176	185
136			177	186
137	147	157	178	187
138		158		188
139		159		189

对应的正则表达式为：
r'(?<=\D)1[38]\d{9}|14[57]\d{8}|15[0235789]\d{8}|17[678]\d{8}(?=\D)'
"""


def re2():
    text = input('请输入一段包含手机号的文字：')
    # 创建正则表达式对象 使用了前瞻和回顾来保证手机号前后不应该出现数字
    pattern = re.compile(r'(?<=\D)1[34578]\d{9}(?=\D)')
    phone_list = re.findall(pattern, text)
    print(phone_list)
    print('----------------------------')
    # 通过迭代器取出匹配对象并获得匹配的内容
    for temp in re.finditer(pattern, text):
        print(temp.group())
    print('----------------------------')
    # 通过search函数指定搜索位置找出所有匹配
    m = pattern.search(text)
    while m:
        print(m.group())
        m = pattern.search(text, m.end())


# 替换字符串中的不良内容
def re3():
    sentence = '你丫是傻叉吗? 我操你大爷的. Fuck you.'
    purified = re.sub('[操肏艹]|fuck|shit|傻[比屄逼叉缺吊屌]|煞笔', '*', sentence, flags=re.IGNORECASE)
    print(purified)  # 你丫是*吗? 我*你大爷的. * you.


# 拆分长字符串
def re4():
    poem = '窗前明月光，疑是地上霜。举头望明月，低头思故乡。'
    sentence_list = re.split(r'[，。 , .]', poem)
    while '' in sentence_list:
        sentence_list.remove('')
    print(sentence_list)


# 替换字符串中的不良内容
def re5():
    sentence = '我:是*<>小贝'
    purified = re.sub(r'[?\/:*"<>|]', '_', sentence, flags=re.IGNORECASE)
    print(purified)  #


def re6():
    sentence = 'https://pics7.baidu.com/feed/b3fb43166d224f4a44a9c3cad0cfe7559922d1f3.jpeg'
    index1 = sentence.rfind('/')
    index2 = sentence.rfind('?')
    if index2 == -1:
        sentence = sentence[index1+1:]
    else:
        sentence = sentence[index1+1:index2]
    print(sentence)


if __name__ == '__main__':
    # re1()
    # re2()
    # re3()
    # re4()
    # re5()
    re6()
