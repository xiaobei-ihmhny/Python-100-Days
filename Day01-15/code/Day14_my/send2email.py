import smtplib
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from smtplib import SMTP


def send_2_email_with_base():
    sender = 'aaa@163.com'
    receivers = ['bbb@qq.com']
    # 邮箱正文内容，第一个参数为内容，第二个参数为格式（plain 为纯文本），第三个参数为编码
    message = MIMEText('我是Python发出的邮件哈', 'plain', 'utf-8')
    # 邮件头信息，这样发出的邮件发送者和接收者怎么感觉少信息呢？
    message['Subject'] = Header('Python示例邮件', 'utf-8')  # 邮件主题
    try:
        smtper = SMTP('smtp.163.com')
        # 请注意此处不是使用密码而是邮件客户端授权码进行登录0
        smtper.login(sender, '')
        smtper.sendmail(sender, receivers, message.as_string())
        print('邮件发送成功')
    except smtplib.SMTPException:
        print('无法发送邮件')
    finally:
        # 关闭服务器
        smtper.quit()


def send_2_email_with_attach():
    # 创建一个带附件的邮件消息对象
    message = MIMEMultipart()

    html_msg = """
    <p>Python 邮件发送HTML格式文件测试...</p>
    <p><a href="http://www.runoob.com">这是一个链接</a></p>
    """

    # 创建文本内容
    html_context = MIMEText(html_msg, 'html', 'utf-8')
    message['Subject'] = Header('本月数据', 'utf-8')
    # 将文本内容添加到邮件消息对象中
    message.attach(html_context)

    # 读取文件并将文件作为附件添加到邮件消息对象中
    txt_filename = 'hello.txt'
    txt = MIMEText(open(txt_filename, 'rb').read(), 'base64', 'utf-8')
    # 设置正确的文件名
    txt.add_header('Content-Disposition', 'attachment', filename=Header(txt_filename, 'utf-8').encode())
    message.attach(txt)

    # 读取文件并将文件作为附件添加到邮件消息对象中
    xls_filename = '汇总数据.xlsx'
    xls = MIMEText(open(xls_filename, 'rb').read(), 'base64', 'utf-8')
    # 设置正确的文件名
    xls.add_header('Content-Disposition', 'attachment', filename=Header(xls_filename, 'utf-8').encode())
    message.attach(xls)

    try:
        smtper = SMTP('smtp.163.com')
        sender = 'aaa@163.com'
        receivers = ['bbb@qq.com']
        # 请注意此处不是使用密码而是邮件客户端授权码进行登录0
        smtper.login(sender, '')
        smtper.sendmail(sender, receivers, message.as_string())
        print('发送完成！')
    except smtplib.SMTPException as e:
        print('邮件发送失败 %s' % e)
    finally:
        smtper.quit()


if __name__ == '__main__':
    send_2_email_with_base()
    # send_2_email_with_attach()
