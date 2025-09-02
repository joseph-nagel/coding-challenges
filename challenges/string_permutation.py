'''String permutation check.'''


def count_chars(a: str) -> dict[str, int]:
    '''Count characters in string.'''

    counts = {}  # type: dict[str, int]

    for char in a:
        if char not in counts.keys():
            counts[char] = 1
        else:
            counts[char] += 1

    return counts


def check_permutation(a: str, b: str, verbose: bool = False) -> bool:
    '''Check whether two strings are permutations.'''

    if len(a) != len(b):
        is_permutation = False
    else:
        is_permutation = count_chars(a) == count_chars(b)

    if verbose:
        print(
            '"{}" and "{}" are {}permutations'.format(
                a, b, '' if is_permutation else 'not '
            )
        )

    return is_permutation


if __name__ == '__main__':

    a = '123'
    b = 'abc'
    c = 'cba'

    _ = check_permutation(a, b, verbose=True)
    _ = check_permutation(b, c, verbose=True)
