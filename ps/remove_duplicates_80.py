"""Solution for problem 80.

https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/?envType=study-plan-v2&envId=top-interview-150
"""

from typing import List

import pytest


@pytest.mark.parametrize(
    "input_nums, output_nums, output_k",
    [
        ([1, 1, 1, 2, 2, 3], [1, 1, 2, 2, 3, 101010], 5),
        ([0, 0, 1, 1, 1, 1, 2, 3, 3], [0, 0, 1, 1, 2, 3, 3, 101010, 101010], 7),
    ],
)
def test_remove_duplicates(input_nums, output_nums, output_k):
    """Test the solution."""
    nums = input_nums[:]
    k = remove_duplicates(nums)

    assert k == output_k
    for index in range(k):
        assert nums[index] == output_nums[index]


def remove_duplicates(nums: List[int]) -> int:
    """Remove duplicates from a sorted array."""
    if len(nums) <= 2:
        return len(nums)

    j = 0

    elem_value = nums[0]
    elem_value_repetition_cnt = 0

    for i in range(len(nums)):
        if elem_value == nums[i]:
            elem_value_repetition_cnt += 1
        else:
            elem_value = nums[i]
            elem_value_repetition_cnt = 1

        if elem_value_repetition_cnt <= 2:
            # swap the element of index i and index j
            tmp = nums[i]
            nums[i] = nums[j]
            nums[j] = tmp

            j += 1

    return j
