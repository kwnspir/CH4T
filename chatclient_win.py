import socket 
import select 
import sys 
import tkinter as tk
import msvcrt
#import threading
import multiprocessing
message=""
'''
79.130.219.238
if len(sys.argv) != 4: 
    print("Correct usage: script, IP address, port number, username")
    exit()
'''     
IP_address = str("192.168.1.177") 
Port = int(1123) 
username = str("GOD")

def click():
    global message
    txttt.insert(tk.INSERT,"\n"+"<" + username + "> " + enttt.get())
    server.send(str.encode("<" + username + "> " + enttt.get()))
    enttt.delete(0, 'end')


def alt_click(event):
    global message
    txttt.insert(tk.INSERT,"\n"+"<" + username + "> " + enttt.get())
    server.send(str.encode("<" + username + "> " + enttt.get()))
    enttt.delete(0, 'end')
  
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.connect((IP_address, Port))

top=tk.Tk()
top.geometry("800x600")
buttt=tk.Button(top,text="Send!",command=click)
enttt=tk.Entry(top,width=650,bg="navy",fg="orange red")
txttt=tk.Text(top,bg="black",fg="green3")
buttt.place(height=50, width=100, x=700, y=550)
enttt.place(width=650, x=0, y=550)
txttt.place(width=800 , height=550)

def mainfunc():
    while True:
        top.update()
        #global meask_for_userinputssage
        sockets_list = [sys.stdin, server]
        #read_sockets,write_socket, error_socket = select.select(sockets_list,[],[])
        ready_to_read = select.select([server], [], [], 1)[0]
        if msvcrt.kbhit(): ready_to_read.append(sys.stdin)

        for socks in ready_to_read:
            #top.update()
            if socks == server: 
                message = socks.recv(2048)
                check="UPD4T3 " in message.decode()
                if check == True:
                    print("UP\n")
                else:
                    print("NOTUP\n")
                    txttt.insert(tk.INSERT,"\n"+message.decode()) 
                    #print(message.decode()) 
            else:
                print("NOTATALL\n") 
                #message = "<"+username+">"+" "+sys.stdin.readline() 
                server.send(str.encode(enttt.get()))
                #top.update() 
                #sys.stdout.write(message) 
                sys.stdout.flush()

    server.close()

top.bind('<Return>', alt_click)
mainfunc()              


