'''
Print directory tree.

Summary
-------
This script prints the structure of a directory.
The output mimics the Unix tree command.

Example
-------
python challenges/tree.py .

'''

from argparse import ArgumentParser, Namespace
from pathlib import Path


MIDDLE = '├── '
LAST = '└── '

LINE = '│   '
EMPTY = '    '


def parse_args() -> Namespace:

    parser = ArgumentParser()

    parser.add_argument('dir_path', type=str, nargs='?', default='.', help='Directory path')

    args = parser.parse_args()

    return args


def print_tree(dir_path: str | Path, prefix: str = '') -> tuple[int, int]:
    '''Print the directory tree structure.'''

    dir_path = Path(dir_path)

    # check whether directory exists
    if not dir_path.exists():
        raise FileNotFoundError('Path does not exist')
    elif not dir_path.is_dir():
        raise FileNotFoundError('Path is not a directory')

    # get list of items
    items = list(dir_path.iterdir())

    # remove hidden files/dirs
    items = [p for p in items if not p.name.startswith('.')]

    # sort items alphabetically
    items = sorted(items)

    # initialize counters
    num_dirs = 1  # count the root dir
    num_files = 0

    # loop over items
    for idx, p in enumerate(items):

        # get some item info
        is_last = idx >= (len(items) - 1)
        is_dir = p.is_dir()

        # set symbol (to be put before name)
        symbol = LAST if is_last else MIDDLE

        # print file/dir name with prefix and symbol
        print(prefix + symbol + p.name)

        if is_dir:

            # set new prefix
            new_prefix = prefix + (EMPTY if is_last else LINE)

            # print subdirectory
            nd, nf = print_tree(p, prefix=new_prefix)

            num_dirs += nd
            num_files += nf

        else:
            num_files += 1

    return num_dirs, num_files


if __name__ == '__main__':

    args = parse_args()
    dir_path = args.dir_path

    print(dir_path)

    num_dirs, num_files = print_tree(dir_path)

    print(f'{num_dirs} directories, {num_files} files')
