from socket import *
import struct

serverSock = socket(AF_INET, SOCK_STREAM)
serverSock.connect(('192.168.0.100', 2000))
serverSock.bind(('192.168.0.100',2000))
serverSock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
serverSock.listen(1)
connectionSock, addr = serverSock.accept()
connectionSock, addr = serverSock.recvfrom(1024)

print(str(addr), '에서 접속이 확인')

data = connectionSock.recv(1024)

while True:
    recvData = connectionSock.recv(1024)
    print(recvData)
   # print('받은 데이터: ', struct.unpack('6f', recvData))
   