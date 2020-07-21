import socket

import main

class Receive():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def __init__(self, host = '', port = 0):
        self.sock.bind((host, port))
        self.sock.listen(10)

    def m_loop(self):
        while True:
            try:
                client, input = self.sock.accept()
                result = main.work(input)
            except KeyboardInterrupt:
                self.sock.close()
                break
            except Exception as e:
                client.sendmsg(e.__str__)
            else:
                if(result != None):
                    client.sendfile(result)
                # print(f"{result.decode('utf-8')}")

if  __name__ == '__main__':
    recv = Receive(host='localhost', port=8888)
    recv.m_loop()