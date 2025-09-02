'''Tests for the three-sum problem.'''

import pytest

from challenges.three_sum import (
    three_sum_brute_force,
    three_sum_two_pointers,
    three_sum_hash_table
)


@pytest.fixture(params=[
    three_sum_brute_force,
    three_sum_two_pointers,
    three_sum_hash_table
])
def implementation(request):
    return request.param


@pytest.mark.parametrize('numbers, target, ids_expected', [
    ([1, 2, 3, 4, 5], 7, [(0, 1, 3)]),
    ([], 7, [])
])
def test_correctness(
    implementation,
    numbers,
    target,
    ids_expected
):

    ids = implementation(numbers, target)

    assert set(ids) == set(ids_expected)
