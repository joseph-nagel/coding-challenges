'''Tests for the two-sum problem.'''

import pytest

from challenges.two_sum import (
    two_sum_brute_force,
    two_sum_two_pointers,
    two_sum_hash_table
)


@pytest.fixture(params=[
    two_sum_brute_force,
    two_sum_two_pointers,
    two_sum_hash_table
])
def implementation(request):
    return request.param


@pytest.mark.parametrize('numbers, target, ids_true', [
    ([1, 2, 3, 4, 5], 7, [(1, 4), (2, 3)]),
    ([], 7, [])
])
def test_correctness(implementation,
                     numbers,
                     target,
                     ids_true):

    ids = implementation(numbers, target)

    assert set(ids) == set(ids_true)

