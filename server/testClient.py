from socket import *
import os
import sys

def recieve():
    clientSock = socket(AF_INET, SOCK_STREAM)
    clientSock.connect(('127.0.0.1', 8080))

    print("connect complete")
    filename = input('select filename : ')
    clientSock.sendall(filename.encode('utf-8'))

    data = clientSock.recv(2048)
    data_transfered = 0

    if not data:
        print('i dont have a file')
        sys.exit()
    nowdir = os.getcwd()
    with open(filename, 'wb') as f:
        try:
            data = f.read(2048)
            while data:
                data_transfered += connectionSock.send(data)
                data = f.read(2048)
        except Exception as ex:
            print(ex)
    print('file %s recieve complete. size %d' %(filename, data_transfered))
