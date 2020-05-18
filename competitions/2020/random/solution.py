#import os
import socket
from caesarcipher import CaesarCipher
cache_file = open('cache.txt','a+')

host = '212.47.229.1'
port = 33002

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host,port))
banner = s.recv(167)
dd = {}

f = open('keys.txt','r')        

for line in f.readlines():
    split = line.strip().split(' ')
    dd[split[0]] = split[1]                
        
while True:
    mes = s.recv(100).decode()    
    if 'Bad answer' in mes:
        break    
    
    else:    
        a = mes.split(' ',1)[1].strip().split('\n')[0]
        print(a)
        
        #print(mes)
        if a.strip() in dd.keys():
            print(a)
            s.send(a + '\n')
        #print(mes + " " + + "\n")
        
    
