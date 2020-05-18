#import os
import socket
from caesarcipher import CaesarCipher
cache_file = open('cache.txt','a+')

host = '212.47.229.1'
port = 33002

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host,port))
banner = s.recv(167)

while True:
    mes = s.recv(100).decode()    
    if 'Bad answer' in mes:
        cache_file.close()        
        xd = open('cache.txt','r').readlines()[:-1]
        ccc = open('cache.txt','w')
        for line in xd:            
            ccc.write(line)
        break    
    
    else:    
        a = mes.split(' ',1)[1].strip().split('\n')[0]
        reply = CaesarCipher(a).cracked    
        s.send(reply + '\n')
        print(mes + " " + reply + "\n")
        cache_file.write(a + ' ' + reply + "\n")
