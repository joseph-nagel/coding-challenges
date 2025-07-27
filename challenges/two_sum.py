'''
Two-sum problem.

Summary
-------
The goal is to find all pairs of array elements that sum to a target value.
Three solutions with different time complexities are implemented.

'''

def two_sum_brute_force(numbers: list[int], target: int) -> list[tuple[int, int]]:
    '''Solve the two-sum problem in brute-force style with O(n^2) time complexity.'''

    ids = []  # type: list[tuple[int, int]]

    for i in range(len(numbers) - 1):

        for j in range(i + 1, len(numbers)):

            if numbers[i] + numbers[j] == target:
                ids.append((i, j))

    return ids


def two_sum_two_pointers(numbers: list[int], target: int) -> list[tuple[int, int]]:
    '''Solve the two-sum problem based on sorted numbers in O(n log(n)) time (due to sorting).'''

    if numbers != sorted(numbers):
        raise ValueError('This function requires the numbers to be sorted')

    ids = []  # type: list[tuple[int, int]]

    l_idx = 0
    r_idx = len(numbers) - 1

    while l_idx < r_idx:

        curr_sum = numbers[l_idx] + numbers[r_idx]

        if curr_sum == target:
            ids.append((l_idx, r_idx))
            l_idx += 1

        elif curr_sum < target:
            l_idx += 1

        else:
            r_idx -= 1

    return ids


def two_sum_hash_table(numbers: list[int], target: int) -> list[tuple[int, int]]:
    '''Solve the two-sum problem based on a hash table (dict) in O(n) time.'''

    if len(numbers) != len(set(numbers)):
        raise ValueError('This approach requires unique numbers')

    ids = []  # type: list[tuple[int, int]]

    seen_dict = {}  # type: dict[int, int]

    for idx, num in enumerate(numbers):

        complement = target - num

        if complement in seen_dict.keys():
            ids.append((seen_dict[complement], idx))

        seen_dict[num] = idx

    return ids


if __name__ == '__main__':

    numbers = [1, 2, 3, 4, 5]
    target = 7

    print(two_sum_brute_force(numbers, target))
    print(two_sum_two_pointers(numbers, target))
    print(two_sum_hash_table(numbers, target))

