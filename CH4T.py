import socket 
import select 
import sys
import msvcrt
message=""

#79.130.219.238
'''
if len(sys.argv) != 4: 
    print("Correct usage: script, IP address, port number, username")
    exit()
     
IP_address = str(sys.argv[1]) 
Port = int(sys.argv[2]) 
username = str(sys.argv[3])
'''
IP_address=str(input("IP : "))
Port = int(input("Port : "))
username = str(input("USERNAME : "))

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    server.connect((IP_address, Port))
except:
    raise

def mainfunc():
    while True:
        sockets_list = [sys.stdin, server]
    
        
        ready_to_read = select.select([server], [], [], 1)[0]
        if msvcrt.kbhit(): ready_to_read.append(sys.stdin)
    
        for socks in ready_to_read: 
            if socks == server:
                message = socks.recv(2048) 
                print(message)
            else: 
                message = sys.stdin.readline() 
                server.send(str.encode(username+" "+message+"&")) 
                sys.stdout.write("<You> ") 
                sys.stdout.write(message) 
                sys.stdout.flush() 


mainfunc()
   
server.close()
