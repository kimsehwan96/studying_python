from socket import *
#init




serverSock = socket(AF_INET, SOCK_STREAM)
serverSock.bind(('',55065))
serverSock.listen(1)

connectionSock, addr = serverSock.accept()

print(str(addr), '에서 접속이 확인')
data = connectionSock.recv(65536)
#print('받은 데이터 : ', data.decode('utf-8'))
print('recevied data : ', data)

while True:

    recvData = connectionSock.recv(65536)
    #print('recieved data : ', recvData.decode('utf-8'))
    print('recieved data : ', recvData)
    #print("this is data : ". recvData)

