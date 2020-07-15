import socket

class Receive():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def __init__(self, host = '', port = 0):
        self.sock.bind((host, port))

    def m_loop(self):
        while True:
            try:
                result = self.sock.recv(1024)
            except KeyboardInterrupt:
                self.sock.close()
                break
            else:
                print(f"{result.decode('utf-8')}")

if  __name__ == '__main__':
    recv = Receive(host='localhost', port=8888)
    recv.m_loop()