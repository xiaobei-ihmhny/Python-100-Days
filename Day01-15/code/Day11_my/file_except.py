import math


def input_demo():
    f = open('致橡树.txt', 'r', encoding='utf-8')
    print(f.read())
    if f:
        f.close()


def input_demo_complete1():
    f = None
    filename = '致橡树.txt'
    encoding = 'utf-8'
    try:
        f = open(filename, 'r', encoding=encoding)
        print(f.read())
    except FileNotFoundError:
        print('指定文件 [%s] 不存在' % filename)
    except LookupError:
        print('指定的编码 [%s] 不存在' % encoding)
    except UnicodeDecodeError:
        print('读取文件时解码异常')
    finally:
        if f:
            f.close()


# 使用 with 关键字的上下文环境，就不需要再关闭文件了
def input_demo_context():
    f = None
    filename = '致橡树.txt'
    encoding = 'utf-8'
    try:
        with open(filename, 'r', encoding=encoding) as f:
            print(f.read())
    except FileNotFoundError:
        print('指定文件 [%s] 不存在' % filename)
    except LookupError:
        print('指定的编码 [%s] 不存在' % encoding)
    except UnicodeDecodeError:
        print('读取文件时解码异常')


import time


def read_demo_methods():
    # 一次性读取
    with open('致橡树.txt', mode='r', encoding='utf-8') as f:
        print(f.read())
        print()
    # for-in 逐行读取
    with open('致橡树.txt', 'r', encoding='utf-8') as f:
        for line in f:
            print(line, end='')
            time.sleep(0.5)
        print()
    # readlines 将文件读取到列表容器中
    with open('致橡树.txt', 'r', encoding='utf-8') as f:
        lines = f.readlines()
    print(lines)


# 判断一个数字是否是素数
def is_prime(num):
    """判断素数"""
    assert num > 0
    for i in (range(2, int(math.sqrt(num)) + 1)):
        if num % i == 0:
            return False
    return True if num != 1 else False


# （1-99之间的素数保存在a.txt中，100-999之间的素数保存在b.txt中，1000-9999之间的素数保存在c.txt中）
def prime_input_file():
    a = open('a.txt', 'w', encoding='utf-8')
    b = open('b.txt', 'w', encoding='utf-8')
    c = open('c.txt', 'w', encoding='utf-8')
    for i in range(1, 10000):
        if is_prime(i):
            if 1 <= i <= 99:
                a.write('{}\n'.format(i))
            elif i <= 999:
                b.write('{}\n'.format(i))
            else:
                c.write('{}\n'.format(i))
    if a:
        a.close()
    if b:
        b.close()
    if c:
        c.close()


def input_copy_output():
    input_file_name = "美女.jpeg"
    try:
        with open(input_file_name, 'rb') as fs1:
            data = fs1.read()
            print(type(data))  # <class 'bytes'>
        with open('美女_copy.jpeg', 'wb') as fs2:
            fs2.write(data)
    except FileNotFoundError as e:
        print('指定的文件%s不存在' % input_file_name)
    except IOError as e:
        print('读写文件时发生异常')
    print('文件操作结束')


import json


def json_serialization():
    my_dict = {
        'name': 'xiaobei',
        'age': 18,
        'friends': ['tietie', 'pangpang'],
        'cars': [
            {
                'brand': 'byd',
                'max_speed': 120
            },
            {
                'brand': 'haojue',
                'max_speed': 95
            }
        ]
    }

    try:
        with open('data.json', 'w', encoding='utf-8') as f:
            json.dump(my_dict, f)
    except IOError as e:
        print('数据读写异常%s' % e)
    print('数据保存完成')


import requests

def json_deserialization():
    try:
        resp = requests.get('https://api.github.com/search/repositories?q=language:python&sort=stars')
        data_model = json.loads(resp.text)
        for item in data_model['items']:
            print(item['full_name'])
    except IOError as e:
        print('读取出现异常')
    print('读取完成')


if __name__ == '__main__':
    # input_demo()
    # input_demo_complete1()
    # input_demo_context()
    # read_demo_methods()
    # prime_input_file()
    # input_copy_output()
    # json_serialization()
    json_deserialization()

