__author__ = 'besimaltnok'

import socket
sniff = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, 3)
sniff.bind(("wlan0mon", 0x0003))
ap_list =[]
