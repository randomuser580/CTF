import requests as req

r = req.get('https://tamuctf.com/files/3384f1ba669c21bf9c168dcb5fd8b4f3/photo.png')
print(r.content)
