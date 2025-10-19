"""Solution for problem 169.

https://leetcode.com/problems/majority-element/description/?envType=study-plan-v2&envId=top-interview-150
"""

from typing import List

import pytest


@pytest.mark.parametrize("input_nums, golden_major_elem", [([3, 2, 3], 3), ([2, 2, 1, 1, 1, 2, 2], 2)])
def test_majority_element(input_nums, golden_major_elem):
    """Test the solution."""
    nums = input_nums[:]

    major_elem = majority_element(nums)

    assert major_elem == golden_major_elem


def majority_element(nums: List[int]):
    """Get the majority element."""
    maj_elem = nums[0]
    maj_elem_cnt = 0
    for elem in nums:
        if maj_elem == elem:
            maj_elem_cnt += 1
        else:
            maj_elem_cnt -= 1

        if maj_elem_cnt == 0:
            maj_elem = elem
            maj_elem_cnt += 1
    return maj_elem
