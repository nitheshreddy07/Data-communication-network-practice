# -*- coding: utf-8 -*-
"""
Created on Wed Feb  2 14:36:13 2022

@author: nithe
"""
import datetime
from socket import*

serverName='localhost'
serverPort=12000
clientSocket=socket(AF_INET, SOCK_DGRAM)
while 1:
     message=input('ENTER A MESSAGE')
     print(message)
     clientSocket.sendto(message.encode(),(serverName,serverPort))
     modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
     a = datetime.datetime.now().time()
     print("message recieved from the server : ")
     print(modifiedMessage.decode())
     print(a)
     
     clientSocket.close()