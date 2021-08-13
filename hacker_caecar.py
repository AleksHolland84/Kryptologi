"""
This function take one argument which is the ciphered text. 
It then loops through the length of the alphabet trying to decrypt
the ciphered text by creating a list of words in the cyphered text 
and matching the words in the controller_text. If there is a match
it returns with a key and plain text.
"""
# This function requires the caesar_decrypt function which also requeres a global alphabet

def hacker(ciphertext):
    controller_text = "HEJ HALLO MED SKAL HISLEN test i"
    for _ in range(0,29):
        _plaintext = caesar_decrypt(ciphertext, _)
        cipher_word = _plaintext.split(' ')
        for word in cipher_word:
            if len(word) > 2:
                if word in controller_text.upper():
                    print("Match found!")
                    print(f'Decrypted with key: {_ }: {_plaintext}')
                    ack = input('Is this correct? (y)es, (n)o: ')
                    if ack == 'y':
                        return _
                    else:
                        continue
                else:
                    pass 
            else:
                pass
        print(f'Tried with key: {_} -   {_plaintext}')
