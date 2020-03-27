import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('192.168.0.5', 2012))

data, addr = sock.recvfrom(1024)

print("recevied data : ", data.decode())