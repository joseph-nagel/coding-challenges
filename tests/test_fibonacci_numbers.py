'''Tests for Fibonacci number generation.'''

import pytest

from challenges.fibonacci_numbers import (
    fib_recursive,
    fib_for_loop,
    fib_generator
)


@pytest.fixture
def fib_expected():
    return [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]


@pytest.fixture(params=[fib_recursive, fib_for_loop])
def function(request):
    return request.param


class TestCorrectness:

    def test_function(self, function, fib_expected):
        fib = [function(idx) for idx in range(len(fib_expected))]
        assert fib == fib_expected

    def test_generator(self, fib_expected):
        fib = [f for f in fib_generator(len(fib_expected))]
        assert fib == fib_expected


@pytest.mark.parametrize('idx', [-1, -10])
class TestNegative:

    def test_function(self, function, idx):
        with pytest.raises(ValueError):
            _ = function(idx)

    def test_generator(self, idx):
        with pytest.raises(ValueError):
            _ = next(fib_generator(idx))
