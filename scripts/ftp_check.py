#!/usr/bin/env python3

import ftplib
import sys


class FTPanonymousCheck:
    def __init__(self) -> None:
        if len(sys.argv) < 3:
            print(f'Example Usage: ./{sys.argv[0]} target port_number')
            sys.exit()

        self.target = sys.argv[1]

        try:
            self.port = int(sys.argv[2])
        except:
            print("[-] port must be an integer!")
            sys.exit()

    def run(self):
        try:
            self.ftp_client = ftplib.FTP()
            self.ftp_client.connect(host=self.target, port=self.port)
            print("[+] Connected Successfully")
        except Exception as e:
            print(f"[-] something went wrong {e}")
            sys.exit()

        try:
            self.ftp_client.login(user='anonymous')
            print(f"[+] the target allows anonymous login: {self.target}:{self.port}")
        except Exception as e:
            print(f"[-] something went wrong {e}")
            sys.exit()


if __name__ == '__main__':
    client = FTPanonymousCheck()
    client.run()
