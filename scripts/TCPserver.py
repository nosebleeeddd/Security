#!/usr/bin/env python3

import socket
import threading
import sys

class MyTCPServer:
    def __init__(self) -> None:
        if len(sys.argv) < 2:
            print(f"Example Usage: {sys.argv[0]} port number")
            sys.exit()
        try:
            self.port = int(sys.argv[1])
        except:
            print("[-] Please use integer as port number")
            sys.exit()
        try:
            self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            self.server_socket.bind(('0.0.0.0', self.port))
            self.server_socket.listen(5)
            print(f"[+] The server starts listening on port{self.port}")
        except Exception as e:
            print(f"[-] Something is wrong: {e}")
            sys.exit()

    def client_handler(self,client_socket,client_addr):
        while True:
            input_data = input(f"{client_addr}")
            if input_data == 'q':
                break
            client_socket.send((input_data+'\n').encode('utf-8'))
            recv_data = client_socket.recv(4096)
            print(recv_data.decode('utf-8'))
        client_socket.close()


    def run(self):
        while True:
            try:
                client_socket, client_addr = self.server_socket.accept()

                t = threading.Thread(target=self.client_handler, args=(client_socket, client_addr))
                t.start()
            except KeyboardInterrupt:
                print('\n'+'[-] Closing program')
                self.server_socket.close()
                sys.exit()

if __name__ == '__main__':
    server = MyTCPServer()
    server.run()
