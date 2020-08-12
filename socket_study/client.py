from socket import *
from time import sleep 
import struct
import random

fmt = '8h40f'
clientSock = socket(AF_INET, SOCK_STREAM)
clientSock.connect(('192.168.0.100', 2006))
clientSock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
print(clientSock)

while True:
    sleep(1)
    data = clientSock.recv(1024)
    print('raw data', data)
    print("parsed data {}".format(struct.unpack(fmt,data)))
    sleep(0.1)
    values = [1024, 512]
    binary_data = struct.pack('h' * len(values), *values)
    clientSock.sendall(binary_data)
    print("bindary was sent {}".format(binary_data))
    clientSock.