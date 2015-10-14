__author__ = 'besimaltnok'

import socket
from time import time
import multiprocessing

port_list = [25, 80, 81, 8080, 22, 21, 445, 139, 3306]


start  = time()
def portscan(port):
    try:
        host = "216.58.208.110"
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1000)
        con = s.connect((host, port))
        print('%d:OPEN' %(port))
    except:
        pass

if __name__ == '__main__':
    pool = multiprocessing.Pool(processes=multiprocessing.cpu_count()*10)
    t = pool.map(portscan, port_list)

