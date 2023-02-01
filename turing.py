import argparse
from rot import rot
import os

implemented_cyphers = ['rot', 'subs', 'hash']

print('-'*50)
print('-'*50)
print('''        __                      
.-----.|  |.-----..-----..-----.
|__ --||  ||  -__||  -__||  _  |
|_____||__||_____||_____||   __|
                         |__|   \n''')

print('This is a cypher library by me.\nCurrently implemented cyphers: {}'.format(implemented_cyphers))
print('-'*50)

parser = argparse.ArgumentParser(description='Encrypt plaintext, decrypt ciphertext.')
parser.add_argument('method', action='store', choices=['en', 'de'])
parser.add_argument('cypher', action='store')
parser.add_argument('arg1', action='store')
args = parser.parse_args()

if args.cypher == 'rot':
    os.system('cls' if os.name == 'nt' else 'clear')
    print('-'*50)
    print('This is the rotation cypher, for now it only deals with lowercase letters')
    plain = input('Plaintext:\n')
    r = int(args.arg1)
    cypher = rot(plain, r)
    print(cypher)
    print('-'*50)
    os.system('cls' if os.name == 'nt' else 'clear')

