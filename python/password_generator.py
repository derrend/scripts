##Python 3.10.6

## Generate determanistic password from seed phrase.
import random
import string
from sys import argv

if len(argv) != 3:
    print('Please supply a password length and seed.')
    exit(1)

try:
    password_length = int(argv[1])

except ValueError:
    print('Password length must be an intiger.')
    exit(1)

seed_phrase = argv[2]
password = ''

random.seed(seed_phrase)
for x in range(password_length):
    password += random.choice(string.ascii_letters + string.digits)

print(password)
