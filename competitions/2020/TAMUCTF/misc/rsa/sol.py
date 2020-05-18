import sys
import socket

def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors


host = 'challenges.tamuctf.com'
port = 8573

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host,port))
banner = s.recv(324).decode().strip()
#carriage return bc newline wasnt getting any output

s.sendall(b'\r\n')

while True:

    mes = s.recv(100).decode().strip()

    if 'Good Job' in mes:
        mes = s.recv(100).decode().strip()
        print(mes)
    
    factors = prime_factors(int(mes))
    factor_str = ((str(factors[0]) + " " + str(factors[1]) + "\n"))
    print(factor_str)
    s.sendall(factor_str.encode())
    



