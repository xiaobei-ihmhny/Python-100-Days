from threading import Thread

import requests
import re

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
}

proxy = {'http': '33.33.33.10:8118'}


# 通过继承Thread类创建自定义的线程类
class DownLoadHandler(Thread):

    def __init__(self, url, filename):
        super().__init__()
        self.url = url
        self.filename = filename

    def run(self):
        filename = self.filename
        suffix = self.get_suffix(True)
        filename = filename + suffix
        print('下载使用的文件名为：%s' % filename)
        try:
            res = requests.get(self.url, headers=headers, proxies=proxy)
            with open(filename, 'wb') as f:
                f.write(res.content)
        except RuntimeError:
            print('下载出错')

    def get_suffix(self, need_dot=False):
        """
        给定一个文件名，返回文件名的后缀

        :param filename: 文件名
        :param need_dot: 返回的后缀名是否需要带点
        :return 文件的后缀名
        """
        index1 = self.url.rfind('/')
        index2 = self.url.rfind('?')
        if index2 == -1:
            filename = self.url[index1 + 1:]
        else:
            filename = self.url[index1 + 1:index2]
        pos = filename.rfind('.')
        if 0 < pos < len(filename) - 1:
            index = pos if need_dot else pos + 1
            return filename[index:]
        else:
            return ''


def main():
    # 通过 requests 模块的get函数获取网络资源
    # 下面的代码是直接使用百度搜索查找美女图片
    # 需要添加 headers 告知服务端当前请求的客户端信息
    resp = requests.get(
        'https://image.baidu.com/search/acjson?tn=resultjson_com&logid=5358515876847266883&ipn=rj&ct=201326592&is=&fp=result&fr=&word=%E7%BE%8E%E5%A5%B3&cg=girl&queryWord=%E7%BE%8E%E5%A5%B3&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=-1&z=&ic=0&hd=&latest=&copyright=&s=&se=&tab=&width=&height=&face=0&istype=2&qc=&nc=1&expermode=&nojc=&isAsync=&pn=30&rn=30&gsm=1e&1672541126815=',
        headers=headers
    )
    data_model = resp.json()
    for mm_dict in data_model['data']:
        try:
            url_dict = mm_dict['replaceUrl'][0]
            url_filename = re.sub(r'[?\/:*"<>|]', '_', mm_dict['fromPageTitle'], flags=re.IGNORECASE)
            url = url_dict['ObjURL']
            print(url)
            print(url_filename)
            # 通过多线程的方式实现图片下载
            DownLoadHandler(url, url_filename).start()
        except KeyError:
            print('当前属性信息获取失败')


if __name__ == '__main__':
    main()
