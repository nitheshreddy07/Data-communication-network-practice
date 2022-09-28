# -*- coding: utf-8 -*-
"""
Created on Wed Feb  9 12:24:51 2022

@author: nithe
"""

import socket
from datetime import datetime, timedelta

host='Localhost'
port=13000
socket= socket.socket(socket.AF_INET,socket.SOCK_STREAM)

socket.connect((host,port))

sentence = input("Enter a lower case string : ")

socket.send(sentence.encode('utf-8'))

modified_message=socket.recv(1024)

print("message recieved from server : ")
print(modified_message.decode('utf-8'))
updated = ( datetime.now() +
		timedelta( hours=0 )).strftime('%H:%M:%S')

print( updated )
socket.close()
