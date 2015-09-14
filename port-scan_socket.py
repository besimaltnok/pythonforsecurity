__author__ = 'besimaltnok'


import socket
for port in range(1,1024):
    try:
        host = "192.168.2.177"
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1000)
        con = s.connect((host, port))
        print('%d:OPEN' %(port))
    except:continue
