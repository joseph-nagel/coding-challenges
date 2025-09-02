'''Tests for string permutation check.'''

import pytest

from challenges.string_permutation import check_permutation


@pytest.mark.parametrize('a, b, expected', [
    ('abc', 'cba', True),
    ('abc', '123', False),
    ('', '', True),
    ('', '1', False)
])
def test_correctness(a, b, expected):
    is_permutation = check_permutation(a, b, verbose=False)
    assert is_permutation == expected
