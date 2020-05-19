import sys
import argparse
import subprocess
from subprocess import PIPE, Popen

def decrypt(command):
    proc = subprocess.Popen(str(command), stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    (out, err) = proc.communicate()
    return err

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-o', type=str, dest='outfile', help='output file for decrypted RSA key', metavar='outfile', default='out.key')
    parser.add_argument('-k', type=str, dest='key', help='input file containing RSA key to crack', metavar='key', required=True)
    parser.add_argument('-w', type=str, dest='wordlist', help="wordlist to crack against", metavar='wordlist', required=True)

    args = parser.parse_args()
    wordlist = [line.strip() for line in open(args.wordlist)]
    
    for word in wordlist:
        cmd = 'openssl rsa -in ' + args.key + ' -out ' + args.outfile + ' -passin pass:' + word
        res = decrypt(cmd)
        if res.startswith(b'writing'):
                print('Key: ' + word + '\nDecrypted key saved to ' + args.outfile)                
                return

    print('Key not found')
    return

if __name__ == '__main__':
    main()
