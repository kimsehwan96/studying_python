import socket



def get_info():
    host_name = socket.gethostname()
    host_ip = socket.gethostbyname(host_name)

    print(host_ip, host_name)

if __name__ == '__main__':
    get_info()


def get_remote_info():
    remote_host = 'www.google.com'
    try:
        print('ip address %s' %(socket.gethostbyname(remote_host))