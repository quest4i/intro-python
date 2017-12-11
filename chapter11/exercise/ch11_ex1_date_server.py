"""
일반 소켓을 사용하여 현재 시간 서비스를 구현하라.
클라이언트가 문자열 'time'을 서버에 보내면 현재 날짜와 시간을 ISO 문자열로 반환한다.
"""

from datetime import datetime
import socket

server_address = ('localhost', 6789)
max_size = 1000

print('Starting the server at', datetime.isoformat(datetime.now()))
print('Waiting for a client to call.')
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(server_address)
server.listen(5)

while True:
    client, addr = server.accept();
    data = client.recv(max_size)

    if data == b'time':
        print('At', datetime.now(), client, 'said', data)
        now = datetime.isoformat(datetime.now()).encode('utf-8')
        client.sendall(now)

client.close()
server.close()