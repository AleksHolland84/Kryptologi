# uses the Caesar cipher to encrypt a text

# Define global variables
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZÆØÅ" #Danish
#alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" #English

controller_text = ['af', 'fordi', 'kom', 'os', 'alle', 'fra', 'kommer', 'over', 'alt', 'fri', 
    'kun', 'på', 'andre', 'få', 'kunne', 'sagde', 'at', 'gik', 'lang', 'se', 'blev', 'glad', 
    'lidt', 'selv', 'bliver', 'godt', 'lige', 'sidste', 'bort', 'ham', 'lille', 'sig', 'da', 
    'han', 'løb', 'sin', 'dag', 'hans', 'man', 'sine', 'de', 'har', 'mange', 'skal', 'dem', 'havde', 
    'med', 'skulle', 'den', 'have', 'meget', 'små', 'der', 'hele', 'men', 'som', 'deres', 'hen', 'mere', 
    'stor', 'det', 'hende', 'mig', 'store', 'dig', 'her', 'min', 'så', 'dog', 'hjem', 'mod', 'tid', 'du', 
    'hun', 'mon', 'til', 'efter', 'hvad', 'må', 'tog', 'eller', 'hver', 'ned', 'ud', 'en', 'hvis', 'nej', 
    'under', 'end', 'hvor', 'noget', 'var', 'er', 'igen', 'nok', 'ved', 'et', 'ikke', 'nu', 'vi', 'far', 
    'ind', 'når', 'vil', 'fik', 'jeg', 'og', 'ville', 'fin', 'jer', 'også', 'være', 'for', 'jo', 'om', 'været', 
    'forbi', 'kan', 'op', 'år.']


# Functions
def caesar(plaintext, cipherkey ):
    """ecnrypt a plane text with the Caesar cipher"""
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

    return(ciphertext)



def caesar_decrypt(ciphertext, cipherkey):
    """This is a decrypt function to the Caesar_cipher script."""
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




def hacker(ciphertext):
    """ This function take one argument which is the ciphered text. 
    It then loops through the length of the alphabet trying to decrypt
    the ciphered text by creating a list of words in the cyphered text 
    and matching the words in the controller_text. If there is a match
    it returns with a key and plain text. """
    for _ in range(0,30):
        _plaintext = caesar_decrypt(ciphertext, _)
        cipher_word = _plaintext.split(' ')
        controller = [wd.upper() for wd in controller_text]
        for word in cipher_word:
            if len(word) > 2:
                if word in controller:
                    print(f"Match found! - word: {word}")
                    print(f'Decrypted with key: {_} : {_plaintext}')
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
        
        

if __name__=='__main__':
    while True:
        try:
            action = input('Encrypt(e) | decrypt(d)')
            if action == 'e' or action == 'd':
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
            elif action == 'f':
                hacker(input('Past in the ciphered text: '))
            else:
                print('You have to type e for encrypt or d for decrypt')

        except KeyboardInterrupt:
            print('Program exited')
