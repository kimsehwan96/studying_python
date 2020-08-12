import random
import socket
from time import sleep
from struct import pack, unpack

host = '192.168.0.100'
port = 2000
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('192.168.0.100', 2000))
s.bind(('192.168.0.100',2000))
#s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

while True:
    values = [random.randint(1, 1000) for x in range(2)]
    binary_data = pack('h' * len(values), *values)
    s.sendall(binary_data)
    sleep(1)
s.close()