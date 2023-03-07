## Generate determanistic password from seed phrase.

import random
import string

seed_phrase = 'insert_seed_phrase_here'
password_length = 64
password = ''

random.seed(seed_phrase)
for x in range(64): password = password + random.choice(string.ascii_letters + string.digits)

print(password)
