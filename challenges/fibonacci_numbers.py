'''Fibonacci sequence.'''


def fib_recursive(n):
    '''Generate Fibonacci numbers recursively.'''

    if n == 0:
        c = 0

    elif n == 1:
        c = 1

    else:
        c = fib_recursive(n - 2) + fib_recursive(n - 1)

    return c


def fib_for_loop(n):
    '''Generate Fibonacci numbers with a for loop.'''

    a = 0
    b = 1

    if n == 0:
        c = a

    elif n == 1:
        c = b

    else:
        for _ in range(n - 1):
            c = a + b
            a = b
            b = c

    return c


def fib_generator(n):
    '''Create Fibonacci numbers with a generator.'''

    a = 0
    b = 1

    for _ in range(n):

        yield a

        a, b = b, a + b


if __name__ == '__main__':

    for f in fib_generator(5):
        print(f)

    for n in range(5, 10):
        print(fib_recursive(n))

    for n in range(10, 15):
        print(fib_for_loop(n))

