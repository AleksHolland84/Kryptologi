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

            # apply shift to the character        
            ciphertext = ciphertext + alphabet[idx]

    return ciphertext
    
    
if __name__=='__main__':
    plaintext = input('Write your text: ')
    key = int(input("key number: "))
    ciphertext = caesar(plaintext, key)
    print(ciphertext)
