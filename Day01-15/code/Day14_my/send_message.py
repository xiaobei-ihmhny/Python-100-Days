import urllib.parse
import urllib.request


# 发送短信
# 使用的是[互亿无线](http://www.ihuyi.com/)短信平台
# （该平台为注册用户提供了50条免费短信以及常用开发语言发送短信的demo，可以登录该网站并在用户自服务页面中对短信进行配置）
def send_message():
    # 接口地址
    url = 'http://106.ihuyi.com/webservice/sms.php?method=Submit'

    # 定义请求的数据
    values = {
        'account': 'xxxxxxxx',
        'password': 'xxxxxxxxxxxx',
        'mobile': '134xxxxxxxx',
        'content': '您的验证码是：7835。请不要把验证码泄露给其他人。',
        'format': 'json',
    }

    # 将数据进行编码
    data = urllib.parse.urlencode(values).encode(encoding='utf-8')
    # 发起请求
    req = urllib.request.Request(url, data)
    response = urllib.request.urlopen(req)
    res = response.read()

    # 打印结果
    print(res.decode('utf-8'))


if __name__ == '__main__':
    send_message()