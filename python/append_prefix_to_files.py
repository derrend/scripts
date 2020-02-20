#!/usr/bin/python3
# Builtins
import os
import glob
from sys import argv


def help_text():
    text = '''
    Keywords:
    help    Displays help text

    Arguments:
    (path=os.getcwd() + '/', search_param='*', count='1', dry_run='True')
    '''
    print(text)


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
    # Add '0' to prefix if single digit.
    if len(str(count)) < 2:
        return '{}0{}_{}'.format(path, str(count), item.split('/')[-1])
    else:
        return '{}{}_{}'.format(path, str(count), item.split('/')[-1])


def main(path=os.getcwd() + '/', search_param='*', count='1', dry_run='True'):
    """Executes main script functionality

    Type:
        Function

    Args:
        argv  (list object, required) list object
        count  (int object, required) integer to be prefixed to file

    Returns:
        None
    """
    # Tests
    count = int(count)

    if dry_run.lower() not in ['true', 'false']:
        raise ValueError('{} cannot be converted into type Bool')

    dry_run = True if dry_run.lower() == 'true' else False

    if path[-1] is not '/':
        path = path + '/'

    if count < 0:
        raise ValueError('count argument value cannot be less than 0')

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
    if len(argv) is 1:
        main()

    elif len(argv) > 1 and argv[1].lower() == 'help':
        help_text()

    elif len(argv) is 2:
        main(argv[1])

    elif len(argv) is 3:
        main(argv[1], argv[2])

    elif len(argv) is 4:
        main(argv[1], argv[2], argv[3])

    else:
        raise ValueError('Too many arguments, did you remember to quote your wildcard? (\'*\')')
