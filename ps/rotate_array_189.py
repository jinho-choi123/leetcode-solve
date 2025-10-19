"""Solution for problem 189.

https://leetcode.com/problems/rotate-array/description/?envType=study-plan-v2&envId=top-interview-150
"""

from typing import List

import pytest


@pytest.mark.parametrize(
    "input_nums, k, output_nums",
    [([1, 2, 3, 4, 5, 6, 7], 3, [5, 6, 7, 1, 2, 3, 4]), ([-1, -100, 3, 99], 2, [3, 99, -1, -100])],
)
def test_rotate_array(input_nums, k, output_nums):
    """Test the solution."""
    nums = input_nums[:]

    rotate_array(nums, k)

    assert nums == output_nums


def _partial_reverse(nums: List[int], start_index: int, end_index: int):
    """Partially reverse the list."""
    assert start_index <= end_index
    assert start_index >= 0
    assert end_index < len(nums)

    for offset in range((end_index - start_index) // 2 + 1):
        tmp = nums[start_index + offset]
        nums[start_index + offset] = nums[end_index - offset]
        nums[end_index - offset] = tmp


def rotate_array(nums: List[int], k: int):
    """Rotate the array by k."""
    k = k % len(nums)

    if k == 0:
        return

    # logger.info(f"input nums: {nums}") # noqa: ERA001
    _partial_reverse(nums, 0, len(nums) - 1)
    # logger.info(f"nums after full reverse: {nums}") # noqa: ERA001
    _partial_reverse(nums, 0, k - 1)
    # logger.info(f"nums after partial 0~(k-1) index reverse: {nums}") # noqa: ERA001
    _partial_reverse(nums, k, len(nums) - 1)
    # logger.info(f"nums after partial k~(n-1) index reverse: {nums}")  # noqa: ERA001
