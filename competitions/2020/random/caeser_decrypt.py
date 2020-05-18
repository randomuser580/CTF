#import os
import socket
from caesarcipher import CaesarCipher
cache_file = open('cache.txt','a+')

host = 'misc.2020.chall.actf.co'
port = 20300

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host,port))
        
while True:
    mes = s.recv(100).decode()    
    if 'Bad answer' in mes:
        break    
    
    else:    
        a = mes.split(' ',1)[1].strip().split('\n')[0]
        print(a)
        
        #print(mes)
        #print(mes + " " + + "\n")
        
    
