#!/usr/bin/python3
import os

path = '.'  # Target folder

c = 1
for i in sorted(os.listdir(path), key=os.path.getctime):  # Order by date, oldest first.
    if len(str(c)) < 2:
        os.rename(i, '0{}_{}'.format(str(c), i))
    else:
        os.rename(i, '{}_{}'.format(str(c), i))

    c += 1
