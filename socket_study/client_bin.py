import random
import socket
from time import sleep
from struct import pack, unpack

host = 'localhost'
port = 12345
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))
count = 0

while True:
    count = count + 1

    values = [random.randint(1, 1000) for x in range(40)]
    binary_data = pack('h' * len(values), *values)

    s.sendall(binary_data)
    sleep(1)

s.close()