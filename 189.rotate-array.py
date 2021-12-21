#
# @lc app=leetcode id=189 lang=python3
#
# [189] Rotate Array
#

# @lc code=start
from abc import abstractmethod


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        Strategy 1: Brute Force
        Runtime: O(n)
        Space: O(n)

        Args:
            nums (List[int]):  a list of integers
            k (int): rotate the array k times
        """

        n = len(nums)
        k %= n
        rotated = [0] * n

        for i in range(n):
            idx = (i + k) % n
            rotated[idx] = nums[i]

        nums[:] = rotated
        return


# @lc code=end
