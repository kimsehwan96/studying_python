import socket
import random
import struct
from time import sleep

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

sock.bind(('127.0.0.1',5006)) #for nazare platform

while True:
    float_data = random.uniform(1,100) #for random float
    data = struct.pack('f', float_data)
    try:
        sock.sendto(data,('127.0.0.1',5006))
        print("data was sent : original data : {}, packed : {}".format(float_data, data))
    except Exception as e:
        print("error was occured {}".format(e))
    sleep(1) # delay for 1 second

# for test one float data test logic.