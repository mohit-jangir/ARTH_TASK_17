import socket
import os
import time
import threading

s = socket.socket(socket.AF_INET , socket.SOCK_DGRAM)

ip = "172.31.4.105"
port = 1234
rip=input('Receiver IP is => ')
rport=int(input('Receiver Port No =>   '))

os.system("tput setaf 2")
print("\t\t\t\tMohit's Chat App...")
os.system("tput setaf 6")
print("\t\t\t\t---------------------")

s.bind((ip , port))
def a():
    while True:
        x = s.recvfrom(1024)
        if x[0].decode()=='exit' or x[0].decode()=='bye':
            os.system("tput setaf 5")
            print('\t\t\t\t\t From other Server :-  Bye-Bye\n\n\n')
            s.sendto('exit'.encode(), (rip, rport))
            os.system("tput setaf 7")
            os._exit(1)
        clientip = x[1][0]
        data = x[0].decode()
        os.system("tput setaf 3")
        print("\n\t\t\t\t\t\t\t " + clientip + ":" + data)
        os.system("tput setaf 6")

        #time.sleep(120)
        #print(os.system(data))

def b():
    while True:
        x = s.recvfrom(1024)
        if x[0].decode()=='exit' or x[0].decode()=='bye':
            os.system("tput setaf 5")
            print('\t\t\t\t\tFrom other Server :-  Bye-Bye')
            s.sendto('exit'.encode(), (rip, rport))
            os.system("tput setaf 7")
            os._exit(1)
        clientip = x[1][0]
        data = x[0].decode()
        os.system("tput setaf 3")
        print("\n\t\t\t\t\t\t\t " + clientip + ":" + data)
        os.system("tput setaf 6")
        #time.sleep(120)
        #print(os.system(data))

def c():
    while True:
        s = socket.socket(socket.AF_INET , socket.SOCK_DGRAM)
        os.system("tput setaf 6")
        print()
        x = input()
        os.system("tput setaf 6")
        s.sendto(x.encode(),(rip,rport))
        os.system("tput setaf 6")


x1 = threading.Thread( target=a )
x2 = threading.Thread( target=b )
x3 = threading.Thread( target=c)

x1.start()
x2.start()
x3.start()

