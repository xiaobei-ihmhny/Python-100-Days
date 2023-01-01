import base64
import json
import socket
from threading import Thread


def start_file_sender_server():
    # 自定义线程类
    class FileSenderThread(Thread):

        def __init__(self, socket_client, file_data):
            super().__init__()
            self.socket_client = socket_client
            self.file_data = file_data

        def run(self):
            beauty_dict = {'name': 'beauty.jpeg', 'data': self.file_data}
            json_str = json.dumps(beauty_dict)
            self.socket_client.send(json_str.encode('utf-8'))
            self.socket_client.close()

    server = socket.socket()
    server.bind(('192.168.31.42', 6789))
    server.listen(512)
    with open('beauty.jpeg', 'rb') as f:
        # JSON是纯文本不能携带二进制数据
        # 所以图片的二进制数据要处理成base64编码
        data = base64.b64encode(f.read()).decode('utf-8')
    while True:
        client, addr = server.accept()
        FileSenderThread(client, data).start()


if __name__ == '__main__':
    start_file_sender_server()
