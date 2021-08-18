#!/usr/bin/env python3
# This script requires the caesar_decrypt function
"""
This is a script ment to be run in the command line with one keyword argument, one argument and one optional flag.
hacker_caecar.py --wordlist=<PATH TO WORDLIST> <PATH TO  CIPHERED TEXT> [opt -v]

The script loops through the length of the alphabet trying to decrypt
the ciphered text by creating a list of words from the cyphered text 
and matching the words in the wordlist. If there is a match
it returns with a key and clear text.

opt flags:
-v             Verbose    (verbose mode)
"""



import sys, pathlib
from caesar import caesar, caesar_decrypt

verbose = False


opts = [opt for opt in sys.argv[1:] if opt.startswith("-")]
argv = {arg for arg in sys.argv[1:] if not arg.startswith("-")}


# Define global variables
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZÆØÅ"
controller_text = list()
args = {}
cipher_file = ''


# Get commandline arguemtns and parse them into a dictionary.
def argparser():
    global verbose
    global cipher_file
    if len(sys.argv) < 2:
        print('missing 1 argument > ripper.py --wordlist=<wordlist.txt>')
            
    else:
        try:
            for opt in opts:
                if opt.startswith('--'):
                    key, value = opt.split("=")
                    args[key] = value
             
                if opt == '-v':
                    verbose = True
            
                if "--wordlist" in args.keys():
                # if keyword --wordlist in arguments, 
                # open wordlist and generate a list of words.
                    path = pathlib.Path(args["--wordlist"]) # get absolut path
                    with open(path, 'r') as wordlist:
                        for word in wordlist.readlines():
                            controller_text.append(word.strip())
                            
            for arg in argv:
                path = pathlib.Path(arg) # get absolut path
                with open(path, 'rb') as cipher:
                    cipher_file = cipher.read().decode("UTF-8")
                    print(cipher_file)
                        
        except KeyboardInterrupt as err:
            print(err)
        
        except ValueError as val_err:
            print(val_err)
            print('ripper.py --wordlist=<wordlist.txt>')
        
        except FileNotFoundError as fnf_error:
            print(fnf_error)
        

def hacker(ciphertext):
    # bruteforce the ciphertext by comparing with words in the file
    # passed in as the --wordlist argument.
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
                        exit()
                    else:
                        continue
                else:
                    pass
            else:
                pass
                
        if verbose == True:
            print(f'Tried with key: {_} -\t{_plaintext}')
            
    print(f'No match found!')
    print('press ctrl+c to exit\n')



if __name__=='__main__':
    try:
        argparser()
        if cipher_file != '':
            hacker(cipher_file) 
        else:
            hacker(input('Past in the ciphered text: '))
   

    except KeyboardInterrupt:
        print('Program exited\n')
        sys.exit()
            
