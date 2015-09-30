__author__ = 'besimaltnok'

from scapy.all import *
 
hidden_ssid = []
find_ssid   = []

def FindHiddenSSID(pkt):
	if pkt.type == 0 and pkt.subtype == 8 :
		if not pkt.info:
			if pkt.addr2 not in hidden_ssid:
				hidden_ssid.append(pkt.addr2)
				
	elif pkt.haslayer(Dot11ProbeResp) and pkt.addr2 in hidden_ssid:
	    if pkt.addr2 not in find_ssid:
	      find_ssid.appen(pkt.addr2)
			  print pkt.addr2, pkt.info

sniff(iface='wlan0mon',count=9999999,prn=FindHiddenSSID)
