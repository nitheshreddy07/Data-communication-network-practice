# -*- coding: utf-8 -*-
"""
Created on Wed Feb  2 14:47:51 2022

@author: nithe
"""
import datetime
from socket import*
serverPort = 12000
serverSocket = socket(AF_INET,SOCK_DGRAM)
serverSocket.bind(('',serverPort))
print("THE SERVER IS READY TO RECIEVE MESSAGES")

while 1:
    message,clientAddress = serverSocket.recvfrom(2048)
    print(" message recieved from server : ")
    print (message.decode())
    modifiedMessage=message.decode().lower()
    serverSocket.sendto(modifiedMessage.encode(),clientAddress)
    a = datetime.datetime.now().time()
    print('modified message send to client')
    print(a)
    
        