import socket 
import select 
import sys
#import threading
import multiprocessing
message=""
'''
if len(sys.argv) != 4: 
    print("Correct usage: script, IP address, port number, username")
    exit()
'''     
IP_address = str("192.168.1.4") 
Port = int(1123) 
username = str("mobileuser")
  
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.connect((IP_address, Port))

def mainfunc():
    while True:
        #global meask_for_userinputssage
        sockets_list = [sys.stdin, server]
        #username = sys.argv[3]
        x=0
        read_sockets,write_socket, error_socket = select.select(sockets_list,[],[])
        for socks in read_sockets:
            #top.update()
            if socks == server: 
                message = socks.recv(2048)
                check="UPD4T3 " in message.decode()
                if check == True:
                    x=x+1
                else: 
                    print(message.decode()) 
            else:
                print("NOTATALL\n") 
                message = "<"+username+">"+" "+sys.stdin.readline() 
                server.send(str.encode(message))
                #top.update() 
                sys.stdout.write(message) 
                sys.stdout.flush()
     

mainfunc()
   
server.close()
