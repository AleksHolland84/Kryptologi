#!/bin/bash

# SCRIPT TO ENCRYPT A TEXTFILE AND SAVE  A HASH OF THE ENTERED PASSWORD
# Use filename as argument

# Check if filename argument is provided
if [ -z "$1" ]; then
    echo "Usage: $0 <filename>"
    exit 1
fi

# Prompt the user for a password
echo "Enter password:"
read -s password

# Generate a hash of the password
hash=$(echo -n "$password" | sha256sum | awk '{print $1}')

# Save the hash to a file
echo "$hash" > password.hash

# Use the password to encrypt the file
echo -n "$password" | openssl enc -aes-256-ctr -pbkdf2 -e -a -in "$1" -out encrypted.txt -pass stdin

# Clear the password variable
unset password
