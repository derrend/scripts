#!/usr/bin/python3
##Python 3.10.6

## Generate determanistic password from seed phrase.
import random
import string
from sys import argv

def generate_password(seed_phrase, password_length):

    random.seed(seed_phrase)
    password = ''

    for x in range(password_length):
        password += random.choice(string.ascii_letters + string.digits)

    return password

## Uncomment to enable test mode.
# test_seed = 'test16749442'

if len(argv) == 2:  ## Test mode.

    try:
        print(generate_password(test_seed, int(argv[1])))
        exit(0)

    except ValueError:
        print('Password length must be an intiger.')
        exit(1)

    except NameError:
        print('Test mode disabled.')
        exit(1)

if len(argv) != 3:
    print('Please supply a password length and seed.')
    exit(1)

try:
    print(generate_password(argv[2], int(argv[1])))
    exit(0)

except ValueError:
    print('Password length must be an intiger.')
    exit(1)
