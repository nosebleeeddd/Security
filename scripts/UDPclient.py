import socket
import sys

class MyUDPclient:
    def init(self)
        if len(sys.argv) < 3:
            print("[-] Please specify target IP and port number")
            sys.exit()
        self.host = sys.argv[1]
        try:
            self.port = int(sys.argv[2])
        except:
            print('[-] Please use integer as a port number')
            sys.exit()
        self.client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        print(f'[+] Connecting to the target: {self.host} : {self.port}')


    def run(self):
        try:
            while True:
                input_data = input("~ ")
                if input_data == 'exit':
                    break
                self.client.sendto(input_data.encode('utf-8'),(self.host, self.port))
                received_data, address_info = self.client.recvfrom(1024)
                print(f"Received from {address_info}")
                print(received_data.decode('utf-8'))

        except Exception as e:
            print("[-] Error happened: ", e)
            sys.exit()
        finally:
            self.client.close()

if __name__ == '__main__':
    client = MyUDPclient()
    client.run()
