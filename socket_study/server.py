from socket import *

serverSock = socket(AF_INET, SOCK_DGRAM)
serverSock.bind(('',12345))
#serverSock.listen(1)

#connectionSock, addr = serverSock.accept()
connectionSock, addr = serverSock.recvfrom(1024)

print(str(addr), '에서 접속이 확인되었어요')

data = connectionSock.recv(1024)
print('받은 데이터 : ', data.decode('utf-8'))

connectionSock.send('I am a sever.'.encode('utf-8'))

print('메시지를 보냈습니다.')

while True:

    recvData = connectionSock.recv(1024)
    print('받은 데이터는 이것이에요 : ', recvData.decode('utf-8'))
