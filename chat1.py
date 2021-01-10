import socket
import os
import time
import threading

s = socket.socket(socket.AF_INET , socket.SOCK_DGRAM)

ip = "172.31.4.105"
port = 1234
clientip=[]
#clientport=""
#rip=input('Receiver IP is => ')
#rport=int(input('Receiver Port No =>   '))
clientport=1234

os.system("tput setaf 2")
print("\t\t\t\tMohit's Chat App...")
os.system("tput setaf 6")
print("\t\t\t\t---------------------")

s.bind((ip , port))

def a():
    while True:
        x = s.recvfrom(1024)
        #global clientip 
        cip= x[1][0]
        if cip not in clientip:
           clientip.append(cip)
        #clientport = x[1][1]
        if x[0].decode()=='exit' or x[0].decode()=='bye':
            i=clientip[0]
            #print(i)
            os.system("tput setaf 5")
            print('\t\t\t\t\t From other Server {} :-  Bye-Bye\n\n\n'.format(i))
            s.sendto('exit'.encode(), (i, clientport))
            os.system("tput setaf 7")
            os._exit(1)
        data = x[0].decode()
        os.system("tput setaf 3")
        print("\n\t\t\t\t\t\t\t " + cip  + ":" + data)
        os.system("tput setaf 6")

        #time.sleep(120)
        #print(os.system(data))

def b():
    while True:
        x = s.recvfrom(1024)
        #global clientip 
        cip= x[1][0]
        if cip not in clientip:
           clientip.append(cip)
        #clientport = x[1][1]

        if x[0].decode()=='exit' or x[0].decode()=='bye':
            i=clientip[1] 
            os.system("tput setaf 5")
            print('\t\t\t\t\tFrom other Server {} :-  Bye-Bye'.format(i))
            s.sendto('exit'.encode(), (i, clientport))
            os.system("tput setaf 7")
            os._exit(1)
        data = x[0].decode()
        os.system("tput setaf 3")
        print("\n\t\t\t\t\t\t\t " + cip  + ":" + data)
        os.system("tput setaf 6")
        #time.sleep(120)
        #print(os.system(data))

def c():
    while True:
        s = socket.socket(socket.AF_INET , socket.SOCK_DGRAM)
        os.system("tput setaf 6")
        #print(clientip)
        print()
        x = input()
        print()
        #print("\n")
        #print(clientip)
        os.system("tput setaf 6")
        for i in clientip:
          s.sendto(x.encode(),(i,clientport))
        #s.sendto(x.encode(),(clientip1,clientport))
        os.system("tput setaf 6")


x1 = threading.Thread( target=a )
x2 = threading.Thread( target=b )
x3 = threading.Thread( target=c)

x1.start()
x2.start()
x3.start()

