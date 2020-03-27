import socket


sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
while True:
    sock.sendto("Hi".encode(), ('192.168.0.1',2012))