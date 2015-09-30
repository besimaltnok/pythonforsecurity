__author__ = 'besimaltnok'
__author__ = 'octosec'

from scapy.all import *

ap_list       = []
wp_mac = '00:13:37'

def DetectPineapple(pkt) :

	if pkt.haslayer(Dot11) :
		
		if pkt.type == 0 and pkt.subtype == 8 or pkt.subtype == 5:
		
			ssid  = pkt.info
			bssid = pkt.addr2
			if  wp_mac in bssid  and (pkt.addr2 not in ap_list) :
				
				ap_list.append(pkt.addr2)
				print "Detect Wifi - Pineappple"

sniff(iface='wlan0mon', prn=DetectPineapple)
