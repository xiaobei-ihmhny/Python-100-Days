def foo():
    pass


def bar():
    pass


# __name__ 是python中一个隐含的变量它代表了模块的名字
# 只有被python解释器直接执行的模块的名字才是__main__
if __name__ == '__main__':
    print('call foo()')
    foo()
    print('call bar()')
    bar()
