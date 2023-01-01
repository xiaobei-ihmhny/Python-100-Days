import base64
import json
import socket


def file_client_start():
    client = socket.socket()
    client.connect(('192.168.31.42', 6789))
    file_data = bytes()
    data = client.recv(1024)
    while data:
        file_data += data
        data = client.recv(1024)
    my_dict = json.loads(file_data.decode('utf-8'))
    filename = my_dict['name']
    filedata = my_dict['data'].encode('utf-8')
    with open('D:\\' + filename,  'wb') as f:
        f.write(base64.b64decode(filedata))
    print('图片已保存！')
    client.close()


if __name__ == '__main__':
    file_client_start()
