__author__ = 'besimaltnok'

AP_mac = '_AP_MAC_'

from scapy.all import *

def ArpPoisoning(pkt):
	if pkt.haslayer(ARP):
		if pkt.op == 2:
			srchw = pkt.hwsrc
			srcip = pkt.psrc
			if srchw == AP :
				print 'Detect ARP Poisoning !\n'
				print 'IP  : ', srcip
				print 'MAC : ', srchw

sniff(iface='wlan0', prn=ArpPoisoning)
