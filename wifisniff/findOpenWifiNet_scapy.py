__author__ = 'besimaltnok'

from scapy.all import *

open_networks = []
ap_list       = []


def FindOpenNet(pkt) :
	
	if pkt.type == 0 and pkt.subtype == 8 :
		if pkt.addr2 not in ap_list :
			ap_list.append(pkt.addr2)
			open_ssid  = pkt.info
			open_bssid = pkt.addr2
			cap = pkt.sprintf("{Dot11Beacon:%Dot11Beacon.cap%}"
								 "{Dot11ProbeResp:%Dot11ProbeResp.cap%}").split('+')

			if 'privacy' not in cap and pkt.info != '':
				print "Detect Open Network MAC Addres : %s and SSID : %s " %(open_bssid, open_ssid)  



sniff(iface='wlan0', prn=FindOpenNet)
