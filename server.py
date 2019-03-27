#author: yue cao 59468165

import socket
import sys
import robot as ro

sk = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host = '127.0.0.1'
port =9000
sk.bind((host,port))
sk.listen(1)
while True:
    clnt,addr =sk.accept()
    print("clnt address:",addr)
    while True:
        data = clnt.recv(1024)
        if not data:
             sys.exit()
        replay=ro.res(data.decode("utf-8"))


        clnt.sendall(replay.encode("utf-8"))
clnt.close()



