#!/usr/bin/env python3
import sys
import socket
from scapy.all import *

if len(sys.argv) < 2:
    print('Please specify Interface to sniff')
    sys.exit()

interface = sys.argv[1]
sniffer_socket = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(3))
sniffer_socket.bind((interface, 0))
try:
    while True:
        raw_data, addr = sniffer_socket.recvfrom(65535)
        packet_data = Ether(raw_data)
        print(packet_data.summary())
except KeyboardInterrupt:
    print("Exiting Program.")
    sniffer_socket.close()
except Exception as e:
    print(f"[-] Something went wrong: {e}")
    sys.exit()



