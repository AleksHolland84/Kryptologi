"""
This function take one argument which is the ciphered text. 
It then loops through the length of the alphabet trying to decrypt
the ciphered text by creating a list of words in the cyphered text 
and matching the words in the controller_text. If there is a match
it returns with a key and plain text.
"""
# This function requires the caesar_decrypt function which also requeres a global alphabet

# Define global variables
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZÆØÅ"
controller_text = list()


# Open wordlist.txt and generate a list of words.
with open('wordlist.txt', 'r') as wordlist:
    for word in wordlist.readlines():
        controller_text.append(word.strip())
        

def hacker(ciphertext):
    for _ in range(0,30):
        _plaintext = caesar_decrypt(ciphertext, _)
        cipher_word = _plaintext.split(' ')
        controller = [wd.upper() for wd in controller_text]
        for word in cipher_word:
            if len(word) > 3:
                if word in controller:
                    print(f"Match found! - word: {word}")
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

