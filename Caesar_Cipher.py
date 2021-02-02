# uses the Caesar cipher to encrypt a text


def caesar(plaintext, cipherkey ):

    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZÆØÅ"
    plaintext = plaintext.upper()
    ciphertext = ""

    # shift each letter in the plain text by the value of 'cipherkey'
    for i in plaintext:
        if i == " ":
            ciphertext = ciphertext + " "
        else:
            idx = alphabet.index(i)

            # wrap around at top on encrypt
            idx =  (idx + cipherkey) % len(alphabet) 

            # prevent underflow on decrpt
            if (idx<0): idx += len(alphabet)

            # apply shift to the character        
            ciphertext = ciphertext + alphabet[idx]

    return(ciphertext)
    
    
if __name__=='__main__':
    plaintext = input('Write your text: ')
    key = int(input("key number: "))
    ciphertext = caesar(plaintext, key)
    print(ciphertext)
