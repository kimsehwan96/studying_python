import random
from time import sleep
from struct import pack, unpack


while True:


    values = [random.randint(1, 1000) for x in range(40)]
    binary_data = pack('h' * len(values), *values)
    print(binary_data)
    binary_unpack = unpack('h' * len(values), binary_data)
    print(binary_unpack)
    sleep(1)
