#!/usr/bin/python3
# Builtins
import os
import glob
from sys import argv

# Settings
dry_run = True  # For live execution set dry_run to False.
path = ''  # Empty string corresponds to current working directory.
# path = '/path/to/target/directory/'  # Set absolute path to target directory, don't forget to include trailing '/'.
search_param = '*'  # Define bash style search parameter ('*.jpg', '*.png') etc.
count = 1  # Setting c to 0 will begin prefix with '00', 1 results in '01' etc.


def append_prefix(path, count, item):
    """Takes an absolute path to a file and prefixes said file with an integer

    Type:
        Function

    Args:
        path  (str object, required) string object
        count  (int object, required) integer to be prefixed to file
        item  (str object, required) name of file to be prefixed

    Returns:
        string object (str): absolute path to file modified with integer prefix
    """
    # Tests
    if type(path) is not str or type(item) is not str:
        raise TypeError('path and item arguments must be type str')

    if path[-1] is not '/':
        raise ValueError('Trailing "/" expected at end of path argument')

    if type(count) is not int:
        raise TypeError('count argument must be type int')

    if count < 0:
        raise ValueError('count argument value cannot be less than 0')

    # Add '0' to prefix if single digit.
    if len(str(count)) < 2:
        return '{}0{}_{}'.format(path, str(count), item.split('/')[-1])
    else:
        return '{}{}_{}'.format(path, str(count), item.split('/')[-1])


def main(argv, count):
    """Executes main script functionality

    Type:
        Function

    Args:
        argv  (list object, required) list object
        count  (int object, required) integer to be prefixed to file

    Returns:
        None
    """
    # # os.listdir does not return absolute path which is required by os.path.getctime function in sorted(key=).
    # lst = sorted(os.listdir(path), key=os.path.getctime)

    # glob module does return the absolute path. os.path.getctime orders files by creation time, oldest first.
    lst = sorted(glob.glob(path + search_param), key=os.path.getctime)

    for item in lst:

        # Only rename files that do not match name of this script.
        if argv[0].split('/')[-1] not in item:

            # Preview changes if dry_run is True.
            if dry_run:
                print(append_prefix(path, count, item))
            else:
                os.rename(item, append_prefix(path, count, item))

            count += 1


if __name__ == '__main__':
    main(argv, count)
