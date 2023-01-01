import socket


def start_socket_client():
    # 1. 创建套接字对象默认使用IPv4和TCP协议
    client = socket.socket()
    # 2. 连接到服务器（需要指定ip地址和端口）
    client.connect(('192.168.31.42', 6789))
    # 3. 从服务器接收数据
    print(client.recv(1024).decode('utf-8'))
    # 4. 关闭连接
    client.close()


if __name__ == '__main__':
    start_socket_client()