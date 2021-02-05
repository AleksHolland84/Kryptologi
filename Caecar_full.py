#!/usr/bin/env python3
# uses the Caesar cipher to encrypt a text


def caesar(plaintext, cipherkey ):

    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZÆØÅ"
    plaintext = plaintext.upper()
    ciphertext = ""

    # shift each letter in the plain text by the value of 'cipherkey'
    for i in plaintext:
        if i not in alphabet:
            ciphertext = ciphertext + i
        else:
            idx = alphabet.index(i)

            # wrap around at top on encrypt
            idx =  (idx + cipherkey) % len(alphabet) 

            # prevent underflow on decrpt
            if (idx<0): idx += len(alphabet)

            # apply shift to the character        
            ciphertext = ciphertext + alphabet[idx]

    return(ciphertext)
    
# This is a decrypt function to the Caesar_cipher script. 

def caesar_decrypt(ciphertext, cipherkey):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZÆØÅ"
    ciphertext = ciphertext.upper()
    plaintext = ""

    # shift each letter in the plain text by the value of 'cipherkey'
    for i in ciphertext:
        if i not in alphabet:
            plaintext = plaintext + i
        else:
            idx = alphabet.index(i)

            # wrap around at top on encrypt
            idx =  (idx - cipherkey) % len(alphabet) 

            # prevent underflow on decrpt
            if (idx<0): idx += len(alphabet)

            # apply shift to the character        
            plaintext = plaintext + alphabet[idx]

    return(plaintext)
 
 
if __name__=='__main__':
    while True:
        try:
            action = input('Encrypt(e) | decrypt(d)')
            if action == 'e' or 'd':
                if action == 'e':
                    plaintext = input('Write your text: ')
                    key = int(input("key number: "))
                    ciphertext = caesar(plaintext, key)
                    print(ciphertext)
                elif action == 'd':
                    ciphertext = input('Write your ciphered text: ')
                    key = int(input("key number: "))
                    plaintext = caesar_decrypt(ciphertext, key)
                    print(plaintext)
            else:
                print('You have to type e for encrypt or d for decrypt')
        
        except KeyboardInterrupt:
            print('Program exited')

