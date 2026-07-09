#!/usr/bin/env python3

import subprocess
import sys
import argparse

class MyMacChanger:
    def __init__(self):
        parameters = self.get_params()
        self.interface, self.mac_addr = parameters

    def get_params(self):
        parser = argparse.ArgumentParser(f'Usage: ./{sys.argv[0]} -i interface -m mac_addr')
        parser.add_argument('-i', '--interface', dest='interface', type=str, help='Specify interface to change MAC')
        parser.add_argument('-m', '--mac_addr', dest='mac_addr', type=str, help='Specify new MAC address')
        args = parser.parse_args()
        if args.interface is None or args.mac_addr is None:
            print(parser.usage)
            sys.exit()
        return args.interface, args.mac_addr


    def run(self):
        try:
            subprocess.call(['ifconfig', self.interface, 'down'])
            subprocess.call(['ifconfig', self.interface, 'hw', 'ether', self.mac_addr])
            subprocess.call(['ifconfig', self.interface, 'up'])
        except Exception as e:
            print(f'[-] Something is wrong! {e}')
            sys.exit()

if __name__ == '__main__':
    mac_changer = MyMacChanger()
    mac_changer.run()
