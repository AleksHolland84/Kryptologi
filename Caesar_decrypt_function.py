# This is a decrypt function to the Caesar_cipher script. 

def caesar_decrypt(ciphertext, cipherkey):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZÆØÅ"
    ciphertext = ciphertext.upper()
    plaintext = ""

    # shift each letter in the plain text by the value of 'cipherkey'
    for i in ciphertext:
        if i == " ":
            plaintext = plaintext + " "
        else:
            idx = alphabet.index(i)

            # wrap around at top on encrypt
            idx =  (idx - cipherkey) % len(alphabet) 

            # prevent underflow on decrpt
            if (idx<0): idx += len(alphabet)

            # apply shift to the character        
            plaintext = plaintext + alphabet[idx]

    return(plaintext)
