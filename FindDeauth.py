#!/usr/bin/env python

import os
import sys


__author__ = 'besimaltnok'

from scapy.all import *


client_file = sys.argv[1]
f           = open(client_file, "r")
file        = f.read()
clientlist  = file.splitlines()

deattack    = []  

imon = 'wlan0mon'

def FindDeauth(pkt):
  if pkt.haslayer(Dot11):
	if pkt.type == 0 and pkt.subtype == 12:
		client = (pkt.addr1).upper()
		AP     = (pkt.addr2).upper()
		if client in clientlist:
			if client not in deattack:
				deattack.append(client)
				info = "De-Attack to : " + AP + "on AP : ", client
				print info   


sniff(iface=imon , count=23232, prn=FindDeauth)
