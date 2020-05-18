def decrypt(text, key):
    keylen = len(key)
    keyPos = 0
    decrypted = ""
    for x in text:
        keyChr = key[keyPos]
        newChr = ord(x)
        newChr = chr((newChr - ord(keyChr)) % 255)
        decrypted += newChr
        keyPos += 1
        keyPos = keyPos % keylen
    return decrypted

#t = open('out.txt').readlines()[0]
t = open('check.txt').readlines()[0]
k = open('passwordreminder.txt').readlines()[0]
#print(t)
print(decrypt(k,t))
#output from check.txt as text and key as password - decrypt - oceZPpeXcCW
