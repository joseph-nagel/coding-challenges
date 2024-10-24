'''
Three-sum problem.

Summary
-------
The three-sum problem asks for finding all triplets of
array elements that sum to a specific target value.

One can address this problem by looping over the
numbers and solving the emerging two-sum problems.

The solutions differ in their time complexity.

'''

def three_sum_brute_force(numbers: list[int], target: int) -> list[tuple[int, int, int]]:
    '''Solve three-sum problem in brute-force style with O(n^3) time complexity.'''

    ids = [] # type: list[tuple[int, int, int]]

    for i in range(len(numbers) - 2):

        for j in range(i + 1, len(numbers) - 1):

            for k in range(j + 1, len(numbers)):

                if numbers[i] + numbers[j] + numbers[k] == target:
                    ids.append((i, j, k))

    return ids


def three_sum_two_pointers(numbers: list[int], target: int) -> list[tuple[int, int, int]]:
    '''Solve three-sum problem based on sorted numbers in O(n^2) time.'''

    if numbers != sorted(numbers):
        raise ValueError('This function requires the numbers to be sorted')

    ids = [] # type: list[tuple[int, int, int]]

    for i in range(len(numbers) - 2):

        l_idx = i + 1
        r_idx = len(numbers) - 1

        while l_idx < r_idx:

            curr_sum = numbers[i] + numbers[l_idx] + numbers[r_idx]

            if curr_sum == target:
                ids.append((i, l_idx, r_idx))
                l_idx += 1

            elif curr_sum < target:
                l_idx += 1

            else:
                r_idx -= 1

    return ids


def three_sum_hash_table(numbers: list[int], target: int) -> list[tuple[int, int, int]]:
    '''Solve three-sum problem based on a hash table in O(n^2) time.'''

    if len(numbers) != len(set(numbers)):
        raise ValueError('This approach requires unique numbers')

    ids = [] # type: list[tuple[int, int, int]]

    for i in range(len(numbers) - 2):

        curr_target = target - numbers[i]

        seen_dict = {} # type: dict[int, int]

        for j in range(i + 1 , len(numbers)):

            complement = curr_target - numbers[j]

            if complement in seen_dict:
                ids.append((i, seen_dict[complement], j))

            seen_dict[numbers[j]] = j

    return ids


if __name__ == '__main__':

    numbers = [1, 2, 3, 4, 5]
    target = 7

    print(three_sum_brute_force(numbers, target))

    print(three_sum_two_pointers(numbers, target))

    print(three_sum_hash_table(numbers, target))

