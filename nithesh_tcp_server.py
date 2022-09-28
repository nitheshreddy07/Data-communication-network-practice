# -*- coding: utf-8 -*-
"""
Created on Wed Feb  9 12:10:27 2022

@author: nithe
"""

import socket
from datetime import datetime, timedelta




host='Localhost'
port= 13000
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host,port))

server.listen(5)

while True:
    communication, adress = server.accept()
    print(f"connection established with {adress}")
    message= communication.recv(1024).decode('utf-8')
    
    
    print(f"message recieved from the client : {message}")
    capitalized_message=message.upper()
    updated = ( datetime.now() +
    		timedelta( hours=0 )).strftime('%H:%M:%S')

    print( updated )
    
    
    communication.send(capitalized_message.encode('utf-8'))
    print("message sent to the client")
    communication.close()
