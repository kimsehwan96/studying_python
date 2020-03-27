import socket

# making a socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

sock.bind(('127.0.0.1',8080))

# maximum data size 200byte
data, addr = sock.recvfrom(200)

#test

print(" recevied dta: ", data.decode())
print("Send Client IP : ", addr[0])
print("Send Client port : ", addr[1])
