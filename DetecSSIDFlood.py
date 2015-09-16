__author__ = 'besimaltnok'

import sys, os
from scapy.all import *

ssid_list = []
ap_list   = []
fake =  []
def DetectSSIDFlood(pkt):

	if pkt.type == 0 and pkt.subtype == 8:
		ssid  = pkt.info
		bssid = pkt.addr2 
		#~ print bssid,ssid
		if bssid  in ap_list:
			if ssid not in ssid_list:
				fake.append(1)
				if len(fake) >= 5 :
					print "*-* Launched SSID Flood *-*  :"
					print "This MAC address launched ssid flood : ", bssid
					exit()

		else:
			ap_list.append(bssid)
			if ssid not in ssid_list:
				ssid_list.append(ssid)	


sniff(iface='wlan6mon',prn=DetectSSIDFlood)
