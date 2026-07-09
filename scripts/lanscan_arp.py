#!/usr/bin/env python3

# A HOST DISCOVERY TOOL THAT SEND ARP PACKETS
# TO IDENTIFY ALL HOSTS ON A NETWORK WITH IP AND MAC

import scapy.all as scapy

import re                               # regex

# Regular expression to recognize IPv4 addresses.
ip_add_range_pattern = re.compile("^(?:[0-9]{1,3}\.){3}[0-9]{1,3}/[0-9]*$")

# Get the address range to ARP
while True:
    ip_add_range_entered = input(
    '''Please enter the ip address and range that
    you want to send the ARP request to (ex. 192.168.1.0/24): ''')

    if ip_add_range_pattern.search(ip_add_range_entered):
        print('%s is a valid ip address range' % ip_add_range_entered)
        break
    else:
        print('invalid input')


# Try ARPing the ip address range supplied by the user.

# The arping() method in scapy creates a packet with ARP message

# sends it to the broadcast mac address ff:ff:ff:ff:ff:ff

# if valid IP address range was supplied the program
    # returns the list of all results

arp_result = scapy.arping(ip_add_range_entered)
